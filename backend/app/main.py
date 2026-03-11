from fastapi import FastAPI, UploadFile, File, HTTPException

from parser import extract_text_from_pdf

app = FastAPI(title="AI Resume Reviewer")


@app.get("/")
def health_check():
    return {"message": "AI Resume Reviewer backend is running"}


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported for now.")

    file_bytes = await file.read()

    try:
        extracted_text = extract_text_from_pdf(file_bytes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse PDF: {str(e)}")

    if not extracted_text.strip():
        raise HTTPException(status_code=400, detail="No text could be extracted from this PDF.")

    return {
        "filename": file.filename,
        "text_preview": extracted_text[:1000],
        "text_length": len(extracted_text),
    }