from typing import Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.models import Role, User
from app.common.database import get_db_session


class UserRepository:
    def __init__(self, db_session: AsyncSession = Depends(get_db_session)):
        self._db_session = db_session

    async def get_user_by_username(self, username: str) -> Optional[User]:
        stmt = select(User).where(User.username == username.lower())
        result = await self._db_session.execute(stmt)
        return result.scalars().unique().one_or_none()

    async def get_roles(self) -> list[Role]:
        stmt = select(Role)
        result = await self._db_session.execute(stmt)
        return result.scalars().all()
