# make a function for standard loggers to be  used across multiple projects

'''
Leting victor kipkemboi
11/28/21
letingvictorkipkemboi@gmail.com


'''
import logging


def MakeFileStreamLogger(name, file_path, stream_handler_level = logging.DEBUG,file_handler_level = logging.DEBUG,stream_handler_format = "%(asctime)s %(levelname)s : %(message)s" , file_handler_format = "%(asctime)s %(levelname)s : %(message)s"):
    logger = logging.getLogger( name )
    # create hanlers
    print('making handlers ....')
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(file_path)
    # formatters
    print('maing formatters .....')
    stream_formatter =  logging.Formatter(stream_handler_format)
    file_formatter = logging.Formatter(file_handler_format)
    # set levels
    print('setting logging levels,,,,,>/')
    stream_handler.setLevel(stream_handler_level)
    file_handler.setLevel(file_handler_level)
    # add formatters
    print('setting formatters................')
    stream_handler.setFormatter(stream_formatter)
    file_handler.setFormatter(file_formatter)
    # add handlers
    print('adding handlers.....................')
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    print('--------------------\nlogger done ! \n')
    return logger
    
applog = MakeFileStreamLogger(
    'AppLogger',
    './data/applogs.txt',
    stream_handler_format = '[ anycolor ] : [ %(message)s ]',
    file_handler_format =  '[ anycolor ] : [ %(message)s ]',

)


if __name__ == '__main__':
    applog.warning('applog test 1,2')
