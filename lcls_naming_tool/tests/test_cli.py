# Unit tests for the LCLS Naming Tool script

import pytest
import json
import os
from pathlib import Path
from lcls_naming_tool.lcls_naming_tool import display_version, load_taxons, functional_component_is_valid, fungible_is_valid, constituent_component_is_valid, increment_is_valid, starts_alphanumeric, validate


def test_display_version(capsys):
    display_version()
    captured = capsys.readouterr()
    curr_ver = os.popen('git describe --tags').read().strip().split('-')
    assert str(captured.out).strip() == curr_ver[0]


load_taxons()


@pytest.mark.parametrize('test_name, expected', [('MR2K4', True), ('TV3L2', True), ('XCS', False)])
def test_functional_component_is_valid(test_name, expected):
    assert functional_component_is_valid(test_name) == expected


@pytest.mark.parametrize('test_name, expected', [('XYZ', False), ('ABCDEF', False), ('LD10', True)])
def test_fungible_is_valid(test_name, expected):
    assert fungible_is_valid(test_name) == expected


@pytest.mark.parametrize('test_name, expected', [('CBS', False), ('CLF', True), ('345', False)])
def test_constituent_component_is_valid(test_name, expected):
    assert constituent_component_is_valid(test_name) == expected


@pytest.mark.parametrize('test_name, expected', [('02', True), ('A36', False), ('3971', True)])
def test_increment_is_valid(test_name, expected):
    assert increment_is_valid(test_name) == expected


@pytest.mark.parametrize('test_name, expected', [('_PCTRLSPRBCK', False), ('PUMPSIZE', True), ('7ULM', True)])
def test_starts_alphanumeric_true(test_name, expected):
    assert starts_alphanumeric(test_name) == expected


@pytest.mark.parametrize('test_name, expected', [('MR2K4:PIP:03', True), ('TV3L2:KBO:PMONRAW', False), ('AT1L9:DG3:GCC', False)])
def test_validate_true_3_elements(test_name, expected):
    assert validate(test_name) == expected


@pytest.mark.parametrize('test_name, expected', [('MR2K4:GGG:PIP:01:PUMPSIZE', False), ('TV3L2:KBO:MRT:08:PMONRAW', False), ('AT1L9:DG3:GIGE:04:3XYZ', False)])
def test_validate_false_5_elements(test_name, expected):
    assert validate(test_name) == expected