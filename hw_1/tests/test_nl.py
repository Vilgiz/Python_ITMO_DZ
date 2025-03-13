import subprocess
import os
import pytest


@pytest.fixture
def artifacts_dir():
    return os.path.join(os.path.dirname(__file__), "..", "artifacts")


@pytest.fixture
def nl_input_file():
    temp_file = os.path.join(os.path.dirname(
        __file__), "test_data", "nl_input.txt")
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write("line1\nline2\nline3\nline4\nline5\n")

    yield temp_file
    os.remove(temp_file)


@pytest.fixture
def nl_input_file_2():
    temp_file = os.path.join(os.path.dirname(
        __file__), "test_data", "nl_input_2.txt")
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write("alpha\nbeta\ngamma\ndelta\nepsilon\n")

    yield temp_file
    os.remove(temp_file)


@pytest.fixture
def empty_file():
    temp_file = os.path.join(os.path.dirname(
        __file__), "test_data", "empty.txt")
    open(temp_file, "w", encoding="utf-8").close()

    yield temp_file
    os.remove(temp_file)


@pytest.fixture
def file_with_empty_lines():
    temp_file = os.path.join(os.path.dirname(
        __file__), "test_data", "empty_lines.txt")
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write("\nline1\n\nline2\n\nline3\n")

    yield temp_file
    os.remove(temp_file)


def test_nl_file(nl_input_file, artifacts_dir):
    result = subprocess.run(
        ["python", os.path.join(os.path.dirname(
            __file__), "..", "cli_nl.py"), nl_input_file],
        capture_output=True,
        text=True
    )

    output_path = os.path.join(artifacts_dir, "nl_output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)

    assert result.returncode == 0

    expected_lines = [f"{i+1}\tline{i+1}" for i in range(5)]
    expected_output = "\n".join(expected_lines)

    assert result.stdout.strip() == expected_output.strip()


def test_nl_stdin(artifacts_dir):
    input_data = "one\ntwo\nthree\nfour\nfive\nsix\n"
    result = subprocess.run(
        ["python", os.path.join(os.path.dirname(__file__), "..", "cli_nl.py")],
        input=input_data,
        capture_output=True,
        text=True
    )

    output_path = os.path.join(artifacts_dir, "nl_stdin_output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)

    assert result.returncode == 0

    expected_lines = [f"{i+1}\t{line}" for i,
                      line in enumerate(input_data.strip().split("\n"))]
    expected_output = "\n".join(expected_lines)

    assert result.stdout.strip() == expected_output.strip()


def test_nl_multiple_files(nl_input_file, nl_input_file_2, artifacts_dir):
    result = subprocess.run(
        ["python", os.path.join(os.path.dirname(__file__), "..", "cli_nl.py"),
         nl_input_file, nl_input_file_2],
        capture_output=True,
        text=True
    )

    output_path = os.path.join(artifacts_dir, "nl_multiple_output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)

    assert result.returncode == 0

    expected_with_headers = [
        f"==> {nl_input_file} <==",
        "1\tline1",
        "2\tline2",
        "3\tline3",
        "4\tline4",
        "5\tline5",
        "",
        f"==> {nl_input_file_2} <==",
        "1\talpha",
        "2\tbeta",
        "3\tgamma",
        "4\tdelta",
        "5\tepsilon"
    ]

    expected_without_headers = [
        "1\tline1",
        "2\tline2",
        "3\tline3",
        "4\tline4",
        "5\tline5",
        "1\talpha",
        "2\tbeta",
        "3\tgamma",
        "4\tdelta",
        "5\tepsilon"
    ]

    actual_output = result.stdout.strip().splitlines()

    assert actual_output in [expected_with_headers, expected_without_headers], (
        f"\nОжидалось:\n{expected_with_headers}\nИЛИ\n{expected_without_headers}\n\n"
        f"Получено:\n{actual_output}"
    )


def test_nl_empty_file(empty_file, artifacts_dir):
    result = subprocess.run(
        ["python", os.path.join(os.path.dirname(
            __file__), "..", "cli_nl.py"), empty_file],
        capture_output=True,
        text=True
    )

    output_path = os.path.join(artifacts_dir, "nl_empty_file_output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)

    assert result.returncode == 0
    assert result.stdout.strip() == ""


def test_nl_file_with_empty_lines(file_with_empty_lines, artifacts_dir):
    result = subprocess.run(
        ["python", os.path.join(os.path.dirname(
            __file__), "..", "cli_nl.py"), file_with_empty_lines],
        capture_output=True,
        text=True
    )

    output_path = os.path.join(artifacts_dir, "nl_empty_lines_output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)

    assert result.returncode == 0

    expected_output = [
        "1\t",
        "2\tline1",
        "3\t",
        "4\tline2",
        "5\t",
        "6\tline3"
    ]

    actual_output = result.stdout.strip().splitlines()
    assert actual_output == expected_output, f"\nОжидалось:\n{expected_output}\n\nПолучено:\n{actual_output}"
