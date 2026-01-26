import pytest
from src.decorators import log, my_function


@pytest.fixture
def function_example():
    @log()
    def my_function(x, y):
        return x + y
    return my_function

@pytest.fixture
def function_example_with_parameter(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    return my_function, log_file

@pytest.mark.parametrize("first_num, second_num, expected",
                         [
                             (1, 2, "my_function ok"),
                             (-1, 2, "my_function ok"),
                             (1, -2, "my_function ok")
                         ]
                         )
def test_log(function_example, first_num, second_num, expected):
    assert function_example(first_num, second_num) == expected


@pytest.mark.parametrize("first_num, second_num, expected",
                         [
                             ("", 2, "my_function error: "
                                     "can only concatenate str (not \"int\") to str. "
                                     "Inputs: ('', 2), {}"),
                             (1, "2", "my_function error: "
                                      "unsupported operand type(s) for +: 'int' and 'str'. "
                                      "Inputs: (1, '2'), {}"),
                             (None, 2, "my_function error: "
                                       "unsupported operand type(s) for +: 'NoneType' and 'int'. "
                                       "Inputs: (None, 2), {}"),
                             (1, None, "my_function error: "
                                       "unsupported operand type(s) for +: 'int' and 'NoneType'. "
                                       "Inputs: (1, None), {}"),
                             ([1, 2], None, "my_function error: "
                                            "can only concatenate list (not \"NoneType\") to list. "
                                            "Inputs: ([1, 2], None), {}"),
                             ([1, 2], 3, "my_function error: "
                                         "can only concatenate list (not \"int\") to list. "
                                         "Inputs: ([1, 2], 3), {}"),
                             ({"1":"2"}, None, "my_function error: "
                                               "unsupported operand type(s) for +: 'dict' and 'NoneType'. "
                                               "Inputs: ({'1': '2'}, None), {}")
                         ]
                         )
def test_log_exceptions(function_example, first_num, second_num, expected):
    assert function_example(first_num, second_num) == expected


@pytest.mark.parametrize("first_num, second_num, expected",
                         [
                             (1, 2, "my_function ok\n"),
                             (-1, -2, "my_function ok\n"),
                             ("", 2, "my_function error: "
                                     "can only concatenate str (not \"int\") to str. "
                                     "Inputs: ('', 2), {}\n"),
                             ([1, 2], None, "my_function error: "
                                            "can only concatenate list (not \"NoneType\") to list. "
                                            "Inputs: ([1, 2], None), {}\n"),
                             (None, 2, "my_function error: "
                                       "unsupported operand type(s) for +: 'NoneType' and 'int'. "
                                       "Inputs: (None, 2), {}\n")
                         ]
                         )
def test_log_capsys(function_example, first_num, second_num, expected, capsys):
    function_example(first_num, second_num)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_log_creates_file(function_example_with_parameter):
    my_function, log_file = function_example_with_parameter
    my_function(1, 2)
    assert log_file.exists()

@pytest.mark.parametrize("first_num, second_num, expected",
                         [
                             ("", 2, "my_function error: "
                                     "can only concatenate str (not \"int\") to str. "
                                     "Inputs: ('', 2), {}"),
                             (1, "2", "my_function error: "
                                      "unsupported operand type(s) for +: 'int' and 'str'. "
                                      "Inputs: (1, '2'), {}"),
                             (None, 2, "my_function error: "
                                       "unsupported operand type(s) for +: 'NoneType' and 'int'. "
                                       "Inputs: (None, 2), {}"),
                             (1, None, "my_function error: "
                                       "unsupported operand type(s) for +: 'int' and 'NoneType'. "
                                       "Inputs: (1, None), {}"),
                             ([1, 2], None, "my_function error: "
                                            "can only concatenate list (not \"NoneType\") to list. "
                                            "Inputs: ([1, 2], None), {}"),
                             ([1, 2], 3, "my_function error: "
                                         "can only concatenate list (not \"int\") to list. "
                                         "Inputs: ([1, 2], 3), {}"),
                             ({"1":"2"}, None, "my_function error: "
                                               "unsupported operand type(s) for +: 'dict' and 'NoneType'. "
                                               "Inputs: ({'1': '2'}, None), {}")
                         ]
                         )
def test_log_check_content(function_example_with_parameter, first_num, second_num, expected):
    my_function, log_file = function_example_with_parameter
    my_function(first_num, second_num)
    content = log_file.read_text(encoding="utf-8")
    assert expected in content

























