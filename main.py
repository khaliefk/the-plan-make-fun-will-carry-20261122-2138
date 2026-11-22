"""Write one short money plan to /output/entry.txt.

No network, no input files: the plan text lives in this file.
"""

import os

PLAN = (
    "Day 1: sell $120 'landing page in 48h' on Fiverr and Contra. "
    "$100 buys a domain, Canva, Apollo. "
    "Find 200 Shopify stores with bad homepages, email each owner a rebuilt mockup, "
    "build it in code. "
    "Close 1 in 40, they already saw it: 5 clients = $600, repeats top $1,000 by day 30."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
