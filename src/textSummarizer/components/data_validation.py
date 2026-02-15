import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validate_status = True
            all_files = os.listdir(self.config.unzip_dir)

            for required_file in self.config.ALL_REQUIRED_FILES:
                if required_file not in all_files:
                    validate_status = False

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"validate_status: {validate_status}")

            return validate_status

        except Exception as e:
            raise e
