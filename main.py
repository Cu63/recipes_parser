import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--update', action='store_true',
                        help='update files without changing hash')
    parser.add_argument('-t', '-test', action='store_true',
                        help='testing program using files from test/')
    return parser


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.test:
        path = './test/'
    elif namespace.update:
        pass
    else:
        pass


if __name__ == "__main__":
    main()
