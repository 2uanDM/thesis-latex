from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import uvicorn
import os
from pathlib import Path

app = FastAPI(title="PDF Viewer API", description="API to serve PDF files for browser viewing")

# Get the directory where this script is located
BASE_DIR = Path(__file__).parent

@app.get("/")
async def root():
    """Root endpoint with basic information"""
    return {
        "message": "PDF Viewer API", 
        "pdf_endpoint": "/pdf/main.pdf",
        "docs": "/docs"
    }

@app.get("/pdf/main.pdf")
async def get_main_pdf():
    """Serve main.pdf file as octet stream for browser viewing"""
    pdf_path = BASE_DIR / "main.pdf"
    
    if not pdf_path.exists():
        raise HTTPException(status_code=404, detail="main.pdf not found")
    
    return FileResponse(
        path=str(pdf_path),
        media_type="application/pdf",
        headers={
            "Content-Disposition": "inline; filename=main.pdf",
            "Cache-Control": "no-cache"
        }
    )

@app.get("/pdf/cover.pdf")
async def get_cover_pdf():
    """Serve Cover.pdf file as octet stream for browser viewing"""
    pdf_path = BASE_DIR / "Cover.pdf"
    
    if not pdf_path.exists():
        raise HTTPException(status_code=404, detail="Cover.pdf not found")
    
    return FileResponse(
        path=str(pdf_path),
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": "inline; filename=Cover.pdf",
            "Cache-Control": "no-cache"
        }
    )

