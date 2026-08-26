import price_calculator
import pytest


def test_calculate_total_from_text_normal_case():
    assert price_calculator.calculate_total_from_text("10, 20, 30") == 60.0, "Result should be 60.0"

def test_calculate_total_from_text_spaces_case():
    assert price_calculator.calculate_total_from_text(" 5, 10 , 15") == 30.0, "Result should be 30.0"

def test_calculate_total_from_text_single_value_case():
    assert price_calculator.calculate_total_from_text("10") == 10.0, "Result should be 10.0"

def test_calculate_total_from_text_invalid_value_raises_value_error():
    with pytest.raises(ValueError):
        price_calculator.calculate_total_from_text("10, apple, 20")

def test_calculate_total_from_text_empty_string_returns_zero():
    assert price_calculator.calculate_total_from_text("") == 0.0, "Empty text should return 0.0"

def test_calculate_total_from_text_whitespace_returns_zero():
    assert price_calculator.calculate_total_from_text("   ") == 0.0, "Whitespace-only text should return 0.0"

def test_calculate_total_from_text_only_separator_raises_value_error():
    with pytest.raises(ValueError):
        price_calculator.calculate_total_from_text(",")

def test_load_prices_text_reads_file(tmp_path):
    file_path = tmp_path / "prices.txt"
    file_path.write_text("10, 20", encoding="utf-8")

    text = price_calculator.load_prices_text(file_path)

    assert text == "10, 20", "Loader should return file content"

def test_load_prices_text_missing_file_raises_error(tmp_path):
    missing_path = tmp_path / "missing.txt"
    with pytest.raises(FileNotFoundError):
        price_calculator.load_prices_text(missing_path)

        