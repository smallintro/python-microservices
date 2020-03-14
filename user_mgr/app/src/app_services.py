import json
from logzero import logger as log
import requests
from app_config import *
from app_repo import UserInfoDao


user_dao = UserInfoDao()


class UserInfoService(object):
    @staticmethod
    def get_user_info(user_id):
        log.debug(f"get_user_info")
        result = user_dao.query_user_info(user_id)
        return result

    @staticmethod
    def add_user_info(user_info):
        log.debug(f"add_user_info")
        user_dao.add_user_info(user_info)
        result = user_dao.query_user_info(user_info.user_id)
        return result

    @staticmethod
    def update_user_info(user_id, user_info):
        log.debug(f"update_user_info")
        result = user_dao.update_user_info(user_id, user_info)
        return result

    @staticmethod
    def del_user_info(user_id):
        log.debug(f"del_user_info")
        result = user_dao.delete_user_info(user_id)
        return result

    @staticmethod
    def assign_asset_to_user(asset_category, user_id):
        log.debug(f"assign_asset_to_user")
        log.debug(f"calling" + assign_asset_api.format(asset_category, user_id))
        response = requests.put(assign_asset_api.format(asset_category, user_id))
        print(response)
        log.debug(
            f"assign_asset_api {response.status_code} {response.ok} {response.content} {response.text}"
        )
        if response.ok:
            asset_id = json.loads(response.content)["data"]["assetid"]
            if asset_id != DEFAULT_ALL:
                log.debug(f"asset {asset_id} will be assigned to {user_id}")
                user_dao.update_user_asset_id(user_id, asset_id)
        return asset_id
