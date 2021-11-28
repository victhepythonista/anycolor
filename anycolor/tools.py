

def TestOk(test_obj):
    name = 'NAME'
    try:name = test_obj.__name__
    except:pass
    print(f'Testing   {type(test_obj)}  {name}......  TESTS  OK !')




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
