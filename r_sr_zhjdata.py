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
    if infoquerybean_dict:
        for item in infoquerybean_dict:
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
            "loanorgcount_queryatotalorg_365": 0,
            "queryatotalorg_30": 0,
            "queryatotalorg_90": 0,
            "queryatotalorg_180": 0,
            "queryatotalorg_365": 0
         }
        result = context.create()
        init_data = context.get("m_sr_zhjdata")
        #获取是否是白名单
        hecate_sr_whitelist = init_data.getString("hecate_sr_whitelist")
        #获取白名单配置
        whitelist_config = init_data.getString["whitelist_config_dict"]
        whitelist_config_dict = json.loads(whitelist_config)
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
            data["loanorgcount_queryatotalorg_365"] = float(loanorgcount/data["queryatotalorg_365"])

        #是否是白名单用户
        if hecate_sr_whitelist == "1":

            if data["overduemorecount"] != -999 and data["overduemorecount"] >=int(
                    whitelist_config_dict["overduemorecount"]):
                output["ZHJ001"] = "0"
            if data["overduemoreamt"] != -999 and data["overduemoreamt"] >= int(
                    whitelist_config_dict["overduemoreamt"]):
                output["ZHJ002"] = "0"
            if data["outstandcount"] != -999 and data["outstandcount"] >= int(
                whitelist_config_dict["outstandcount"]):
                output["ZHJ003"] = "0"
            if data["loanbal"] != -999 and data["loanbal"] >= int(
                    whitelist_config_dict["loanbal"]):
                output["ZHJ004"] = "0"
            if data["overduecount"] != -999 and data["overduecount"] >= int(
                    whitelist_config_dict["overduecount"]):
                output["ZHJ005"] = "0"
            if data["overdueamt"] != -999 and data["overdueamt"] >= int(
                    whitelist_config_dict["overdueamt"]):
                output["ZHJ006"] = "0"

            if data["loanorgcount_queryatotalorg_365"] != -999 and data["loanorgcount_queryatotalorg_365"] <= int(
                    whitelist_config_dict["loanorgcount_queryatotalorg_365"]):
                output["ZHJ007"] = "0"

            if data["queryatotalorg_30"] != -999 and data["queryatotalorg_30"] >= int(
                    whitelist_config_dict["queryatotalorg_30"]):
                output["ZHJ008"] = "0"

            if data["queryatotalorg_90"] != -999 and data["queryatotalorg_90"] >= int(
                    whitelist_config_dict["queryatotalorg_90"]):
                output["ZHJ009"] = "0"
            if data["queryatotalorg_180"] != -999 and data["queryatotalorg_180"] >= int(
                    whitelist_config_dict["queryatotalorg_180"]):
                output["ZHJ010"] = "0"
            if data["queryatotalorg_365"] != -999 and data["queryatotalorg_365"] >= int(
                    whitelist_config_dict["queryatotalorg_365"]):
                output["ZHJ011"] = "0"

            if data["insuranceamt"] != -999 and data["insuranceamt"] >= int(
                    whitelist_config_dict["insuranceamt"]):
                output["ZHJ0012"] = "0"

            if data["insurancecount"] != -999 and data["insurancecount"] >= int(
                    whitelist_config_dict["insurancecount"]):
                output["ZHJ0013"] = "0"

            if data["insuranceorgcount"] != -999 and data["insuranceorgcount"] >= int(
                    whitelist_config_dict["insuranceorgcount"]):
                output["ZHJ0014"] = "0"
            if data["insurancebal"] != -999 and data["insurancebal"] >= int(
                    whitelist_config_dict["insurancebal"]):
                output["ZHJ0015"] = "0"

        else:
            if data["overduemorecount"] != -999 and data["overduemorecount"] >= int(
                    non_whitelist_config_dict["overduemorecount"]):
                output["ZHJ001"] = "0"
            if data["overduemoreamt"] != -999 and data["overduemoreamt"] >= int(
                    non_whitelist_config_dict["overduemoreamt"]):
                output["ZHJ002"] = "0"
            if data["outstandcount"] != -999 and data["outstandcount"] >= int(
                    non_whitelist_config_dict["outstandcount"]):
                output["ZHJ003"] = "0"
            if data["loanbal"] != -999 and data["loanbal"] >= int(
                    non_whitelist_config_dict["loanbal"]):
                output["ZHJ004"] = "0"
            if data["overduecount"] != -999 and data["overduecount"] >= int(
                    non_whitelist_config_dict["overduecount"]):
                output["ZHJ005"] = "0"
            if data["overdueamt"] != -999 and data["overdueamt"] >= int(
                    non_whitelist_config_dict["overdueamt"]):
                output["ZHJ006"] = "0"

            if data["loanorgcount_queryatotalorg_365"] != -999 and data["loanorgcount_queryatotalorg_365"] <= int(
                    non_whitelist_config_dict["loanorgcount_queryatotalorg_365"]):
                output["ZHJ007"] = "0"

            if data["queryatotalorg_30"] != -999 and data["queryatotalorg_30"] >= int(
                    non_whitelist_config_dict["queryatotalorg_30"]):
                output["ZHJ008"] = "0"

            if data["queryatotalorg_90"] != -999 and data["queryatotalorg_90"] >= int(
                    non_whitelist_config_dict["queryatotalorg_90"]):
                output["ZHJ009"] = "0"
            if data["queryatotalorg_180"] != -999 and data["queryatotalorg_180"] >= int(
                    non_whitelist_config_dict["queryatotalorg_180"]):
                output["ZHJ010"] = "0"
            if data["queryatotalorg_365"] != -999 and data["queryatotalorg_365"] >= int(
                    non_whitelist_config_dict["queryatotalorg_365"]):
                output["ZHJ011"] = "0"

            if data["insuranceamt"] != -999 and data["insuranceamt"] >= int(
                    non_whitelist_config_dict["insuranceamt"]):
                output["ZHJ0012"] = "0"

            if data["insurancecount"] != -999 and data["insurancecount"] >= int(
                    non_whitelist_config_dict["insurancecount"]):
                output["ZHJ0013"] = "0"

            if data["insuranceorgcount"] != -999 and data["insuranceorgcount"] >= int(
                    non_whitelist_config_dict["insuranceorgcount"]):
                output["ZHJ0014"] = "0"
            if data["insurancebal"] != -999 and data["insurancebal"] >= int(
                    non_whitelist_config_dict["insurancebal"]):
                output["ZHJ0015"] = "0"

        is_pass = 1

        if "0" in output.values():
            is_pass = 1   #不启用
            result.setLong("score", 1000)

        result_dict = {"pass": is_pass}
        result_json = json.dumps(result_dict)
        result.setString("content", result_json)
        for key, value in output.items():
            result.setString(key, value)





        output = {"rule_01": "1"}
        is_pass = 1
        result.setLong("score", 0)
        try:
            scorecust = int(init_data.getString("scorecust"))
            score_limit = int(init_data.getString("score_limit"))

            if score_limit == -999:
                score_limit = 480

            result.setString("score_limit", str(score_limit))
            if scorecust != -999 and scorecust <= score_limit:
                output["rule_01"] = "0"

            if "0" in output.values():
                is_pass = 0
                result.setLong("score", 1000)
        except:
            log = context.getLog()
            log.error("Error <r_sr_zhjdata.py>:class r_360_rs" + traceback.format_exc())
        finally:
            for key, value in output.items():
                result.setString(key, value)
            result_dict = {"pass": is_pass}
            result_json = json.dumps(result_dict)
            result.setString("content", result_json)