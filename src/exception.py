import traceback,sys

class CustomException(Exception):
    def __init__(self, error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg=self.get_detailed_error_msg(error_msg=error_msg,error_detail=error_detail)

    @staticmethod
    def get_detailed_error_msg(error_msg,error_detail:sys):
        _,_,exc_tb=error_detail.exc_info()
        file_name=exc_tb.tb_frame.f_code.co_filename
        line_no=exc_tb.tb_lineno
        return f"Error occured in {file_name}, line number: {line_no}: {error_msg}"
    

    def __str__(self):
        return self.error_msg
    
