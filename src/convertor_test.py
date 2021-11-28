from convertor import Convertor



'''
script for testing the 'convertor.py' file
'''

def TestOk(test_obj):
    name = 'NAME'
    try:name = test_obj.__name__
    except :
        # # TODO:  ahandle these errors
        raise
    print(f'Testing   {type(test_obj)}  {name}......  TESTS  OK !')



white_rgba = 255,255,255,1
white_kivy_rgba = 1,1,1,1
white_hex = '#ffffff'
white_rgb = 255,255,255
white_hsv = 0,0,255
#white_hsl =
def ScriptTests():
    print('Running unit tests for  color check functions and other functions')
    if ColorIsRGB(white_rgb) == True:TestOk(ColorIsRGB)
    if ColorIsHEX(white_hex) == True:TestOk(ColorIsHEX)
    if ColorIsRGBA(white_rgba) == True:TestOk(ColorIsRGBA)
    if ColorIsKivyRGBA(white_kivy_rgba) == True:(TestOk(ColorIsKivyRGBA))

    #if ColorIsHSL(white_hsl) == True:(TestOk(ColorIsKivyRGBA))
    #if ColorIsHSV(white_hsv) == True:TestOk(ColorIsHSV)


def ConvertorTests():
    c = Convertor()

    tests = {
            'rgb_to_hex':c.rgb_to_hex(white_rgb) ,
            'kivy_rgba_to_rgb':c.kivy_rgba_to_rgb(white_kivy_rgba),
            'kivy_rgba_to_rgba':c.kivy_rgba_to_rgba(white_kivy_rgba) ,

    }

    for test_name,result in tests.items():
        print(f'\n->/testing  {test_name} function ....')
        print(f'[{test_name}]  [ {result} ]..[  TEST  done ]')

        #print(f'!!!!! {test_name} result -> {result} ....[  TEST  FAIL ]   !!!!')
if __name__ == '__main__':
    print('\n\nRunning testss on convertor.py  ....  \n\n')
    #ScriptTests()
    ConvertorTests()
    print("\n\n Tests COMPLETE... \n\n  :) \n\n")

'''



functions
-----------
- get color mode froms of a random mode
- convert to any color-value from a value
- convert to several value ! :
'''
