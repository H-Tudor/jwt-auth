# Python JOSE User Guide

This page covers how to create and use a JWT token by properly using the
python-jose provided functionality because the provided documentation seems
lacking.

## Flows

There are 2 JWT flows
1. Creation
2. Consumption

The JWT creation flow has the following steps
1. get the required keys (in `jwk` format):
2. prepare  the payload in the `jwt` standard
3. encode the payload into a *signed* token  
4. encrypt the token according to the `jwe` standard

The JWT Consumption flow has the following steps:
1. decrypt the token using the decryption key
2. decode the token using the signing key counterpart (which automatically
validates some claims)
3. validate the custom claims

## Cryptography

The cryptography associated with the JWT flows supports the following
approaches:

1. Direct / symmetric:
    - regarding the token *signing*, requires using
        - the HMAC `HS` family of algorithms 
        - the same symmetric key for both encoding and decoding
    - regarding the token *encryption*, requires using
        - the direct `DIR` algorithm or the AES Key Wrap (A256KW) algorithms
        - and the same symmetric key for encryption and decryption
2. Asymmetric
    - this allows the use of RSA or Elliptical Curves (ECDSA) algorithms
    - regarding the token *signing*, requires using
        - the `RS` / `ES` family of algorithms 
        - the public key for encoding
        - the private key decoding
    - regarding the token *encryption*, requires using
        - only available with a RSA Key
        - the RSA (`RSA_OAEP_256`) algorithm
        - the public key for encryption
        - the private key for decryption

In either approach, the key file must be shared across systems

## OpenSSL for Key FileGeneration

How to generate the keys
- HMAC: openssl rand -out keys/hmac_key.pem 32
- RSA: openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048 
- ECDH: openssl ecparam -name prime256v1 -genkey -noout -out keys/ecdh_key.pem
--
