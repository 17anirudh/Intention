from types.structer import DocumentMetaData
from typing import BinaryIO, IO, Optional, Union, List
from io import BytesIO
import fitz
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

class IngestionService:
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path

    def _ingest_pdf(self, file: Union[str, BinaryIO, IO]) -> Optional[DocumentMetaData]:
        try:
            doc = fitz.open(file)
            text = ""
            count: int = 0
            for page in doc:
                text += page.get_text()
                count += 1
            return DocumentMetaData(
                title=doc.get_metadata().get("title"),
                date_conducted=doc.get_metadata().get("creationdate"),
                page_nums=count,
                text=text
            )
        except Exception as e:
            print(f"Error ingesting PDF: {e}")
            return None
        finally:
            doc.close()

    def _ingest_docx(self, file: Union[str, BinaryIO, IO]) -> Optional[DocumentMetaData]:
        text: List[str] = []
        doc = Document(file)
        counter: int = 0
        try:
            for child in doc.element.body:
                counter += 1
                if child.tag.endswith('p'):
                    para = Paragraph(child, doc)
                    text = " ".join(para.text.split()).strip()
                    if text:
                        if para.style.name.startswith('Heading'):
                            level = para.style.name.split()[-1]
                            prefix = "#" * (int(level) if level.isdigit() else 1)
                            text.append(f"{prefix} {text}")
                        else:
                            text.append(text)
                
                elif child.tag.endswith('tbl'):
                    table = Table(child, doc)
                    markdown_content.append(self._process_table(table))

            return DocumentMetaData(
                title=doc.core_properties.title,
                date_conducted=doc.core_properties.created,
                page_nums=counter,
                text="\n".join(text)
            )
        except Exception as e:
            print(f"Error ingesting DOCX: {e}")
            return None
        finally:
            doc.close()

    def ingest(self, file: Union[str, BinaryIO, IO]) -> Optional[DocumentMetaData]:
        ext: str = file.split('.')[-1] if isinstance(file, str) else ''
        match ext:
            case 'pdf':
                return self._ingest_pdf(file)
            case 'docx':
                return self._ingest_docx(file)
            case _:
                raise ValueError("Unsupported file type")

    def ingest_all(self, files: List[Union[str, BinaryIO, IO]]) -> List[Optional[DocumentMetaData]]:
        return [self.ingest(file) for file in files]