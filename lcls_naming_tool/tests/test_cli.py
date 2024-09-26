# Unit tests for the LCLS Naming Tool script

import pytest
import json
from pathlib import Path
from lcls_naming_tool import display_version, load_taxons, functional_component_is_valid, fungible_is_valid, constituent_component_is_valid, increment_is_valid, starts_alphanumeric, validate


def test_display_version(capsys):

    display_version()
    captured = capsys.readouterr()
    assert str(captured.out).strip() == 'v1.0.0'


def test_load_taxons():
    pass


load_taxons()


def test_functional_component_is_valid_true():
    is_valid = functional_component_is_valid('TV2K4')
    assert is_valid == True


def test_functional_component_is_valid_false():
    is_valid = functional_component_is_valid('ZZ2K4')
    assert is_valid == False


def test_fungible_is_valid_true():
    is_valid = fungible_is_valid('XGMD')
    assert is_valid == True


def test_fungible_is_valid_false():
    is_valid = fungible_is_valid('GGG_HHH')
    assert is_valid == False


def test_constituent_component_is_valid_true():
    is_valid = constituent_component_is_valid('ETM')
    assert is_valid == True


def test_constituent_component_is_valid_false():
    is_valid = constituent_component_is_valid('XYZ')
    assert is_valid == False


def test_increment_is_valid_true():
    is_valid = increment_is_valid('03')
    assert is_valid == True


def test_increment_is_valid_false():
    is_valid = increment_is_valid('8')
    assert is_valid == False


def test_starts_alphanumeric_true():
    is_valid = starts_alphanumeric('PCTRLSPRBCK')
    assert is_valid == True


def test_starts_alphanumeric_false():
    is_valid = starts_alphanumeric('_=PCTRLSPRBCK')
    assert is_valid == False


def test_validate():
    pass
