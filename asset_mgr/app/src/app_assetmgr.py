from fastapi import FastAPI, Query
from logzero import logger as log
from starlette import status
from app_services import AssetInfoService
from app_models import AssetMgrRequest, AssetMgrResponse
from app_config import *

app = FastAPI()

asset_service = AssetInfoService()


@app.get(
    "/v1/assetmgr/{assetid}",
    response_model=AssetMgrResponse,
    status_code=status.HTTP_200_OK,
)
def get_asset_info(assetid: str = DEFAULT_ALL):
    log.info(f"get_asset_info request {assetid}")
    try:
        result_data = asset_service.get_asset_info(assetid)
        result_status = STATUS_SUCCESS
    except Exception as e:
        result_data = str(e)
        result_status = STATUS_FAILURE
    log.info(f"get_asset_info response {assetid}")
    response = AssetMgrResponse(status=result_status, data={"assets": result_data})
    log.debug(f"get_asset_info response {response}")
    return response


@app.post(
    "/v1/assetmgr", response_model=AssetMgrResponse, status_code=status.HTTP_201_CREATED
)
def add_asset_info(asset_info: AssetMgrRequest):
    log.info(f"add_asset_info request {asset_info}")
    try:
        result_data = asset_service.add_asset_info(asset_info)
        result_status = STATUS_SUCCESS
    except Exception as e:
        result_data = str(e)
        result_status = STATUS_FAILURE
    response = AssetMgrResponse(status=result_status, data={"asset": result_data})
    log.debug(f"add_asset_info response {response}")
    return response


@app.put(
    "/v1/assetmgr/assignuser",
    response_model=AssetMgrResponse,
    status_code=status.HTTP_201_CREATED,
)
def assign_asset_to_user(asset_category: str = Query(...), userid: str = Query(...)):
    log.info(f"assign_asset_to_user request {asset_category} {userid}")
    try:
        result_data = asset_service.assign_asset_to_user(asset_category, userid)
        result_status = STATUS_SUCCESS
    except Exception as e:
        result_data = str(e)
        result_status = STATUS_FAILURE
    response = AssetMgrResponse(status=result_status, data={"assetid": result_data})
    log.debug(f"assign_asset_to_user response {response}")
    return response


@app.put(
    "/v1/assetmgr/{assetid}",
    response_model=AssetMgrResponse,
    status_code=status.HTTP_201_CREATED,
)
def update_asset_info(assetid: str, asset_info: AssetMgrRequest):
    log.info(f"update_asset_info request {asset_info}")
    try:
        result_data = asset_service.update_asset_info(assetid, asset_info)
        result_status = STATUS_SUCCESS
    except Exception as e:
        result_data = str(e)
        result_status = STATUS_FAILURE
    response = AssetMgrResponse(status=result_status, data={"asset": result_data})
    log.debug(f"update_asset_info response {response}")
    return response


@app.delete(
    "/v1/assetmgr/{assetid}",
    response_model=AssetMgrResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def del_asset_info(assetid: str):
    log.info(f"del_asset_info request {assetid}")
    try:
        result_data = asset_service.del_asset_info(assetid)
        result_status = STATUS_SUCCESS
    except Exception as e:
        result_data = str(e)
        result_status = STATUS_FAILURE
    response = AssetMgrResponse(
        status=result_status, data={"assetid": assetid, "deleted": result_data}
    )
    log.debug(f"del_asset_info response {response}")
    return response
