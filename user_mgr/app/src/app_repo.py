from logzero import logger as log
from app_database import DataBaseObj
from app_models import UserInfo, UserInfoReq

db_obj = DataBaseObj()


class UserInfoDao(object):
    @staticmethod
    def query_user_info(user_id=-1):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(UserInfo)
            if user_id == -1:
                result = query_result.all()
            else:
                result = query_result.filter(UserInfo.user_id == user_id).all()
            session.commit()
            log.debug(result)
        except Exception as e:
            session.rollback
            log.exception(f"query_user_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result

    @staticmethod
    def add_user_info(user_info: UserInfoReq):
        session = db_obj.get_db_session()
        try:
            query_result = (
                session.query(UserInfo)
                .filter(UserInfo.user_id == user_info.user_id)
                .all()
            )
            if len(query_result) > 0:
                log.error(f" user already exists {user_info.user_id}")
            else:
                new_user = UserInfo(
                    user_id=user_info.user_id,
                    user_name=user_info.user_name,
                    user_email=user_info.user_email,
                    user_role=user_info.user_role,
                    user_assets=user_info.user_assets,
                )
                log.debug(f"add_user_info {new_user}")
                session.add(new_user)
                session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"add_user_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")

    @staticmethod
    def update_user_info(user_id: int, user_info: UserInfoReq):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(UserInfo).filter(UserInfo.user_id == user_id)
            if len(query_result.all()) == 0:
                log.error(f" user not found", user_info.user_id)
            else:
                query_result.update(
                    {
                        UserInfo.user_name: user_info.user_name,
                        UserInfo.user_email: user_info.user_email,
                        UserInfo.user_assets: user_info.user_assets,
                        UserInfo.user_role: user_info.user_role,
                    }
                )
                session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"update_user_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")

    @staticmethod
    def delete_user_info(user_id=-1):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(UserInfo)
            if user_id == -1:
                result = query_result.delete()
            else:
                result = query_result.filter(UserInfo.user_id == user_id).delete()
            session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"delete_user_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
