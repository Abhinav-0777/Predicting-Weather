import logging

def setup_logger() :
    
    """For configuring the log file.
    """

    logging.basicConfig(filename='file.log', 
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s"
                        )