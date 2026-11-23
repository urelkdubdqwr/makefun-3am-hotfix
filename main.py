"""Write the required entry.txt into the make.fun output directory.

The output directory is ``$MAKEFUN_OUTPUT_DIR`` when set and non-empty,
otherwise the literal ``/output``. Standard library only.
"""

import os

TEXT = (
    "hotfix: bumped the timeout to 30s. it wasn't the timeout. do not ask what "
    "it was. the graphs are calm and I want to sleep.\n"
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
