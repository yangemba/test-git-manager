import argparse
import logging


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-x", "--xarg", help="")
    args = parser.parse_args()

    x = int(args.xarg)

    logging.warning(f' X^2 = {x ** 2}!')
