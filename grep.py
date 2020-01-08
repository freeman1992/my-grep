import argparse
import re
from enum import Enum
from argparse import Namespace


class Color(Enum):
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'


def colorize_search(line: str, word: str, flags=0) -> str:
    return re.sub(rf"({word})", rf"{Color.RED.value}\1{Color.DEFAULT.value}", line, flags=flags)


def format_orig_line(pattern: str, orig_line: str, display_orig_line: bool = False, ignore_case: bool = False) -> str:
    if display_orig_line:
        return colorize_search(orig_line, pattern, re.IGNORECASE if ignore_case else 0)
    return ""


def get_frequency(line_text: str, pattern: str, ignore_case: bool) -> int:
    if ignore_case:
        return line_text.lower().count(pattern.lower())

    return line_text.count(pattern)


def print_search(line_number: int, frequency: int, pattern: str, orig_line: str, display_orig_line: bool,
                 ignore_case: bool = False) -> None:
    print(f"{line_number}:\t({frequency}) {format_orig_line(pattern, orig_line, display_orig_line, ignore_case)}",
          end="\n" if not display_orig_line else "")


def init_arguments() -> Namespace:
    parser = argparse.ArgumentParser(description="Search for PATTERN in FILE and displays line and frequency.")
    parser.add_argument("path_file", type=str, help='path to the file to inspect', metavar="FILE")
    parser.add_argument("search_string", type=str, help='a string to search', metavar="PATTERN")
    parser.add_argument("-m", "--max-count", type=int, help='stop after NUM selected lines', metavar="N")
    parser.add_argument("-i", "--ignore-case", action="store_true", help="ignore case distinctions")
    parser.add_argument("-s", "--show", action="store_true", help="displays the whole line with text",
                        dest="display_orig_line")
    parser.add_argument("-t", "--total", action="store_true", help="displays total number of lines found")

    return parser.parse_args()


def main() -> None:
    args = init_arguments()
    total_search = 0

    with open(args.path_file, 'r') as opened_file:
        for line, content in enumerate(opened_file, start=1):
            if args.max_count:
                if total_search == args.max_count:
                    break
            char_frequency = get_frequency(content, args.search_string, args.ignore_case)
            if char_frequency > 0:
                print_search(line, char_frequency, args.search_string, content, args.display_orig_line,
                             args.ignore_case)
                total_search += 1
        if args.total:
            print(f"Total lines found: {total_search}")


if __name__ == "__main__":
    main()
