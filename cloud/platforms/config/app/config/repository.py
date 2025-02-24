from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.database import get_db_session
from app.config.models import AppSetting, SystemSettings


class ReadSystemSettingsRepository:
    def __init__(self, db_session: AsyncSession = Depends(get_db_session)):
        self.db_session = db_session

    async def get(self) -> SystemSettings:
        stmt = select(SystemSettings)
        result = await self.db_session.execute(stmt)
        return result.scalars().one()


class ReadAppSettingsRepository:
    def __init__(self, db_session: AsyncSession = Depends(get_db_session)):
        self.db_session = db_session

    async def get_settings_by_key(self, keys: List[str]) -> List[AppSetting]:
        stmt = select(AppSetting).where(AppSetting.key.in_(keys))
        result = await self.db_session.execute(stmt)
        return list(result.scalars().all())

    async def get_all_settings(self):
        stmt = select(AppSetting)
        result = await self.db_session.execute(stmt)
        return list(result.scalars().all())
