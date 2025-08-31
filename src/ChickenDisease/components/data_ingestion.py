
import os
import urllib.request as request
import zipfile
from ChickenDisease import logger
from ChickenDisease.utils.common_functions import get_size
from ChickenDisease.entity.config_entity import DataIngestionConfig
from pathlib import Path


# create the DataIngestion class which will do the real work of downloading and extracting the data
#  - constructor should take the DataIngestionConfig object as input
#  - create the download_file method to download the file from source_URL to local_data_file
#  - create the extract_zip_file method to extract the zip file into the unzip_dir
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(url=self.config.source_URL, 
                                                     filename=self.config.local_data_file)
            file_size = get_size(Path(filename))
            logger.info(f"Downloaded file: {filename}, size= {file_size}, with headers: {headers}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file} with size: {get_size(self.config.local_data_file)} bytes")
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_dir_path = self.config.unzip_dir
        os.makedirs(name=unzip_dir_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zipped_content:
            zipped_content.extractall(path=unzip_dir_path)
            logger.info(msg=f"Extracted files to: {unzip_dir_path}")   
