#!/usr/bin/env python3
import os
import sys
import argparse
from colorama import Fore, Style, init

init(autoreset=True)


def get_size(path):
    try:
        size = os.path.getsize(path)
        return f"{size / 1024:.1f} KB"
    except OSError:
        return "?"


def print_tree(
    path,
    prefix="",
    depth=None,
    level=0,
    show_files=False,
    show_hidden=False,
    show_size=False,
    sort="name",
):
    """Recursively prints directory structure with depth control and optional file info."""
    if depth is not None and level >= depth:
        return

    try:
        entries = os.listdir(path)
    except PermissionError:
        print(prefix + Fore.RED + "[Access Denied]" + Style.RESET_ALL)
        return

    if not show_hidden:
        entries = [e for e in entries if not e.startswith(".")]

    dirs = [e for e in entries if os.path.isdir(os.path.join(path, e))]
    files = [e for e in entries if os.path.isfile(os.path.join(path, e))] if show_files else []

    # Sorting logic
    def safe_getsize(p):
        try:
            return os.path.getsize(p)
        except Exception:
            return 0

    if sort == "size":
        dirs.sort(key=lambda d: safe_getsize(os.path.join(path, d)))
        files.sort(key=lambda f: safe_getsize(os.path.join(path, f)))
    elif sort == "time":
        dirs.sort(key=lambda d: os.path.getmtime(os.path.join(path, d)))
        files.sort(key=lambda f: os.path.getmtime(os.path.join(path, f)))
    else:
        dirs.sort()
        files.sort()

    entries = dirs + files
    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        connector = "└── " if i == len(entries) - 1 else "├── "
        is_dir = os.path.isdir(full_path)
        color = Fore.BLUE + Style.BRIGHT if is_dir else Fore.WHITE
        size_info = f" [{get_size(full_path)}]" if show_size and not is_dir else ""
        print(prefix + connector + color + entry + Style.RESET_ALL + size_info)

        new_prefix = prefix + ("    " if i == len(entries) - 1 else "│   ")
        if is_dir:
            print_tree(
                full_path,
                new_prefix,
                depth,
                level + 1,
                show_files,
                show_hidden,
                show_size,
                sort,
            )


def banner():
    """Display a small banner when run interactively."""
    print(
        Fore.GREEN
        + Style.BRIGHT
        + "\n🌳  PyTree — Modern, colorful CLI replacement for the tree command\n"
        + Style.RESET_ALL
    )


def main():
    parser = argparse.ArgumentParser(
        prog="pytree",
        description="Display a visual tree of directories and files with colors, sizes, and depth control.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root directory path (default: current directory)",
    )
    parser.add_argument(
        "-d",
        "--depth",
        type=int,
        help="Limit how many directory levels to display",
    )
    parser.add_argument(
        "-f",
        "--files",
        action="store_true",
        help="Include files in the tree view",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Show hidden files and directories (those starting with '.')",
    )
    parser.add_argument(
        "-s",
        "--size",
        action="store_true",
        help="Display file sizes in KB next to filenames",
    )
    parser.add_argument(
        "--sort",
        choices=["name", "size", "time"],
        default="name",
        help="Sort entries by name, size, or modification time",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Export tree output to a text file",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable color output",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="pytree 1.1.0",
        help="Show version information and exit",
    )

    args = parser.parse_args()

    # Disable color if requested or output is piped
    if args.no_color or not sys.stdout.isatty():
        init(strip=True)

    root = os.path.abspath(args.path)
    if not os.path.exists(root):
        print(Fore.RED + f"Error: Path not found -> {root}" + Style.RESET_ALL)
        sys.exit(1)

    if sys.stdout.isatty():
        banner()

    print(Fore.GREEN + Style.BRIGHT + root + Style.RESET_ALL)

    # Capture output if exporting to a file
    if args.output:
        from io import StringIO
        buffer = StringIO()
        sys_stdout = sys.stdout
        sys.stdout = buffer
        print_tree(
            root,
            depth=args.depth,
            show_files=args.files,
            show_hidden=args.all,
            show_size=args.size,
            sort=args.sort,
        )
        sys.stdout = sys_stdout
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(buffer.getvalue())
        print(Fore.YELLOW + f"\n[✔] Output saved to {args.output}" + Style.RESET_ALL)
    else:
        print_tree(
            root,
            depth=args.depth,
            show_files=args.files,
            show_hidden=args.all,
            show_size=args.size,
            sort=args.sort,
        )


if __name__ == "__main__":
    main()
