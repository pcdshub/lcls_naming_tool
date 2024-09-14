#!/usr/bin/env python3

'''
    LCLS Naming Tool

    A tool for checking the form and content (but not meaning) of PV names with
    respect to the LCLS naming convention.

    A valid PV name is in the format FFFFF:GGG:CCC:NN:XXXX, where GGG and NN are
    optional and can be omitted. The XXXX is omitted for device names.

    All permutations of valid PV and device names according to 
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
'''


import sys
import json
import re


fc_dict = {}
fg_dict = {}
ccc_dict = {}
beam_sources = {'K': '', 'L': ''}
beam_numbers = {'0': '', '1': '', '2': '', '3': '', '4': '', '5': ''}


def load_taxons():
    global fc_dict
    global fg_dict
    global ccc_dict

    # Read the json files containing all the taxons
    with open('taxons/functional_component_taxon.json') as fc_file:
        fc_dict = json.load(fc_file)

    with open('taxons/fungible_element_taxon.json') as fg_file:
        fg_dict = json.load(fg_file)

    with open('taxons/ccc_taxon.json') as ccc_file:
        ccc_dict = json.load(ccc_file)


def functional_component_is_valid(fc_taxon):
    
    # check length of the functional component
    if (len(fc_taxon) == 5):
        fc_prefix = fc_taxon[0] + fc_taxon[1]
        fc_source_ltr = fc_taxon[3]
        fc_beam_num = fc_taxon[4]
    else:
        return False

    # validate FFFFF
    try:
        fc_dict[fc_prefix]
        beam_sources[fc_source_ltr]
        beam_numbers[fc_beam_num]

    except KeyError:
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


def constituent_component_is_valid(ccc_taxon):
    try:
        ccc_dict[ccc_taxon]
    except:
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


def is_alphanumeric(taxon):
    # check the element starts with a letter or number 
    match = re.search('^[a-zA-Z0-9]', taxon)
    if match:
        return True
    else:
        return False


def validate(user_input):
    try:
        assert '.' not in user_input
        assert (len(user_input) <= 60)

    except AssertionError:
        print('Invalid')
        return False

    pv_name = [x.strip() for x in user_input.split(':')]

    for element in pv_name:
        if not is_alphanumeric(element):
            print('Invalid')
            return False

    # Check the length of the name
    if (len(pv_name) < 2) or (len(pv_name) > 5):
        print('Invalid')
        return False

    # Validate the functional component (FFFFF)
    fc_taxon = list(pv_name[0])
    fc_valid = functional_component_is_valid(fc_taxon)

    second_element = pv_name[1]

    if fc_valid:
        # Check for name with 2 elements (FFFFF:CCC)
        if (len(pv_name)==2):
            ccc_valid = constituent_component_is_valid(second_element)

            if ccc_valid:
                print('Valid')
                return True
            else:
                print('Invalid')
                return False

        third_element = pv_name[2]

        # check for name with 3 elements (FFFFF:GGG:CCC, FFFFF:CCC:NN, FFFFF:CCC:XXXX)
        if (len(pv_name) == 3):
            fg_valid = fungible_is_valid(second_element)
            ccc_valid = constituent_component_is_valid(second_element)

            if fg_valid:   
                ccc_valid = constituent_component_is_valid(third_element)
                if ccc_valid:
                    print('Valid')
                    return True
                else:
                    print('Invalid')
                    return False
            elif ccc_valid:
                    element_valid = is_alphanumeric(third_element)
                    if element_valid:
                        print('Valid')
                        return True
                    else:
                        print('Invalid')
                        return False
            else:
                print('Invalid')
                return False

        fourth_element = pv_name[3]

        # Check for name with 4 elements (FFFFF:GGG:CCC:NN, FFFFF:GGG:CCC:XXXX, FFFFF:CCC:NN:XXXX)
        if (len(pv_name) == 4):
            fg_valid = fungible_is_valid(second_element)
            ccc_valid = constituent_component_is_valid(second_element)

            if fg_valid:
                ccc_valid = constituent_component_is_valid(third_element)
                fourth_element_valid = is_alphanumeric(fourth_element)

                if ccc_valid and fourth_element_valid:
                    print('Valid')
                    return True
                else:
                    print('Invalid')
                    return False
                
            elif ccc_valid:
                third_element_valid = is_alphanumeric(third_element)
                fourth_element_valid = is_alphanumeric(fourth_element)

                if third_element_valid and fourth_element_valid:
                    print('Valid')
                    return True
                else:
                    print('Invalid')
                    return False
                
            else:
                print('Invalid')
                return False

        # check for name with 5 elements (FFFFF:GGG:CCC:NN:XXXX)
        if (len(pv_name) == 5):
            fg_taxon = pv_name[1]
            fg_valid = fungible_is_valid(fg_taxon)

            ccc_taxon = pv_name[2]
            ccc_valid = constituent_component_is_valid(ccc_taxon)

            nn_taxon = pv_name[3]
            nn_valid = increment_is_valid(nn_taxon)

            fifth_element = pv_name[4]
            fifth_element_valid = is_alphanumeric(fifth_element)

            if fg_valid and ccc_valid and nn_valid and fifth_element_valid:
                print('Valid')
                return True
            else:
                print('Invalid')
                return False

    else:
        print('Invalid')
        return False


def main():

    load_taxons()

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
        validate(line)


if __name__ == "__main__":
    main()
