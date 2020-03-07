from logzero import logger as log
from app_database import DataBaseObj
from app_models import UserInfo

db_obj = DataBaseObj()


class UserInfoDao(object):
    @staticmethod
    def query_user_info(user_id):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(UserInfo)
            if user_id == "-1":
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
    def add_user_info(user_info):
        session = db_obj.get_db_session()
        try:
            query_count = (
                session.query(UserInfo)
                .filter(UserInfo.user_id == user_info.user_id)
                .count()
            )
            if query_count > 0:
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
                result = new_user
        except Exception as e:
            session.rollback
            log.exception(f"add_user_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result

    @staticmethod
    def update_user_info(user_id, user_info):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(UserInfo).filter(UserInfo.user_id == user_id)
            if query_result.count() == 0:
                log.error(f" user not found {user_id}")
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
                result = user_info
        except Exception as e:
            session.rollback
            log.exception(f"update_user_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result

    @staticmethod
    def delete_user_info(user_id):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(UserInfo).filter(UserInfo.user_id == user_id)
            if query_result.count() == 0:
                log.error(f" user not found {user_id}")
            else:
                result = query_result.delete()
            session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"delete_user_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result
