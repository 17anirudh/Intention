from fastapi import HTTPException
from fastapi.routing import APIRouter
from services.ingestion import IngestionService
from custom.controllers import IngestionResponse, IngestionRequest
import logging

router = APIRouter()
logger = logging.getLogger("app")

@router.post("/ingestion", response_model=IngestionResponse)
async def ingest(request: IngestionRequest):
    ingestion_service = IngestionService()
    try:
        for file in request.file:
            ingestion_service.ingest(file)
        return IngestionResponse(
            failed_files=None,
            time_taken=f"{timeit.default_timer() - t1:.3f}s"
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal processing error: {str(e)}")
    finally:
        for file in request.file:
            file.close()