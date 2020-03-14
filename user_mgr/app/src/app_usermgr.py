from fastapi import FastAPI, Query
from logzero import logger as log
from starlette import status
from app_services import UserInfoService
from app_models import UserInfoReq, UserMgrResponse
from app_config import *


app = FastAPI()

user_service = UserInfoService()


@app.get(
    "/v1/usermgr/{userid}",
    response_model=UserMgrResponse,
    status_code=status.HTTP_200_OK,
)
def get_user_info(userid: str = DEFAULT_ALL):
    log.info(f"get_user_info request {userid}")
    try:
        result_data = user_service.get_user_info(userid)
        result_status = STATUS_SUCCESS
    except Exception as e:
        result_data = str(e)
        result_status = STATUS_FAILURE
    response = UserMgrResponse(status=result_status, data={"users": result_data})
    log.debug(f"get_user_info response {response}")
    return response


@app.post(
    "/v1/usermgr", response_model=UserMgrResponse, status_code=status.HTTP_201_CREATED
)
def add_user_info(user_info: UserInfoReq):
    log.info(f"add_user_info request {user_info}")
    try:
        result_data = user_service.add_user_info(user_info)
        result_status = STATUS_SUCCESS
    except Exception as e:
        result_data = str(e)
        result_status = STATUS_FAILURE
    response = UserMgrResponse(status=result_status, data={"users": result_data})
    log.debug(f"add_user_info response {response}")
    return response


@app.put(
    "/v1/usermgr/assignasset",
    response_model=UserMgrResponse,
    status_code=status.HTTP_201_CREATED,
)
def assign_asset_to_user(asset_category: str = Query(...), userid: str = Query(...)):
    log.info(f"assign_asset_to_user request {asset_category} {userid}")
    try:
        result_data = user_service.assign_asset_to_user(asset_category, userid)
        result_status = STATUS_SUCCESS
    except Exception as e:
        result_data = str(e)
        result_status = STATUS_FAILURE
    response = UserMgrResponse(status=result_status, data={"users": result_data})
    log.debug(f"assign_asset_to_user response {response}")
    return response


@app.put(
    "/v1/usermgr/{userid}",
    response_model=UserMgrResponse,
    status_code=status.HTTP_201_CREATED,
)
def update_user_info(userid: str, user_info: UserInfoReq):
    log.info(f"update_user_info request {userid}")
    try:
        result_data = user_service.update_user_info(userid, user_info)
        result_status = STATUS_SUCCESS
    except Exception as e:
        result_data = str(e)
        result_status = STATUS_FAILURE
    response = UserMgrResponse(status=result_status, data={"users": result_data})
    log.debug(f"update_user_info response {response}")
    return response


@app.delete(
    "/v1/usermgr/{userid}",
    response_model=UserMgrResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def del_user_info(userid: str):
    log.info(f"del_user_info request {userid}")
    try:
        result_data = user_service.del_user_info(userid)
        result_status = STATUS_SUCCESS
    except Exception as e:
        result_data = str(e)
        result_status = STATUS_FAILURE
    response = UserMgrResponse(status=result_status, data={"users": result_data})
    log.debug(f"del_user_info response {response}")
    return response
