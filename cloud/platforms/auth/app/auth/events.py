import uuid
from datetime import datetime
from typing import Optional

from app.auth import crypto
from app.auth.models import Role, User
from app.auth.schemas import SecretPassword
from app.common.event_sourcing.events import Event


class CreateUserEvent(Event[User]):
    event_type: str = "USER_CREATE_EVENT"
    display_name: str = "User created"

    def __init__(self, requester_username: str, username: str, password: SecretPassword):
        super().__init__(requester_username)
        self.username = username
        self.password = password

    def process(self, entity: Optional[User] = None) -> User:
        return User(
            id=uuid.uuid4(),
            username=self.username.lower(),
            password=crypto.hash_password(self.password.get_secret_value()),
        )


class AddRoleToUserEvent(Event[User]):
    event_type: str = "USER_ADD_ROLE_EVENT"
    display_name: str = "Role added to user"

    def __init__(self, requester_username: str, role: Role):
        super().__init__(requester_username)
        self.role = role

    def process(self, entity: User) -> User:
        entity.roles.append(self.role)
        return entity


class SuccessfulLoginEvent(Event[User]):
    event_type: str = "SUCCESSFUL_LOGIN_EVENT"
    display_name: str = "Login successful"

    def process(self, entity: User) -> User:
        return entity


class FailedLoginAttemptEvent(Event[User]):
    event_type: str = "FAILED_LOGIN_ATTEMPT_EVENT"
    display_name: str = "Login failed"

    def process(self, entity: User) -> User:
        return entity


class SuccessfulLogoutEvent(Event[User]):
    event_type: str = "SUCCESSFUL_LOGOUT_EVENT"
    display_name: str = "Logged out"

    def process(self, entity: User) -> User:
        return entity


class FailedLogoutEvent(Event[User]):
    event_type: str = "FAILED_LOGOUT_EVENT"
    display_name: str = "Logout failed"

    def process(self, entity: User) -> User:
        return entity


class UserAccountLockedEvent(Event[User]):
    event_type: str = "USER_ACCOUNT_LOCKED_EVENT"
    display_name: str = "User account locked"

    def __init__(self, username: str, locked_until: datetime):
        super().__init__(username)
        self.locked_until = locked_until

    def process(self, entity: User) -> User:
        entity.locked_until = self.locked_until
        return entity
