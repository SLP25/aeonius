from aeonius_parser import parse
from language.context import Context

import sys


def help():
    print("                aeonius                    ")
    print("     A functional extension for Python     ")
    print("===========================================")
    print()
    print("Valid arguments:")
    print("-h: Get help")
    print("-d: Whether to run on debug mode. In debug")
    print("mode, the compiled python code is printed")
    print("to stdout instead of to a file")
    print("--input: The input aeonius file")
    print("--output: The python file to write the parsed")
    print("program to")


def parse_args(single_flags, valid_args):

    result = {}

    argv = []

    for s in single_flags:
        result[s[1:]] = False

    # Remove flags that don't take any arguments
    # and process them now
    for str in sys.argv:
        if str in single_flags:
            # Remove initial '-' from string
            result[str[1:]] = True
        else:
            argv = argv + [str]

    # User provided arguments start at index 1 (0 is the process name)
    # In this format arguments are passed as (note we have removed flags that
    # take no arguments)
    # program --flag1 value1 --flag2 value2 ...
    # In this schema, the values are stored in odd positions and flags
    # in even positions.
    # As such, we iterate over the even indices of the argv list
    for i in range(2, len(argv), 2):
        if argv[i - 1] in valid_args:
            # Remove first '--' chars from argv
            result[argv[i - 1][2:]] = argv[i]
        else:
            print(f"Invalid argument {argv[i - 1]}")
            exit(1)

    return result


def transpile(input, debug):
    parsed = parse(input)

    with open("aeonius_stdlib.py", "r") as f:
        stdlib = f.read()
    
    context = Context()
    context.symbols = Context.stdlib_symbols

    if debug:
        return parsed.to_python(context)
    else:
        return stdlib + parsed.to_python(context)

def main():
    single = [
        "-h",
        "-d"
    ]

    valid_arguments = [
        "--input",
        "--output"
    ]

    args = parse_args(single, valid_arguments)

    if args["h"]:
        help()
        return

    with open(args["input"], "r") as f:
        data = f.read()

    parsed = transpile(data, args["d"])

    if (args["d"]):
        print(parsed)

    else:
        with open(args["output"], "w") as g:
            g.write(parsed)


def import_main():
    args = parse_args(single, valid_arguments)
    with open(args["input"], "r") as f:
        data = f.read()

    parsed = parse(data)
    exec(parsed.to_python(Context()))


def aeonius_import(path):
    with open(path, "r") as f:
        data = f.read()
        parsed = parse(data)
        exec(parsed.to_python(Context()))


if __name__ == "__main__":
    main()
