# -*- coding: utf-8 -*-
"""
@author: mm_Einstein
@software: PyCharm
@file: r_360_rs.py
@time: 2020/4/17
"""
import json
import traceback


class r_360_rs(object):
    def init(self, context):
        pass

    def rule(self, context):
        result = context.create()
        init_data = context.get("m_360_rs")
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


