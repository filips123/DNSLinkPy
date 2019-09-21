"""Command line program for DNSLink protocol."""

import argparse
import sys

from . import resolve


def handle_resolve(args):
    """Handle resolve."""

    for protocol in resolve(args.domain, args.protocol, args.depth):
        print(protocol)


def main():
    """Handle command line program."""

    parser = argparse.ArgumentParser(
        prog=__package__,
        description='Python implementation of DNSLink protocol'
    )
    subparsers = parser.add_subparsers()

    resolve_parser = subparsers.add_parser(
        name='resolve',
        help='resolve a DNSLink record'
    )
    resolve_parser.set_defaults(which='resolve')
    resolve_parser.add_argument('domain', help='a domain to resolve')
    resolve_parser.add_argument('--protocol', help='a record protocol', type=str, default=None)
    resolve_parser.add_argument('--depth', help='a recursion depth', type=int, default=16)

    if len(sys.argv) == 1: # pragma: no cover
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    if args.which == 'resolve':
        handle_resolve(args)


if __name__ == '__main__': # pragma: no cover
    main()
