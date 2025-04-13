# Logger is for the purpose that any execution that probably happens we should be able to log all those information in the execution so that we can track the errors even in the custom exception
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #This is how we want our log message/file with day, month, year etc
logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
#cwd => current working directory it takes both logs in forward and naming convention
os.makedirs(logs_path, exist_ok=True) #This says that even if files/folders are present keep appending new files/folders created

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", #This is how my entire message will get printed
    level = logging.INFO,
)

