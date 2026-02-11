from textSummarizer.pipeline.stage01_data_ingestion import DataIngestionPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_ingestion = DataIngestionPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
