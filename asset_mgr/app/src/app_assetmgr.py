from fastapi import FastAPI, Query
from logzero import logger as log
from app_services import AssetInfoService
from app_models import AssetInfo, AssetInfoReq

app_v1 = FastAPI()

asset_service = AssetInfoService()


@app_v1.get("/v1/assetmgr/{assetid}")
def get_asset_info(assetid: str = "-1"):
    log.info(f"get_asset_info {assetid}")
    result = asset_service.get_asset_info(assetid)
    return {"asset_info": result}


@app_v1.post("/v1/assetmgr")
def add_asset_info(asset_info: AssetInfoReq):
    log.info(f"add_asset_info {AssetInfoReq}")
    result = asset_service.add_asset_info(asset_info)
    return {"asset_info": result}


@app_v1.put("/v1/assetmgr/assign")
def assign_asset_to_user(asset_category: str = Query(...), userid: str = Query(...)):
    log.info(f"assign_asset_to_user {asset_category} {userid}")
    result = asset_service.assign_asset_to_user(asset_category, userid)
    return {"message": result}


@app_v1.put("/v1/assetmgr/{assetid}")
def update_asset_info(assetid: str, asset_info: AssetInfoReq):
    log.info(f"update_asset_info {AssetInfoReq}")
    result = asset_service.update_asset_info(assetid, asset_info)
    return {"asset_info": result}


@app_v1.delete("/v1/assetmgr/{assetid}")
def del_asset_info(assetid: str):
    log.info(f"del_asset_info {assetid}")
    result = asset_service.del_asset_info(assetid)
    return {"message": result}


