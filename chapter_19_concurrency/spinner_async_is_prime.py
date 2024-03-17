# Пример 19.5. spinner_async.py: сопрограммы spin и slow
import asyncio
import itertools
import math


async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


async def is_prime(n: int) -> int:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True


# Пример 19.4. spinner_async.py: функция main и сопрограмма supervisor
def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')


async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinner object: {spinner}')
    result = await is_prime(5_000_111_000_222_021)
    spinner.cancel()
    return result


if __name__ == '__main__':
    main()
