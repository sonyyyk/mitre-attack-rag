from fastapi import APIRouter
from fastapi import Form
from fastapi import Request
from fastapi.templating import Jinja2Templates

from app.embeddings.encoder import EmbeddingEncoder
from app.vector_db.manager import VectorDBManager
from app.reports.manager import ReportManager

from fastapi.responses import FileResponse
from app.export.pdf_exporter import PDFExporter

router = APIRouter()

templates = Jinja2Templates(
    directory="templates"
)

encoder = EmbeddingEncoder()
vector_db = VectorDBManager()
report_manager = ReportManager()
pdf_exporter = PDFExporter()

@router.post("/export")
def export(
    request: Request,
    query: str = Form(...)
):

    results = vector_db.search_text(
        query,
        encoder,
        top_k=5,
    )

    report = report_manager.generate(
        query,
        results,
    )

    filename = pdf_exporter.export(report)

    return FileResponse(
        filename,
        media_type="application/pdf",
        filename=filename,
    )

@router.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "report": None
        }
    )


@router.post("/analyze")
def analyze(
    request: Request,
    query: str = Form(...)
):

    results = vector_db.search_text(
        query,
        encoder,
        top_k=5,
    )

    report = report_manager.generate(
        query,
        results,
    )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "report": report,
            "query": query,
        }
    )