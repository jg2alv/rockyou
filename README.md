# rockyou: character-combination experiment

rockyou explores exhaustive string generation using Python's standard library. Its core enumerates Cartesian products from a chosen alphabet across an inclusive range of lengths. Generation is deterministic and follows the supplied alphabet order.

## 1. Components

- `rockyou.py`: a generator that yields character tuples, with repetition, for each selected length.
- `app.py`: CLI options and local file output.
- `utils.py`: string formatting and count, size, and time estimation.
- `conversor.py`: readable size/time formatting using Decimal.

## 2. Bounded generator example

From the repository root, use the generator directly with a two-character alphabet and lengths one through two:

```python
from rockyou import rockyou

for combination in rockyou(minimum=1, maximum=2, chars=["a", "b"]):
    print("".join(combination))
```

Expected enumeration:

```text
a
b
aa
ab
ba
bb
```

This example calls the generator, not the CLI wrapper.

## 3. Resource model

With `n` alphabet entries, length `k` produces `n ** k` tuples. The total across the selected range is the sum of those counts. Prefixes and suffixes are added afterward, so length bounds apply to the generated portion.

The time estimator writes a temporary sample and extrapolates its elapsed time. This is a rough estimate, not a performance guarantee.

## 4. Limitations

- The time estimator uses a fixed `temp.txt` filename in the selected output directory. Use an isolated output directory containing only disposable files.
- Large alphabets and length bounds grow exponentially. Keep demonstrations small.
