import fitz, logging # PyMuPDF

logger = logging.getLogger("pdf_service")

class Pdf:
    def __init__(self, inp: any, is_stream: bool = False) -> None:
        self.doc = None
        try:
            if is_stream: # Utilize FastAPI's streaming for memory efficiency
                self.doc = fitz.open(stream=inp, filetype="pdf")
            else:
                self.doc = fitz.open(inp)
                
            if self.doc.is_encrypted:
                raise ValueError("PDF is encrypted/password protected.")
                
        except Exception as e:
            logger.error(f"Failed to initialize PDF: {e}")
            raise ValueError(f"Invalid PDF source: {str(e)}")

    def to_markdown(self) -> str:
        """
        Converts PDF to Markdown string. 
        Returns empty string if extraction fails.
        """
        if not self.doc or self.doc.page_count == 0:
            return ""

        full_text = []
        try:
            for page in self.doc:
                # get_text("dict") is robust but can fail on malformed pages
                page_dict = page.get_text("dict")
                blocks = page_dict.get("blocks", [])
                
                # Sort blocks: Top-to-Bottom, then Left-to-Right
                blocks.sort(key=lambda b: (b["bbox"][1], b["bbox"][0]))
                
                for b in blocks:
                    if "lines" in b:
                        lines = []
                        for l in b["lines"]:
                            # Join spans and strip invisible characters
                            span_text = " ".join([s["text"].strip() for s in l["spans"] if s["text"].strip()])
                            if span_text:
                                lines.append(span_text)
                        
                        block_str = " ".join(lines).strip()
                        if block_str:
                            full_text.append(block_str)
                
                full_text.append("\n---\n")
            
            return "\n".join(full_text)

        except Exception as e:
            logger.error(f"Error during Markdown conversion: {e}")
            # In RAG, partial data is often better than no data
            return "\n".join(full_text)
        finally:
            # Clean up memory immediately
            if self.doc:
                self.doc.close()