from datetime import UTC, datetime, timedelta

import pytest
from common_schemas.jwt import AccessTokenClaims, JWTClaims, RefreshTokenClaims, RoleNames
from pydantic import ValidationError


def test_role_names_enum():
    assert RoleNames.ADMIN == "admin"
    assert RoleNames.TECH == "tech"
    assert RoleNames.CLINICAL == "clinical"
    assert RoleNames.ORGANIZATION == "organization"

    with pytest.raises(ValueError):
        RoleNames("invalid_role")


def test_access_token_claims():
    current_time = datetime.now(UTC)
    exp_time = current_time + timedelta(minutes=15)
    claims_data = {
        "sub": "123",
        "nbf": current_time.timestamp(),
        "exp": exp_time.timestamp(),
        "iat": current_time.timestamp(),
        "jti": "unique-id",
        "aud": "test-audience",
        "iss": "test-issuer",
        "username": "testuser",
        "roles": [RoleNames.CLINICAL],
    }

    access_claims = AccessTokenClaims(**claims_data)

    # Ensure correct subclass
    assert access_claims.token_type == "access"


def test_access_token_claims_user_id():
    current_time = datetime.now(UTC)
    exp_time = current_time + timedelta(minutes=15)
    claims_data = {
        "sub": "123",
        "nbf": current_time.timestamp(),
        "exp": exp_time.timestamp(),
        "iat": current_time.timestamp(),
        "jti": "unique-id",
        "aud": "test-audience",
        "iss": "test-issuer",
        "user_id": "testuser",
        "roles": [RoleNames.CLINICAL],
    }

    access_claims = AccessTokenClaims(**claims_data)

    # Ensure correct subclass
    assert access_claims.token_type == "access"


# Test for RefreshTokenClaims
def test_refresh_token_claims():
    current_time = datetime.now(UTC)
    exp_time = current_time + timedelta(days=1)
    claims_data = {
        "sub": "123",
        "nbf": current_time.timestamp(),
        "exp": exp_time.timestamp(),
        "iat": current_time.timestamp(),
        "jti": "unique-id",
        "aud": "test-audience",
        "iss": "test-issuer",
        "username": "testuser",
        "roles": [RoleNames.ORGANIZATION],
    }

    refresh_claims = RefreshTokenClaims(**claims_data)

    # Ensure correct subclass
    assert refresh_claims.token_type == "refresh"


# Validation Test for JWTClaims
def test_jwt_claims_validation():
    invalid_claims_data = {
        "sub": "123",
        "nbf": datetime.now(UTC).timestamp(),
        "exp": "not-a-timestamp",  # Invalid
        "iat": datetime.now(UTC).timestamp(),
        "jti": "unique-id",
        "aud": "test-audience",
        "iss": "test-issuer",
        "username": "testuser",
        "roles": ["invalid-role"],  # Invalid
    }

    with pytest.raises(ValidationError):
        JWTClaims(**invalid_claims_data)
