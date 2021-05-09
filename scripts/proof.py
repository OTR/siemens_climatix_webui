"""
Script for parsing Web UI
"""
import argparse
from datetime import datetime
import logging
from pathlib import Path
from time import sleep

from lxml import html
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError

user = "WEB"  # FIXME: refactor it. add to global CONFIG variable
passwd = "SBTAdmin!"

# requests.exceptions.ConnectionError: HTTPConnectionPool(host='169.254.186.211', port=80):


CONFIG = {
    "hosts": {
        "1.1": "169.254.188.220",
        "1.2": "169.254.130.48",
        "1.3": "169.254.1.28",
        "1.4": "169.254.1.42",
        "2.1": "169.254.97.128",  # "2.1" : "169.254.186.211",
        "2.2": "169.254.53.139",
        "2.3": "169.254.45.14",
        "2.4": "169.254.58.171",  # "2.4" : "169.254.219.248",
        "3.1": "169.254.157.21",
        "3.2": "169.254.2.251",  # "169.254.102.205",
        "3.3": "169.254.164.35",
        "3.4": "169.254.154.250",
        "4.1": "169.254.154.245",
        "4.2": "169.254.242.245",
        "4.3": "169.254.56.35",
        "4.4": "169.254.252.44",
    },
    "translate": {
        "0": "1.1",
        "1": "1.2",
        "2": "1.3",
        "3": "1.4",
        "4": "2.1",
        "5": "2.2",
        "6": "2.3",
        "7": "2.4",
        "8": "3.1",
        "9": "3.2",
        "A": "3.3",
        "B": "3.4",
        "C": "4.1",
        "D": "4.2",
        "E": "4.3",
        "F": "4.4"
    }
}


class MySession(requests.Session):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)  # FIXME:
        self.auth = HTTPBasicAuth(user, passwd)
        self.id = kwargs["_id"]
        self.host = CONFIG["hosts"][self.id]
        self.basedir = "C:/Users/User/AppData/logs/"  # FIXME: get rid of hardcoded path
        self.basename = "ЦВУ_" + self.id.replace(".", "_")

    def gettime(self) -> str:
        """@return string"""

        return datetime.now().strftime("%d.%m.%Y %H:%M")

    def getr(self, path):
        # Get relative path
        # example self.getr("/main.htm")
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

    def main_menu_read(self):
        """Get dynamic values for Main menu"""
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

    def get_settings_read(self):
        """Get settings for unit"""
        pass

    def get_inputs_read(self):
        """Get input values from sensors"""
        body = self.getr("/HMI00013Read.cgi")
        body = body.replace("\r\n", "")
        body_list = body.split("|")
        # float(body_list[5].split(",")[-1])

    def main_menu_pretty(self):
        """"""
        params = self.main_menu_read()

        params["temp_intake"] = round(params["temp_intake"] * 10.0) / 10.0
        params["temp_exhaust"] = round(params["temp_exhaust"] * 10.0) / 10.0

        params["hum_intake"] = round(params["hum_intake"]) / 1.0
        params["hum_exhaust"] = round(params["hum_exhaust"]) / 1.0

        params["vol_intake"] = round(params["vol_intake"] / 100.0) * 100.0
        params["vol_exhaust"] = round(params["vol_exhaust"] / 100.0) * 100.0

        params["time"] = self.gettime()

        params["id"] = self.id

        return params

    def get_crash_hist_entry(self, entry_id):
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

    def get_crash_hist(self):
        """As list of dictionaries"""
        history = []
        is_last = False
        i = 0
        while not is_last:
            i += 1
            entry = self.get_crash_hist_entry(i)
            if entry["text"] == "":
                is_last = True
            else:
                entry["time_found"] = self.gettime()
                history.append(entry)

        # history is DESCEND so reverse it
        history.reverse()

        return history

    def simple_text_hist(self) -> None:
        """"""
        hist = self.get_crash_hist()
        hist_as_plain_text = ""
        for entry in hist:
            pattern = f'{entry["time_found"]}\t{entry["text"].ljust(60)}\t' \
                      f'{entry["priority"]}\t{entry["prior_text"].ljust(15)}\t' \
                      f'{entry["date"]}'
            hist_as_plain_text += pattern + "\n"
        timestamp = str(self.gettime())
        # 12.12.2021 14:50 => 12_12_2021_14_50
        timestamp = timestamp.replace(" ", "_")
        timestamp = timestamp.replace(".", "_")
        timestamp = timestamp.replace(":", "_")
        path = self.basedir + timestamp + "_crash_hist_" + self.basename + ".txt"
        with open(path, "w") as f1:
            f1.write(hist_as_plain_text)

    def simple_txt(self) -> None:
        """"""
        params = self.main_menu_pretty()

        pattern = f'{params["time"]}\t{params["temp_intake"]}\t' \
                  f'{int(params["vol_intake"])}\t\t{params["temp_exhaust"]}\t' \
                  f'{int(params["vol_exhaust"])}\n'

        path = self.basedir + self.basename + ".txt"
        with open(path, "a") as f1:
            f1.write(pattern)


def main(mode="infinite_loop", loglevel=logging.ERROR, **args):
    """"""
    project_dir = Path(__file__).resolve().parent.parent
    log_file = project_dir / "logs" / "log.txt"
    # Establish logger object
    my_logger = logging.getLogger("monitor")
    fh = logging.FileHandler(log_file)
    fh.setLevel(loglevel)
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s %(message)s",
                                  datefmt="%Y.%m.%d %H:%M:%S")
    fh.setFormatter(formatter)
    my_logger.addHandler(fh)
    # Reminder: critical > error > warning > info > debug
    my_logger.error("help me")
    if mode:
        if mode == "infinite_loop":
            """Безконечно запрашивать температуру и расход
            и писать в файл"""
            while True:
                for key in CONFIG["hosts"].keys():
                    my_sess = MySession(_id=key)
                    my_sess.simple_txt()

                sleep(10 * 60)  # half an hour
        elif mode == "temp_vol_once":
            """Запросить температуру и расход один раз и записать
            в файл"""
            for key in CONFIG["hosts"].keys():
                my_sess = MySession(_id=key)
                my_sess.simple_txt()
        elif mode == "crash_hist_once_for_all":
            for key in CONFIG["hosts"].keys():
                my_sess = MySession(_id=key)
                my_sess.simple_text_hist()
        elif mode == "crash_hist_once" and args.get("cvu") is not None:
            _id = CONFIG["translate"][args.get("cvu")]
            my_sess = MySession(_id=_id)
            history = my_sess.get_crash_hist()
            return history  # List of dicts

    else:
        pass  # TODO: sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug",
                        action="store_true",
                        help="Debug mode. Verbose output."
                        )
    parser.add_argument("--mode",
                        default="temp_vol_once",
                        choices=["temp_vol_once",
                                 "infinite_loop",
                                 "crash_hist_once_for_all",
                                 "crash_hist_once"],
                        help="The mode of launching")
    parser.add_argument("--cvu",
                        default=None,
                        choices=["0", "1", "2", "3",
                                 "4", "5", "6", "7",
                                 "8", "9", "A", "B",
                                 "C", "D", "E", "F"],
                        help="Identifyer of Central Ventilation Unit")
    args = parser.parse_args()

    mode = "temp_vol_once"
    loglevel = logging.ERROR
    cvu = None

    if args.debug:
        loglevel = logging.DEBUG

    if args.mode == "crash_hist_once" and args.cvu is not None:
        mode = args.mode
        main(mode=mode, loglevel=loglevel, cvu=args.cvu)
    else:
        if args.mode:
            mode = args.mode
        main(mode=mode, loglevel=loglevel)
