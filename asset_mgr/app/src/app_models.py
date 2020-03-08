from pydantic import BaseModel
from sqlalchemy import Column, Numeric, String
from app_database import Base


class AssetInfo(Base):

    __tablename__ = "T_ASSET_INFO"

    asset_id = Column(String, primary_key=True, nullable=False)
    asset_name = Column(String, nullable=False)
    asset_owner = Column(String)
    asset_category = Column(String, nullable=False)

    def __repr__(self):
        return "AssetInfo(%s, %s, %s, %s)" % (
            self.asset_id,
            self.asset_name,
            self.asset_owner,
            self.asset_category,
        )


class AssetCategory(Base):

    __tablename__ = "T_ASSET_CATEGORY"

    category_name = Column(String, primary_key=True, nullable=False)
    asset_count = Column(Numeric)

    def __repr__(self):
        return "AssetCategory(%s, %d)" % (self.category_name, self.asset_count,)


class AssetInfoReq(BaseModel):
    asset_id: str
    asset_name: str
    asset_owner: str = None
    asset_category: str

