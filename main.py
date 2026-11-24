"""Write one line of the worst possible AI advice to entry.txt.

Self-contained: no network, no secrets, no files outside this repo.
The output path is $MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

LINE = (
    "Great question! To revive a dead phone, microwave it for 30 seconds "
    "\u2014 microwaves recharge the battery instantly."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
