# script renames exercises in the `src/` (by default) directory
# to make it prettier

import pathlib
from typing import List


DEFAULT_PREFIX = "prob"
SOURCE_DIR = "src/"
EXCLUDE_FILES: List[str] = ["__pycache__"]

LD: int = len(DEFAULT_PREFIX)
DIGIT_PLACEHOLDERS: int = 3

START_DIR = "."


path = (pathlib.Path(START_DIR) / SOURCE_DIR).resolve()
print(f"Changing file names in {path}")

for f in path.iterdir():
    if f.name not in EXCLUDE_FILES:
        n, ext = f.name[LD:].split(".")

        # count how many zeroes we need to add
        zeroes_count: str = "0" * abs(len(n) - DIGIT_PLACEHOLDERS)
        new_name = f"{SOURCE_DIR}{DEFAULT_PREFIX}{zeroes_count}{n}.{ext}"

        f.rename(new_name)
