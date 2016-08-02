#!/usr/bin/env python3
#日志记录脚本，借助logging模块实现
import logging
def main():
    logging.basicConfig(
        #定义日志文件存放位置
        filename="file.log",
        #定义日志级别
        level=logging.WARNING,
        #定义日志格式
        format="%(levelname)s:%(asctime)s:%(message)s"
    )
    #测试数据
    hostname = "www.nextkara.net"
    item = "spam"
    filename = "data.csv"
    mode = "r"
    #日志不同级别所对应的操作，信息对应输出到日志文件
    logging.critical("Host %s unknow", hostname)
    logging.error("Couldn't find %r",item)
    logging.warning("Feature is deprecated")
    logging.info('Opening file %r, mode = r', filename, mode)
    logging.debug("got here")
if __name__ == "__main__":
    main()
'''
Level 	Numeric value
CRITICAL   	50
ERROR 	    40
WARNING 	30
INFO 	    20
DEBUG 	    10
NOTSET  	0

Attribute name 	                Format                              	Description
args 	        You shouldn’t need to format this yourself.     The tuple of arguments merged into msg to produce message, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary).
asctime 	    %(asctime)s 	                                Human-readable time when the LogRecord was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time).
created 	    %(created)f 	                                Time when the LogRecord was created (as returned by time.time()).
exc_info 	    You shouldn’t need to format this yourself. 	Exception tuple (à la sys.exc_info) or, if no exception has occurred, None.
filename 	    %(filename)s 	                                Filename portion of pathname.
funcName 	    %(funcName)s 	                                Name of function containing the logging call.
levelname 	    %(levelname)s 	                                Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
levelno 	    %(levelno)s 	                                Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
lineno 	        %(lineno)d 	                                    Source line number where the logging call was issued (if available).
module 	        %(module)s 	                                    Module (name portion of filename).
msecs 	        %(msecs)d 	                                    Millisecond portion of the time when the LogRecord was created.
message 	    %(message)s 	                                The logged message, computed as msg % args. This is set when Formatter.format() is invoked.
msg 	        You shouldn’t need to format this yourself. 	The format string passed in the original logging call. Merged with args to produce message, or an arbitrary object (see Using arbitrary objects as messages).
name 		    (name)s 	                                    Name of the logger used to log the call.
pathname 	    %(pathname)s 	                                Full pathname of the source file where the logging call was issued (if available).
process 	    %(process)d 	                                Process ID (if available).
processName 	%(processName)s 	                            Process name (if available).
relativeCreated %(relativeCreated)d 	                        Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.
stack_info  	You shouldn’t need to format this yourself.     Stack frame information (where available) from the bottom of the stack in the current thread, up to and including the stack frame of the logging call which resulted in the creation of this record.
thread 	        %(thread)d 	                                    Thread ID (if available).
threadName 	    %(threadName)s 	                                Thread name (if available).

'''
