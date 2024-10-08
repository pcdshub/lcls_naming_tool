#!/usr/bin/env python3

"""
LCLS Naming Tool

A tool for checking the form and content (but not meaning) of names with
respect to the LCLS naming convention.

Functional component source letters and beampath numbers come from
https://docs.google.com/drawings/d/1Sg7pT2TlKq8PgM7UstmJJBLKeqROQeDWbkD0sDoTDdY/edit

A valid name is in the format FFFFF:GGG:CCC:NN:XXXX, where GGG and NN are
optional and can be omitted. The XXXX is omitted for device names.

All permutations of valid names according to
LCLS_Photon_Source_and_Systems_Nomenclature.pdf. Names ending in XXXX are
PV names. Without XXXX are device names.

    FFFFF:CCC
    FFFFF:CCC:NN
    FFFFF:CCC:XXXX
    FFFFF:CCC:NN:XXXX
    FFFFF:GGG:CCC
    FFFFF:GGG:CCC:NN
    FFFFF:GGG:CCC:XXXX
    FFFFF:GGG:CCC:NN:XXXX

This script only checks the validity of PV and device names.
"""

import argparse
import json
import os
import re
import subprocess
import sys

fc_dict = {}
fg_dict = {}
ccc_dict = {}
beam_sources = ("K", "L")
beam_numbers = ("0", "1", "2", "3", "4", "5")


def try_get_lcls_taxons_cfg():
    if os.getenv("LCLS_NAMING_TOOL_TAXONS_DIR"):
        return str(os.getenv("LCLS_NAMING_TOOL_TAXONS_DIR"))
    else:
        current_dir = os.path.join(os.path.dirname(__file__), "")
        return current_dir + "/taxons"


def get_version():
    result = subprocess.run(
        ["git", "describe", "--tags"], capture_output=True, text=True
    )
    return (str(result.stdout).strip().split("-"))[0]


def load_taxons():
    global fc_dict
    global fg_dict
    global ccc_dict

    lcls_taxons_cfg = try_get_lcls_taxons_cfg()

    # Read the json files containing all the taxons
    with open(lcls_taxons_cfg + "/functional_component_taxon.json") as fc_file:
        fc_dict = json.load(fc_file)

    with open(lcls_taxons_cfg + "/fungible_element_taxon.json") as fg_file:
        fg_dict = json.load(fg_file)

    with open(lcls_taxons_cfg + "/ccc_taxon.json") as ccc_file:
        ccc_dict = json.load(ccc_file)


def functional_component_is_valid(fc_taxon):
    fc_length = len(fc_taxon)

    if 4 < len(fc_taxon) < 9:
        fc_prefix = fc_taxon[:2]  # max length is currently 2 letters
        fc_seq_num = fc_taxon[2 : fc_length - 2]  # max length set to 4
        # max length is currently 1 letter
        fc_source_ltr = fc_taxon[fc_length - 2 : fc_length - 1]
        # max length is currently 1 digit
        fc_beam_num = fc_taxon[fc_length - 1 : fc_length]
    else:
        return False

    # validate FFFFF
    try:
        fc_dict[fc_prefix]
        int(fc_seq_num)

        if (fc_source_ltr not in beam_sources) or (fc_beam_num not in beam_numbers):
            raise NameError

        if int(fc_seq_num[0]) == 0:  # zero padding for sequence number is not allowed
            raise ValueError

    except (KeyError, NameError, ValueError):
        return False

    else:
        return True


def fungible_is_valid(fg_taxon):
    try:
        fg_elements = fg_taxon.split("_")

        for name in fg_elements:
            fg_dict[name]

    except KeyError:
        return False

    else:
        return True


def constituent_component_is_valid(ccc_taxon):
    try:
        ccc_dict[ccc_taxon]

    except KeyError:
        return False
    else:
        return True


def increment_is_valid(nn_taxon):
    # check the increment is an int and has at least 2 digits
    if len(nn_taxon) >= 2:
        try:
            int(nn_taxon)

        except ValueError:
            return False

        else:
            return True
    else:
        return False


def starts_alphanumeric(taxon):
    # check the element starts with a letter or number
    return bool(re.search("^[a-zA-Z0-9]", taxon))


def validate(user_input):
    if ("." in user_input) or (len(user_input) > 60):
        return False

    name = [x.strip() for x in user_input.upper().split(":")]

    for element in name:
        if not starts_alphanumeric(element):
            return False

    # Check the length of the name
    if (len(name) < 2) or (len(name) > 5):
        return False

    # Validate the functional component (FFFFF)
    fc_taxon = str(name[0])
    fc_valid = functional_component_is_valid(fc_taxon)

    second_element = name[1]

    if fc_valid:
        # Check for name with 2 elements (FFFFF:CCC)
        if len(name) == 2:
            ccc_valid = constituent_component_is_valid(second_element)

            if ccc_valid:
                return True
            else:
                return False

        third_element = name[2]

        # check for name with 3 elements (FFFFF:GGG:CCC, FFFFF:CCC:NN, FFFFF:CCC:XXXX)
        if len(name) == 3:
            fg_valid = fungible_is_valid(second_element)
            ccc_valid = constituent_component_is_valid(second_element)

            if fg_valid:
                ccc_valid = constituent_component_is_valid(third_element)
                if ccc_valid:
                    return True
                else:
                    return False
            elif ccc_valid:
                element_valid = starts_alphanumeric(third_element)
                if element_valid:
                    return True
                else:
                    return False
            else:
                return False

        fourth_element = name[3]

        # Check for name with 4 elements (FFFFF:GGG:CCC:NN, FFFFF:GGG:CCC:XXXX, FFFFF:CCC:NN:XXXX)
        if len(name) == 4:
            fg_valid = fungible_is_valid(second_element)
            ccc_valid = constituent_component_is_valid(second_element)

            if fg_valid:
                ccc_valid = constituent_component_is_valid(third_element)
                fourth_element_valid = starts_alphanumeric(fourth_element)

                if ccc_valid and fourth_element_valid:
                    return True
                else:
                    return False

            elif ccc_valid:
                increment_valid = increment_is_valid(third_element)
                cspv_valid = starts_alphanumeric(fourth_element)

                if increment_valid and cspv_valid:
                    return True
                else:
                    return False

            else:
                return False

        # check for name with 5 elements (FFFFF:GGG:CCC:NN:XXXX)
        if len(name) == 5:
            fg_taxon = name[1]
            fg_valid = fungible_is_valid(fg_taxon)

            ccc_taxon = name[2]
            ccc_valid = constituent_component_is_valid(ccc_taxon)

            nn_taxon = name[3]
            nn_valid = increment_is_valid(nn_taxon)

            fifth_element = name[4]
            fifth_element_valid = starts_alphanumeric(fifth_element)

            if fg_valid and ccc_valid and nn_valid and fifth_element_valid:
                return True
            else:
                return False

    else:
        return False


def main():
    load_taxons()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "string", nargs="*", type=str, help="PV or device name to validate"
    )
    parser.add_argument("-v", "--version", action="store_true")
    args = parser.parse_args()

    if args.version:
        version = get_version()
        print(version)
        sys.exit()

    # If no strings are provided via command line arguments, read from stdin
    if not args.string:
        args.string = sys.stdin.read().splitlines()

    # Process the strings
    for string in args.string:
        if validate(string):
            print("Valid")
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
