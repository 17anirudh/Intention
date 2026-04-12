from docx import Document # python-docx
import io 
import logging
from typing import Any

logger = logging.getLogger("docx_service")

class DocxProcessor:
    def __init__(self, inp: Any, is_stream: bool = False):
        try:
            if is_stream:
                self.doc = Document(io.BytesIO(inp))
            else:
                self.doc = Document(inp)
        except Exception as e:
            logger.error(f"Docx Initialization Failed: {e}")
            raise ValueError(f"Invalid Word Document: {str(e)}")

    def _process_table(self, table) -> str:
        """Converts a docx table object into a Markdown table."""
        data = []
        for row in table.rows:
            # Clean each cell: split/join removes internal tabs and newlines
            data.append([" ".join(cell.text.split()) for cell in row.cells])
        
        if not data:
            return ""

        # Create Markdown Table
        headers = data[0]
        rows = data[1:]
        
        md_table = f"| {' | '.join(headers)} |\n"
        md_table += f"| {' | '.join(['---'] * len(headers))} |\n"
        for row in rows:
            md_table += f"| {' | '.join(row)} |\n"
        
        return f"\n{md_table}\n"

    def to_markdown(self) -> str:
        """
        Parses paragraphs and tables in their document order.
        """
        markdown_content = []
        
        try:
            # The 'element' attribute allows us to iterate in the exact order
            # they appear in the XML (paragraph vs table)
            for child in self.doc.element.body:
                # Check if element is a paragraph
                if child.tag.endswith('p'):
                    from docx.text.paragraph import Paragraph
                    para = Paragraph(child, self.doc)
                    text = " ".join(para.text.split()).strip()
                    if text:
                        # Simple logic: if bold, make it a header
                        if para.style.name.startswith('Heading'):
                            level = para.style.name.split()[-1]
                            prefix = "#" * (int(level) if level.isdigit() else 1)
                            markdown_content.append(f"{prefix} {text}")
                        else:
                            markdown_content.append(text)
                
                # Check if element is a table
                elif child.tag.endswith('tbl'):
                    from docx.table import Table
                    table = Table(child, self.doc)
                    markdown_content.append(self._process_table(table))

            return "\n\n".join(markdown_content)

        except Exception as e:
            logger.error(f"Docx Parsing Error: {e}")
            return f"*(Error parsing Word document: {e})*"