'''


In this script use the ColorConvertor class to convert
colors...simple as that


peace !!


'''

import colorsys
from PIL import ImageColor


from .loggers  import applog
from .color_is import *
from .tools import *
from .constants import *




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





if __name__ == '__main__':
    applog.warning(' Convertor.py  runnning tests....')
