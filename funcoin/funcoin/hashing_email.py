from hashlib import sha256

SECRET_PHRASE = 'helloWorld'


def get_hash_with_secret_phrase(input_data: str, secret_phrase: str) -> str:
    combined = input_data + secret_phrase
    return sha256(combined.encode()).hexdigest()


MESSAGE_BODY = "Hey Bob, I think you should learn about Blockchains! " \
    "I've been investing in Bitcoin and currently have exactly 12.03 BTC in my  account."


print(get_hash_with_secret_phrase(MESSAGE_BODY, SECRET_PHRASE))
