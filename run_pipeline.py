from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data
from config.logger import log_message

try:
    log_message("ETL Pipeline Started")

    extracted_data = extract_data()
    log_message("Data Extracted Successfully")

    transformed_data = transform_data(extracted_data)
    log_message("Data Transformed Successfully")

    load_data(transformed_data)
    log_message("Data Loaded Successfully")

    print("ETL Pipeline Completed Successfully")

except Exception as e:
    log_message(f"Error occurred: {e}")
    print("Error occurred:", e)