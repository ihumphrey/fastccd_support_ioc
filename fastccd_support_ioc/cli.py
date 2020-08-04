"""Console script for fastccd_support_ioc."""
import argparse
from textwrap import dedent
import sys
from caproto.server import ioc_arg_parser, run
from .fastccd_support_ioc import SupportIOC


def main():
    """Console script for fastccd_support_ioc."""

    ioc_options, run_options = ioc_arg_parser(
        default_prefix='XF:7011:',
        desc=dedent(SupportIOC.__doc__))
    ioc = SupportIOC(**ioc_options)
    run(ioc.pvdb, **run_options)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
