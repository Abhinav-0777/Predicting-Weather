import pandas as pd
import logging
from src.components.data_ingestion import load_data
from src.utils.logger import setup_logger
from dataclasses import dataclass

def main() :

    setup_logger()

    try :
        data = load_data("weatherAUS.csv")
        logging.info("Data loaded successfully.")
    except Exception as e :
        logging.error(f'{e} occurred while opening file.')
        print(e)

if __name__ == "__main__":
    main()
