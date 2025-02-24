import uuid
from datetime import UTC, datetime

from cache import RedisCache

from app.settings import config


def add_failed_authentication_attempt(username: str):
    client = RedisCache()
    if not config.BRUTE_FORCE_PROTECTION_ENABLED or not client.connected:
        return

    unique_identifier = uuid.uuid4()
    key = f"{config.PROJECT_NAME}:{username}:authentication_attempt_fail:{unique_identifier}"
    timestamp = datetime.now(UTC).timestamp()
    client.set(key, timestamp, ttl=config.BRUTE_FORCE_ATTEMPT_TTL_SECONDS)


def get_failed_authentication_attempts_count(username: str) -> int:
    client = RedisCache()

    if not config.BRUTE_FORCE_PROTECTION_ENABLED or not client.connected:
        return 0

    count = 0
    pattern = f"{config.PROJECT_NAME}:{username}:authentication_attempt_fail:*"
    for _ in client.scan(pattern):
        count += 1

    return count


def block_account_temporarily(username: str):
    client = RedisCache()

    if not config.BRUTE_FORCE_PROTECTION_ENABLED or not client.connected:
        return

    key = f"{config.PROJECT_NAME}:{username}:account_blocked"
    timestamp = datetime.now(UTC).timestamp()
    client.set(key, timestamp, ttl=config.AUTHENTICATION_ACCOUNT_LOCKOUT_IN_SECONDS)
