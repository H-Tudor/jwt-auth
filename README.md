# JWT Auth

A simple `python-jose` wrapper made for easy integration of advance functionality

This library provides pre-made handlers for HMAC, RSA ECDSA (encoding-only) jwt
encoding and encryption.

## Installation

HTTP
```sh
pip install https://https://github.com/H-Tudor/jwt-auth
```

SSH
```sh
pip install git+ssh://git@github.com/H-Tudor/jwt-auth.git
```

## How To Use

After installation you can run the demo:




```python
from jwt_auth.handlers import RSAHandler

def main():
    issuer = "localhost"
    audience = str(issuer)
    file = "keys/rsa_key.pem"
    payload = {"sub": str(issuer)}
    handler = RSAHandler(issuer, audience, file)

    token = handler.create_token(payload)
    print("Encrypted Token:", token, end="\n\n")

    decoded = handler.extract_token(token)
    print("Decoded Token", decoded)

if __name__ == "__main__":
    main()
```