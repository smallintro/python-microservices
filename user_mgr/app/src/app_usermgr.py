from fastapi import FastAPI
from logzero import logger as log
from app_services import UserInfoService
from app_models import UserInfo, UserInfoReq

app_v1 = FastAPI()

userservice = UserInfoService()


@app_v1.get("/v1/usermgr/{userid}")
def get_user_info(userid: int):
    log.info(f"get_user_info {userid}")
    result = userservice.get_user_info(userid)
    return {"user_info": result}


@app_v1.post("/v1/usermgr")
def add_user_info(user_info: UserInfoReq):
    log.info(f"add_user_info {UserInfoReq}")
    result = userservice.add_user_info(user_info)
    return {"user_info": result}


@app_v1.put("/v1/usermgr/{userid}")
def update_user_info(userid: int, user_info: UserInfoReq):
    log.info(f"update_user_info {UserInfoReq}")
    result = userservice.update_user_info(userid, user_info)
    return {"user_info": result}


@app_v1.delete("/v1/usermgr/{userid}")
def del_user_info(userid: int):
    log.info(f"del_user_info {userid}")
    result = userservice.del_user_info(userid)
    return {"message": result}
