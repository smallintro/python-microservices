from logzero import logger as log
from app_database import DataBaseObj
from app_models import AssetInfo, AssetCategory

db_obj = DataBaseObj()


class AssetInfoDao(object):
    @staticmethod
    def query_asset_info(asset_id):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(AssetInfo)
            if asset_id == "-1":
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
    def add_asset_info(asset_info):
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
                AssetInfoDao.update_asset_category(asset_info.asset_category, 1)
                new_asset = AssetInfo(
                    asset_id=asset_info.asset_id,
                    asset_name=asset_info.asset_name,
                    asset_owner=asset_info.asset_owner,
                    asset_category=asset_info.asset_category,
                )
                log.debug(f"add_asset_info {new_asset}")
                session.add(new_asset)
                session.commit()
                result = new_asset
        except Exception as e:
            session.rollback
            log.exception(f"add_asset_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result

    @staticmethod
    def update_asset_info(asset_id, asset_info):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(AssetInfo).filter(
                AssetInfo.asset_id == asset_id
            )
            if query_result.count() == 0:
                log.error(f" user not found", asset_info.asset_id)
            else:
                old_category = query_result.first().asset_category
                query_result.update(
                    {
                        AssetInfo.asset_name: asset_info.asset_name,
                        AssetInfo.asset_owner: asset_info.asset_owner,
                        AssetInfo.asset_category: asset_info.asset_category,
                    }
                )
                if old_category != asset_info.asset_category:
                    AssetInfoDao.update_asset_category(asset_info.asset_category, 1)
                    AssetInfoDao.update_asset_category(old_category, -1)
                session.commit()
                result = AssetInfo
        except Exception as e:
            session.rollback
            log.exception(f"update_asset_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result

    @staticmethod
    def delete_asset_info(asset_id):
        session = db_obj.get_db_session()
        try:
            query_result = session.query(AssetInfo).filter(AssetInfo.asset_id == asset_id)
            if query_result.count() == 0:
                log.error(f" asset not found {asset_id}")
                result = 0
            else:
                old_category = query_result.first().asset_category
                AssetInfoDao.update_asset_category(old_category, -1)
                result = query_result.delete()
            session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"delete_asset_info operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result

    @staticmethod
    def update_asset_category(category, count):
        log.debug(f"update_asset_category {category} {count}")
        session = db_obj.get_db_session()
        try:
            query_result = session.query(AssetCategory).filter(AssetCategory.category_name == category)
            if query_result.count() == 0:
                new_category = AssetCategory(
                    category_name=category,
                    asset_count=1,
                )
                log.debug(f"adding asset category {category}")
                session.add(new_category)
            else:
                query_result.update(
                    {
                        AssetCategory.asset_count: query_result.first().asset_count+count,
                    }
                )
                log.debug(f"updating asset category {category}")
            session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"update_asset_category operation failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
