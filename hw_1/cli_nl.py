import sys


def nl(files=None):
    """
    Выводит пронумерованные строки из одного или нескольких файлов.
    """
    if not files:
        lines = sys.stdin.readlines()
        for i, line in enumerate(lines, start=1):
            print(f"{i}\t{line}", end="")
        return

    multiple_files = len(files) > 1

    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Ошибка: Файл '{file}' не найден.", file=sys.stderr)
            continue
        except Exception as e:
            print(f"Ошибка при чтении '{file}': {e}", file=sys.stderr)
            continue

        if multiple_files:
            print(f"==> {file} <==")

        for i, line in enumerate(lines, start=1):
            print(f"{i}\t{line}", end="")

        if multiple_files:
            print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        nl(sys.argv[1:])
    else:
        nl()
