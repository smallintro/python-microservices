from logzero import logger
from app_repo import AssetInfoDao
from app_models import AssetInfo, AssetInfoReq


assetdao = AssetInfoDao()


class AssetInfoService(object):
    @staticmethod
    def get_asset_info(asset_id: str):
        logger.debug(f"get_asset_info")
        result = assetdao.query_asset_info(asset_id)
        return result

    @staticmethod
    def add_asset_info(asset_info: AssetInfoReq):
        logger.debug(f"add_asset_info")
        assetdao.add_asset_info(asset_info)
        result = assetdao.query_asset_info(asset_info.asset_id)
        return result

    @staticmethod
    def update_asset_info(asset_id: str, asset_info: AssetInfoReq):
        logger.debug(f"update_asset_info")
        assetdao.update_asset_info(asset_id, asset_info)
        result = assetdao.query_asset_info(asset_id)
        return result

    @staticmethod
    def del_asset_info(asset_id: str):
        logger.debug(f"del_asset_info")
        result = assetdao.delete_asset_info(asset_id)
        return result
