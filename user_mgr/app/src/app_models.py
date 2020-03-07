from pydantic import BaseModel
from sqlalchemy import Column, Numeric, String
from app_database import Base


class UserInfo(Base):

    __tablename__ = "T_USER_INFO"

    user_id = Column(Numeric, primary_key=True, nullable=False)
    user_name = Column(String)
    user_email = Column(String)
    user_role = Column(Numeric)
    user_assets = Column(String)

    def __repr__(self):
        return "UserInfo(%d, %s,%s,%s,%s)" % (
            self.user_id,
            self.user_name,
            self.user_email,
            self.user_role,
            self.user_assets,
        )


class UserInfoReq(BaseModel):
    user_id: int
    user_name: str
    user_email: str
    user_role: int = None
    user_assets: str = None
