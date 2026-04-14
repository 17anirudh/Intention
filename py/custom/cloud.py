from enum import Enum

class MimeTypes(str, Enum):
    pdf = "application/pdf"
    gif = "image/gif"
    tiff = "image/tiff"
    jpeg = "image/jpeg"
    png = "image/png"
    bmp = "image/bmp"
    webp = "image/webp"
    html = "text/html"
    docx = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    pptx = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    xlsx = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"