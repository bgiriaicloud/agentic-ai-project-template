import logging
import sys
import os

def setup_logging(log_level_str: str = "INFO"):
    log_level = getattr(logging, log_level_str.upper(), logging.INFO)
    
    # Ensure logs directory exists
    log_dir = "data/logging"
    os.makedirs(log_dir, exist_ok=True)
    
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"{log_dir}/agent_activity.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )
    logging.info("Logging initialized.")
