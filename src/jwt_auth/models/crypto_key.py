from dataclasses import dataclass, field
from jose import jwk, utils

from ..types import KeyType


@dataclass
class CryptoKey:
    file: str
    sign_algo: str
    encrypt_algo: str | None = field(default=None)
    obj: KeyType = field(init=False)

    def __post_init__(self):
        self.obj = self._read_private_key()

    def _read_private_key(self) -> KeyType:
        with open(self.file, "rb") as f:
            return jwk.construct(f.read(), algorithm=self.sign_algo)

    def private_key(self):
        return self.obj.to_pem()

    def public_key(self):
        return self.obj.public_key().to_pem()


class HMACKey(CryptoKey):
    def _read_private_key(self) -> KeyType:
        with open(self.file, "rb") as f:
            return jwk.construct(
                {"kty": "oct", "k": utils.base64url_encode(f.read()).decode("utf-8")},
                algorithm=self.sign_algo,
            )

    def public_key(self):
        return self.obj.prepared_key

    def private_key(self):
        return self.obj.prepared_key
