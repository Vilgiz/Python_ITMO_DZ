import sys
import os


def tail(file=None, num_lines=10):
    """
    Выводит последние num_lines строк из файла или из stdin.
    """
    lines_to_show = []

    try:
        if file:
            if not os.path.exists(file):
                print(f"Ошибка: Файл '{file}' не найден.", file=sys.stderr)
                return

            with open(file, 'r', encoding='utf-8') as f:
                lines_to_show = f.readlines()[-num_lines:]

            if len(sys.argv) > 2:
                print(f"==> {file} <==")

        else:
            lines_to_show = sys.stdin.readlines()[-17:]

        for line in lines_to_show:
            print(line, end='')

    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)


if __name__ == "__main__":
    num_lines = 10

    args = sys.argv[1:]
    if "-n" in args:
        try:
            index = args.index("-n")
            num_lines = int(args[index + 1])
            args = args[:index] + args[index + 2:]
        except (IndexError, ValueError):
            print("Ошибка: Некорректный аргумент для -n", file=sys.stderr)
            sys.exit(1)

    if args:
        for i, filename in enumerate(args):
            if i > 0:
                print()
            tail(filename, num_lines)
    else:
        tail(num_lines=17)
