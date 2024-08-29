'''
LCLS Naming Tool

A tool for checking the form and content (but not meaning) of names with respect to the LCLS naming convention.
The following variables are used according to LCLS_Photon_Source_and_Systems_Nomenclature.pdf:

fc_prefix           # functional component prefix
fc_seq_num          # functional component sequence number 
fc_source_ltr       # functional component source letter
fc_beam_num         # functional component beam path number
fg_1                # fungible element (GGG_GGG) first part (before the underscore)
fg_2                # fungible element second part (can be empty)
ccc                 # constituent component type
nn                  # increment
xxxx                # control system process variable

name_type           # 1 indicates a PV. 2 indicates a device.
'''

import os
import re


fc_name ='' 
fg_name = ''
pv_name = ''
device_name = ''

fc_prefix_dict = {'AT': 'Attenuator',
                    'AL': 'Alignment Laser',
                    'BS': 'Bremsstrahlung Collimator'
                }

fg_dict = {'4FCCM': '',
            '4FFOCUS': '',
            'ATM': '',
            'BCS': '',
            'BCM': '',
            'BEND': '',
            'C1': '',
            'C2': ''
            }

def add_fungible():

    global fg_name
    fg_term = input('\nEnter a fungible element term (GGG): ')

    if fg_term in fg_dict:
        if not fg_name: # if this is first term to be added to the fungible element
            fg_name = fg_term
            fg_term = ''
        else:
            fg_name += ('_' + fg_term)
            fg_term = ''
    else:
        user_response = input('\nThis term does not exist in the current list of fungible terms. Continue using this name? (y/n): ')

        while (user_response not in ['y', 'n']):
            user_response = input('\nI didn\'t recognize that letter. Continue using this name? (y/n): ')

        if user_response=='y':
            if not fg_name: # if this is first term to be added to the fungible element
                fg_name = fg_term
            else:
                fg_name += ('_' + fg_term)


if __name__ == '__main__':

    print('\nThe LCLS Naming Tool is designed to check the form and content (but not meaning) \nof names with respect to the LCLS naming convention.')

    name_type = input("\nAre you creating a PV or device name? (enter 1 for PV, 2 for device): ")

    while (name_type not in ['1', '2']):
        name_type = input("\nPlease enter 1 for PV, 2 for device): ")

    # FC prefix
    print('\n=========================================\n         Functional Component        \n=========================================\n')
    print('The functional component name is formed by prepending a two-letter component mnemonic \nprefix and sequence number to the beam path designation.')

    fc_prefix = input("\nEnter the prefix of the functional component: ")

    while (fc_prefix not in fc_prefix_dict.keys()):
        fc_prefix = input("\nThis name is not in the Photon Beamline Component list. Please try again: ")

    fc_name += fc_prefix
    print('%s: %s' %(fc_prefix, fc_prefix_dict[fc_prefix]))

    # FC sequence number
    fc_seq_num =  input("\nEnter the sequence number of the functional component: ")
    fc_name += str(fc_seq_num)

    # FC source letter
    fc_source_ltr = input("\nEnter the functional component undulator source letter (L or K): ")

    while (fc_source_ltr not in ['L', 'K']):
        fc_source_ltr = input("\nThis is not an undulator source letter. Please enter L or K: ")

    fc_name += fc_source_ltr

    # FC beam path number
    fc_beam_num = int(input("\nEnter the beam path number of the functional component (0-5): "))

    while not (0 <= int(fc_beam_num) <= 5):
        fc_beam_num = input("\nThis is not a valid beam path number. Please enter a number between 0 and 5: ")

    fc_name += str(fc_beam_num)

    print('\nThe functional component name is %s' % fc_name)

    # Fungible element first part
    print('\n=========================================\n         Fungible Element        \n=========================================\n')
    print('The fungible element can include multiple mnemonic terms separated by underscores. \nThe fungible element typically follows the format \'GGG\' with multiple \'GGG\' values \nseparated by an underscore.')

    add_another_fg = True

    while add_another_fg:
        add_fungible()

        user_response = input("\nAdd another fungible term? (y/n): ")

        while (user_response not in ['y', 'n']):
            user_response = input("\nI didn't recognize that response. Add another fungible term? (y/n): ")

        if user_response=='y':
            add_another_fg = True
        else:
            add_another_fg = False

    print('\nThe fungible element is %s.\n' % fg_name)

    pv_name = str(fc_name) + ":" + str(fg_name)

    print('The PV name is %s.\n' % pv_name)
