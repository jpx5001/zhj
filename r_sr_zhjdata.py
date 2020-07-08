#!/usr/bin/python
"""
@author: mm_Einstein
@software: PyCharm
@file: r_360_rs.py
@time: 2020/4/17
"""
import datetime
import json
import traceback



def days(nowdate,ddate):
    date1 = datetime.datetime.strptime(nowdate[0:10], "%Y-%m-%d")

    date2 = datetime.datetime.strptime(ddate[0:10], "%Y-%m-%d")
    num = (date1 - date2).days
    return num

def cal_dqst(init_data,data):
    infoquerybean = init_data.getString("infoquerybean")
    infoquerybean_dict = json.loads(infoquerybean)
    today = str(datetime.date.today())
    queryatotalorg_30 = 0
    queryatotalorg_90 = 0
    queryatotalorg_180 = 0
    queryatotalorg_365 = 0
    if infoquerybean_dict:#判断一下
        for item in infoquerybean_dict:
            if item["s_value"] in "贷前审批":
               day = days(today, item["ddate"])
               if day <= 30:
                queryatotalorg_30 = queryatotalorg_30 + 1

               if day <= 90:
                queryatotalorg_90 = queryatotalorg_90 + 1

               if day <= 180:
                 queryatotalorg_180 = queryatotalorg_180 + 1
               if day <= 365:
                 queryatotalorg_365 = queryatotalorg_365 + 1

    data["queryatotalorg_30"] = queryatotalorg_30
    data["queryatotalorg_90"] = queryatotalorg_90
    data["queryatotalorg_180"] = queryatotalorg_180
    data["queryatotalorg_365"] = queryatotalorg_365

    return data

class r_360_rs(object):
    def init(self, context):
        pass

    def rule(self, context):
        output = {
        "ZHJ001":"1",
        "ZHJ002": "1",
        "ZHJ003": "1",
        "ZHJ004": "1",
        "ZHJ005": "1",
        "ZHJ006": "1",
        "ZHJ007": "1",
        "ZHJ008": "1",
        "ZHJ009": "1",
        "ZHJ010": "1",
        "ZHJ011": "1",
        "ZHJ012": "1",
        "ZHJ013": "1",
        "ZHJ014": "1",
        "ZHJ015": "1"

        }
        data = {
            "overduemorecount": -999,
            "overduemoreamt": -999,
            "outstandcount": -999,
            "loanbal": -999,
            "overduecount": -999,
            "overdueamt": -999,
            "insuranceamt": -999,
            "insurancecount": -999,
            "insuranceorgcount": -999,
            "insurancebal": -999,
            "loanorgcount_queryatotalorg_365": 10000,
            "queryatotalorg_30": 0,
            "queryatotalorg_90": 0,
            "queryatotalorg_180": 0,
            "queryatotalorg_365": 0
         }
        result = context.create()
        init_data = context.get()

        #获取非白名单配置
        non_whitelist_config = init_data.getString["non_whitelist_config_dict"]
        non_whitelist_config_dict = json.loads(non_whitelist_config)

        #获取直接得到的数据参数是10个，以下为10个可以直接得到的参数
        try:
          data["overduemorecount"] = int(init_data.getString("overduemorecount"))
        except:
            pass

        try:
         data["overduemoreamt"] = int(init_data.getString("overduemoreamt"))
        except:
            pass

        try:
         data["outstandcount"] = int(init_data.getString("outstandcount"))
        except:
            pass

        try:
            data["loanbal"] = int(init_data.getString("loanbal"))
        except:
            pass

        try:
           data["overduecount"] = int(init_data.getString("overduecount"))
        except:
            pass
        try:
             data["overdueamt"] = int(init_data.getString("overdueamt"))
        except:
            pass

        try:
             data["insuranceamt"] = int(init_data.getString("insuranceamt"))
        except:
            pass

        try:
            data["insurancecount"] = int(init_data.getString("insurancecount"))
        except:
            pass

        try:
            data["insuranceorgcount"] = int(init_data.getString("insuranceorgcount"))
        except:
            pass

        try:
            data["insurancebal"] = int(init_data.getString("insurancebal"))
        except:
            pass

        #分析30天，90天，180天，365天的方法,并添加到data字典中
        cal_dqst(init_data, data)
        #添加机构数参数，用于计算 "机构数/最近一年。。。"
        try:
           loanorgcount = int(init_data.getString("loanorgcount"))
        except:
            pass
        #计算审批率
        if data["queryatotalorg_365"] is not 0:
            data["loanorgcount_queryatotalorg_365"] = (float(loanorgcount))/(float(data["queryatotalorg_365"])) ###

        try:
            if data["overduemorecount"] != -999 and data["overduemorecount"] >= int(
                    non_whitelist_config_dict["overduemorecount_limit"]):
                output["ZHJ001"] = "0"
            if data["overduemoreamt"] != -999 and data["overduemoreamt"] > int(
                    non_whitelist_config_dict["overduemoreamt_limit"]):
                output["ZHJ002"] = "0"
            if data["outstandcount"] != -999 and data["outstandcount"] >= int(
                    non_whitelist_config_dict["outstandcount_limit"]):
                output["ZHJ003"] = "0"
            if data["loanbal"] != -999 and data["loanbal"] >= int(
                    non_whitelist_config_dict["loanbal_limit"]):
                output["ZHJ004"] = "0"
            if data["overduecount"] != -999 and data["overduecount"] >= int(
                    non_whitelist_config_dict["overduecount_limit"]):
                output["ZHJ005"] = "0"
            if data["overdueamt"] != -999 and data["overdueamt"] >= int(
                    non_whitelist_config_dict["overdueamt_limit"]):
                output["ZHJ006"] = "0"

            if data["loanorgcount_queryatotalorg_365"] != -999 and data["loanorgcount_queryatotalorg_365"] <= float(
                    non_whitelist_config_dict["loanorgcount_queryatotalorg_365_limit"]):
                output["ZHJ007"] = "0"

            if data["queryatotalorg_30"] != -999 and data["queryatotalorg_30"] >= int(
                    non_whitelist_config_dict["queryatotalorg_30_limit"]):
                output["ZHJ008"] = "0"

            if data["queryatotalorg_90"] != -999 and data["queryatotalorg_90"] >= int(
                    non_whitelist_config_dict["queryatotalorg_90_limit"]):
                output["ZHJ009"] = "0"
            if data["queryatotalorg_180"] != -999 and data["queryatotalorg_180"] >= int(
                    non_whitelist_config_dict["queryatotalorg_180_limit"]):
                output["ZHJ010"] = "0"
            if data["queryatotalorg_365"] != -999 and data["queryatotalorg_365"] >= float(
                    non_whitelist_config_dict["queryatotalorg_365_limit"]):
                output["ZHJ011"] = "0"

            if data["insuranceamt"] != -999 and data["insuranceamt"] > int(
                    non_whitelist_config_dict["insuranceamt_limit"]):
                output["ZHJ0012"] = "0"

            if data["insurancecount"] != -999 and data["insurancecount"] > int(
                    non_whitelist_config_dict["insurancecount_limit"]):
                output["ZHJ0013"] = "0"

            if data["insuranceorgcount"] != -999 and data["insuranceorgcount"] > int(
                    non_whitelist_config_dict["insuranceorgcount_limit"]):
                output["ZHJ0014"] = "0"
            if data["insurancebal"] != -999 and data["insurancebal"] > int(
                    non_whitelist_config_dict["insurancebal_limit"]):
                output["ZHJ0015"] = "0"
        except:
            pass
        finally:
            score = 0 #0

            if "0" in output.values():
                score = 0   #不启用
                #result.setLong("score", 1000)

            result.setLong("score",score)
            for key, value in output.items():
                result.setString(key, value)



