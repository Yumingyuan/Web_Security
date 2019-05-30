import requests
import re
r=requests.get("http://www.wsb.com/Assignment2/case32.php",allow_redirects=False)
result=re.search('<div id="demo">(.*)</div>',r.text).group(1)
print("result:",result)
