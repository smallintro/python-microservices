from fastapi import FastAPI, Query
from logzero import logger as log
from app_services import UserInfoService
from app_models import UserInfo, UserInfoReq
from app_config import *


app_v1 = FastAPI()

user_service = UserInfoService()


@app_v1.get("/v1/usermgr/{userid}")
def get_user_info(userid: str = default_user_id):
    log.info(f"get_user_info {userid}")
    result = user_service.get_user_info(userid)
    return {"message": result}


@app_v1.post("/v1/usermgr")
def add_user_info(user_info: UserInfoReq):
    log.info(f"add_user_info {UserInfoReq}")
    result = user_service.add_user_info(user_info)
    return {"message": result}


@app_v1.put("/v1/usermgr/assignasset")
def assign_asset_to_user(asset_category: str = Query(...), userid: str = Query(...)):
    log.info(f"assign_asset_to_user {asset_category} {userid}")
    result = user_service.assign_asset_to_user(asset_category, userid)
    log.debug(f"assign_asset_to_user response {result}")
    return {"message": result}


@app_v1.put("/v1/usermgr/{userid}")
def update_user_info(userid: str, user_info: UserInfoReq):
    log.info(f"update_user_info {UserInfoReq}")
    result = user_service.update_user_info(userid, user_info)
    return {"message": result}


@app_v1.delete("/v1/usermgr/{userid}")
def del_user_info(userid: str):
    log.info(f"del_user_info {userid}")
    result = user_service.del_user_info(userid)
    return {"message": result}
