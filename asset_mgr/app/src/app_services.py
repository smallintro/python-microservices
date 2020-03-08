from logzero import logger
from app_repo import AssetInfoDao, AssetUserDao
from app_models import AssetInfo, AssetInfoReq


asset_dao = AssetInfoDao()
asset_user_dao = AssetUserDao()


class AssetInfoService(object):
    @staticmethod
    def get_asset_info(asset_id):
        logger.debug(f"get_asset_info")
        result = asset_dao.query_asset_info(asset_id)
        return result

    @staticmethod
    def add_asset_info(asset_info):
        logger.debug(f"add_asset_info")
        asset_dao.add_asset_info(asset_info)
        result = asset_dao.query_asset_info(asset_info.asset_id)
        return result

    @staticmethod
    def update_asset_info(asset_id, asset_info):
        logger.debug(f"update_asset_info")
        result = asset_dao.update_asset_info(asset_id, asset_info)
        return result

    @staticmethod
    def del_asset_info(asset_id):
        logger.debug(f"del_asset_info")
        result = asset_dao.delete_asset_info(asset_id)
        return result

    @staticmethod
    def assign_asset_to_user(asset_category, user_id):
        logger.debug(f"assign_asset_to_user")
        asset_id = asset_user_dao.get_available_asset_by_category(asset_category)
        if asset_id is not None:
            asset_user_dao.assign_asset_to_user(asset_id, user_id)
            return asset_id
        else:
            return "No {} available, Please contact asset admin".format(asset_category)
