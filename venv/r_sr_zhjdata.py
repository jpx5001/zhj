#!/usr/bin/python
"""
@author: mm_Einstein
@software: PyCharm
@file: r_360_rs.py
@time: 2020/4/17
"""
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
            if (day <= 30):
                queryatotalorg_30 = queryatotalorg_30 + 1

            if (day <= 90):
                queryatotalorg_90 = queryatotalorg_90 + 1

            if (day <= 180):
                queryatotalorg_180 = queryatotalorg_180 + 1
            if (day <= 365):
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
            "ZHJ001": 1,
            "ZHJ002": 1,
            "ZHJ003": 1,
            "ZHJ004": 1,
            "ZHJ005": 1,
            "ZHJ006": 1,
            "ZHJ007": 1,
            "ZHJ008": 1,
            "ZHJ009": 1,
            "ZHJ010": 1,
            "ZHJ011": 1,
            "ZHJ012": 1,
            "ZHJ013": 1,
            "ZHJ014": 1,
            "ZHJ015": 1
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
        hecate_sr_whitelist = init_data.getString("hecate_sr_whitelist")
        whitelist_config = init_data.getString["whitelist_config_dict"]
        whitelist_config_dict = json.loads(whitelist_config)
        non_whitelist_config = init_data.getString["non_whitelist_config_dict"]
        non_whitelist_config_dict = json.loads("non_whitelist_config")

        data["overduemorecount"] = int(init_data.getString("overduemorecount"))
        data["overduemoreamt"] = int(init_data.getString("overduemoreamt"))
        data["outstandcount"] = int(init_data.getString("outstandcount"))
        data["loanbal"] = int(init_data.getString("loanbal"))
        data["overduecount"] = int(init_data.getString("overduecount"))
        data["overdueamt"] = int(init_data.getString("overdueamt"))
        data["insuranceamt"] = int(init_data.getString("insuranceamt"))
        data["insurancecount"] = int(init_data.getString("insurancecount"))
        data["insuranceorgcount"] = int(init_data.getString("insuranceorgcount"))
        data["insurancebal"] = int(init_data.getString("insurancebal"))


        cal_dqst(init_data, data)
        loanorgcount = int(init_data.getString("loanorgcount"))
        if data["queryatotalorg_365"] is not 0:
            data["loanorgcount_queryatotalorg_365"]=float(loanorgcount/data["queryatotalorg_365"])

        if hecate_sr_whitelist == "1":

            if data["overduemorecount"] != -999 and data["overduemorecount"] >=int(whitelist_config_dict["overduemorecount"]):
                output["ZHJ001"] = "1"
            if data["overduemoreamt"] != -999 and data["overduemoreamt"] >= int(
                    whitelist_config_dict["overduemoreamt"]):
                output["ZHJ001"] = "1"
            if data["overduemoreamt"] != -999 and data["overduemoreamt"] >= int(
                whitelist_config_dict["overduemoreamt"]):
                output["ZHJ001"] = "1"
            if data["loanbal"] != -999 and data["loanbal"] >= int(
                    whitelist_config_dict["loanbal"]):
                output["ZHJ001"] = "1"
            if data["overduecount"] != -999 and data["overduecount"] >= int(
                    whitelist_config_dict["overduecount"]):
                output["ZHJ001"] = "1"
            if data["overdueamt"] != -999 and data["overdueamt"] >= int(
                    whitelist_config_dict["overdueamt"]):
                output["ZHJ001"] = "1"
            if data["insuranceamt"] != -999 and data["insuranceamt"] >= int(
                    whitelist_config_dict["insuranceamt"]):
                output["ZHJ001"] = "1"
            if data["insurancecount"] != -999 and data["insurancecount"] >= int(
                    whitelist_config_dict["insurancecount"]):
                output["ZHJ001"] = "1"
            if data["insuranceorgcount"] != -999 and data["insuranceorgcount"] >= int(
                    whitelist_config_dict["insuranceorgcount"]):
                output["ZHJ001"] = "0"
            if data["insurancebal"] != -999 and data["insurancebal"] >= int(
                    whitelist_config_dict["insurancebal"]):
                output["ZHJ001"] = "0"
            if data["queryatotalorg_30"] != -999 and data["queryatotalorg_30"] >= int(
                    whitelist_config_dict["queryatotalorg_30"]):
                output["ZHJ001"] = "0"
            if data["queryatotalorg_30"] != -999 and data["queryatotalorg_30"] >= int(
                    whitelist_config_dict["queryatotalorg_30"]):
                output["ZHJ001"] = "0"
            if data["queryatotalorg_30"] != -999 and data["queryatotalorg_30"] >= int(
                    whitelist_config_dict["queryatotalorg_30"]):
                output["ZHJ001"] = "0"
            if data["overduemoreamt"] != -999 and data["overduemorecount"] >= int(
                    whitelist_config_dict["overduemoreamt"]):
                output["ZHJ001"] = "0"

        else:
            if context.getString("overduemorecount") != -999 and context.getString("overduemorecount") >= non_whitelist_config_dict["overduemorecount_limlt"]:
                output["ZHJ001"] = "0"
            if context.getString("overduemorecount") != -999 and context.getString("overduemorecount") >= 1:
                output["ZHJ001"] = "0"
            if context.getString("overduemorecount") != -999 and context.getString("overduemorecount") >= 1:
                output["ZHJ001"] = "0"
            if context.getString("overduemorecount") != -999 and context.getString("overduemorecount") >= 1:
                output["ZHJ001"] = "0"
            if context.getString("overduemorecount") != -999 and context.getString("overduemorecount") >= 1:
                output["ZHJ001"] = "0"
            if context.getString("overduemorecount") != -999 and context.getString("overduemorecount") >= 1:
                output["ZHJ001"] = "0"
            if context.getString("overduemorecount") != -999 and context.getString("overduemorecount") >= 1:
                output["ZHJ001"] = "0"
            if context.getString("overduemorecount") != -999 and context.getString("overduemorecount") >= 1:
                output["ZHJ001"] = "0"
            if context.getString("overduemorecount") != -999 and context.getString("overduemorecount") >= 1:
                output["ZHJ001"] = "0"
            if context.getString("overduemorecount") != -999 and context.getString("overduemorecount") >= 1:
                output["ZHJ001"] = "0"
            if context.getString("overduemorecount") != -999 and context.getString("overduemorecount") >= 1:
                output["ZHJ001"] = "0"

        is_pass = 1

        if "0" in output.values():
            is_pass = 0
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
            log.error("Error <r_360_rs.py>:class r_360_rs" + traceback.format_exc())
        finally:
            for key, value in output.items():
                result.setString(key, value)
            result_dict = {"pass": is_pass}
            result_json = json.dumps(result_dict)
            result.setString("content", result_json)