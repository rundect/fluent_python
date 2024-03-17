# Пример 19.5. spinner_async.py: сопрограммы spin и slow
import asyncio
import itertools


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


async def slow() -> int:
    await asyncio.sleep(3)
    return 42


# Пример 19.4. spinner_async.py: функция main и сопрограмма supervisor
def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')


async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel()
    return result


if __name__ == '__main__':
    main()
