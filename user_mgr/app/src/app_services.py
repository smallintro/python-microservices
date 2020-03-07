from logzero import logger
from app_repo import UserInfoDao
from app_models import UserInfo, UserInfoReq


userdao = UserInfoDao()


class UserInfoService(object):
    @staticmethod
    def get_user_info(user_id: int):
        logger.debug(f"get_user_info")
        result = userdao.query_user_info(user_id)
        return result

    @staticmethod
    def add_user_info(user_info: UserInfoReq):
        logger.debug(f"add_user_info")
        userdao.add_user_info(user_info)
        result = userdao.query_user_info(user_info.user_id)
        return result

    @staticmethod
    def update_user_info(user_id: int, user_info: UserInfoReq):
        logger.debug(f"update_user_info")
        userdao.update_user_info(user_id, user_info)
        result = userdao.query_user_info(user_id)
        return result

    @staticmethod
    def del_user_info(user_id: int):
        logger.debug(f"del_user_info")
        result = userdao.delete_user_info(user_id)
        return result
