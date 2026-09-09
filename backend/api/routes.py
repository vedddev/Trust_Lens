from fastapi import APIRouter, HTTPException
from models.schemas import AnalyzeRequest, AnalyzeResponse, UrlRequest, UrlResponse
from agents.url_analyzer import analyze_url
from services.analysis_service import analyze_text
router = APIRouter(prefix='/api')
@router.get('/health')
async def health(): return {'status':'ok'}
@router.post('/analyze', response_model=AnalyzeResponse)
async def analyze(payload: AnalyzeRequest):
    if not payload.text.strip(): raise HTTPException(status_code=422, detail='Message text cannot be empty.')
    return analyze_text(payload.text, payload.language)
@router.post('/analyze-url', response_model=UrlResponse)
async def url_analysis(payload: UrlRequest):
    try: return await analyze_url(payload.url)
    except ValueError as exc: raise HTTPException(status_code=422, detail=str(exc)) from exc
