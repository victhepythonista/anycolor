from .color_is import *

def AllColorModes( anonymous_color):
    # get all  Possible color modes of the given anonymous
    data_type = type(anonymous_color)
    color_modes_found = []
    if data_type == str:
        if anonymous_color.startswith('#'):
            try:
                if ColorIsHEX(anonymous_color):
                    print(f'Anonymous color  {anonymous_color} is  in hexadecimal form')
                    color_modes_found.append('hex')
                    # what else to do !!??
                else:
                    print('color is not in hexadecimal form ...sadly :( ')
            except TypeError:
                print('Color is not in hexadecimal form')

        else:
            print('Definately not in hexadecimal form ')
    if data_type in [list,tuple]:
        # :)

        modes = ['rgb','rgba', 'kivy_rgba']
        print(f"the color could be in {modes} modes ")
        length =len(anonymous_color)
        if  length == 3:
            # check rgb ,hsl,hsv
            for md in ['rgb']:
                if ColorIs(anonymous_color,md):
                    color_modes_found.append(md)
                    continue
                else:
                    continue

        elif length == 4:
            # check kivy_rgba, or rgba
            for md in ['rgba', 'kivy_rgba']:
                if ColorIs(anonymous_color, md):
                    color_modes_found.append(md)
                    print(f'Anonymous color could be in [{md}]  form ')

        else:
            print('No color modes found :(')
    return color_modes_found
