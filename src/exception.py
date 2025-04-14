import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # three inputs are taken in which the first 2 are neglected and 3rd one is exc_tb
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name, exc_tb.tb_lineno,str(error)

    )

    return error_message

     # exc_tb => in which file and which line has the error occured

# The above function should be called only when error occured. That's why the below class is created to override
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
