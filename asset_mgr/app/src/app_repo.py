from logzero import logger as log
from app_database import DataBaseObj
from app_models import AssetInfo, AssetCategory

db_obj = DataBaseObj()


class AssetInfoDao(object):
    @staticmethod
    def query_asset_info(asset_id):
        log.debug(f"query_asset_info {asset_id}")
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
            log.exception(f"query_asset_info failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result

    @staticmethod
    def add_asset_info(asset_info):
        log.debug(f"add_asset_info {asset_info}")
        session = db_obj.get_db_session()
        try:
            count_result = (
                session.query(AssetInfo)
                .filter(AssetInfo.asset_id == asset_info.asset_id)
                .count()
            )
            if count_result > 0:
                log.warn(f" user already exists {asset_info.asset_id}")
            else:
                AssetInfoDao.update_asset_category(asset_info.asset_category, 1)
                new_asset = AssetInfo(
                    asset_id=asset_info.asset_id,
                    asset_name=asset_info.asset_name,
                    asset_category=asset_info.asset_category,
                    asset_owner=asset_info.asset_owner,
                )
                log.debug(f"add_asset_info {new_asset}")
                session.add(new_asset)
                session.commit()
                result = new_asset
        except Exception as e:
            session.rollback
            log.exception(f"add_asset_info failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result

    @staticmethod
    def update_asset_info(asset_id, asset_info):
        log.debug(f"update_asset_info {asset_info}")
        session = db_obj.get_db_session()
        try:
            query_result = session.query(AssetInfo).filter(
                AssetInfo.asset_id == asset_id
            )
            if query_result.count() == 0:
                log.warn(f" asset not found {asset_info.asset_id}")
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
                result = (
                    session.query(AssetInfo)
                    .filter(AssetInfo.asset_id == asset_id)
                    .all()
                )
        except Exception as e:
            session.rollback
            log.exception(f"update_asset_info failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result

    @staticmethod
    def delete_asset_info(asset_id):
        log.debug(f"delete_asset_info {asset_id}")
        session = db_obj.get_db_session()
        try:
            query_result = session.query(AssetInfo).filter(
                AssetInfo.asset_id == asset_id
            )
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
            log.exception(f"delete_asset_info failed {e}")
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
            query_result = session.query(AssetCategory).filter(
                AssetCategory.category_name == category
            )
            if query_result.count() == 0:
                new_category = AssetCategory(category_name=category, asset_count=1,)
                log.debug(f"adding asset category {category}")
                session.add(new_category)
            else:
                query_result.update(
                    {
                        AssetCategory.asset_count: query_result.first().asset_count
                        + count,
                    }
                )
                log.debug(f"updating asset category {category}")
            session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"update_asset_category failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")


class AssetUserDao:
    @staticmethod
    def get_available_asset_by_category(asset_category):
        log.debug(f"get_available_asset_by_category {asset_category}")
        session = db_obj.get_db_session()
        try:
            asset_id = (
                session.query(AssetInfo.asset_id)
                .filter(
                    AssetInfo.asset_category == asset_category,
                    AssetInfo.asset_owner.is_(None),
                )
                .first()
            )
        except Exception as e:
            log.exception(f"get_available_asset_by_category failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return asset_id

    @staticmethod
    def assign_asset_to_user(asset_id, user_id):
        log.debug(f"assign_asset_to_user {asset_id} {user_id}")
        session = db_obj.get_db_session()
        try:
            result = (
                session.query(AssetInfo)
                .filter(AssetInfo.asset_id == asset_id)
                .update({AssetInfo.asset_owner: user_id})
            )
            session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"assign_asset_to_user failed {e}")
        finally:
            if session is not None:
                session.close()
                log.debug(f"session closed")
        return result
