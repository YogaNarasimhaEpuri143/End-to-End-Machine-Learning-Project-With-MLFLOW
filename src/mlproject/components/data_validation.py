import pandas as pd
from mlproject.utils.common import create_directories
from mlproject.entity.config_entity import DataValidationConfig
from mlproject import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        create_directories([self.config.root_dir])
        logger.info(f"Directory: {self.config.root_dir} created!")

    def validation_all_columns(self) -> bool:

        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_schema:
                if col not in all_cols:
                    validation_status = False
                else:
                    validation_status = True
                with open(self.config.STATUS_FILE, "w") as f:
                    f.write(f"Validation Status: {validation_status}")

            return validation_status
        except Exception as e:
            raise e