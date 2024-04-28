from src.pseudo_pointpillars import logger
from src.pseudo_pointpillars.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info(">>>>>> Starting pipeline <<<<<<")

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
