from ChickenDisease import logger
from ChickenDisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


## 1 ##
# This script is the entry point for the data ingestion stage of the ChickenDisease project.
# It initializes the data ingestion pipeline and executes the main function to download and extract the dataset.
STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed successfully <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e