from mlproject.utils.common import create_directories
from sklearn.model_selection import train_test_split
from mlproject import logger
from mlproject.entity.config_entity import DataTransformationConfig
import pandas as pd
import os

class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config
        create_directories([self.config.root_dir])
        logger.info(f"Directory: {self.config.root_dir} created!")

    def transform_data(self):

        try:
            data = pd.read_csv(self.config.data_path)
            
            # split the data
            train, test = train_test_split(data)

            train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

            logger.info("Splitted the data into train and test and saved in files")

        except Exception as e:
            raise e