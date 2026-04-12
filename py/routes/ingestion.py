from fastapi import HTTPException
from fastapi.routing import APIRouter
from ..services.pdf import Pdf
from ..services.docx import DocxProcessor
from ..types.document import TypeEnum, DocumentResponse, DocumentRequest
import logging

router = APIRouter()
logger = logging.getLogger("app")

def fault(markdown: Any, filename: str) -> DocumentResponse:
    if not markdown:
        raise HTTPException(
            status_code=400, 
            detail=f"Could not extract text from {filename}."
        )
        
    return DocumentResponse(data=markdown)

@router.post("/ingestion", response_model=DocumentResponse)
async def ingest(request: DocumentRequest):
    try:
        file_type: TypeEnum = TypeEnum(request.content_type)
        file_name: str = request.file.filename
        content = await request.file.read()
        match file_type:
            case TypeEnum.PDF:
                processor = Pdf(content, is_stream=True)
                markdown = processor.to_markdown()
                fault(markdown, file_name)
            case TypeEnum.DOCX:
                processor = DocxProcessor(content, is_stream=True)
                markdown = processor.to_markdown()
                fault(markdown, file_name)
            case _:
                raise HTTPException(status_code=400, detail=f"Unsupported file type: {file_type}")
       
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal processing error: {str(e)}")