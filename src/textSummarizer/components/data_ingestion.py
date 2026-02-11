import os
import urllib.request as request
import zipfile
import requests
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info("Downloading started...")
            response = requests.get(self.config.source_URL, stream=True)
            response.raise_for_status()  # 🔥 THIS LINE IS CRITICAL

            with open(self.config.local_data_file, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            logger.info(f"File downloaded successfully at: {self.config.local_data_file}")
        else:
            logger.info(
            f"File already exists of size: {get_size(self.config.local_data_file)}"
        )

            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        if not zipfile.is_zipfile(self.config.local_data_file):
            raise ValueError("Downloaded file is not a valid ZIP file")

        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
