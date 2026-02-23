import textSummarizer
from textSummarizer.pipeline.stage01_data_ingestion import DataIngestionPipeline
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

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


STAGE_NAME = "Data Validation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_validation = DataValidationPipeline()
        data_validation.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    
STAGE_NAME = "Data Transformation Stage"

if __name__ == "__main__":
    try:
        logger.info(f"************ Stage {STAGE_NAME} started ************")
        data_transformation = DataTransformationPipeline()
        data_transformation.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e    
    
    
STAGE_NAME = "Model Trainer Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        model_trainer = ModelTrainerPipeline()
        model_trainer.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    
STAGE_NAME = "Model Evaluation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        model_evaluation = ModelEvaluationPipeline()
        model_evaluation.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e          