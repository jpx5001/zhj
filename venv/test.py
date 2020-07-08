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

whitelist_config_dict = {
        "overduemorecount_limit": "1",
        "overduemoreamt_limit": "0",
        "outstandcount_limit": "5",
        "loanbal_limit": "50000",
        "overduecount_limit": "3",
        "overdueamt_limit": "10000",
        "insuranceamt_limit": "0",
        "insurancecount_limit": "0",
        "insuranceorgcount_limit": "0",
        "insurancebal_limit": "0",
        "loanorgcount_queryatotalorg_365_limit": "0.1",
        "queryatotalorg_30_limit": "30",
        "queryatotalorg_60_limit": "50",
        "queryatotalorg_180_limit": "70",
        "queryatotalorg_365_limit": "100"

    }
config_data = {}

non_whitelist_config_dict = {
    "overduemorecount_limit": "1",
    "overduemoreamt_limit": "0",
    "outstandcount_limit": "5",
    "loanbal_limit": "50000",
    "overduecount_limit": "3",
    "overdueamt_limit": "10000",
    "insuranceamt_limit": "0",
    "insurancecount_limit": "0",
    "insuranceorgcount_limit": "0",
    "insurancebal_limit": "0",
    "loanorgcount_queryatotalorg_365_limit": "0.1",
    "queryatotalorg_30_limit": "30",
    "queryatotalorg_60_limit": "50",
    "queryatotalorg_180_limit": "70",
    "queryatotalorg_365_limit": "100"
}
#dictMerge = dict(whitelist_config_dict.items()+non_whitelist_config_dict.items())

#config_data = {whitelist_config_dict.items() + non_whitelist_config_dict.items()}

str1 = json.dumps(whitelist_config_dict)
str2 = json.dumps(non_whitelist_config_dict)
config_data = {
    "whitelist" : str1,
    "non_whitelist" : str2

}
whitelist_confi = json.loads(config_data["whitelist"])
print(whitelist_confi)
print(config_data["whitelist"])
print(dict)
print(type(whitelist_config_dict))

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
