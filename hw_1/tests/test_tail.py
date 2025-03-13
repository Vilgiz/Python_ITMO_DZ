import subprocess
import os
import pytest


@pytest.fixture
def artifacts_dir():
    return os.path.join(os.path.dirname(__file__), "..", "artifacts")

 
@pytest.fixture
def tail_input_file():
    temp_file = os.path.join(os.path.dirname(
        __file__), "test_data", "tail_input.txt")
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write("\n".join(str(i) for i in range(1, 21)) + "\n")

    yield temp_file

    os.remove(temp_file)


@pytest.fixture
def tail_input_file_2():
    temp_file = os.path.join(os.path.dirname(
        __file__), "test_data", "tail_input_2.txt")
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write("\n".join(str(i) for i in range(21, 41)) + "\n")

    yield temp_file

    os.remove(temp_file)


def test_tail_file(tail_input_file, artifacts_dir):
    result = subprocess.run(
        ["python", os.path.join(os.path.dirname(
            __file__), "..", "cli_tail.py"), tail_input_file],
        capture_output=True,
        text=True
    )

    output_path = os.path.join(artifacts_dir, "tail_output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)

    assert result.returncode == 0

    expected = "\n".join(str(i) for i in range(11, 21))
    assert result.stdout.strip() == expected.strip()


def test_tail_stdin(artifacts_dir):
    input_data = "\n".join(str(i) for i in range(1, 26))
    result = subprocess.run(
        ["python", os.path.join(os.path.dirname(
            __file__), "..", "cli_tail.py")],
        input=input_data,
        capture_output=True,
        text=True
    )

    output_path = os.path.join(artifacts_dir, "tail_stdin_output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)

    assert result.returncode == 0

    expected = "\n".join(str(i) for i in range(9, 26))
    assert result.stdout.strip() == expected.strip()


def test_tail_multiple_files(tail_input_file, tail_input_file_2, artifacts_dir):
    result = subprocess.run(
        ["python", os.path.join(os.path.dirname(__file__), "..", "cli_tail.py"),
         tail_input_file, tail_input_file_2],
        capture_output=True,
        text=True
    )

    output_path = os.path.join(artifacts_dir, "tail_multiple_output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)

    assert result.returncode == 0

    expected_output = (
        f"==> {tail_input_file} <==\n" +
        "\n".join(str(i) for i in range(11, 21)) +
        f"\n\n==> {tail_input_file_2} <==\n" +
        "\n".join(str(i) for i in range(31, 41))
    )

    assert result.stdout.strip() == expected_output.strip()


def test_tail_n_option(tail_input_file, artifacts_dir):
    result = subprocess.run(
        ["python", os.path.join(os.path.dirname(__file__), "..", "cli_tail.py"),
         "-n", "5", tail_input_file],
        capture_output=True,
        text=True
    )

    output_path = os.path.join(artifacts_dir, "tail_n_output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)

    assert result.returncode == 0

    expected_lines = "\n".join(str(i)
                               for i in range(16, 21))
    expected_output = f"==> {tail_input_file} <==\n{expected_lines}"

    assert result.stdout.strip() == expected_output.strip()
