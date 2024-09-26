# Unit tests for the LCLS Naming Tool script

import pytest
import json
from pathlib import Path
from lcls_naming_tool.lcls_naming_tool import display_version, load_taxons, functional_component_is_valid, fungible_is_valid, constituent_component_is_valid, increment_is_valid, starts_alphanumeric, validate


@pytest.fixture
def valid_name():
    return ['MR2K4', 'KBO', 'PIP', '01', 'PUMPSIZE']


@pytest.fixture
def invalid_name():
    return ['ABC12345M9', 'ABC', 'NBC', '7', '_PCTRLSPRBCK']


def test_display_version(capsys):

    display_version()
    captured = capsys.readouterr()
    assert str(captured.out).strip() == 'v1.0.0'


load_taxons()


def test_functional_component_is_valid_true(valid_name):
    is_valid = functional_component_is_valid(valid_name[0])
    assert is_valid == True


def test_functional_component_is_valid_false(invalid_name):
    is_valid = functional_component_is_valid(invalid_name[0])
    assert is_valid == False


def test_fungible_is_valid_true(valid_name):
    is_valid = fungible_is_valid(valid_name[1])
    assert is_valid == True


def test_fungible_is_valid_false(invalid_name):
    is_valid = fungible_is_valid(invalid_name[1])
    assert is_valid == False


def test_constituent_component_is_valid_true(valid_name):
    is_valid = constituent_component_is_valid(valid_name[2])
    assert is_valid == True


def test_constituent_component_is_valid_false(invalid_name):
    is_valid = constituent_component_is_valid(invalid_name[2])
    assert is_valid == False


def test_increment_is_valid_true(valid_name):
    is_valid = increment_is_valid(valid_name[3])
    assert is_valid == True


def test_increment_is_valid_false(invalid_name):
    is_valid = increment_is_valid(invalid_name[3])
    assert is_valid == False


def test_starts_alphanumeric_true(valid_name):
    is_valid = starts_alphanumeric(valid_name[4])
    assert is_valid == True


def test_starts_alphanumeric_false(invalid_name):
    is_valid = starts_alphanumeric(invalid_name[4])
    assert is_valid == False


def test_validate_true_3_elements(valid_name):
    test_name = valid_name[0] + ':' + valid_name[2] + ':' + valid_name[3]
    assert validate(test_name) == True


def test_validate_false_5_elements(invalid_name):
    test_name = ':'.join(str(name) for name in invalid_name)
    assert validate(test_name) == False
