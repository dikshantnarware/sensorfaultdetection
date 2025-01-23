import sys

"""
this function is used to get the error message and the line number where the error occurred
:param error: error message
:param error_detail: error detail
:return: error message with line number
"""
"""explain the function in detail
:param error: error message
:param error_detail: error detail
:return: error message with line number

"""
"""explain this code in detail
:param error: error message
:param error_detail: error detail
:return: error message with line number

"""

"""
there are two classes defined in this file:
1. CustomException
2. error_message_detail

"""
"""sumary_line

"""




def error_message_detail(error, error_detail: sys):#function to get the error message and the line number where the error occurred
    _, _, exc_tb = error_detail.exc_info()#getting the error message and the line number where the error occurred

    file_name = exc_tb.tb_frame.f_code.co_filename#file name where the error occurred

    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )#error message with line number

    return error_message#returning the error message with line number


"""
there are two classes defined in this file:
1. CustomException
2. error_message_detail

"""
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

"""which method is used to get the error message and the line number where the error occurred
:param error: error message
:param error_detail: error detail
:return: error message with line number

"""

class CustomException(Exception):#class to raise custom exception
    def __init__(self, error_message, error_detail: sys):#constructor to initialize the error message and the error detail
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)#calling the super class constructor

        self.error_message = error_message_detail(# getting the error message and the line number where the error occurred
            error_message, error_detail=error_detail
        )#getting the error message and the line number where the error occurred

    def __str__(self):#function to return the error message with line number
        return self.error_message#returning the error message with line number
