




class m_361_rs(object):
    def init(self,context):
        pss
    def mapper(self,context):
        result = context.create()
        output = {"scorecust":"-999","score_limlit":"-999"}
        try:
            scorecust = context.get("scorecashonyx360_rs")
            conntent = json.loads(scorecust)
        except:




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