from logzero import logger
from usermgr_database import *
from usermgr_models import UserInfo, UserInfoReq

class UserInfoDao(object):

    @staticmethod
    def query_user_info(user_id = -1):
        logger.debug(f" [BEGINS]")
        session = get_db_session()
        try:
            query_result = session.query(UserInfo)
            if user_id == -1:
                result = query_result.all()
            else:
                result = query_result.filter(UserInfo.user_id==user_id).all()
            session.commit()
            logger.debug(result)
        except Exception as e:
            session.rollback
            logger.exception(f"operation failed", e)
        finally:
            if session is not None:
                session.close()
                logger.debug(f"session closed")
        logger.debug(f" [ENDS]")
        return result


    @staticmethod
    def add_user_info(user_info: UserInfoReq):
        logger.debug(f" [BEGINS]")
        session = get_db_session()
        try:
            query_result = session.query(UserInfo).filter(UserInfo.user_id == user_info.user_id).all()
            if len(query_result) > 0:
                logger.error(f" user already exists",user_info.user_id)
            else:
                session.add(user_info)
                session.commit()
        except Exception as e:
            session.rollback
            logger.exception(f"operation failed", e)
        finally:
            if session is not None:
                session.close()
                logger.debug(f"session closed")
        logger.debug(f" [ENDS]")

    @staticmethod
    def update_user_info(user_id: int,user_info: UserInfoReq):
        logger.debug(f" [BEGINS]")
        session = get_db_session()
        try:
            query_result = session.query(UserInfo).filter(UserInfo.user_id == user_id)
            if len(query_result.all()) == 0:
                logger.error(f" user not found", user_info.user_id)
            else:
                query_result.update({UserInfo.user_name:user_info.user_name, UserInfo.user_email:user_info.user_email,
                         UserInfo.user_assets: user_info.user_assets, UserInfo.user_role:user_info.user_role})
                session.commit()
        except Exception as e:
            session.rollback
            logger.exception(f"operation failed", e)
        finally:
            if session is not None:
                session.close()
                logger.debug(f"session closed")
        logger.debug(f" [ENDS]")

    @staticmethod
    def delete_user_info(user_id=-1):
        logger.debug(f" [BEGINS]")
        session = get_db_session()
        try:
           query_result = session.query(UserInfo)
           if user_id == -1:
               result = query_result.delete()
           else:
               result = query_result.filter(UserInfo.user_id==user_id).delete()
           session.commit()
        except Exception as e:
            session.rollback
            logger.exception(f"operation failed", e)
        finally:
            if session is not None:
                session.close()
                logger.debug(f"session closed")
        logger.debug(f" [ENDS]")
        return result