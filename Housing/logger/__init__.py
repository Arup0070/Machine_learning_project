import logging
from datetime import datetime
import os
LOG_DIR="houshing_logs"
Current_time_stemp=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
Logfile_name=f"log_{Current_time_stemp}.log"
os.makedirs(LOG_DIR,exist_ok=True)
Logfile_Path= os.path.join(LOG_DIR,Logfile_name)
logging.basicConfig(filename=Logfile_Path,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO
)    

