# -*- coding: utf-8 -*-

"""
===
CLI
===

Console script.
"""

from __future__ import absolute_import, division, print_function

import argparse

#####################################################################
# CLI
#####################################################################

def main():
    """
    Configure maps and charts from the cli.

    Parameters
    ----------

    Returns
    -------
    out: None.
    """
    parser = argparse.ArgumentParser(
        description='Solid reasons to show after the fact!')
    parser.add_argument(
        '-e',
        '--estimate',
        help='Estimate the price of an ad.',
        required=False)

    args = parser.parse_args()

if __name__ == "__main__":
    main()
