#!/usr/bin/env python3

import sys
import argparse
import logging

from draco.run import run
from draco import __version__

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Draco Visualization recommendation system.",
        epilog="There is a moment in every dawn when light floats, there is the possibility of magic. Creation holds its breath.")

    parser.add_argument("query", nargs="?", type=argparse.FileType("r"), default=sys.stdin,
                        help="The CompassQL query (partial Vega-Lite spec).")
    parser.add_argument("--out", nargs="?", type=argparse.FileType("w"), default=sys.stdout,
                        help="specify the Vega-Lite output file")
    parser.add_argument('--version', action='version',
                        version=__version__)
    args = parser.parse_args()

    logger.info(f"Processing query: {args.query.name} ...")

    run(args.query, args.out)

    # close open files
    if args.query is not sys.stdin:
        args.query.close()

    if args.out is not sys.stdout:
        args.out.close()

    logger.info(f"Complete task.")


if __name__ == '__main__':
    main()
