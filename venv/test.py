import json
import datetime





dict1 ="{\"non\":{\"name\":\"zhangsan\",\"age\":\"15\"},\"zheng\":{\"name\":\"zhaosi\",\"age\":\"19\"}}"
json_info = json.loads(dict1)
data = "[{\"s_value\":\"贷前审批\",\"ddate\":\"2020-05-06\",\"ordernum\":\"1\"},{\"s_value\":\"贷前审批\",\"ddate\":\"2020-07-06\",\"ordernum\":\"2\"}]"
date1=datetime.datetime.strptime("2020-08-06"[0:10],"%Y-%m-%d")
date2 =datetime.datetime.strptime("2020-07-06"[0:10],"%Y-%m-%d")
num=(date1-date2).days

data_dict = json.loads(data)
today = str(datetime.date.today())
queryatotalorg_30 = 0
queryatotalorg_90 = 0
queryatotalorg_180 = 0
queryatotalorg_365 = 0

def days(nowdate, ddate):
    date1 = datetime.datetime.strptime(nowdate[0:10], "%Y-%m-%d")

    date2 = datetime.datetime.strptime(ddate[0:10], "%Y-%m-%d")
    num = (date1 - date2).days
    return num

if data_dict:
   for item in data_dict:
    # print(item)
    # print(type(item["ddate"]))
    day = days(today,item["ddate"])
    if day <= 30:
      queryatotalorg_30 = queryatotalorg_30+1
    if day <= 90:
      queryatotalorg_90 = queryatotalorg_90 + 1


print(queryatotalorg_30)
