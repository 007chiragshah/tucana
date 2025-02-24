import pytest
from create_user import create_user
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.crypto import hash_password, verify_password
from app.auth.models import User


@pytest.mark.asyncio
async def test_create_user(async_db_session: AsyncSession):
    await create_user(async_db_session, "test@sibel.com", "secretpass", "admin, tech")

    stmt = select(User)
    result = await async_db_session.execute(stmt)
    user = result.scalars().unique().one_or_none()
    assert user
    assert user.username == "test@sibel.com"
    assert user.password != "secretpass"

    valid, _ = verify_password("secretpass", user.password)
    assert valid

    assert {"admin", "tech"} == {r.name for r in user.roles}


@pytest.mark.asyncio
async def test_create_user_duplicated(async_db_session: AsyncSession):
    user = User(
        id="07480f69-b1d1-43b3-a9c0-c6ed3c9a55c9",
        username="test@sibel.com",
        password=hash_password("other"),
    )
    async_db_session.add(user)
    await async_db_session.flush()

    await create_user(async_db_session, "test@sibel.com", "secretpass", "admin, tech")

    stmt = select(User)
    result = await async_db_session.execute(stmt)
    user = result.scalars().unique().one_or_none()
    assert user
    assert user.username == "test@sibel.com"
    valid, _ = verify_password("other", user.password)
    assert valid
