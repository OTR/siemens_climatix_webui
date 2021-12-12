"""
A script for polling PLC builtin web server. Business logic is placed here.
"""
import argparse
import logging
from datetime import datetime
from pathlib import Path
from time import sleep
from typing import Union

import requests
from lxml import html
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError

# TODO: Don't forget to replace `test_settings` with `prod_settings`
#  in case of production
from config.settings.test_settings import AHU_IPS, AHU_HISTORY_DIR
from config.settings.test_settings import SIEMENS_USER, SIEMENS_PASSWD


# TODO: catch `requests.exceptions.ConnectionError`
#  `HTTPConnectionPool(host='169.254.186.211', port=80)`


class PLCWebClient(requests.Session):
    """A Web Client to poll data from builtin PLC Web Server."""

    def __init__(self, **kwargs):
        """"""
        super(PLCWebClient, self).__init__()
        self.auth = HTTPBasicAuth(SIEMENS_USER, SIEMENS_PASSWD)
        self.name = kwargs["name"]
        self.host = AHU_IPS["hosts"][self.name]
        self.log_dir = AHU_HISTORY_DIR
        self.basename = "ЦВУ_" + self.name.replace(".", "_")

    def get_current_time(self) -> str:
        """
        Return current formatted time.

        :return: a string with date
        """
        return datetime.now().strftime("%d.%m.%Y %H:%M")

    def getr(self, path: str) -> Union[str, None]:
        """
        Get absolute URL from query. Example: `self.getr("/main.htm")`

        :param path: a query
        :return: decoded with UTF-8 HTML source
        """
        url = f"http://{self.host}{path}"
        try:
            resp = self.get(url)
            if resp.status_code == 404:
                return None
        except ConnectionError as e:
            print(len(e.args))  # FIXME: MyLogger.error(e.args)
            raise e
        resp.encoding = "UTF-8"

        return resp.text

    def main_menu(self):
        """
        Основное меню

        Темп приток id="o041"
        Темп вытяжка span id="o051"
        Расход приток span id="o061"
        Расход вытяжка span id="o066
        body = self.getr("/HMI00010.cgi")
        """
        body = self.getr("/HMI00010.cgi")
        tree = html.fromstring(body)
        print(tree.xpath('//span[@id="o061"]//text()')[0].strip())

    def main_menu_read(self) -> dict:
        """
        Make a request to PLC Web Server, parse response body which is a mess.
        `HMI00010Read.cgi` is an endpoint to get dynamically changed values to
        draw `Main menu`.

        :return: a dict containing intake and exhaust temperature, relative
            humidity, and air volume.
        """
        body = self.getr("/HMI00010Read.cgi")
        body = body.replace("\r\n", "")
        body_list = body.split("|")
        temp_intake = float(body_list[5].split(",")[-1])
        hum_intake = float(body_list[6].split(",")[-1])
        temp_exhaust = float(body_list[7].split(",")[-1])
        hum_exhaust = float(body_list[8].split(",")[-1])
        vol_intake = float(body_list[9].split(",")[-1])
        vol_exhaust = float(body_list[10].split(",")[-1])

        return {
            "temp_intake": temp_intake,
            "temp_exhaust": temp_exhaust,
            "hum_intake": hum_intake,
            "hum_exhaust": hum_exhaust,
            "vol_intake": vol_intake,
            "vol_exhaust": vol_exhaust
        }

    def get_settings_read(self) -> None:
        """Get settings for unit."""
        raise NotImplementedError

    def get_inputs_read(self) -> None:
        """Get input values from sensors."""
        body = self.getr("/HMI00013Read.cgi")
        body = body.replace("\r\n", "")
        body_list = body.split("|")
        # float(body_list[5].split(",")[-1])

    def main_menu_pretty(self) -> dict:
        """"""
        params = self.main_menu_read()

        params["temp_intake"] = round(params["temp_intake"] * 10.0) / 10.0
        params["temp_exhaust"] = round(params["temp_exhaust"] * 10.0) / 10.0

        params["hum_intake"] = round(params["hum_intake"]) / 1.0
        params["hum_exhaust"] = round(params["hum_exhaust"]) / 1.0

        params["vol_intake"] = round(params["vol_intake"] / 100.0) * 100.0
        params["vol_exhaust"] = round(params["vol_exhaust"] / 100.0) * 100.0

        params["time"] = self.get_current_time()

        params["id"] = self.name

        return params

    def get_crash_hist_entry(self, entry_id) -> dict:
        """
        From 0x01
        http://169.254.188.220/HMI65210.cgi?tid:0x26%200x01
        Definitely up to 0x32
        http://169.254.188.220/HMI65210.cgi?tid:0x26%200x42
        Or maybe 0x46
        """
        priority_mapping = {"0": "Опасно (A)",
                            "1": "Критич.(А)",
                            "2": "Низкий (В)",
                            "3": "Предупр. (C)",
                            "4": "Нет аварии",
                            "5": "История соб."}
        body = self.getr(f"/HMI65210.cgi?tid:0x26%20{hex(entry_id)}")
        tree = html.fromstring(body)
        crash = {}
        crash["text"] = tree.xpath('//span[@id="o008"]//text()')[0].strip()
        crash["priority"] = tree.xpath('//span[@id="o014"]//text()')[0].strip()
        crash["prior_text"] = priority_mapping[crash["priority"]]

        date = ""
        date += tree.xpath('//span[@id="o017"]//text()')[0].strip()  # day
        date += tree.xpath('//span[@id="o018"]//text()')[0].strip()  # dot
        date += tree.xpath('//span[@id="o020"]//text()')[0].strip()  # month
        date += tree.xpath('//span[@id="o021"]//text()')[0].strip()  # dot
        date += tree.xpath('//span[@id="o023"]//text()')[0].strip()  # year
        date += " "  # space
        date += tree.xpath('//span[@id="o026"]//text()')[0].strip()  # hours
        date += tree.xpath('//span[@id="o027"]//text()')[0].strip()  # column
        date += tree.xpath('//span[@id="o029"]//text()')[0].strip()  # minutes
        date += tree.xpath('//span[@id="o030"]//text()')[0].strip()  # colimn
        date += tree.xpath('//span[@id="o032"]//text()')[0].strip()  # seconds
        # Now date is like "21.03.2021 14:05:50"
        crash["date"] = date

        return crash

    def get_crash_hist(self) -> list[dict]:
        """
        Get a crash history (alarms, faults, warnings), i.e. logs.

        :return: a list of dicts, each dict represents a history entry
        """
        history = []
        is_last = False
        i = 0
        while not is_last:
            i += 1
            entry = self.get_crash_hist_entry(i)
            if entry["text"] == "":
                is_last = True
            else:
                entry["time_found"] = self.get_current_time()
                history.append(entry)

        # history is DESCEND by default so reverse it
        history.reverse()

        return history

    def simple_text_hist(self) -> None:
        """Write crash history in a plain text file."""
        hist = self.get_crash_hist()
        hist_as_plain_text = ""
        for entry in hist:
            pattern = f'{entry["time_found"]}\t' \
                      f'{entry["text"].ljust(60)}\t' \
                      f'{entry["priority"]}\t' \
                      f'{entry["prior_text"].ljust(15)}\t' \
                      f'{entry["date"]}'
            hist_as_plain_text += pattern + "\n"
        timestamp = str(self.get_current_time())
        # 12.12.2021 14:50 => 12_12_2021_14_50
        timestamp = timestamp.replace(" ", "_")  # FIXME:
        timestamp = timestamp.replace(".", "_")
        timestamp = timestamp.replace(":", "_")
        path = self.log_dir + timestamp + "_crash_hist_" + self.basename + ".txt"
        with open(path, "w") as f1:
            f1.write(hist_as_plain_text)

    def simple_txt(self) -> None:
        """
        Write intake and exhaust temperature and air volume
        in a plain text file.
        """
        params = self.main_menu_pretty()

        pattern = f'{params["time"]}\t{params["temp_intake"]}\t' \
                  f'{int(params["vol_intake"])}\t\t{params["temp_exhaust"]}\t' \
                  f'{int(params["vol_exhaust"])}\n'

        path = self.log_dir + self.basename + ".txt"
        with open(path, "a") as f1:
            f1.write(pattern)


def main(run_mode="infinite_loop", use_loglevel=logging.ERROR, **args) -> None:
    """
    Run different methods depend on parsed options.

    :param run_mode:
    :param use_loglevel:
    """
    project_dir = Path(__file__).resolve().parent.parent
    log_file = project_dir / "logs" / "log.txt"
    # Establish logger object
    my_logger = logging.getLogger("monitor")
    fh = logging.FileHandler(log_file)
    fh.setLevel(use_loglevel)
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s %(message)s",
                                  datefmt="%Y.%m.%d %H:%M:%S")
    fh.setFormatter(formatter)
    my_logger.addHandler(fh)
    # Reminder: critical > error > warning > info > debug

    if run_mode:
        if run_mode == "infinite_loop":
            """Безконечно запрашивать температуру и расход
            и писать в файл"""
            while True:
                for key in AHU_IPS["hosts"].keys():
                    my_sess = PLCWebClient(_id=key)
                    my_sess.simple_txt()

                sleep(10 * 60)  # half an hour
        elif run_mode == "temp_vol_once":
            """Запросить температуру и расход один раз и записать
            в файл"""
            for key in AHU_IPS["hosts"].keys():
                my_sess = PLCWebClient(_id=key)
                my_sess.simple_txt()
        elif run_mode == "crash_hist_once_for_all":
            for key in AHU_IPS["hosts"].keys():
                my_sess = PLCWebClient(_id=key)
                my_sess.simple_text_hist()
        elif run_mode == "crash_hist_once" and args.get("ahu") is not None:
            _id = AHU_IPS["translate"][args.get("ahu")]
            my_sess = PLCWebClient(_id=_id)
            history = my_sess.get_crash_hist()
            return history  # List of dicts FIXME: should not return

    else:
        pass  # TODO: sys.exit()


def parse_arguments() -> argparse.Namespace:
    """
    Parse arguments from console.

    :return: named arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug",
                        action="store_true",
                        help="Debug mode. Verbose output."
                        )
    parser.add_argument("--mode",
                        default="temp_vol_once",
                        choices=["temp_vol_once", "infinite_loop",
                                 "crash_hist_once_for_all", "crash_hist_once"
                                 ],
                        help="The mode of launching")
    parser.add_argument("--ahu",
                        default=None,
                        choices=["0", "1", "2", "3", "4", "5", "6", "7", "8",
                                 "9", "A", "B", "C", "D", "E", "F"
                                 ],
                        help="Identifier of Central Ventilation Unit")

    return parser.parse_args()


if __name__ == "__main__":
    named_args = parse_arguments()

    mode = "temp_vol_once"
    loglevel = logging.ERROR
    ahu = None

    if named_args.debug:
        loglevel = logging.DEBUG

    if named_args.mode == "crash_hist_once" and named_args.ahu is not None:
        mode = named_args.mode
        main(run_mode=mode, use_loglevel=loglevel, ahu=named_args.ahu)
    else:
        if named_args.mode:
            mode = named_args.mode
        main(run_mode=mode, use_loglevel=loglevel)
