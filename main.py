import logging
import logging.config
import base64
import random
import string


# zadanie nr 1
def logs():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # stworzenie console handler'a, ktory zapisuje/wyswietla dziennik i nadaje mu parametr debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # stworzenie formatter'a
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # dodanie formatter'a do ch
    ch.setFormatter(formatter)

    # dodanie ch do logger'a
    logger.addHandler(ch)

    # hierarchia - DEBUG < INFO < WARNING < ERROR < CRITICAL
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


logs()


# zadanie nr 2
def encode(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def decode(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message


to_encode = input("Please enter nessage to encode:\n ")
base64_bytes = encode(to_encode)
print("Encoded text: " + base64_bytes)
message_bytes = decode(base64_bytes)
print("Decoded text: " + message_bytes)


# zadanie nr 3
def secure_password():
    length = int(input('\nEnter the length of password (must be longer than 8 characters): '))

    combined_list = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    if length < 8:
        print("Your password must contain at least 8 characters!")
    else:
        password = " ".join(random.sample(combined_list, k=length))
        return password


print("Your new password is: ", secure_password())
