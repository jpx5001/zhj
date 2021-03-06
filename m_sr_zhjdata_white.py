#!/usr/bin/python
import datetime
import json
import traceback

EMPTY_STR = "-999"

def to_json(java_object):
    result = {}
    try:
        content = java_object.getString("content")
        result = json.loads(content) if content else {}
    except:
        pass
    return result
def config_pull(context):
    # default config
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


    config = context.get("sr_zhjdata_config")
    jsonobj = {}

    try:
        jsonobj = json.loads(config.getString("config_data"))

        whitelist_config_dict.update(jsonobj["whitelist_config_dict"])
        non_whitelist_config_dict.update(jsonobj["non_whitelist_config_dict"])
    except:
        pass
    config_data = {
        "whitelist_config_dict": json.dumps(whitelist_config_dict),
        "non_whitelist_config_dict": json.dumps(non_whitelist_config_dict)
    }
    return config_data


class m_sr_zhjdata_white(object):

    def init(self, context):
        pass

    def mapper(self, context):
        # 命中外部风险名单
        output = {
            "overduemorecount": "-999",
            "overduemoreamt": "-999",
            "outstandcount": "-999",
            "loanbal": "-999",
            "overduecount": "-999",
            "overdueamt": "-999",
            "insuranceamt": "-999",
            "insurancecount": "-999",
            "insuranceorgcount": "-999",
            "insurancebal": "-999",
            "infoquerybean": "-999", #明细信息
            "loanorgcount": "-999" ,#机构数

            "hecate_sr_whitelist": "1",
            #"whitelist_config_dict": json.dumps(whitelist_config_dict),
            #"non_whitelist_config_dict": json.dumps(non_whitelist_config_dict),


        }
        config_data = config_pull(context)
        output["whitelist_config_dict"] = config_data["whitelist_config_dict"]
        output["non_whitelist_config_dict"] = config_data["non_whitelist_config_dict"]

        # output["hecate_sr_whitelist"] = 1
        # try:
        #     hecate_white_list = context.getList("hecate_white_list")
        #
        #     if hecate_white_list:
        #        output["hecate_sr_whitelist"] = 1
        #     else:
        #        output["hecate_sr_whitelist"] = 0
        # except:
        #     log = context.getLog()
        #     log.error("Error <m_sr_zhjdata.py>获取白名单失败 | %s" % (traceback.format_exc()))

        try:
            zhj_data = context.get("sr_zhj_data")
            zhj_data_st = zhj_data.getString("content")
            zhi_data_dict = json.loads(zhj_data_st)
            if zhj_data_st:
               for item in zhi_data_dict:
                   if(zhi_data_dict[item] is not None):
                       output[item] = zhi_data_dict[item]
            else:
                pass
        except:
            pass

        finally:
            result = context.create()
            for key, value in output.items():
                result.setString(key, str(value))

