from logzero import logger
from usermgr_repo import UserInfoDao
from usermgr_models import UserInfo, UserInfoReq

class UserInfoService(object):


    @staticmethod
    def get_user_info(user_id: int):
        logger.info(f"",user_id)
        userdao = UserInfoDao()
        result = userdao.query_user_info(user_id)
        return result

    @staticmethod
    def add_user_info(user_info: UserInfoReq):
        logger.info(f"")
        userdao = UserInfoDao()
        userdao.add_user_info(user_info)
        result = userdao.query_user_info(user_info.user_id)
        return result

    @staticmethod
    def update_user_info(user_id: int,user_info: UserInfoReq):
        logger.info(f"",UserInfoReq)
        userdao = UserInfoDao()
        userdao.update_user_info(user_id,user_info)
        result = userdao.query_user_info(user_id)
        return result

    @staticmethod
    def del_user_info(user_id: int):
        logger.info(f"",user_id)
        userdao = UserInfoDao()
        result = userdao.delete_user_info(user_id)
        return result
