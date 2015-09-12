__author__ = 'exak'

import sys


def main(word):
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Please provide an argument')
        exit(1)
    main(sys.argv[1])
