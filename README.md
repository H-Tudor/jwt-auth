# JWT Auth

A simple `python-jose` wrapper made for easy integration of advance functionality

This library provides 3 pre-made JWT handlers:
- **HMAC** - uses a secret string key for signing and symmetric encryption
- **RSA** - using a private / public key pair (RSA generated) for signing and asymmetric encryption
- **ECDSA** - using a private / public key pair (Elliptical Curves Based) for signing **only**

The library allows creation of you own handler with, for example, separate keys of encoding & encryption

In the `docs` folder I put a mini JWT / JOSE explanation which sits at the foundation of this library

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

```bash
jwt-auth-demo
```

Or write the following script

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