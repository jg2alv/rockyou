import itertools
import os
import time

import conversor


class Estimator:
    def __init__(self, args: list) -> None:
        self.path = args.path
        self.chars = args.character_set
        self.min = args.minimum_length
        self.max = args.maximum_length
        self.separator = args.separator

    def estimate(self) -> str:
        s, t, a = self.estimate_size(), self.estimate_time(), self.estimate_ammount()
        return f'Total size: {s}\nTotal time (rough estimate): {t}\nTotal ammount: {a}'

    def estimate_size(self) -> str:
        # Couting separator characters.
        # Removing 1 because the last combination won't have a leading separator character.
        n = self.estimate_ammount() - 1
        _len = len(self.chars)

        for i in range(self.min, self.max + 1):
            n += _len ** i * i

        return conversor.to_readable_size(n)

    def estimate_time(self) -> str:
        def benchmark() -> float:
            start = time.time()

            with open(path, 'wb+') as f:
                for c in itertools.product(self.chars):
                    f.write(bytes(join(c, self.separator), 'utf-8'))

                f.seek(-1, os.SEEK_END)
                f.truncate()

            end = time.time()
            os.remove(path)

            return end - start

        path = f'{self.path}/temp.txt'
        n = self.estimate_ammount(1, 1)
        av = sum([ benchmark() for _ in range(500) ]) / 500

        return conversor.to_readable_time(av * self.estimate_ammount() / n)

    def estimate_ammount(self, min: int = None, max: int = None) -> int:
        n = 0
        _len = len(self.chars)

        for i in range(min or self.min, (max or self.max) + 1):
            n += _len ** i

        return n

def join(combination: tuple, separator: str) -> str:
    return '{}{}'.format(''.join(combination), separator)
