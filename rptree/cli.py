import argparse
import pathlib
import sys

from . import __version__
from .rptree import DirectoryTree

def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    tree = DirectoryTree(root_dir)
    tree.generate()

def parse_cmd_line_arguments()
    parser = argpars.ArgumentParser(
        prog="tree",
        description="PyTree, a directory tree generator",
        epiloge="Thanks for using PyTree!",
    )
    parser.version = f"PyTree v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        meta_var="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR",
    )
    return parser.parse_args()