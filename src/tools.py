

def TestOk(test_obj):
    name = 'NAME'
    try:name = test_obj.__name__
    except:pass
    print(f'Testing   {type(test_obj)}  {name}......  TESTS  OK !')
