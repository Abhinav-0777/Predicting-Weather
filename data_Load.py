import pandas as pd
import logging
import os

def load_data(file_path : str) -> pd.DataFrame :
    """Loads a .csv or .xlsx file and returns its dataframe.

    Args:
        file_path (str): Path of the file to be loaded.

    Raises:
        FileNotFoundError: Raised if file not found.
        ValueError: Raised if file format not supported.

    Returns:
        pd.DataFrame: Dataframe of the data.
    """
    logging.info("Data Loading started.")

    if not os.path.isfile(file_path) :
        logging.error("The file_path entered doesn't exist.")
        raise FileNotFoundError("The file_path doesn't exist.") 

    if file_path.lower().endswith(".csv") :
        return pd.read_csv(file_path)
    
    elif file_path.lower().endswith(".xlsx") :
        return pd.read_excel(file_path)
    
    else :
        logging.error("User entered wrong file format.")
        raise ValueError("Unsupported File Format.")