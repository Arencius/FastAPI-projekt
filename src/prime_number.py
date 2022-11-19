from fastapi import APIRouter


prime_router = APIRouter()


@prime_router.get('/prime/{number}')
def is_prime(number: str):
    if not number.lstrip('-+').isdigit():
        raise ValueError('Given string is not a number')

    number = int(number)
    if number < 2:
        return False

    for i in range(2, int(number//2)):
        if number % i == 0:
            return False

    return True
