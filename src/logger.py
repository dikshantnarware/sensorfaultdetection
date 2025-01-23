# This file is used to log the information of the application.
import logging #importing the logging module
import os#importing the os module
from datetime import datetime #importing the datetime module

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #creating a log file with the current date and time    

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)#creating a path for the log file        

os.makedirs(logs_path, exist_ok=True)#creating a directory for the log file

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)#creating a path for the log file
#configuring the logging module with the log file path, format, and level of logging
logging.basicConfig(#configuring the logging module with the log file path, format, and level of logging
    filename=LOG_FILE_PATH,#path of the log file
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",#format of the log message
    level=logging.INFO,#level of logging
)#configuring the logging module with the log file path, format, and level of logging 

