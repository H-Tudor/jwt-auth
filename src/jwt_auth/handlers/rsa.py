from jose import constants

from ..types import AppIdType
from ..models.crypto_key import CryptoKey
from .base import BaseJoseHandler


class RSAHandler(BaseJoseHandler):
    def __init__(
        self, issuer: AppIdType, audience: AppIdType | list[AppIdType], file: str
    ):
        key = CryptoKey(
            file=file,
            sign_algo=constants.Algorithms.RS256,
            encrypt_algo=constants.Algorithms.RSA_OAEP_256,
        )

        super().__init__(issuer, audience, key, key)
