import argparse

from gen_planet.gen import main


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a planet')
    parser.add_argument(
        'num',
        type=int,
        default=5,
        nargs='?',
        help='the number of planets to generate'
    )

    args = parser.parse_args()
    main(args.num)
