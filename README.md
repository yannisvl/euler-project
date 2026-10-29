# Project Euler — mathematical programming exercises

A personal collection of Python solutions and experiments for numbered Project Euler problems. Topics include elementary number theory, combinatorics, search, dynamic programming and numerical computation.

**Contains solutions and spoilers.** This is a learning archive rather than a single packaged application.

## Layout

Numbered directories correspond to problem IDs, for example `0001/`, `0014/` and `0096/`. `EulerUtils/` contains a small prime-related helper package. Some directories include working notes, alternate attempts or local input files.

## Run one exercise

Use Python 3. For example:

```bash
cd 0001
python 1.py
```

Run other scripts from their own directories when they read relative input paths. Some exercises use NumPy:

```bash
python -m pip install numpy
```

## Reading suggestions

- `0001/1.py`: inclusion–exclusion through sums of multiples.
- `0014/14.py`: reuse of previously computed Collatz chain lengths.
- `0096/`: Sudoku-related search code.
- `EulerUtils/PrimeLib/PrimeUtils.py`: basic primality helper.

The collection has no unified test runner, dependency lockfile or guarantee that every working attempt is complete. Runtime varies widely across problems. Consult [Project Euler](https://projecteuler.net/) for the original statements and its solution-sharing guidance before publishing this archive.
