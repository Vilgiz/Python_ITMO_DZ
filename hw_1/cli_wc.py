import sys
import os


def count_stats(file=None):
    """
    Подсчитывает количество строк, слов и символов.
    """
    lines, words, chars = 0, 0, 0

    try:
        if file:
            if not os.path.exists(file):
                print(f"Ошибка: Файл '{file}' не найден.", file=sys.stderr)
                return None
            if not os.path.isfile(file):
                print(f"Ошибка: '{file}' не является файлом.", file=sys.stderr)
                return None

            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    lines += 1
                    words += len(line.split())
                    chars += len(line)

        else:
            for line in sys.stdin:
                lines += 1
                words += len(line.split())
                chars += len(line)

    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return None

    return lines, words, chars


if __name__ == "__main__":
    total_lines = 0
    total_words = 0
    total_chars = 0
    file_count = len(sys.argv[1:])

    if file_count > 0:
        for filename in sys.argv[1:]:
            result = count_stats(filename)
            if result:
                lines, words, chars = result
                total_lines += lines
                total_words += words
                total_chars += chars
                print(f"{lines} {words} {chars} {filename}")

        if file_count > 1:
            print(f"{total_lines} {total_words} {total_chars} total")
    else:
        lines, words, chars = count_stats()
        print(f"{lines} {words} {chars}")
