from . tools import *
from . constants import *


'''
author - leting victor kipkemboi
github - victhepythonista

this script has functions that check if a color value is
within its required parameters ....

they are quite self explanatory

'''
def ColorIsRGB(color_value):
    '''
    check if a color   is  rgb -
    # rtype : bool
    '''
    if type(color_value) in [list,tuple]:
        digit_check = lambda x:NumberCheck(x,RGB_MAX)
        check_list = map(digit_check, color_value)
        if all(check_list):
            # all numbers are withun rgb range
            return True
    return False

def ColorIsHEX(color_value):
    '''
    check if a color   is  rgb -
    # rtype : bool
    '''
    if type(color_value) ==str:
        contents = '#abcdef123456789'
        if len(color_value) != 7:return False
        char_check = lambda x:True if x in contents else False
        check_list = map(char_check, color_value)
        if all(check_list):
            return True
    return False


def ColorIsRGBA(color_value):
    '''
    check if color is in rgba format
    '''
    d_type = type(color_value)
    if d_type in [list,tuple]:
        if len(color_value) == 4:
            # check rgb firrst
            rgb_check = lambda x:NumberCheck(x,RGB_MAX)
            if all(list(map(rgb_check, color_value[0:-1]))):
                if NumberCheck(color_value[-1], 1):
                    # the alpha value is ok
                    return True
    return False

def ColorIsKivyRGBA(color_value):
    '''
    check if a color is in a correct
    kvrgba format
    '''
    if type(color_value) in [list,tuple]:
        color_value = list(color_value) # much easier to work with lists
        if len(color_value) == 4:
            # next check if all values are less than one
            if all([NumberCheck(value,1) for value in color_value] ):
                return True
    return False



def ColorIs(color_value, mode):
    '''
    check if color_value is in the provided mode
:)
    '''
    value_type = type(color_value)
    mode = mode.lower()
    COLOR_IS_FUNCTIONS= {

	'hex':ColorIsHEX,
	'rgb':ColorIsRGB,
	'rgba':ColorIsRGBA,
     'kivy_rgba':ColorIsKivyRGBA,


    }
    if mode in COLOR_IS_FUNCTIONS:
        print('./ Searching for  color test function........')
        is_color_function = COLOR_IS_FUNCTIONS[mode]
        print(f'color test function found -> {is_color_function.__name__}')
        print('color value :',color_value)
        if is_color_function(color_value):
            return True
        print('data_error or mode  is not supported')
        return False
    print(f'-----\n\n!!{mode} is not supported or something....')
