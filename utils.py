import os
import time

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

        return conversor.to_readable_size(n)

    def estimate_time(self) -> str:
        def benchmark(path) -> float:
            start = time.time()

            with open(path, 'wb+') as f:
                [f.write(bytes(join(c, self.separator), 'utf-8'))
                 for c in rockyou.rockyou(1, 1, self.chars)]

                f.seek(-1, os.SEEK_END)
                f.truncate()

            end = time.time()
            os.remove(path)

            return end - start

        n = self.estimate_ammount(1, 1)
        av = sum([benchmark(f'{self.path}/temp.txt')
                  for _ in range(750)]) / 750

        return conversor.to_readable_time(av * self.estimate_ammount() / n)

    def estimate_ammount(self, min: int = None, max: int = None) -> int:
        n = 0
        _len = len(self.chars)

        for i in range(min or self.min, (max or self.max) + 1):
            n += _len ** i

        return n


def join(combination: tuple, separator: str) -> str:
    return '{}{}'.format(''.join(combination), separator)
