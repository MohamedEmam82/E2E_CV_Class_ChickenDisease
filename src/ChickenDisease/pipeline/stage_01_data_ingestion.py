from ChickenDisease.config.configuration import ConfigurationManager
from ChickenDisease.components.data_ingestion import DataIngestion
from ChickenDisease import logger


# This is the first stage of the data ingestion pipeline for the Chicken Disease project.
# It handles downloading the dataset from a specified URL and extracting it from a zip file.
# The `DataIngestionTrainingPipeline` class orchestrates the data ingestion stage by doing the following:
#   - initializing data ingestion configuration,
#   - creating the directory structure if it doesn't exist,
#   - creating an instance of the `DataIngestion` class,
#   - calling methods to download and extract the data.
STAGE_NAME = "Data Ingestion Stage"
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()