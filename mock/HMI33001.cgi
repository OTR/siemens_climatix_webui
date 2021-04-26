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

<td width=12 class="sk"><span id="o002" sz=1 lg="4. 506" li=-2>

</span></td>

<td width=336 class="sk"><span id="o005" sz=28>

+++?42?+++</span></td>

</tr></table></td>

<td id="lk0" width=36 lv=253>&nbsp;

<a id="a0" href="javascript:JTP('HMI00010.cgi')"><img src="HMIlink.gif"></a></td>

</tr></table></div><div id="d1"><table><tr><td id='l1' width=384><table id='t1'><tr>

<td width=228 class="lt"><span id="o008" sz=19 lg="4. 531" li=-2>

</span></td>

<td class="sp" width=24>&nbsp;</td>

<td width=108 align=right class="et"><span id="o011" sz=9 e="

&nbsp;*??" it="e" lv=253 mi="val:0x0 0x0 0x3002" >

+++?42?+++</span></td>

</tr></table></td>

<td id="e1" width=36>&nbsp;

<a href="javascript:CIT('l1','t1')"><img src="HMIedit.gif"></a></td>

</tr></table></div><div id="d2"><table><tr><td id='l2' width=384><table id='t2'><tr>

<td width=228 class="lt"><span id="o013" sz=19 lg="4. 532" li=-2>

</span></td>

<td class="sp" width=24>&nbsp;</td>

<td width=60 align=right class="v">

<span id="o016" it="v" lv=253 sz=5 mi="val:0x0 0x0 0x113">

+++?42?+++</span></td>

<td width=48><span id="u016" class="u">

&nbsp;</span></td>

</tr></table></td>

<td id="e2" width=36>&nbsp;

<a href="javascript:CIT('l2','t2')"><img src="HMIedit.gif"></a></td>

</tr></table></div>

<script type="text/javascript">

function PP() {

HEL();

BTL('o002');

HLK('lk0');

BTL('o008');

BEV('o011');

HELK('d1','e1');

BTL('o013');

HELK('d2','e2');

SAR(); }

function GFR()

{ return ("HMI33001Read.cgi"); }

</script>

</body></html>

