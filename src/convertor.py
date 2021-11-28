'''


In this script use the ColorConvertor class to convert
colors...simple as that


peace !!


'''

import colorsys
from PIL import ImageColor


HUE_MAX = 360
SATURATION_MAX  = 100
RGB_MAX = 255

COLOR_MODES_COVERED = 'hex', 'hsl', 'hsv', 'rgb', 'rgba', 'kivy_rgba'
CONVERSION_ERROR_BASE = "[COLOR CONVERSION ERROR >> %s\]"



def RoundOffValues(iterable, points  = 2):
    # rounds off vslues in the interable to the specified point
    IsNum = lambda x: (type(x) == int) or (type(x) == float)
    # make sure all values  are integers
    assert( all([IsNum(num) for num in iterable])), 'Error {self.__name__} requies  an iterable containing only floats or integers'
    # return the data type  provided
    return type(iterable)([round(num,points) for num in iterable])

def CheckAlpha(alpha):
    if alpha :
        if alpha <= 1:
            return alpha
    return 1

class ColorValueError(Exception):
    '''
    raise when a wrong color value is provided
    '''
    pass

def NumberCheck(num, maximum = 100, minimum = 0):
    '''
    # CHECK IF A NUMBER is within range of mininumim
    # and maximum parametes
    # rtype : bool
    '''
    if type(num) == int  or type(num) == float:
        ' it is a number or float'
        if minimum <= num <= maximum:
            return True
    return False


def ColorIsRGB(color_value):
    '''
    check if a color   is  rgb -
    # rtype : bool
    '''
    if type(color_value) == tuple:
        digit_check = lambda x:NumberCheck(x, 0, RGB_MAX)
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

def ColorIsHSV(color_value):
    '''

    check if a color   is  HSV
    '''
    if type(color_value) == tuple :
        if len(color_value) == 3:
            h,s,v = color_value
            if NumberCheck(h, 360) and NumberCheck(s, 100) and NumberCheck(v, 100):
                return True
    return False
def ColorIsHSL(color_value):
    '''

    check if a color   is  HSV
    '''
    if type(color_value) == tuple :
        if len(color_value) == 3:
            h,s,l = color_value
            if NumberCheck(h, 360) and NumberCheck(s, 100) and NumberCheck(v, 100):
                return True
    return False


def ColorIsRGBA(color_value):
    '''
    check if color is in rgba format
    '''
    d_type = type(color_value)
    if d_type == tuple:
        if len(color_value) == 4:
            # check rgb firrst
            if all(list(map(NumberCheck, color_value[0:-1]))):
                if NumberCheck(color_value[-1], 1):
                    # the alpha value is ok
                    return True
    return False

def ColorIsKivyRGBA(color_value):
    '''
    check if a color is in a correct
    kvrgba format
    '''
    color_value = list(color_value) # much easier to work with lists
    if len(color_value) == 4:
        # next check if all values are less than one
        if all([value < 1 for value in color_value] ):
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
    'hsv':ColorIsHSV,
    'hsl':ColorIsHSL,

    }
    if mode in COLOR_IS_FUNCTIONS:
        is_color_function = COLOR_IS_FUNCTIONS[mode]
        if is_color_function(color_value):
            return True
        print(mode,' is not supported')
        return False



#-----------
class Convertor:
    '''

    contains functions for changing color modes between
    -hsl
    -hsv
    -rgba
    -rgb
    -kivy rgba
    '''

    # CONVERSIONS

    # rgb/kivy_rgba
    @staticmethod
    def rgb_to_kivy_rgba(RGB, alpha = 1):
        '''
        convert rgb to  kivy rgba color values

        '''
        conversion = lambda x:  round(x/RGB_MAX, 2)
        rgba = list(map(conversion, RGB))
        rgba.append(alpha)
        rgba = tuple(rgba)
        # convert to a tuple since that the needed format
        return rgba

    #
    @staticmethod
    def kivy_rgba_to_rgb(RGBA):
        conversion = lambda x: int(round(x*RGB_MAX))
        r,g,b,a =  list(map(conversion, RGBA))
        rgb = r,g,b
        return rgb

    # rgb/hex
    @staticmethod
    def rgb_to_hex(rgb):
        r,g,b = rgb
        res = "#{:X}{:X}{:X}".format(r,g,b).lower()
        return  res

    # convert hex/rgb
    @staticmethod
    def hex_to_rgb(hex_value):
        return ImageColor.getcolor(hex_value , "RGB")

    # conversion rgba/kvrgba
    @staticmethod
    def kivy_rgba_to_rgba(kv_rgba_color_value, alpha = None):
        alpha = CheckAlpha(kv_rgba_color_value[-1])
        conversion = lambda c:c*RGB_MAX
        rgb_value = map(conversion,kv_rgba_color_value[0:-1])
        return RoundOffValues(tuple(rgb_value) + (alpha,))

    @staticmethod
    def rgba_to_kivy_rgba(RGBA, alpha = 1 ):
        alpha = CheckAlpha(RGBA[-1])
        conversion = lambda x:  round(RGB_MAX/x, 2)
        rgba = tuple(map(conversion, RGBA))
        # convert to a tuple since that the needed format
        return rgba


    def kivy_rgba_to_all(self, kv_rgba_value):
        # convert a given color mode in kv_rgba  and convert it
        # to all other modes
        # return a dictionary of the former
        kv_rgba = kv_rgba_value
        alpha = CheckAlpha(kv_rgba[-1])
        rgb = self.kivy_rgba_to_rgb(kv_rgba)
        hex = self.rgb_to_hex(rgb)
        #hsl = self.rgb_to_hsl(rgb)
        hsv = self.rgb_to_hsv(rgb)
        rgba =  self.kivy_rgba_to_rgba(kv_rgba)
        res = {

            'rgb':rgb,
            'hex':hex,
            'hsv':hsv,
            'rgba':rgba,
            'kivyrgba':kv_rgba,
        }

        return res

    def GetAll(self, anonymous_color):
        # get all color modes of the given anonymous
        pass
