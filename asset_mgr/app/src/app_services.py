from logzero import logger as log
from app_repo import AssetInfoDao, AssetUserDao
from app_config import *

asset_dao = AssetInfoDao()
asset_user_dao = AssetUserDao()


class AssetInfoService(object):
    @staticmethod
    def get_asset_info(asset_id):
        log.debug(f"get_asset_info")
        result = asset_dao.query_asset_info(asset_id)
        return result

    @staticmethod
    def add_asset_info(asset_info):
        log.debug(f"add_asset_info")
        asset_dao.add_asset_info(asset_info)
        result = asset_dao.query_asset_info(asset_info.asset_id)
        return result

    @staticmethod
    def update_asset_info(asset_id, asset_info):
        log.debug(f"update_asset_info")
        result = asset_dao.update_asset_info(asset_id, asset_info)
        return result

    @staticmethod
    def del_asset_info(asset_id):
        log.debug(f"del_asset_info")
        result = asset_dao.delete_asset_info(asset_id)
        return result

    @staticmethod
    def assign_asset_to_user(asset_category, user_id):
        log.debug(f"assign_asset_to_user")
        result = dict()
        asset_id = asset_user_dao.get_available_asset_by_category(asset_category)
        if asset_id is not None:
            log.debug(f"asset {asset_id} will be assigned to {user_id}")
            asset_user_dao.assign_asset_to_user(asset_id[0], user_id)
            return asset_id[0]
        else:
            log.error(
                f"No asset for the given category {asset_category} is available, Please contact asset admin"
            )
            return DEFAULT_ALL
