import argparse
import tempfile
from pathlib import Path

from .package import extract_pptx, build_pptx


def do_fix_fonts(args):
    with tempfile.TemporaryDirectory(prefix="pptx-font-fix-") as tmp_dir:
        tmp_path = Path(tmp_dir)
        extract_pptx(args.src, tmp_path)
        build_pptx(tmp_path, args.dst)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('src', type=Path)
    parser.add_argument('dst', type=Path)
    args = parser.parse_args()
    do_fix_fonts(args)


if __name__ == '__main__':
    main()
