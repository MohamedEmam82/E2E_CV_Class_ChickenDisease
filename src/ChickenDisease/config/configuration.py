from ChickenDisease.constants import *
from ChickenDisease.utils.common_functions import *
from ChickenDisease.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    # create a constructor
    # create the artifacts_root folder "artifacts" described in config.yaml which is the root folder for all other data stages artifacts
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])


    # create the "data_ingestion" folder inside the "artifacts" folder, to store all the data ingestion artifacts
    #   - read the data_ingestion section from config.yaml
    # create and return the DataIngestionConfig dataclass object "data_ingestion_config"
    #   - define the attributes of the DataIngestionConfig dataclass from the data_ingestion section of config.yaml
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(root_dir = config.root_dir,
                                                    source_URL = config.source_URL,
                                                    local_data_file = config.local_data_file,
                                                    unzip_dir = config.unzip_dir)
        return data_ingestion_config