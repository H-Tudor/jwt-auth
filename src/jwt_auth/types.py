from typing import Union
from uuid import UUID


try:
    from jose.backends.cryptography_backend import CryptographyRSAKey as RSAKey  # noqa: F401
except ImportError:
    from jose.backends.rsa_backend import RSAKey  # noqa: F401

try:
    from jose.backends.cryptography_backend import CryptographyECKey as ECKey  # noqa: F401
except ImportError:
    from jose.backends.ecdsa_backend import ECDSAECKey as ECKey  # noqa: F401

from jose.backends.cryptography_backend import CryptographyAESKey as AESKey  # noqa: F401

try:
    from jose.backends.cryptography_backend import CryptographyHMACKey as HMACKey  # noqa: F401
except ImportError:
    from jose.backends.native import HMACKey  # noqa: F401

from jose.backends.base import DIRKey  # noqa: F401


KeyType = Union[AESKey, RSAKey, DIRKey, ECKey, HMACKey]
AppIdType = Union[int, str, UUID]
