#!/usr/bin/env python
# encoding: utf-8

import pickle
import sys

last_filename = 'last.pkl'


def set_last(list_, filename=last_filename):
    """
    list_ like [1, 0, 0, 0, 0]
    f is a file object
    """
    with open(filename, 'w') as f:
        pickle.dump(list_, f)


def get_last(filename=last_filename):
    with open(filename) as f:
        print(pickle.load(f))


if __name__ == '__main__':

    try:
        args = sys.argv[1]
    except IndexError:
        args = None

    if not args:
        get_last()
    else:
        last_list = args.split(',')
        set_last(last_list)
        get_last()
