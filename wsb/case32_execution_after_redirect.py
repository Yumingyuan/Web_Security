import requests
import re
r=requests.get("http://www.wsb.com/Assignment2/case32.php")
#print(r.history[0].text)
result=re.search('<div id="demo">(.*)</div>',r.history[0].text).group(1)
print(result)
