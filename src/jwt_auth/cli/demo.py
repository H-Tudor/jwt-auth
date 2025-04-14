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