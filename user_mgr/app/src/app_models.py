from pydantic import BaseModel
from sqlalchemy import Column, Numeric, String
from app_database import Base


class UserInfo(Base):

    __tablename__ = "T_USER_INFO"

    user_id = Column(String, primary_key=True, nullable=False)
    user_name = Column(String)
    user_email = Column(String)
    user_role = Column(String)
    user_assets = Column(String)  # comma separated asset ids

    def __repr__(self):
        return "UserInfo(%s, %s,%s,%s,%s)" % (
            self.user_id,
            self.user_name,
            self.user_email,
            self.user_role,
            self.user_assets,
        )


class UserInfoReq(BaseModel):
    user_id: str
    user_name: str
    user_email: str
    user_role: int = None
    user_assets: str = None
