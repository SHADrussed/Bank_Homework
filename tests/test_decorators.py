import pytest

from src.decorators import log


@pytest.fixture
def my_function():
    @log()
    def my_function(x, y):
        return x + y

    return my_function


def test_log_ok(capsys, my_function):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


@pytest.mark.parametrize(
    "x, y, expected_error",
    [
        (1, "2", "unsupported operand type(s) for +: 'int' and 'str'"),
        (1, None, "unsupported operand type(s) for +: 'int' and 'NoneType'"),
    ],
)
def test_log_errors(capsys, my_function, x, y, expected_error):
    my_function(x, y)
    captured = capsys.readouterr()
    assert captured.out == f"my_function error {expected_error}. Inputs: (({x}, {repr(y)}), {{}})\n"


def test_log_file(tmpdir):
    log_file = tmpdir.join("mylog.txt")

    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    my_function(1, None)

    file_content = log_file.read()
    expected_content = (
        "my_function error unsupported operand type(s) for +: 'int' and 'NoneType'. Inputs: ((1, None), {})\n"
    )
    assert file_content == expected_content
