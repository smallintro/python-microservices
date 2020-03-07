from fastapi import FastAPI
from logzero import logger as log
from app_services import AssetInfoService
from app_models import AssetInfo, AssetInfoReq

app_v1 = FastAPI()

assetservice = AssetInfoService()


@app_v1.get("/v1/assetmgr/{assetid}")
def get_asset_info(assetid: str):
    log.info(f"get_asset_info {assetid}")
    result = assetservice.get_asset_info(assetid)
    return {"asset_info": result}


@app_v1.post("/v1/assetmgr")
def add_asset_info(asset_info: AssetInfoReq):
    log.info(f"add_asset_info {AssetInfoReq}")
    result = assetservice.add_asset_info(asset_info)
    return {"asset_info": result}


@app_v1.put("/v1/assetmgr/{assetid}")
def update_asset_info(assetid: str, asset_info: AssetInfoReq):
    log.info(f"update_asset_info {AssetInfoReq}")
    result = assetservice.update_asset_info(assetid, asset_info)
    return {"asset_info": result}


@app_v1.delete("/v1/assetmgr/{assetid}")
def del_asset_info(assetid: str):
    log.info(f"del_asset_info {assetid}")
    result = assetservice.del_asset_info(assetid)
    return {"message": result}
