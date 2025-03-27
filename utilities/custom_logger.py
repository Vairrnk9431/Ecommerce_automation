import logging
import os

LOG_FILE = os.path.abspath(".\\logs\\nopcommerce.log")

class Log_Maker:
    @staticmethod
    def log_gen():
        # Create the 'logs' directory if it doesn't exist
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        
        # Delete the log file if it exists (Fresh log on each run)
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)

        # Configure logging with a fresh log file
        if not logging.getLogger().hasHandlers():  # Prevent duplicate handlers
            logging.basicConfig(
                filename=LOG_FILE,
                format='%(asctime)s: %(levelname)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S %p',
                force=True,
                level=logging.INFO
            )

        logger = logging.getLogger()
        return logger

# Usage Example
if __name__ == "__main__":
    logger = Log_Maker.log_gen()
    logger.info("Starting the application.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")