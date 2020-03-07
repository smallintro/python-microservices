from logzero import logger as log
from app_database import DataBaseObj
from app_models import AssetInfo, AssetInfoReq

db_obj = DataBaseObj()


class AssetInfoDao(object):
    @staticmethod
    def query_asset_info(asset_id=-1):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(AssetInfo)
            if asset_id == -1:
                result = query_result.all()
            else:
                result = query_result.filter(AssetInfo.asset_id == asset_id).all()
            session.commit()
            log.debug(result)
        except Exception as e:
            session.rollback
            log.exception(f"query_asset_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result

    @staticmethod
    def add_asset_info(asset_info: AssetInfoReq):
        session = db_obj.get_db_session()
        try:
            count_result = (
                session.query(AssetInfo)
                .filter(AssetInfo.asset_id == asset_info.asset_id)
                .count()
            )
            if count_result > 0:
                log.error(f" user already exists {asset_info.asset_id}")
            else:
                new_asset = AssetInfo(
                    asset_id=asset_info.asset_id,
                    asset_name=asset_info.asset_name,
                    asset_owner=asset_info.asset_owner,
                    asset_catagory=asset_info.asset_catagory,
                    asset_count=asset_info.asset_count,
                )
                log.debug(f"add_asset_info {new_asset}")
                session.add(new_asset)
                session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"add_asset_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")

    @staticmethod
    def update_asset_info(asset_id: int, asset_info: AssetInfoReq):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(AssetInfo).filter(AssetInfo.asset_id == asset_id)
            if query_result.count() == 0:
                log.error(f" user not found", asset_info.asset_id)
            else:
                query_result.update(
                    {
                        AssetInfo.asset_name: asset_info.asset_name,
                        AssetInfo.asset_owner: asset_info.asset_owner,
                        AssetInfo.asset_catagory: asset_info.asset_catagory,
                        AssetInfo.asset_count: asset_info.asset_count,
                    }
                )
                session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"update_asset_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")

    @staticmethod
    def delete_asset_info(asset_id=-1):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(AssetInfo)
            if asset_id == -1:
                query_result.delete()
            else:
                query_result.filter(AssetInfo.asset_id == asset_id).delete()
            session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"delete_asset_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
