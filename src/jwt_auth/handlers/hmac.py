from jose import constants

from ..types import AppIdType
from ..models.crypto_key import HMACKey
from .base import BaseJoseHandler


class HMACHandler(BaseJoseHandler):
    def __init__(
        self, issuer: AppIdType, audience: AppIdType | list[AppIdType], file: str
    ):
        key = HMACKey(
            file=file,
            sign_algo=constants.Algorithms.HS256,
            encrypt_algo=constants.Algorithms.A256KW,
        )

        super().__init__(issuer, audience, key, key)
