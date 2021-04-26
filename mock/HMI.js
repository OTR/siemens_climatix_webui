
if(typeof(FileExt)!="function"){function FileExt(){return".cgi";}}
function HasTrend(){return typeof getRoot().isTrendLoaded=='boolean'&&getRoot().isTrendLoaded;}
var __hmiRoot_cached=null;function getRoot(){if(__hmiRoot_cached==null){var root=window;do{try{if(typeof root.isHmiRoot!='boolean'||!root.isHmiRoot)
root=root.parent;else
break;}catch(e){break;}}while(root!=window.top);__hmiRoot_cached=root;}
return __hmiRoot_cached;}
function getFrameDocumentById(id){var frameWindow=getFrameWindowById(id);return frameWindow==null?null:frameWindow.document;}
function getFrameWindowById(id){var hmiRoot=getRoot();if(hmiRoot!=null){var tag=hmiRoot.document.getElementById(id);if(tag!=null)
return tag.contentWindow;}
return null;}
function CloseEditor(){var parInp=getRoot().document.getElementById("InputEditor");if(parInp)
parInp.style.display="none";var parHMI=getFrameWindowById("HMI");if(parHMI){if(parHMI.window.httpTimeout!=null){parHMI.window.editorOpen=false;parHMI.window.processing=false;clearTimeout(parHMI.window.httpTimeout);parHMI.window.AutoRefresh();}}}
function OpenEditor(){var parHMI=getFrameWindowById("HMI");if(parHMI!=null){parHMI.window.editorOpen=true;parHMI.window.processing=true;if(parHMI.window.httpTimeout!=null)
clearTimeout(parHMI.window.httpTimeout);if(parHMI.window.xmlHttp!=null)
parHMI.window.xmlHttp.abort();}
var inputDoc=getFrameDocumentById("Input");if(inputDoc){var inputEdit=getRoot().document.getElementById("InputEditor");if(inputEdit)
inputEdit.style.display="block";var tag=getRoot().document.getElementById('inputeditorcontrolbuttons');if(tag)
tag.style.visibility="visible";}}
function THT(){var docHMI=getFrameDocumentById("HMI");if(docHMI!=null){var elems=docHMI.getElementsByTagName("span");if(elems!=null){for(var i=0;i<elems.length;i++)
{var elem=elems[i];var size=elem.getAttribute("sz");if(size!=null){var txt=elem.getAttribute('name');if(txt==null)
txt=elem.innerHTML;txt=trimText(txt);if(txt.length>size)
txt=txt.substring(0,size);elem.setAttribute('name',txt);elem.innerHTML=MaskUserChar(txt);}}}}}
function MaskUserChar(text){var frame=getFrameWindowById("HMI");if(frame){var sz="<span class=\"icon\">";var ez="</span>";var o=-1;var n=0;for(var i=0;i<text.length;i++){var c=text.charCodeAt(i);if(c>=getRoot().userfontstart&&c<=getRoot().userfontend){if(n>0)
n++;else
{o=i;n=1;}}else{if(n>0)
{text=text.substring(0,o)+sz+
text.substring(o,o+n)+ez+
text.substring(o+n);i=o+sz.length+n+ez.length-1;o=-1;n=0;}}}
if(n>0)
text=text.substring(0,o)+sz+
text.substring(o)+ez;}
return text;}
function TestTest(tableId)
{alert("1");}
function trimText(text)
{text=text.replace(/&nbsp;/g,' ');text=text.replace(/^\s*/g,'').replace(/\s*$/g,'');return text;}
function GetDefaultNaN(){return"******************************";}
function EvalMemId(strMemId)
{var strPar=GetUrlParameter(getFrameWindowById("HMI").location.href,"tid",":");if(strPar!="")
{var arrMemIdPar=strMemId.split(":")
var arrMemId=arrMemIdPar[1].split(" ");var iObjTypeMem=parseInt(arrMemId[0]);if(iObjTypeMem==0)
{var arrObjId=strPar.split(" ");arrMemId[0]=arrObjId[0];arrMemId[1]=arrObjId[1];arrMemIdPar[1]=arrMemId.join(" ");strMemId=arrMemIdPar.join(":");}}
return strMemId;}
function BIV(inputLink)
{var bUseLimits=false;var strValue=inputLink.innerHTML;var attr=inputLink.getAttribute("lv");var iLevel=attr?parseInt(attr):255;attr=inputLink.getAttribute("mi");var strName=attr?attr:"";attr=inputLink.getAttribute("sz");var iSize=attr?parseInt(attr):0;attr=inputLink.getAttribute("ll");var iLow=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;attr=inputLink.getAttribute("hl");var iHigh=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;attr=inputLink.getAttribute("hn");var strNan=attr?attr:"*";var bHasNan=attr?true:false;var bReplace=(iLevel>=GSL());if(bReplace)
{strName=EvalMemId(strName);var inputText="<input type=text class='vi'"+" name='"+strName+"' size="+iSize+" value='"+strValue+"'";if(bHasNan)
inputText=inputText+" hn='"+strNan+"'";if(bUseLimits)
inputText=inputText+" ll="+iLow+" hl="+iHigh;inputText=inputText+">";inputLink.parentNode.innerHTML=inputText;}
return bReplace;}
function BIP(inputLink)
{var attr=inputLink.getAttribute("sz");var iSize=attr?parseInt(attr):0;attr=inputLink.getAttribute("tl");var iTempl=attr?parseInt(attr):0;var strName="pwd";switch(iTempl)
{case 65410:strName="pwd";break;case 65450:strName="str:0x28 0x1 0x1";break;case 65451:strName="str:0x28 0x1 0x3";break;case 65452:strName="str:0x28 0x1 0x5";break;case 65453:strName="str:0x28 0x1 0x7";break;case 65454:strName="str:0x28 0x1 0x9";break;case 65455:strName="str:0x28 0x1 0xB";break;case 65456:strName="str:0x28 0x1 0xD";break;case 65457:strName="str:0x28 0x1 0xF";break;}
var inputText="<input type=password class='si'"+" size="+iSize+" maxlength="+iSize+" name='"+strName+"'>";inputLink.parentNode.innerHTML=inputText;return true;}
function GetHashCode(str){var hashValue=0;if(str==null||str.length==0)
return hashValue;for(var i=0;i<str.length;i++){var c=str.charCodeAt(i);hashValue=((hashValue<<5)-hashValue)+c;hashValue=hashValue&hashValue;}
return hashValue;}
function findPos(obj,commonOffsetParent){var curleft=0,curtop=0;if(obj&&obj.offsetParent){do{curleft+=obj.offsetLeft;curtop+=obj.offsetTop;}while((obj=obj.offsetParent)&&obj!=null&&obj.tagName!='BODY'&&obj!=commonOffsetParent);}
return{left:curleft,top:curtop};}
var _currentOpenDropdown=null;function showDropdown(e,el,id){var docInp=getFrameDocumentById("Input");var dropdown=docInp.getElementById(id);el.blur();if(_currentOpenDropdown!=null){var isCurrent=_currentOpenDropdown==dropdown;docInp.onclick();if(isCurrent)
return;}
var pos=findPos(el,dropdown.offsetParent);dropdown.style.left=pos.left;dropdown.style.top=pos.top+el.offsetHeight;dropdown.style.minWidth=el.offsetWidth-2;dropdown.style.display='block';if(pos.left+dropdown.offsetWidth>docInp.body.clientWidth){dropdown.style.left=pos.left+el.offsetWidth-dropdown.offsetWidth;}
_currentOpenDropdown=dropdown;var prevOnClick=docInp.onclick;docInp.onclick=function(){dropdown.style.display='none';docInp.onclick=prevOnClick;_currentOpenDropdown=null;};if(e.stopPropagation){e.stopPropagation();}else{e.cancelBubble=true;}}
function setDropdownValue(id,val,html){var docInp=getFrameDocumentById("Input");var dropdown=docInp.getElementById(id);dropdown.innerHTML=html;docInp.getElementById(id+'-value').value=val;docInp.getElementById(dropdown.href.substring(dropdown.href.indexOf('#')+1)).style.display='none';}
function BIE(inputLink)
{var bUseLimits=false;var attr=inputLink.getAttribute("name");var strValue=attr?attr:inputLink.innerHTML;attr=inputLink.getAttribute("lv");var iLevel=attr?parseInt(attr):255;attr=inputLink.getAttribute("ll");var iLow=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;attr=inputLink.getAttribute("hl");var iHigh=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;attr=inputLink.getAttribute("of");var iOffset=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;attr=inputLink.getAttribute("mi");var strName=attr?attr:"";attr=inputLink.getAttribute("e");var strEnum=attr?attr:"";attr=inputLink.getAttribute("lg");var strLang=attr?attr:"";attr=inputLink.getAttribute("li");var iLang=attr?parseInt(attr,10):-2;var bReplace=(iLevel>=GSL());if(bReplace)
{strName=EvalMemId(strName);var iStart=0;var iEnd=-1;if(bUseLimits)
{iStart=iLow+iOffset;iEnd=iHigh+iOffset;if(iStart<0)iStart=0;}
if(!strEnum)
{if(iLang<0)
iLang=parseInt(GL());var arrTexts=getRoot().languages[strLang];if(iLang>=arrTexts.length)
iLang=0;strEnum=arrTexts[iLang];}
var enumValue=GetEnum(strEnum);if(bUseLimits){if(iEnd>=enumValue.length)
iEnd=enumValue.length-1;}
else{iEnd=enumValue.length-1;}
var bBuildIcon=false;var inputText="<select name='"+strName+"' class='ei' size=1>";for(var i=iStart;iEnd<0||(iEnd>=0&&i<=iEnd);i++)
{if(i>=enumValue.length)
break;var enumValueIndex=enumValue[i];if(enumValueIndex=="??")
continue;var strEnumValueMask=MaskUserChar(enumValueIndex);if(strEnumValueMask!=enumValueIndex){bBuildIcon=true;break;}
var iValue=bUseLimits?(i-iOffset):i;if(enumValueIndex==strValue)
inputText=inputText+"<option selected value="+iValue+">"+
strEnumValueMask+"</option>";else
inputText=inputText+"<option value="+iValue+">"+
strEnumValueMask+"</option>";}
inputText=inputText+"</select>";if(bBuildIcon)
{var tempID="ID"+GetHashCode(strName);var iCurrentValue=0;inputText="<ul id='"+tempID+"-menu' class='dropdown-menu' style='display:none'><li></li>";for(var i=iStart;iEnd<0||(iEnd>=0&&i<=iEnd);i++)
{if(i>=enumValue.length)
break;var enumValueIndex=enumValue[i];if(enumValueIndex=="??")
continue;var iValue=bUseLimits?(i-iOffset):i;if(enumValueIndex==strValue)
iCurrentValue=iValue;enumValueIndex=MaskUserChar(enumValueIndex);if(!(enumValueIndex.replace(/^\s+$/,'')))
enumValueIndex='&nbsp;';inputText=inputText+"<li><a href='#"+iValue+"' onclick=\"setDropdownValue('"+tempID+"', "+"this.href.substring(this.href.indexOf('#') + 1), this.innerHTML); return false\">"+
enumValueIndex+"</a></li>";}
inputText=inputText+"</ul>";if(strValue)
strValue=MaskUserChar(strValue);else
strValue='&nbsp;';inputText=inputText+"<input type='hidden' id='"+tempID+"-value"+"' name='"+strName+"' value='"+iCurrentValue+"' />"+"<a class='dropdown' id='"+tempID+"' href='#"+tempID+"-menu' "+"onclick=\"showDropdown(event, this, this.href.substring(this.href.indexOf('#') + 1)); "+"return false\">"+strValue+"</a>";}
inputLink.parentNode.innerHTML=inputText;}
return bReplace;}
function BIB(inputLink)
{var strValue=inputLink.innerHTML;var attr=inputLink.getAttribute("id");var inputId=attr?attr:"";attr=inputLink.getAttribute("lv");var iLevel=attr?parseInt(attr):255;attr=inputLink.getAttribute("mi");var strName=attr?attr:"";attr=inputLink.getAttribute("e");var strEnum=attr?attr:"";var bReplace=(iLevel>=GSL());if(bReplace)
{strName=EvalMemId(strName);strName=strName.replace("bit","val");var inputText="";var iValue=parseInt(strValue);var aBF=strEnum.split('#');for(var i=0;i<aBF.length;i++)
{if(aBF[i]=="-")
break;inputText+="<input type='checkbox' name='bit' class='bi' value="+i;var bChecked=((iValue>>i)&1)!=0;if(bChecked)
inputText+=" checked";inputText+="> "+aBF[i]+"<br>";}
inputText+="<input type='hidden' name='bitval' value='"+strName+"'>";inputLink.parentNode.innerHTML=inputText;}
return bReplace;}
function CIT(lineId,tableId)
{var docHMI=getFrameDocumentById("HMI");var docInp=getFrameDocumentById("Input");if(null!=docHMI&&null!=docInp)
{var tableTagSrc=docHMI.getElementById(lineId);var tableTextSrc=tableTagSrc.innerHTML;var tableTagDst=docInp.getElementById("LineInput");tableTagDst.innerHTML=tableTextSrc;var tableInput=docInp.getElementById(tableId);tableInput.style.tableLayout="auto";tableInput.style.width=440+"px";var inputFields=docInp.getElementsByTagName("span");var inputLinkAvailable=false;var j=0;while(j<inputFields.length)
{var bReplaced=false;var inputLink=inputFields[j];if(inputLink&&inputLink.getAttribute("id"))
{inputLink.parentNode.removeAttribute("width");var inputType=inputLink.getAttribute("it");switch(inputType)
{case"v":bReplaced=BIV(inputLink);if(bReplaced)
inputLinkAvailable=true;break;case"e":bReplaced=BIE(inputLink);break;case"b":bReplaced=BIB(inputLink);break;case"pw":bReplaced=BIP(inputLink);if(bReplaced)
inputLinkAvailable=true;break;}}
if(bReplaced)j=0;else j++;}
CIPE();OpenEditor();}}
function CheckLimits(iValue,iLow,iHigh)
{iValue=parseFloat(iValue);var docInp=getFrameDocumentById("Input");;if(null!=docInp)
{var tagError=docInp.getElementById('Error');if(iValue<iLow)
{tagError.innerHTML="&nbsp;Value is too small !";return false;}
if(iValue>iHigh)
{tagError.innerHTML="&nbsp;Value is too high !";return false;}}
return true;}
function EvalLimits(iValue,bUseLimits,iLow,iHigh,iOffset,iMax)
{var iIndex=iValue+iOffset;if(iIndex>=0&&iIndex<=iMax)
{if(bUseLimits)
{if(iValue<iLow)iIndex=iLow+iOffset;if(iValue>iHigh)iIndex=iHigh+iOffset;}}
else
{if(iIndex<0)
{if(bUseLimits)
iIndex=iLow+iOffset;else
iIndex=0;}
if(iIndex>iMax)
{if(bUseLimits)
iIndex=iHigh+iOffset
else
iIndex=iMax;}}
if(iIndex<0)iIndex=0;if(iIndex>iMax)iIndex=iMax;return iIndex;}
function HI(queryId,hideId)
{var docHMI=getFrameDocumentById("HMI");;if(null!=docHMI)
{var tagQuery=docHMI.getElementById(queryId);var tagHide=docHMI.getElementById(hideId);if(tagQuery!=null&&tagHide!=null)
{var textQuery=trimText(tagQuery.innerHTML);if(textQuery.length==0)
tagHide.style.visibility="hidden";else
tagHide.style.visibility="visible";}}}
function CheckForm()
{var inputTag=getFrameDocumentById("Input").getElementsByTagName("input");var iNum=inputTag.length;for(var j=0;j<iNum;j++)
{var inputLink=inputTag[j];var bUseLimit=false;var attr=inputLink.getAttribute("ll");var iLowLimit=attr?attr:0;bUseLimit=attr?true:bUseLimit;attr=inputLink.getAttribute("hl");var iHighLimit=attr?attr:0;bUseLimit=attr?true:bUseLimit;attr=inputLink.getAttribute("hn");var strNan=attr?attr:GetDefaultNaN();var bHasNAN=attr?true:false;attr=inputLink.getAttribute("li");var iLang=attr?parseInt(attr,10):-2;if(bUseLimit)
{var iValue=inputLink.value;if(!CheckLimits(iValue,iLowLimit,iHighLimit))
{inputLink.focus();return false;}}
if(bHasNAN)
{try
{var arrTexts=getRoot().languages[strNan];if(iLang<0)
iLang=parseInt(getFrameWindowById("Input").GL());if(iLang>=arrTexts.length)
iLang=0;strNan=trimText(arrTexts[iLang]);}
catch(Error)
{strNan=GetDefaultNaN();}
var strValue=trimText(inputLink.value);if(strValue.toLowerCase()=="null"||0==strValue.indexOf("*")||0==strNan.indexOf(strValue))
inputLink.value="nan";}}
return true;}
function SubmitForm()
{var inputDoc=getFrameDocumentById("Input");if(null!=inputDoc&&CheckForm())
inputDoc.getElementById('Input').submit();}
function ClearForm()
{var inputDoc=getFrameDocumentById("Input");if(null!=inputDoc)
inputDoc.getElementById('Input').reset();}
function JTP(strUrl)
{CIPE();var locHMI=getFrameWindowById("HMI").location;if(null!=locHMI)
{if(xmlHttp!=null&&processing)
{processing=false;xmlHttp.abort();xmlHttp=null;}!!httpTimeout&&window.clearTimeout(httpTimeout);getRoot().document.getElementById("busy").style.display="";if(locHMI.pathname.indexOf("HMI65400"+FileExt())>=0&&strUrl.indexOf("HMI00001"+FileExt())>=0)
{locHMI.href=strUrl+"?pwd=";}
else
locHMI.href=strUrl;}}
function OnLoadInput()
{var parInp=getFrameWindowById("Input");if(null!=parInp)
{if(!!parInp.location.search)
{if(0==ParseBF())
{if(isPwInput())
GoHome();else
RefreshPage();}}}}
function RefreshPage(){var parHMI=getFrameWindowById("HMI");if(null!=parHMI){getRoot().document.getElementById("busy").style.display="";parHMI.location.reload();}}
function ParseBF(){var iRet=0;var parInp=getFrameWindowById("Input");if(null!=parInp){var iBit=0;var strSearch="";var aArgs=unescape(parInp.location.search).slice(1).split('&');for(var i=0;i<aArgs.length;i++){var iDelim=aArgs[i].indexOf('=');var strArg=aArgs[i].slice(0,iDelim);var strValue=aArgs[i].slice(iDelim+1);switch(strArg){case"bit":var iValue=parseInt(strValue);iBit|=(1<<iValue);break;case"bitval":if(strSearch.length>0)
strSearch+="&";strSearch+=escape(strValue)+"="+iBit;iBit=0;iRet++;break;}}
if(strSearch.length>0)
parInp.location.search='?'+strSearch;}
return iRet;}
function isPwInput()
{var strPar=GetUrlParameter(getFrameWindowById("Input").location.href,"pwd","=");var bPwInput=(strPar!="");return bPwInput;}
function RefreshInputPage()
{var parInp=getFrameWindowById("Input");if(null!=parInp){parInp.window.location.reload();}}
function GoHome()
{var docHMI=getFrameDocumentById("HMI");if(null!=docHMI)
{var tag=docHMI.getElementById("a0");if(tag)
{var hrefAttr=unescape(tag.href);eval(hrefAttr);}
else
{JTP('HMI00001'+FileExt());}}}
function GoAlarm()
{JTP('HMI65000'+FileExt());}
function CIP(){var inputDoc=getFrameDocumentById("Input");var hmiDoc=getFrameDocumentById("HMI");var title=hmiDoc.getElementById("d0");getRoot().document.getElementById('displyuppermiddle').innerHTML=MaskUserChar(title.innerHTML);title.innerHTML="";if(null!=inputDoc){var tagError=inputDoc.getElementById("Error");if(null!=tagError){var errorText=trimText(tagError.innerHTML);if(errorText.length==0)
CloseEditor();}
var tagLI=inputDoc.getElementById('LineInput');if(null!=tagLI)
tagLI.innerHTML="<table><tr><td>&nbsp;</td></tr></table>";var tag=getRoot().document.getElementById('inputeditorcontrolbuttons');if(tag)
tag.style.visibility="hidden";}}
function CIPE()
{var inputDoc=getFrameDocumentById("Input");if(null!=inputDoc)
{var tagErr=inputDoc.getElementById('Error');if(null!=tagErr)
tagErr.innerHTML="&nbsp;";}}
function JI(strPage)
{CIPE();var hmiLoc=getFrameWindowById("HMI").location;hmiLoc.href=strPage+hmiLoc.search;}
function AddTrendLinks(){var doc=getFrameDocumentById("HMI");if(doc){var elems=doc.getElementsByTagName("span");if(elems){for(var i=0;i<elems.length;i++){var elem=elems[i];elem.legendName="";if(elem.parentNode&&elem.parentNode.className=="v"){if(elem.parentNode.parentNode&&elem.parentNode.parentNode.firstElementChild&&elem.parentNode.parentNode.firstElementChild.firstElementChild){elem.legendName=elem.parentNode.parentNode.firstElementChild.firstElementChild.innerHTML;}
elem.className="trendvalue";if(elem.legendName.length<=0)
elem.legendName="-------";elem.onclick=function(){if(HasTrend())
getRoot().AddToTrend(this.id,this.legendName);};}}}}}
function DL(){getRoot().BuildLanguages();PP();CIP();THT();AddTrendLinks();getRoot().document.getElementById("busy").style.display="none";}
function HideEmptyLine(tagLine){if(tagLine){var tagItems=tagLine.getElementsByTagName("span");var iNumItems=tagItems.length;for(var i=0;i<iNumItems;i++){var tagText=tagItems[i].innerHTML;if(tagText.indexOf("+++?42?+++")>=0)
return false;}}
return true;}
function HEL(){var frame=getFrameDocumentById("HMI");if(frame){var tagLines=frame.getElementsByTagName("div");var iNumLines=tagLines.length;for(var l=0;l<iNumLines;l++){var tagline=tagLines[l];tagline.style.display=HideEmptyLine(tagline)?"block":"none";}}
var line=getRoot().document.getElementById('displyuppermiddle');if(!HideEmptyLine(line))
line.innerHTML="";}
function HELK(divId,editId){var frameHMI=getFrameDocumentById("HMI");if(frameHMI){var docDiv=frameHMI.getElementById(divId);var docEdit=frameHMI.getElementById(editId);if(null!=docDiv&&null!=docEdit){var inputFields=docDiv.getElementsByTagName("span");var inputNum=inputFields.length;var showEditLink=false;for(var j=0;j<inputNum;j++){var inputLink=inputFields[j];if(inputLink){var attr=inputLink.getAttribute("it");if(attr){if(attr=="pw"){showEditLink=true;break;}}
attr=inputLink.getAttribute("lv");if(attr){var rqstLevel=parseInt(attr);var actLevel=GSL();if(rqstLevel>=actLevel){showEditLink=true;break;}}}}
if(!showEditLink)
docEdit.innerHTML="";}}}
function HLK(linkId){var tableLink=getFrameDocumentById("HMI").getElementById(linkId);if(tableLink){var attr=tableLink.getAttribute("lv");var rqstLevel=attr?parseInt(attr,10):-1;var actLevel=GSL();if(rqstLevel<actLevel)
tableLink.innerHTML="";}}
function HLL(lineId,rqstLevel)
{var actLevel=GSL();if(rqstLevel<actLevel)
{var tableLink=getFrameDocumentById("HMI").getElementById(lineId);if(tableLink)
{tableLink.innerHTML="";tableLink.style.position="absolute";}}}
function HAI(inputId,applids)
{var actId=GAI();if(0==actId)
return;var iLastIndex=0;var applIdIndex="";for(var i=0;1;i++)
{applIdIndex="";var iPos=applids.indexOf(',',iLastIndex);if(iPos<0)
break;applIdIndex=applids.substr(iLastIndex,iPos-iLastIndex);iLastIndex=iPos+1;if(applIdIndex==actId)
break;}
if(applIdIndex=="")
{var inputLink=getFrameDocumentById("HMI").getElementById(inputId);if(inputLink)
{inputLink.innerHTML=""
inputLink.style.position="absolute";}}}
function SIL(inputId,rqstLevel)
{var actLevel=GSL();if(actLevel>rqstLevel){var inputLink=getFrameDocumentById("HMI").getElementById(inputId);if(inputLink){var attr=inputLink.getAttribute("v");var inputValue=attr?attr:"";inputLink.parentNode.innerHTML=inputValue;}}}
function BEV(tagId)
{var parHMI=getFrameWindowById("HMI");if(null!=parHMI)
{var tag=getFrameDocumentById("HMI").getElementById(tagId);if(tag)
{if(tag.innerHTML.indexOf("***")>=0)
return;var attr=tag.getAttribute("e");var enumValue=attr?attr:"";attr=tag.getAttribute("ll");var iLowLimit=attr?parseInt(attr,10):0;var bUseLimits=attr?true:false;attr=tag.getAttribute("hl");var iHighLimit=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;attr=tag.getAttribute("of");var iOffset=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;enumValue=GetEnum(enumValue);var iValue=parseInt(tag.innerHTML,10);var iMax=enumValue.length-1;var iIndex=EvalLimits(iValue,bUseLimits,iLowLimit,iHighLimit,iOffset,iMax);tag.innerHTML=enumValue[iIndex];}}}
function GetEnum(strEnum)
{var aEnum=new Array();var strItem="";var iItem=0;for(var i=0;i<strEnum.length;i++)
{var ch=strEnum.charAt(i);switch(ch)
{case'\\':i++;if(i<strEnum.length)
strItem+=strEnum.charAt(i);break;case'*':aEnum[iItem++]=strItem;strItem="";break;default:strItem+=ch;}}
if(strItem.length>0)
aEnum[iItem++]=strItem;return aEnum;}
function BEVL(tagId)
{var docHMI=getFrameDocumentById("HMI");if(null!=docHMI)
{var tag=docHMI.getElementById(tagId);if(tag){if(tag.innerHTML.indexOf("***")>=0)
return;var bUseLimits=false;var attr=tag.getAttribute("ll");var iLowLimit=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;attr=tag.getAttribute("hl");var iHighLimit=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;attr=tag.getAttribute("of");var iOffset=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;attr=tag.getAttribute("lg");var strLang=attr?attr:null;attr=tag.getAttribute("li");var iLang=attr?parseInt(attr,10):-2;if(iLang<0)
iLang=parseInt(GL());if(strLang){var arrTexts=getRoot().languages[strLang];if(iLang>=arrTexts.length)
iLang=0;var text=arrTexts[iLang];var enumValue=GetEnum(text);var iValue=parseInt(tag.innerHTML,10);var iMax=enumValue.length-1;var iIndex=EvalLimits(iValue,bUseLimits,iLowLimit,iHighLimit,iOffset,iMax);tag.innerHTML=enumValue[iIndex];}}}}
function BTL(tagId)
{var tag=getFrameDocumentById("HMI").getElementById(tagId);if(tag)
{if(tag.innerHTML.indexOf("***")>=0)
return;var attr=tag.getAttribute("lg");var strLang=attr?attr:null;attr=tag.getAttribute("li");var iLang=attr?parseInt(attr,10):-2;if(iLang<0)
iLang=parseInt(GL());if(strLang)
{var arrTexts=getRoot().languages[strLang];if(iLang>=arrTexts.length)
iLang=0;var text=arrTexts[iLang];tag.innerHTML=text;}}}
function PrintNaN(tag)
{if(!!tag)
{var iValue=tag.innerHTML;if(trimText(iValue.toLowerCase())=="nan")
{var attr=tag.getAttribute("sz");var iSize=attr?parseInt(attr,10):0;attr=tag.getAttribute("hn");var strNan=attr?attr:GetDefaultNaN();attr=tag.getAttribute("li");var iLang=attr?parseInt(attr,10):-2;if(strNan&&iSize>0)
{try
{var arrTexts=getRoot().languages[strNan];if(iLang<0)
iLang=parseInt(GL());if(iLang>=arrTexts.length)
iLang=0;var nullvalue=trimText(arrTexts[iLang]);tag.setAttribute('name',nullvalue);tag.innerHTML=nullvalue.substring(0,iSize);}
catch(Error)
{tag.innerHTML="*";}}}}}
function HN(tagId){var tag=getFrameDocumentById("HMI").getElementById(tagId);if(tag){PrintNaN(tag);}}
function TR(tagId){var tag=getFrameDocumentById("HMI").getElementById(tagId);if(tag){var attr=tag.getAttribute("sz");var iSize=attr?parseInt(attr,10):0;var strValue=tag.innerHTML;if(strValue.length>iSize){strValue=strValue.substring(strValue.length-iSize);tag.innerHTML=strValue;}}}
function TL(tagId){var tag=getFrameDocumentById("HMI").getElementById(tagId);if(tag){var attr=tag.getAttribute("sz");var iSize=attr?parseInt(attr,10):0;var strValue=tag.innerHTML;if(strValue.length>iSize){strValue=strValue.substring(0,iSize);tag.innerHTML=strValue;}}}
function BuildRightValue(tagId)
{var tag=getFrameWindowById("HMI").getElementById(tagId);if(tag)
{}}
function DoLogonoff(){var secValue=document.getElementById("displyupperleft");var loggedIn=secValue.innerHTML.length==0?false:true;var locHMI=document.getElementById("HMI");if(!loggedIn&&(locHMI!=null))
locHMI.src="./HMI65410"+FileExt();else
locHMI.src="./HMI00001"+FileExt()+"?pwd=";}
function GetUrlParameter(strUrl,name,delim){var strRet="";strUrl=unescape(strUrl);if(strUrl.length>0){name=name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");var regexS="[\\?&]"+name+delim+"([^&#]*)";var regex=new RegExp(regexS);var results=regex.exec(strUrl);if(results!=null)
strRet=unescape(results[1]);}
return strRet;}
var xmlHttp=null;var processing=false;var editorOpen=false;var autoRefreshValueTime=2000;var httpTimeout=null;function AutoRefresh()
{if(processing||editorOpen)
return false;processing=true;var url="";var parHMI=getFrameWindowById("HMI");if(parHMI!=null&&typeof(parHMI.window.GFR)=='function')
{var sstr=parHMI.window.location.search;url=parHMI.window.GFR()+sstr;}
if(url.length<=0)
{processing=false;httpTimeout=setTimeout(AutoRefresh,autoRefreshValueTime);return;}
xmlHttp=GetXMLHttpRequest();if(xmlHttp!=null)
{xmlHttp.open("GET",url,true);xmlHttp.onreadystatechange=StateChangedHandler;xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");xmlHttp.send(null);}}
function SAR()
{httpTimeout=setTimeout(AutoRefresh,autoRefreshValueTime);}
function StateChangedHandler()
{if(null!=xmlHttp)
{switch(xmlHttp.readyState)
{case 4:if(xmlHttp.status!=200)
{processing=false;httpTimeout=setTimeout(AutoRefresh,autoRefreshValueTime);}
else
{DoWork(xmlHttp);}
break;default:return false;break;}}}
function DoWork(xmlHttp){var xmlDoc=xmlHttp.responseText;if(xmlDoc.length<=0){processing=false;httpTimeout=setTimeout(AutoRefresh,autoRefreshValueTime);return;}
xmlDoc=escape(xmlDoc);xmlDoc=xmlDoc.replace(/%0D/g,"");xmlDoc=xmlDoc.replace(/%0A/g,"");xmlDoc=unescape(xmlDoc);var entries=xmlDoc.split("|");for(var i=0;i<entries.length;i++){if(entries[i].length>0){var entry=entries[i].split(",");var ElementID=entry[0];var ElementType=entry[1];var ElementData=entry[2];var ElementHide=null;if(entry.length>3)
ElementHide=entry[3];if(ElementID.length>0){var parHMI=getFrameDocumentById("HMI");if(parHMI!=null){var htmlElement=parHMI.getElementById(ElementID);if(htmlElement!=null){htmlElement.innerHTML=ElementData;htmlElement.setAttribute('name',ElementData);if(ElementHide!=null){htmlElement=parHMI.getElementById(ElementHide);if(null!=htmlElement){var textData=trimText(ElementData);htmlElement.style.visibility=textData.length==0?"hidden":"visible";}}
if(ElementData!=null&&ElementData.indexOf("+++?42?+++")>=0)
continue;if(ElementData!=null&&ElementData.indexOf("***")>=0)
continue;switch(ElementType){case"e":BuildEnumRead(ElementID);break;case"v":BuildValueRead(ElementID,false);break;case"vr":BuildValueRead(ElementID,false);TR(ElementID);htmlElement.setAttribute('name',htmlElement.innerHTML);break;case"n":BuildValueRead(ElementID,true);break;}}}}}}
HEL();THT();processing=false;httpTimeout=setTimeout(AutoRefresh,autoRefreshValueTime);}
function GetXMLHttpRequest()
{try{xmlHttp=new XMLHttpRequest();}catch(e){try
{xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");}catch(e){try{xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");}catch(e){return null;}}}
return xmlHttp;}
function BuildValueRead(tagId,hasnan)
{var docHMI=getFrameDocumentById("HMI");if(null!=docHMI)
{var tag=docHMI.getElementById(tagId);if(tag&&hasnan)
{PrintNaN(tag);}}}
function BuildEnumRead(tagId){var frame=getFrameWindowById("HMI");var doc=getFrameDocumentById("HMI");if(frame&&doc){var tag=doc.getElementById(tagId);if(tag){if(tag.innerHTML.indexOf("***")>=0)
return;if(tag.attributes==null)
return;var attr=tag.getAttribute("e");var strEnum=attr?attr:"";attr=tag.getAttribute("of");var iOffset=attr?parseInt(attr,10):0;var bUseLimits=attr?true:false;attr=tag.getAttribute("ll");var iLowLimit=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;attr=tag.getAttribute("hl");var iHighLimit=attr?parseInt(attr,10):0;bUseLimits=attr?true:bUseLimits;attr=tag.getAttribute("lg");var strLang=attr?attr:"";attr=tag.getAttribute("li");var iLang=attr?parseInt(attr,10):-2;var iValue=parseInt(tag.innerHTML,10);if(!strEnum)
{var arrTexts=getRoot().languages[strLang];if(iLang<0)
iLang=parseInt(frame.window.GL());if(iLang>=arrTexts.length)
iLang=0;strEnum=arrTexts[iLang];}
var enumValue=GetEnum(strEnum);var iMax=enumValue.length-1;var iIndex=EvalLimits(iValue,bUseLimits,iLowLimit,iHighLimit,iOffset,iMax);var text=enumValue[iIndex];tag.setAttribute('name',text);text=MaskUserChar(text);tag.innerHTML=text;}}}
var xmlHttpAlarmRequest=null;var autoCheckAlarmTime=5000;function CheckAlarmState()
{xmlHttpAlarmRequest=GetXMLHttpRequest();if(xmlHttpAlarmRequest!=null)
{var url="HMIAlarmRead"+FileExt();xmlHttpAlarmRequest.open("GET",url,true);xmlHttpAlarmRequest.onreadystatechange=AlarmStateHandler;xmlHttpAlarmRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded");xmlHttpAlarmRequest.send(null);return;}
setTimeout(CheckAlarmState,autoCheckAlarmTime);}
function SAS()
{oldAlarmState=-1;oldInfoState=-1;CheckAlarmState();}
var oldAlarmState=-1;var oldInfoState=-1;function AlarmStateHandler()
{if(null!=xmlHttpAlarmRequest)
{switch(xmlHttpAlarmRequest.readyState)
{case 4:if(xmlHttpAlarmRequest.status!=200)
{}
else
{if((xmlHttpAlarmRequest.responseText!=null)&&(xmlHttpAlarmRequest.responseText.length>0))
{try
{var xmlDoc=xmlHttpAlarmRequest.responseText;if(xmlDoc.length>0)
{xmlDoc=escape(xmlDoc);xmlDoc=xmlDoc.replace(/%0D/g,"");xmlDoc=xmlDoc.replace(/%0A/g,"");xmlDoc=unescape(xmlDoc);var entries=xmlDoc.split("|");var alarmState=-1;var infoState=-1;if(entries.length>0)
{if((entries[1].indexOf("+++?42?+++")>=0)||(entries[1].indexOf("***")>=0)||(entries[1]=="0"))
{alarmState=parseInt(entries[0]);setAlarmButton(alarmState);}
else
{alarmState=parseInt(entries[1]);setExtAlarmButton(alarmState);}
if((entries[2].indexOf("+++?42?+++")>=0)||(entries[2]=="***"))
infoState=0;else
infoState=parseInt(entries[2]);if(oldInfoState!=infoState)
{setExtInfoButton(infoState);oldInfoState=infoState;}}}}
catch(Error)
{}}}
setTimeout(CheckAlarmState,autoCheckAlarmTime);break;default:return false;break;}}}
function setAlarmButton(alarmState)
{var tag=document.getElementById("alarmbutton");if(null!=tag)
{switch(alarmState)
{case 0:tag.className="hmibuttonnormal";break;case 1:tag.className="hmibuttonalarmactive";break;case 2:tag.className="hmibuttonalarmnotcritical";break;default:break;}}}
function setExtAlarmButton(alarmStateParam)
{var tag=document.getElementById("alarmbutton");setHmiButton(tag,alarmStateParam);}
function setExtInfoButton(infoStateParam)
{var tag=document.getElementById("infobutton");setHmiButton(tag,infoStateParam);}
function setHmiButton(tag,state)
{if(null!=tag)
{var red1On=((state&0x01)!=0);var red1Flashing=((state&0x02)!=0);var green1On=((state&0x10)!=0);var green1Flashing=((state&0x20)!=0);var red1Off=(red1On&&red1Flashing);var red1DontChange=(!red1On&&!red1Flashing);var green1Off=green1On&&green1Flashing;var green1DontChange=(!green1On&&!green1Flashing);if(red1DontChange&&green1DontChange);else if(red1Off&&green1Off)
tag.className="hmibuttonnormal";else if(red1Off&&green1On)
tag.className="hmibuttongreenon";else if(red1Off&&green1Flashing)
tag.className="hmibuttongreenflashing";else if(red1On&&green1Off)
tag.className="hmibuttonredon";else if(red1Flashing&&green1Off)
tag.className="hmibuttonredflashing";else if(red1DontChange&&green1Off)
{if(tag.className.indexOf("hmibuttonnormal")>=0)
tag.className="hmibuttonnormal";else if(tag.className.indexOf("hmibuttonredon")>=0)
tag.className="hmibuttonredon";else if(tag.className.indexOf("hmibuttonredflashing")>=0)
tag.className="hmibuttonredflashing";else if(tag.className.indexOf("hmibuttongreenon")>=0)
tag.className="hmibuttonnormal";else if(tag.className.indexOf("hmibuttongreenflashing")>=0)
tag.className="hmibuttonnormal";else if(tag.className.indexOf("hmibuttonyellowon")>=0)
tag.className="hmibuttonredon";else if(tag.className.indexOf("hmibuttonyellowflashing")>=0)
tag.className="hmibuttonredflashing";else if(tag.className.indexOf("hmibuttonyellowredflashing")>=0)
tag.className="hmibuttonredon";else if(tag.className.indexOf("hmibuttonyellowgreenflashing")>=0)
tag.className="hmibuttonredflashing";}
else if(red1DontChange&&green1On)
{if(tag.className.indexOf("hmibuttonnormal")>=0)
tag.className="hmibuttongreenon";else if(tag.className.indexOf("hmibuttonredon")>=0)
tag.className="hmibuttonyellowon";else if(tag.className.indexOf("hmibuttonredflashing")>=0)
tag.className="hmibuttonyellowgreenflashing";else if(tag.className.indexOf("hmibuttongreenon")>=0)
tag.className="hmibuttongreenon";else if(tag.className.indexOf("hmibuttongreenflashing")>=0)
tag.className="hmibuttongreenon";else if(tag.className.indexOf("hmibuttonyellowon")>=0)
tag.className="hmibuttonyellowon";else if(tag.className.indexOf("hmibuttonyellowflashing")>=0)
tag.className="hmibuttonyellowgreenflashing";else if(tag.className.indexOf("hmibuttonyellowredflashing")>=0)
tag.className="hmibuttonyellowon";else if(tag.className.indexOf("hmibuttonyellowgreenflashing")>=0)
tag.className="hmibuttongreenon";}
else if(red1DontChange&&green1Flashing)
{if(tag.className.indexOf("hmibuttonnormal")>=0)
tag.className="hmibuttongreenflashing";else if(tag.className.indexOf("hmibuttonredon")>=0)
tag.className="hmibuttonyellowredflashing";else if(tag.className.indexOf("hmibuttonredflashing")>=0)
tag.className="hmibuttonyellowflashing";else if(tag.className.indexOf("hmibuttongreenon")>=0)
tag.className="hmibuttongreenflashing";else if(tag.className.indexOf("hmibuttongreenflashing")>=0)
tag.className="hmibuttongreenflashing";else if(tag.className.indexOf("hmibuttonyellowon")>=0)
tag.className="hmibuttonyellowredflashing";else if(tag.className.indexOf("hmibuttonyellowflashing")>=0)
tag.className="hmibuttonyellowflashing";else if(tag.className.indexOf("hmibuttonyellowredflashing")>=0)
tag.className="hmibuttonyellowredflashing";else if(tag.className.indexOf("hmibuttonyellowgreenflashing")>=0)
tag.className="hmibuttonyellowflashing";}
else if(red1Off&&green1DontChange)
{if(tag.className.indexOf("hmibuttonnormal")>=0)
tag.className="hmibuttonnormal";else if(tag.className.indexOf("hmibuttonredon")>=0)
tag.className="hmibuttonnormal";else if(tag.className.indexOf("hmibuttonredflashing")>=0)
tag.className="hmibuttonnormal";else if(tag.className.indexOf("hmibuttongreenon")>=0)
tag.className="hmibuttongreenon";else if(tag.className.indexOf("hmibuttongreenflashing")>=0)
tag.className="hmibuttongreenflashing";else if(tag.className.indexOf("hmibuttonyellowon")>=0)
tag.className="hmibuttongreenon";else if(tag.className.indexOf("hmibuttonyellowflashing")>=0)
tag.className="hmibuttongreenflashing";else if(tag.className.indexOf("hmibuttonyellowredflashing")>=0)
tag.className="hmibuttongreenflashing";else if(tag.className.indexOf("hmibuttonyellowgreenflashing")>=0)
tag.className="hmibuttongreenon";}
else if(red1On&&green1DontChange)
{if(tag.className.indexOf("hmibuttonnormal")>=0)
tag.className="hmibuttonredon";else if(tag.className.indexOf("hmibuttonredon")>=0)
tag.className="hmibuttonredon";else if(tag.className.indexOf("hmibuttonredflashing")>=0)
tag.className="hmibuttonredon";else if(tag.className.indexOf("hmibuttongreenon")>=0)
tag.className="hmibuttonyellowon";else if(tag.className.indexOf("hmibuttongreenflashing")>=0)
tag.className="hmibuttonyellowredflashing";else if(tag.className.indexOf("hmibuttonyellowon")>=0)
tag.className="hmibuttonyellowon";else if(tag.className.indexOf("hmibuttonyellowflashing")>=0)
tag.className="hmibuttonyellowredflashing";else if(tag.className.indexOf("hmibuttonyellowredflashing")>=0)
tag.className="hmibuttongreenflashing";else if(tag.className.indexOf("hmibuttonyellowgreenflashing")>=0)
tag.className="hmibuttonyellowon";}
else if(red1Flashing&&green1DontChange)
{if(tag.className.indexOf("hmibuttonnormal")>=0)
tag.className="hmibuttonredflashing";else if(tag.className.indexOf("hmibuttonredon")>=0)
tag.className="hmibuttonredflashing";else if(tag.className.indexOf("hmibuttonredflashing")>=0)
tag.className="hmibuttonredflashing";else if(tag.className.indexOf("hmibuttongreenon")>=0)
tag.className="hmibuttonyellowgreenflashing";else if(tag.className.indexOf("hmibuttongreenflashing")>=0)
tag.className="hmibuttonyellowflashing";else if(tag.className.indexOf("hmibuttonyellowon")>=0)
tag.className="hmibuttonyellowgreenflashing";else if(tag.className.indexOf("hmibuttonyellowflashing")>=0)
tag.className="hmibuttonyellowflashing";else if(tag.className.indexOf("hmibuttonyellowredflashing")>=0)
tag.className="hmibuttonyellowflashing";else if(tag.className.indexOf("hmibuttonyellowgreenflashing")>=0)
tag.className="hmibuttonyellowgreenflashing";}
else if(red1On&&green1On)
tag.className="hmibuttonyellowon";else if(red1Flashing&&green1On)
tag.className="hmibuttonyellowgreenflashing";else if(red1On&&green1Flashing)
tag.className="hmibuttonyellowredflashing";else if(red1Flashing&&green1Flashing)
tag.className="hmibuttonyellowflashing";}}
var xmlHttpSecLevelRequest;var autoCheckLogonStatusTime=5000;function CheckLogonStatus()
{xmlHttpSecLevelRequest=GetXMLHttpRequest();if(xmlHttpSecLevelRequest!=null)
{var url="HMISecLevelRead"+FileExt();xmlHttpSecLevelRequest.open("GET",url,true);xmlHttpSecLevelRequest.onreadystatechange=LogonStatusHandler;xmlHttpSecLevelRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded");xmlHttpSecLevelRequest.send(null);return;}
setTimeout(CheckLogonStatus,autoCheckLogonStatusTime);}
function SLS()
{CheckLogonStatus();}
function LogonStatusHandler()
{if(null!=xmlHttpSecLevelRequest)
{switch(xmlHttpSecLevelRequest.readyState)
{case 4:if(xmlHttpSecLevelRequest.status!=200)
{}
else
{if((xmlHttpSecLevelRequest.responseText!=null)&&(xmlHttpSecLevelRequest.responseText.length>0)){try
{var secLevel=parseInt(xmlHttpSecLevelRequest.responseText);setLogonStatus(secLevel);}catch(Error){}}}
setTimeout(CheckLogonStatus,autoCheckLogonStatusTime);break;default:return false;break;}}}
function setLogonStatus(secLevel)
{var secLevelLocation=document.getElementById("displyupperleft");var loginButton=document.getElementById("login");if(null!=secLevelLocation)
{if(secLevel==253){secLevelLocation.innerHTML="";loginButton.innerHTML="Login";}
else{secLevelLocation.innerHTML=secLevel;loginButton.innerHTML="Logout";}}}