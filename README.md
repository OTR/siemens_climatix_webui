# Installation #

* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser // (optional)



o023,v,10.633| // Наруж темп
o029,v,62.43| // Наруж влаж
o035,v,23.921| // Темп рец приток
o041,v,27.63| // Влаж рец приток
o047,v,19.2375| // Темп приток 1
o053,v,19.3464| // Темп приток 2
o059,v,39.51| // Влаж приток
o065,v,26.638| // Темп вытяжка
o071,v,22.98| // Влаж вытяжка
o077,v,13.2905| // Темп гликоля 1
o083,v,13.1105| // Темп гликоля 2
o089,v,5.787|  // Давл гликоля 1
o095,v,2.249|  // Давл гликоля 2
o101,v,0|		// DP фильтр G3
o107,v,0|		// DP фильтр F7
o113,v,+++?42?+++| // DP фильтр G4 (float)
o119,v,0|		// DP вент П1
o125,v,0|		// DP вент П2
o131,v,0|		// DP вент В1
o137,v,0|		// DP вент В2
o143,v,+++?42?+++|
o149,v,+++?42?+++|
o155,v,0|		// Прит заслон 1 ОбрС
o159,e,1|		
o164,v,0|
o168,e,1|
o173,v,0|
o177,e,1|
o182,v,0|
o186,e,1|
o191,v,100|		// ОбрСвКлапОхл
o195,e,1|
o200,v,100|
o204,e,1|
o209,v,0.56|
o215,v,0|
o225,e,1|
o231,e,0|
o237,e,0|
o245,e,0|
o251,e,0|
o257,e,0|
o265,e,+++?42?+++|
o273,e,+++?42?+++|
o279,e,0|
o285,e,0|
o291,e,0|
o297,e,1|
o303,e,0|
o311,e,0|
o317,e,0|
o323,e,0|
o329,e,0|
o335,e,0|
o341,e,0|
o347,e,0|
o353,e,0|
o359,e,0|
o365,e,0|


o023,v,13.922|  .
o029,v,52.36|  .
o035,v,19.257|  .
o041,v,34.12|  .
o047,v,18.9325|  .
o053,v,18.2135|  .
o059,v,35|  .
o065,v,23.635|  .
o071,v,26.95|  .
o077,v,13.0591|  .
o083,v,13.1105|  .
o089,v,2.276|  .
o095,v,2.294|  .
o101,v,17.6|  .
o107,v,61.65|  .
o113,v,20.3|  .
o119,v,109.8|  .
o125,v,115.2|  .
o131,v,96.3|  .
o137,v,104.4|  .
o143,v,+++?42?+++|  .
o149,v,+++?42?+++|  .
o155,v,74.4875|  .
o161,v,74.5875|  // Прит заслон 2 ОбрС
o167,v,75.125|		// Выт заслон 1 ОбрС
o173,v,74.65|		// Выт заслон 2 ОбрС
o179,v,25.1125|		// Рец заслон 1 ОбрС
o185,v,25.2125|		// Рец заслон 2 ОбрС
o191,v,0.77|		// ОбрСвКлапОхл
o197,v,1.375|		// Вода проводим
o207,e,1|			// Уровень увлаж Активный
o213,e,0|			// Детектор увлаж Пассивный
o219,e,0|			// Холод маш ОбрСв
o227,e,0|			// Производительность
o233,e,0|			// Контр напряж
o239,e,0|			// Сервис
o247,e,0|			// Сервис вент В val:0x2204 0x89283DD4 0x100
o255,e,0|			// Сервис увлаж
o261,e,0|			// Пожар
o267,e,0|			// Дым 1
o273,e,0|			// Дым 2
o279,e,1|			// Авария дым Активный
o285,e,0|			// Авария холод маш
o293,e,1|			// Вент П1 ОбрСв
o299,e,0|			// Вент П1 Авария
o305,e,1|			// Вент П2 ОбрСв
o311,e,0|			// Вент П2 Авария
o317,e,1|			// Вент В1 ОбрСв
o323,e,0|			// Вент В1 Авария
o329,e,1|			// Вент В2 ОбрСв
o335,e,0|			// Вент В2 Авария
o341,e,0|			// Насос увлаж ОбрСв
o347,e,0|			// Насос увлаж Авария


Уставки 00015

o005,e,5|		// 
o010,e,3|		// 
o015,e,2|		// 
o023,v,185|		// Уст перепад G3
o028,v,200|		// Уст перепад F7
o033,v,150|		// Уст перепад G4
o042,e,1|		// 
o047,e,1|		// 
o052,v,18|		// 
o057,v,24|		// 
o062,v,22|		// 
o067,v,18|		// 
o074,v,30|		// 
o079,v,65|		// 
o084,v,45|		// 
o089,v,45|		// 
o094,v,55.0468|		// 
o103,e,1|		// 
o110,e,1|		// 
o115,v, 0.95|		// 
o120,v,54550|		// 
o125,v,51822.5|		// 
o130,v,17000|		// 
o138,v,16150|		// 
o145,v,-40|		// 
o150,v,32.5|		// 
o155,v,   9.0|		// 
o162,e,0|		// 
o167,v,  11.0|		// 
o177,v,99300|		// 
o182,v,5|		// 
o187,v,5|		// 
o193,v,100|		// 
o198,v,5|		// 
o203,v,6|		// 
o211,v,150|		// 
o217,v,150|		// 
o223,v,150|		// 
o228,v,20|		// 
o234,v,0|		// 
o241,v,   2.0|		// 
o246,v,   1.0|		// 
o251,v,5|		// 
o256,v,   2.0|		// 
o261,v,0.3|		// 
o266,v,1|		// 
o271,v,   2.0|		// 
o276,v,26|		// 
o283,v,0|		// 
o288,v,5|		// 
o293,v,2|		// 
o298,v,10|		// 
o305,e,0|		// 
o312,v,150|		// 
o321,v,55.8|		// 
o326,v,50.2|		// 
o331,v,59.2|		// 
o339,v,2|		// 
o344,v,  15.0|		// 
o349,v,   5.0|		// 


asgiref	== 3.3.4
certifi	== 2020.12.5
chardet	== 4.0.0
Django	== 3.2
h11		== 0.12.0
httpcore	== 0.12.3
httpx	== 0.17.1
idna	== 2.10
lxml	== 4.6.3
pip		== 20.2.3
pytz	== 2021.1
requests	== 2.25.1
rfc3986	== 1.4.0
setuptools	== 49.2.1
sniffio	== 1.2.0
sqlparse	== 0.4.1
urllib3	== 1.26.4
		