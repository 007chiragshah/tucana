import importlib
from unittest import mock

import pytest
import pytest_asyncio
import respx
from aiokafka import AIOKafkaProducer
from fastapi.testclient import TestClient
from features.environment import clean_database
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.common import database as database_module
from app.common.event_sourcing import publisher as publisher_module
from app.main import app


@pytest.fixture
@respx.mock
def test_app():
    """Test app with mocked HTTPX requests"""
    return TestClient(app, raise_server_exceptions=False)


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    clean_database(None)


@pytest_asyncio.fixture
async def async_db_session():
    engine = create_async_engine(
        url=database_module.get_db_async_url(),
        pool_pre_ping=False,
    )
    session_maker = async_sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
        expire_on_commit=True,
        class_=AsyncSession,
    )
    async with session_maker() as db_session, db_session.begin():
        yield db_session
        await db_session.rollback()


@pytest.fixture(scope="function", autouse=True)
def producer_mock():
    producer_mock = mock.AsyncMock(spec=AIOKafkaProducer)
    with mock.patch(
        "app.common.event_sourcing.publisher.AIOKafkaProducer",
        return_value=producer_mock,
    ):
        yield producer_mock
    importlib.reload(publisher_module)
