import base64
import secrets
from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock, patch

import jwt
import pytest
from common_schemas.jwt import AccessTokenClaims, RoleNames
from fastapi import WebSocketException, status
from jwt import ExpiredSignatureError, InvalidSignatureError

from src.realtime.authentication import get_token, handle_token_errors

logger = MagicMock(info=MagicMock())


LOCAL_PRIVATE_KEY = (
    "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpN"
    "SUlKS0FJQkFBS0NBZ0VBcHlEaC9BSllFdXFuMlRGVXhqa"
    "zc5eno2V1VGcmJ3Rk5DaFdyWWUvY3ROK3ZpdnJVCnVPak"
    "t6YXFHZ3VwT0tKclZlSE8wMTJkM1ZrRGozM1p1QzROd2x"
    "xZjYvOUY4QnFCd3BoWHVsNkhOelB6YmdBL28KbUdBN1I4"
    "aXZpZ2l3VC8rY2lseEJ4V004WFdFRmZNTmdCdGhVbGtDe"
    "FB5MnRkRjNJNTdTbVBtUzdhNjNsZ3RWTgpxSXZvMVdVVl"
    "IzeVpPelA4OGU1Y0FsTXZYaGkvTmMrZFlTckZZdVpON1F"
    "wbTJCMmVIQzVmQlI4TXFRQ0lWL2JvCjdoVmx3d2R6dll5"
    "WkdkN3p4dzNwVERGYXliSjcxVmh2Nk5oVmpYdkIrckVDT"
    "W9KMWFxRExjdkFwcE1yT29wUkMKRjZxR0pUZDRobWhlUE"
    "NQc3kvb3V0TnFhOVNHK3VxSlVFR29tSjNyaGJadzdJdlo"
    "3T0VSQXN2eE9rbCs4MVNjcQo3elIrb0pEN0RzTFcvOFBv"
    "RXlsMnc4b1dyWkNWZTRjNFNUL2dKOGxlVDlBbkNBcnN1Q"
    "VpDR2JJZ3B2MnRDKzVyCnAwZTRkR3JGdlRoNVpaVmx6b2"
    "pvOW1JdmNTZHlZRGFiY0dMZTEzNmgwU1VjNDNYbDJrTXl"
    "aRDUrN2ZoelNMMkMKVjhQM282eE0rb1c1NlJ3QjE5S1BP"
    "cVZ3Uit0eVBTVE1MMXpaTGw5bmkvbW1ndk1uTTQrTlpkM"
    "FliaXZ3Zy9GaAp6RkRrT2dwVEtmNWNvU2Z1SUpPYmtieT"
    "NNZ2MzM3NWQm1JZ2dXNnFjR2tzNFlEVC9SSEY1ZUZFNm5"
    "2YVZTMy9pCnpOTmY0eFQvZTQ5dHRweG9MSTZNc0Fub2Zp"
    "Q0YwS0d4b1FiNUU0YnlndXRieS94NUh3NmJNNm9PeDZzQ"
    "0F3RUEKQVFLQ0FnQWtkSnhHdzk0aFZqVkJ2Nng5eHF0Sm"
    "JYQXdld0FyeVExY2QwaVlodUZPUlFLK0hxTzdKL0JnOTJ"
    "MNgorSkFPOUdNL01JSVFnSDI3LzFDVmhIaFJvNXl5Q0Rk"
    "TWlRMzBSaGY4YW9sT1l4bUlydGxVY0dQc3BRVVpUZkhZC"
    "mVyZTI0NHRxZE9CVjVhVWJ1MWVlbE9HRDdMbGF3d2JHd0"
    "xoMnl5UlJRb3NHemlOQnhEOXRrQWl1RE1LL2xacVUKS3Q"
    "0ajExM0VDaG5nMmZOWm82MUYyQ0U4dWo4dktReHplZExn"
    "TG1tNFBQYzJIMFU4TWlVTGh3emRMaWF4NlpTNgpFb3FzN"
    "VlDb2VXVGIzV0l2My9KNklaM2JuU0RnU1ZBUlZuNGp0V2"
    "hXVjNlNWZTQ2dWU3JJdE8xTHkwTVNxQ3h1CnFTSnhIT2N"
    "Bd1hSaHQ5T1lTQUdhSldHUDZRK2tMMmRSOEJTdTVoU1U4"
    "ZVR3VDhCTitaRlNXWmlLWXdPNlkrTkYKbXZLemN2cUFJU"
    "EtYRFhUYTlWZjVPcG41Q0t4SHpmU3ozalViemtNZ1lBNz"
    "FRMWFxYzZQT2xaYnI0dWxJd2pPdApRWDdvV0o2K2Y5QUd"
    "QUFdwQ3pnNFpMWXFUeE12dVBTYi9ia2Ixcks5U1NIUVB1"
    "OElEb1I1M1E4OUN0VVZWWnhRCnlyY2xCUkR4ZFNjeEo4b"
    "Ww2ajBzRVY4V2FjK1FhTG1xM0E2cDJZeHhmMnZDUVhybG"
    "Fnb3RnZnRxdW9mcUZZWSsKWEdkOEdVN0pSaFZZNDZwbzh"
    "hYSt1dHptV0tobERYSHdnODBvZFhnR0RQbjlUK2d1QUZ2"
    "MWJlNXpJeFhNWWZ5eApWQ2x4WlJTRk9HeENOTkZjVEVGO"
    "DdSSGRiMGtMR0t0MTFMdWpNWUNyVmJ0UW5WSXlxUUtDQV"
    "FFQTRlUGp0bStRCjBmK290emFYTnpkaGU4ZFNoL1Nicyt"
    "XYVhOK0xvK1BCOVdPYVY0andaWVVjSFlDZEFGKzhrdTdC"
    "QXN4dlBHTnIKMmExVkJXSmFHN1dVNktVaW1xaG1pcUNNb"
    "mpSdzVoazhLeHNrY0xJM2laRFZINm5aR0hPQlZuSkphWD"
    "grZ2c3Sgo4a0o3VXY4SHhQY0g0VDJvSVphUWlkUEtsQXp"
    "xUVR2MTM3YUVweTZ4TjRlenlZUGpsYzU2bWYyL2VDU25S"
    "TktMClNsZWpQN2lsWWhFQ3FXalh2UmVrOCtKYU55S2JSO"
    "FQ2TC9kenRsZWc2NHlPMTkyUks3SXF4WlFIZ3luZllqN1"
    "MKdGkxME8xUjFCdm5sOVFMOGN2OWYwYkltc00xTU52dDR"
    "ZazJMajdEalZhLytmTlAxNlBONHd2UlFXOVc0RzBwWApy"
    "UmxZQjYzaUh1WUJvd0tDQVFFQXZXZlp5M1d2alI0dUwrQ"
    "m9HU054M0t5WnNwQkFDMnFiN1pNd2ovT1F6QUNZCjlOWV"
    "NObHYvcXdiSWxGZy9SRXNqTko4bWFQY013MEFsTlovTmx"
    "nc2Y3L0I1bzNZQ0lKT2xGWVpiZGEyRVhqcXIKc2tGNHFE"
    "ZC9LQVYrSHRGSmJ2cTEwVGtWY216Q1F5SVR5bkM5L3UzM"
    "npvRGxUWEJFU3grT1h3bHR4YkEvcmd0NQpkRmJuNlRCWl"
    "phN3pjcWlCUlBCNGlwK0w1ZHZrckdWalQrZzBtVmdVQ21"
    "2USs5OXBNN2Z1Wk56NzhGYXhIZmRCCmU2RlpFUkxxcStw"
    "aHhWNkUzQ0pOWHJOZXhtSUgzWmk1SHBZVHZYcnppWEF1T"
    "VE0aWNDbGN6Y0xCNHhlT3F3Z2QKcVVjbExQK0tmVXVpUD"
    "ZMMGtvUjl6SXBzWWIrSEhGU2gvdUkrejBaU1dRS0NBUUF"
    "ZQU5OTnE0VkVDMXF1UFVyTQpQMEpJbU9HWU9OSGl4OThq"
    "UjAzYldIUmYwdm12bTRtUUFCa0F1WTMxWURiMWxoRkVid"
    "HpUR2UxMzhBYzh6enFyCi94dVhyUlNFUXFqQ3lsU202d0"
    "9rTDhKSkFsVlk5RmNhY3gxeWcrWGh4MFJUSDBuVndBT3d"
    "aa25uU0ZFNmZJY2kKMHUwdmJoSFRuK0EwQlNGZG9oR3la"
    "T0MzcVBsbm1ucVNZQVVtd0xFS1ZpcUkrb0hDRG9NSHVTZ"
    "TcrcHdLUldDdApqd2t0WDBxdGVUbTZBSzk5ZEZ2endHYW"
    "xlakg5aWtvN1BYQmdWOWI1UWJGeDFVMEhEd2dCdEpOSGN"
    "JVU5XT2dtCm1aOXA3YXROdlAwOWx5U3RYT05nWkZCaWdj"
    "TDJ2ZUVxVmMxQkRuVHZFQkFoQnowU3hSOFBKMU14dmFPe"
    "ERUVWQKKzJycEFvSUJBUUMydi9jekN2QkJsdmMxbHE2YV"
    "lzckFBNEdnK3ZId2tnSzFiaW1URzQyQWFLc3N3VWg5VHJ"
    "NWApUOHBFNkFqVFdqUXoxOE4xejdsdXd2dWtDL2FQYVZo"
    "OWFHZlZRazIzSlA1S0VJTTZ2aHRUMkFSR1VFbWM5VDhwC"
    "lhITmVSTTAzMll1SXZpMWxaRzdqMjRPQTl0czdtRnRrME"
    "pWdTdIM1loakFXbnNCZDJEcjVNWFVVdmEyeUg4YUMKQ0J"
    "ZNWNVQ1pSZlRvdkJ4OXduZVhwNVAxUzdWRXArbGVUTDB0"
    "NlZoV1lJZ1NwZTRvN1Z5ajd5Z3RvM2FPdE5QYwo0SjlKa"
    "25OYSszWHZnOTVVUjg0VEVBSzk4a3hGck5aQ3JBekZwRC"
    "t5UFJhZ0tlUnR1eE1iRHcrZmYxZnRYUHRBCi9iTWs5NVJ"
    "Ic3JLMm9uRUV0NG9qMmIwY2N5dnJUb3l4QW9JQkFEamZ3"
    "WjIxZWRQL1ZCMFlIMHo0bGM5b3pUT0YKbXg5M21XTDZyN"
    "jF0NmpVT09zZTRuNE4wZERtbWJRY0h5V21FWTkvMVdDbz"
    "F6L3RBMC91OS9tQzZNYkVoQjEraApGOUFCQWRZN1dpcnV"
    "zYkJZakFldSt2NWlOMTVXYUwrVURQb0I3Wjc5S00rZVVV"
    "OWc4TUI3a3VCYmJiMm00SzUrCjlpWDdkT3hYRkRFeHQxM"
    "zh4eFAvK1p2UG1UNDBOajIrUllndHNsR25zbXNPeVk0dm"
    "0rYk82MnZMMDd3UzlObysKR0lZSjhyMVNiVUZrWnpnaWU"
    "1WkhwM28yd3J2Vy9GajlWWlBxbGhGQ2V4TUdYMTlybm5P"
    "ZW4zcW01MlFGS0MxZgorbjZHZEVzdGdiNXVKeUtseGZqe"
    "DQwNDJBZGFORXJKUjZLNmdMZXpVK2Y0aTNCQzNrUzZpYm"
    "VhOGQ1cz0KLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0"
    "tLS0K"
)


def get_token_claims(roles: list[RoleNames], username: str, sub: str) -> dict:
    iat = datetime.now(UTC)
    claims = AccessTokenClaims(
        iat=iat.timestamp(),
        sub=sub,
        nbf=iat.timestamp(),
        exp=(iat + timedelta(days=1)).timestamp(),
        roles=[r.value for r in roles],
        username=username,
        token_type="access",
        jti=secrets.token_urlsafe(8),
        aud="tucana",
        iss="auth",
    ).model_dump()
    return claims


def generate_valid_jwt_token(
    roles: list[RoleNames],
    username: str = "olivia",
    sub: str = "6feb4bf0-63c6-49fd-afaa-4498b5dc56b0",
) -> str:
    key1 = base64.b64decode(LOCAL_PRIVATE_KEY).decode("utf-8")
    claims = get_token_claims(roles, username, sub)
    return jwt.encode(claims, key=key1, algorithm="RS256")


def test_handle_token_errors_valid_token():
    token = generate_valid_jwt_token([RoleNames.CLINICAL])
    result = handle_token_errors(token)
    assert result == token


@patch("src.realtime.authentication.decode")
def test_handle_token_errors_invalid_signature_error(mock_decode):
    mock_decode.side_effect = InvalidSignatureError("Invalid signature")
    with pytest.raises(WebSocketException) as exc_info:
        handle_token_errors("invalid_token")

    assert exc_info.value.code == status.WS_1008_POLICY_VIOLATION
    assert exc_info.value.reason == "Authentication error"


@patch("src.realtime.authentication.decode")
def test_handle_token_errors_expired_signature_error(mock_decode):
    mock_decode.side_effect = ExpiredSignatureError("Token expired")
    with pytest.raises(WebSocketException) as exc_info:
        handle_token_errors("expired_token")

    assert exc_info.value.code == status.WS_1008_POLICY_VIOLATION
    assert exc_info.value.reason == "Authentication error"


@patch("src.realtime.authentication.handle_token_errors")
def test_get_token(mock_handle_token_errors):
    token = "valid_token"
    mock_handle_token_errors.return_value = token

    result = get_token(token)

    assert result == token
    mock_handle_token_errors.assert_called_once_with(token)
