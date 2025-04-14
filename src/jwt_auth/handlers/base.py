from uuid import UUID
from jose import jwe, jwt, constants

from ..models.jwt_base import Jwt, jwt_validation_options
from ..models.crypto_key import CryptoKey
from ..types import AppIdType


class BaseJoseHandler:
    issuer: AppIdType
    audience: list[AppIdType]
    encoding_key: CryptoKey
    encryption_key: CryptoKey | None = None
    jwt_validation_options: dict = jwt_validation_options

    def __init__(
        self,
        issuer: AppIdType,
        audience: AppIdType | list[AppIdType],
        encoding_key: CryptoKey,
        encryption_key: CryptoKey | None = None,
    ):
        self.issuer = issuer
        self.audience = audience
        self.encoding_key = encoding_key
        self.encryption_key = encryption_key

        self.__post_init__()

    def create_token(self, payload: dict | None = None):
        if not self.encoding_key:
            raise AttributeError(
                "Encoding key not set", name="encoding_key", object=self
            )

        token = jwt.encode(
            self._get_payload(payload),
            self.encoding_key.private_key(),
            algorithm=self.encoding_key.sign_algo,
        )

        if not self.encryption_key:
            return token

        return jwe.encrypt(
            plaintext=token,
            key=self.encryption_key.public_key(),
            algorithm=self.encryption_key.encrypt_algo,
            encryption=constants.Algorithms.A256GCM,
            zip=constants.ZIPS.DEF,
        ).decode("utf-8")

    def extract_token(self, token: str):
        if not self.encoding_key:
            raise AttributeError(
                "Encoding key not set", name="encoding_key", object=self
            )

        if self.encryption_key:
            token = jwe.decrypt(token, self.encryption_key.private_key())

        return jwt.decode(
            token=token,
            key=self.encoding_key.public_key(),
            algorithms=self.encoding_key.sign_algo,
            audience=self.issuer,
            issuer=self.audience,
        )

    def __post_init__(self):
        if not isinstance(self.issuer, str):
            self.issuer = str(self.issuer)

        if isinstance(self.audience, UUID):
            self.audience = str(self.audience)

        if isinstance(self.audience, str):
            return

        if not isinstance(self.audience, list):
            raise AttributeError(
                "Audience is neither string or list", name="audience", obj=self
            )

        for i in range(len(self.audience)):
            if isinstance(self.audience[i], str):
                continue

            self.audience[i] = str(self.audience[i])

    def _get_payload(self, data: dict | None = None):
        """Get Payload Dict

        Args:
            data (dict | None, optional): additional data to include in the token. Example: {"sub", "email", "role"}. Defaults to None

        Returns:
            dict: dictionary with objects already prepared for json encryption
        """

        params = Jwt(iss=self.issuer, aud=self.audience).model_dump(mode="json")
        if not data or not isinstance(data, dict):
            return params

        for key, value in data.items():
            params[key] = value

        return params
