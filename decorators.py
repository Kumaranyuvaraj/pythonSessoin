def fun(func):
    def wrapper(arg1,arg2):
        argument1 = arg1.capitalize()
        argument2 = arg2.capitalize()
        string_method = func(argument1,argument2)
        return string_method
    return wrapper
                                                 
import datetime
import re                                    
def period(time):
    def wrapper(arg1,arg2):
        argument1 = arg1
        argument2 = arg2
        now = datetime.datetime.now()
        string_change = str(now)
        string_method = time(argument1,argument2,string_change)
        return string_method
    return wrapper







