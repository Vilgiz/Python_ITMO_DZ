import subprocess
import os
import pytest
import re


@pytest.fixture
def artifacts_dir():
    return os.path.join(os.path.dirname(__file__), "..", "artifacts")


@pytest.fixture
def wc_input_file():
    return os.path.join(os.path.dirname(__file__), "test_data", "wc_input.txt")


@pytest.fixture
def wc_input_file_2():
    temp_file = os.path.join(os.path.dirname(
        __file__), "test_data", "wc_input_2.txt")
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write("Another test file.\nIt has multiple lines.\nAnd words.")

    yield temp_file
    os.remove(temp_file)


def test_wc_file(wc_input_file, artifacts_dir):
    result = subprocess.run(
        ["python", os.path.join(os.path.dirname(
            __file__), "..", "cli_wc.py"), wc_input_file],
        capture_output=True,
        text=True
    )

    print("\n--- STDOUT ---")
    print(result.stdout)

    assert result.returncode == 0

    with open(wc_input_file, "r", encoding="utf-8") as f:
        content = f.read()

    expected_lines = content.count("\n")
    if content and not content.endswith("\n"):
        expected_lines += 1

    expected_words = len(content.split())
    expected_chars = len(content)

    output_lines = result.stdout.strip().split("\n")

    assert any(
        re.search(
            rf"\b{expected_lines} {expected_words} {expected_chars}\b", line)
        for line in output_lines
    ), f"Не найдено: {expected_lines} {expected_words} {expected_chars} в {result.stdout}"


def test_wc_multiple_files(wc_input_file, wc_input_file_2, artifacts_dir):
    result = subprocess.run(
        ["python", os.path.join(os.path.dirname(__file__), "..", "cli_wc.py"),
         wc_input_file, wc_input_file_2],
        capture_output=True,
        text=True
    )

    print("\n--- STDOUT ---")
    print(result.stdout)

    assert result.returncode == 0

    total_lines, total_words, total_chars = 0, 0, 0
    expected_outputs = []

    for filename in [wc_input_file, wc_input_file_2]:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
        lines = content.count(
            "\n") + (1 if content and not content.endswith("\n") else 0)
        words = len(content.split())
        chars = len(content)
        total_lines += lines
        total_words += words
        total_chars += chars
        expected_outputs.append(f"{lines} {words} {chars}")

    expected_outputs.append(f"{total_lines} {total_words} {total_chars} total")

    output_lines = result.stdout.strip().split("\n")
    for expected in expected_outputs:
        assert any(re.search(rf"\b{expected}\b", line)
                   for line in output_lines), f"Не найдено: {expected} в {result.stdout}"
