# -*- coding: utf-8 -*-
"""
@author: mm_Einstein
@software: PyCharm
@file: m_360_rs.py
@time: 2020/4/17
"""

import json
import traceback

EMPTY_STR = "-999"


def get_string(java_object, key):
    """
    get string from java object
    :param java_object:
    :param key:
    :return:
    """
    if java_object:
        try:
            value = java_object.getString(key)
        except Exception as e:
            value = None
            print(e)
        finally:
            result = value if value else EMPTY_STR
            return result


class LimitScore(object):
    def get_data(self, context):
        output = {"score_limit": "-999"}
        try:
            acard = context.get("hecate_360_score")
            data = get_string(acard, "config_data")
            output["score_limit"] = str(json.loads(data)["score_limit"] if data != EMPTY_STR and "score_limit" in json.loads(data) else "-999")
        except:
            log = context.getLog()
            log.error(
                "Error <m_360_rs.py>获取渠道类别信息失败 | %s" % (traceback.format_exc())
            )
        finally:
            return output


class m_360_rs(object):
    def init(self, context):
        pass

    def mapper(self, context):
        result = context.create()
        output = {"scorecust": "-999", "score_limit": "-999"}
        try:
            scorecust = context.get("scorecashonyx360_rs")
            content = json.loads(scorecust.getString("content"))
            output["scorecust"] = content.get("scorecust", "-999") if "scorecust" in content and content["scorecust"] else "-999"
            output.update(LimitScore().get_data(context))
        except:
            log = context.getLog()
            log.error(
                "Error <m_360_rs.py>获取信息失败 | %s" % (traceback.format_exc())
            )
        finally:
            for key, value in output.items():
                result.setString(key, str(value))
