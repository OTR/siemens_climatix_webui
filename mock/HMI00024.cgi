<html>

<head>

<link rel="stylesheet" href="HMI.css">

<meta http-equiv=Content-Type content="text/html; charset=utf-8">

<meta http-equiv=Content-Language content=en-us>

<meta http-equiv="expires" content="0">

<meta http-equiv="pragma" content="no-cache">

<meta http-equiv="cache-control" content="no-cache">

<title>?title</title>

<script type="text/javascript">

function createNonCachedScriptInclude(scriptUrl) {

	var hmilang = document.createElement('script');

	hmilang.type = 'text/javascript';

	hmilang.src = scriptUrl + '?nocache=' + new Date().getTime();

	var s = document.getElementsByTagName('script')[0];

	s.parentNode.insertBefore(hmilang, s);

}



<!--createNonCachedScriptInclude('HMI.js');-->

</script>

<script type="text/javascript" src="HMI.js"></script>

</head>

<script type="text/javascript">

function GSL() { return (

253); }

function GAI() { return (

0); }

function GL() { return (

1); }

</script>

<body onload="DL()"><div id='d0'><table><tr>

<td id='l0' width=384><table id='t0'><tr>

<td width=84 class="sk"><span id="o002" sz=7 lg="2. 314" li=-2>

</span></td>

<td width=264 class="sk"><span id="o004" sz=22 lg="2. 313" li=-2>

</span></td>

</tr></table></td>

<td id="lk0" width=36 lv=253>&nbsp;

<a id="a0" href="javascript:JTP('HMI00001.cgi')"><img src="HMIlink.gif"></a></td>

</tr></table></div><div id="d1"><table><tr><td id='l1' width=384><table id='t1'><tr>

<td width=180 class="lt"><span id="o007" sz=15 lg="2. 314" li=-2>

</span></td>

<td class="sp" width=12>&nbsp;</td>

<td width=72 align=right class="et"><span id="o010" sz=6 e="

Выкл*Вкл*??" it="e" lv=4 mi="val:0x2302 0x12C76478 0x100" >

0</span></td>

<td class="sp" width=-12>&nbsp;</td>

<td width=12 class="pt"><span id="o012" sz=30>/</span></td>

<td class="sp" width=12>&nbsp;</td>

<td width=72 align=right class="et"><span id="o015" sz=6 e="

Авто*АСДУ*HMI*??" >

0</span></td>

</tr></table></td>

<td id="e1" width=36>&nbsp;

<a href="javascript:CIT('l1','t1')"><img src="HMIedit.gif"></a></td>

</tr></table></div><div id="d2"><table><tr><td id='l2' width=384><table id='t2'><tr>

<td width=348 class="lt"><span id="o017" sz=29 lg="2. 323" li=-2>

</span></td>

</tr></table></td>

</tr></table></div><div id="d3"><table><tr><td id='l3' width=384><table id='t3'><tr>

<td width=132 class="lt"><span id="o019" sz=11 lg="2. 324" li=-2>

</span></td>

<td class="sp" width=12>&nbsp;</td>

<td width=108 align=right class="v" size=9><span id="o023" sz=9>

0</span></td>

<td width=12><span id="u023" class="u">

%</span></td>

</tr></table></td>

</tr></table></div><div id="d4"><table><tr><td id='l4' width=384><table id='t4'><tr>

<td width=132 class="lt"><span id="o025" sz=11 lg="2. 325" li=-2>

</span></td>

<td width=108 align=right class="v" size=9><span id="o028" sz=9>

0</span></td>

<td width=12><span id="u028" class="u">

%</span></td>

</tr></table></td>

</tr></table></div><div id="d5"><table><tr><td id='l5' width=384><table id='t5'><tr>

<td width=132 class="lt"><span id="o030" sz=11 lg="2. 326" li=-2>

</span></td>

<td class="sp" width=12>&nbsp;</td>

<td width=108 align=right class="v">

<span id="o033" it="v" lv=4 sz=9 mi="val:0x2300 0x12C7E9E4 0x100">

0</span></td>

<td width=12><span id="u033" class="u">

%</span></td>

</tr></table></td>

<td id="e5" width=36>&nbsp;

<a href="javascript:CIT('l5','t5')"><img src="HMIedit.gif"></a></td>

</tr></table></div>

<script type="text/javascript">

function PP() {

HEL();

BTL('o002');

BTL('o004');

HLK('lk0');

BTL('o007');

BEV('o010');

BEV('o015');

HELK('d1','e1');

BTL('o017');

BTL('o019');

BTL('o025');

BTL('o030');

HELK('d5','e5');

SAR(); }

function GFR()

{ return ("HMI00024Read.cgi"); }

</script>

</body></html>

