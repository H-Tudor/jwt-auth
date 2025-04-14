import sys
from uuid import uuid4

from ..handlers import HMACHandler, RSAHandler, ECDSAHandler


APP_ID = uuid4()
PAYLOAD = {"sub": str(uuid4())}


def main() -> None:
    jwt_handler = get_handler()

    token = jwt_handler.create_token(PAYLOAD)
    print("Token:", token, end="\n\n")

    decoded = jwt_handler.extract_token(token)
    print("Decoded:", decoded, end="\n\n")


def get_handler():
    if len(sys.argv) == 1:
        return test_hmac()

    match sys.argv[1]:
        case "rsa":
            return test_rsa()
        case "ecdsa":
            return test_ecdsa()
        case _:
            return test_hmac()


def test_hmac():
    return HMACHandler(issuer=APP_ID, audience=[APP_ID], file="keys/hmac_key.pem")


def test_rsa():
    return RSAHandler(issuer=APP_ID, audience=[APP_ID], file="keys/rsa_key.pem")


def test_ecdsa():
    return ECDSAHandler(issuer=APP_ID, audience=[APP_ID], file="keys/ecdh_key.pem")


if __name__ == "__main__":
    main()
