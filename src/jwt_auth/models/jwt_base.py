from calendar import timegm
from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from ..types import AppIdType


class Jwt(BaseModel):
    """JWT Reserved Claims
    - jti = JWT ID, ensures JTW uniqueness, used to counter replays and
    - sub = subject, who the token was issued for (eg. user)
    - iss = issuer, the server from where the token originates
    - aud = audience, list of the servers which were ment to consume the token
    - iat = issued at, the moment in UTC when the token was issued
    - nbf = not before, token cannot be used before this time
    - exp = expires at, token cannot be used after this time
    """

    jti: UUID = Field(default_factory=uuid4, init=False)
    iss: AppIdType = Field(default_factory=uuid4)
    aud: AppIdType | list[AppIdType] = Field(default="")
    iat: datetime = Field(default_factory=datetime.now, init=False)
    nbf: datetime = Field(default_factory=datetime.now)
    exp: datetime = Field(
        default_factory=lambda: datetime.now() + timedelta(minutes=15)
    )

    class Config:
        json_encoders = {
            datetime: lambda x: timegm(x.astimezone(timezone.utc).utctimetuple())
        }


jwt_validation_options = {
    "require_jti": True,
    "require_sub": True,
    "require_iss": True,
    "require_aud": True,
    "require_iat": True,
    "require_nbf": True,
    "require_exp": True,
}
