import os
import time
from decimal import Decimal

import conversor
import rockyou


class Estimator:
    def __init__(self, args: list) -> None:
        self.path = args.path
        self.chars = args.character_set
        self.max = args.max_length
        self.min = args.min_length
        self.separator = args.separator

    def estimate(self) -> str:
        return f'Total size: {self.estimate_size()}\nTotal time (rough estimate): {self.estimate_time()}\nTotal ammount: {self.estimate_ammount()}'

    def estimate_size(self) -> str:
        # Couting separator characters.
        # Removing 1 because the last combination won't have a leading separator character.
        n = self.estimate_ammount() - 1
        _len = len(self.chars)

        for i in range(self.min, self.max + 1):
            n += _len ** i * i

        return conversor.to_readable_size(Decimal(n))

    def estimate_time(self) -> str:
        n = self.estimate_ammount(1, 1)
        path = f'{self.path}/temp.txt'
        start = time.time()

        with open(path, 'wb+') as f:
            [f.write(bytes(join(c, self.separator), 'utf-8'))
             for c in rockyou.rockyou(1, 1, self.chars)]

            f.seek(-1, os.SEEK_END)
            f.truncate()

        end = time.time()
        os.remove(path)

        return conversor.to_readable_time(Decimal(end - start) * Decimal(self.estimate_ammount()) / Decimal(n))

    def estimate_ammount(self, min: int = None, max: int = None) -> int:
        n = 0
        _len = len(self.chars)

        for i in range(min or self.min, (max or self.max) + 1):
            n += _len ** i

        return n


def join(combination: tuple, separator: str) -> str:
    return '{}{}'.format(''.join(combination), separator)
