#!/usr/bin/env python3

'''
    LCLS Naming Tool

    A tool for checking the form and content (but not meaning) of PV names with
    respect to the LCLS naming convention.

    A valid PV name is in the format FFFFF:GGG:CCC:NN:XXXX, where GGG and NN are
    optional and can be omitted.

    This script only checks the validity of PV names (not devices).
'''


import sys
import json


fc_dict = {}
fg_dict = {}
ccc_dict = {}
beam_sources = {'K': '', 'L': ''}
beam_numbers = {'0': '', '1': '', '2': '', '3': '', '4': '', '5': ''}


def functional_component_is_valid(fc_taxon):
    # check length of the functional component
    if (len(fc_taxon) == 5):
        fc_prefix = str(fc_taxon[0] + fc_taxon[1])
        fc_source_ltr = str(fc_taxon[3])
        fc_beam_num = str(fc_taxon[4])
    else:
        return False

    # FFFFF is required
    try:
        fc_dict[fc_prefix]
        beam_sources[fc_source_ltr]
        beam_numbers[fc_beam_num]

    except KeyError:
        return False

    else:
        return True


def constituent_component_is_valid(ccc_taxon):
    try:
        ccc_dict[ccc_taxon]
    except:
        return False
    else:
        return True


def fungible_is_valid(fg_taxon):
    try:
        fg_components = fg_taxon.replace(
            '_', ' ').replace(':', ' ').split()

        for name in fg_components:
            fg_dict[name]

    except KeyError:
        return False

    else:
        return True


def increment_is_valid(nn_taxon):
    # check the increment is an int and has at least 2 digits
    try:
        assert int(nn_taxon)
        assert len(nn_taxon) >= 2

    except ValueError:
        return False

    else:
        return True


def main():

    fc_valid = True
    fg_valid = True
    ccc_valid = True
    nn_valid = True

    global fc_dict
    global fg_dict
    global ccc_dict

    # Read the json files containing all the taxons
    with open('functional_component_taxon.json') as fc_file:
        fc_dict = json.load(fc_file)

    with open('fungible_element_taxon.json') as fg_file:
        fg_dict = json.load(fg_file)

    with open('ccc_taxon.json') as ccc_file:
        ccc_dict = json.load(ccc_file)

    # Check if user entered a file name or PV name (a string)
    if not sys.stdin.isatty():
        input_stream = sys.stdin
    else:
        try:
            input_filename = sys.argv[1]
        except IndexError:
            message = 'File name not entered.'
            raise IndexError(message)
        else:
            input_stream = open(input_filename, newline='')

    for line in input_stream:
        try:
            assert '.' not in line
            assert (len(line) <= 60)

        except AssertionError:
            print('Invalid')
            return

        pv_name = line.split(':')

        # Check the length of the PV name is valid
        if (len(pv_name) < 3) or (len(pv_name) > 5):
            print('Invalid')
            return

        # parse the functional component (FFFFF)
        fc_taxon = list(pv_name[0])
        fc_valid = functional_component_is_valid(fc_taxon)

        if fc_valid:

            # check for PV name with 3 elements
            if (len(pv_name) == 3):
                ccc_taxon = pv_name[1]
                ccc_valid = constituent_component_is_valid(ccc_taxon)

                if ccc_valid:
                    print('Valid')
                else:
                    print('Invalid')

            # check for PV name with 4 elements
            if (len(pv_name) == 4):
                fg_taxon = pv_name[1]
                fg_valid = fungible_is_valid(fg_taxon)

                nn_taxon = pv_name[2]
                nn_valid = increment_is_valid(nn_taxon)

                if (fg_valid and not nn_valid):
                    ccc_taxon = pv_name[2]
                    ccc_valid = constituent_component_is_valid(ccc_taxon)

                    if ccc_valid:
                        print('Valid')
                    else:
                        print('Invalid')

                if (not fg_valid and nn_valid):
                    ccc_taxon = pv_name[1]
                    ccc_valid = constituent_component_is_valid(ccc_taxon)

                    if ccc_valid:
                        print('Valid')
                    else:
                        print('Invalid')

            # check for PV name with 5 elements
            if (len(pv_name) == 5):
                fg_taxon = pv_name[1]
                fg_valid = fungible_is_valid(fg_taxon)

                ccc_taxon = pv_name[2]
                ccc_valid = constituent_component_is_valid(ccc_taxon)

                nn_taxon = pv_name[3]
                nn_valid = increment_is_valid(nn_taxon)

                if fg_valid and ccc_valid and nn_valid and fc_valid:
                    print('Valid')
                else:
                    print('Invalid')

        else:
            print('Invalid')


if __name__ == '__main__':
    main()
