import time

from src.utils.logger import Logger

register_timer = Logger()

logger_timer = register_timer.get_tracking(__name__)

def time_complexity(name_process):
    
    def decorator_factory(func): 

        def wraper(*args, **kwargs): 
            t1 = time.time() 
            result = func(*args, **kwargs) 
            t2 = time.time() 

            duration = t2-t1
            logger_timer.info(f'DONE PROCESS {name_process} IN {duration:.4f}s')
            return result 
        
        return wraper 
    
    return decorator_factory