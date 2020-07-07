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
    config_dict = {
        "id_evidence_level_limit": "A", # ,分隔
        "id_forecast_level_limit": "A",
        "id_all_level_limit": "A",
        "idTmplevel_limit": "At,Bt",
        "cell_evcellence_level_limit": "A",
        "cell_forecast_level_limit": "A",
        "cell_all_level_limit": "A",
        "cellTmplevel_limit": "At,Bt",
    }
    config = context.get("hecate_sr_risklist_white_config")
    jsonobj = {}
    try:
        jsonobj = json.loads(config.getString("content"))
    except:
        pass
    config_dict.update(jsonobj)
    return config_dict


class m_sr_risklist_white(object):

    def init(self, context):
        pass

    def mapper(self, context):
        # 命中外部风险名单
        output = {
            "id_evidence_level": "-999",
            "id_forecast_level": "-999",
            "id_all_level": "-999",
            "idTmplevel": "-999",
            "cell_evcellence_level": "-999",
            "cell_forecast_level": "-999",
            "cell_all_level": "-999",
            "cellTmplevel": "-999",
        }
        list_product = [
            "id_forecast_level", "id_evidence_level", "id_evidence_type", "id_forecast_des",
            "id_forecast_type", "id_all_level", "id_all_type", "idTmpdes", "idTmptype",
            "idTmplevel", "cell_evidence_type", "cell_evidence_level", "cell_evidence_des",
            "cell_forecast_des", "cell_forecast_type", "cell_forecast_level", "cell_all_type",
            "cell_all_level", "cell_all_des", "cellTmptype", "cellTmpdes", "cellTmplevel",
        ]
        list_flag = ["flag_risklist"]
        list_product_objs = ["id_evidence_des", "id_all_des"]

        try:
            output["threshold_config"] = json.dumps(config_pull(context))
            risklist = context.get("br_RiskList")
            # 介个是引擎给的content
            risklistjson = to_json(risklist)
            # 介个是超超给返回的content
            risklistjson = risklistjson.get("content")  # content

            if risklistjson:
                product = risklistjson.get("product")
                if product:
                    for item in list_product:
                        output[item] = (
                            str(product[item])
                            if item in product and product[item] else "-999"
                        )
                    for item in list_product_objs:
                        output[item] = (
                            product[item]
                            if item in product and product[item] else {}
                        )
                flag = risklistjson.get("flag")
                if flag:
                    for item in list_flag:
                        output[item] = (
                            str(flag[item])
                            if item in flag and flag[item] else "-999"
                        )

  

        except:
            log = context.getLog()
            log.error("Error <m_sr_risklistwhite.py>获取外部风险名单失败 | %s" % (traceback.format_exc()))
        finally:
            result = context.create()
            for key, value in output.items():
                result.setString(key, str(value))
