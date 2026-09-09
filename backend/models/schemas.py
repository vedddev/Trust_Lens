from typing import Literal
from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    text: str = Field(min_length=1, max_length=12000)
    language: Literal['auto', 'en', 'hi', 'mr'] = 'auto'

class Signal(BaseModel):
    key: str
    severity: Literal['low', 'medium', 'high']
    title: str
    description: str
    evidence: str | None = None
    source: Literal['rule', 'ai', 'url'] = 'rule'

class Entity(BaseModel):
    text: str
    type: str

class Claim(BaseModel):
    text: str
    type: str
    status: Literal['verified', 'likely', 'unverified', 'contradicted', 'insufficient_evidence']
    reasoning: str

class AnalyzeResponse(BaseModel):
    risk_score: int
    risk_level: Literal['LOW', 'MODERATE', 'HIGH', 'CRITICAL']
    classification: Literal['potential_scam', 'caution', 'likely_legitimate']
    summary: str
    detected_language: str
    context: str
    intent: str
    signals: list[Signal]
    entities: list[Entity]
    claims: list[Claim]
    recommendations: list[str]
    confidence: float
    limitations: list[str]
    ai_enhanced: bool = False

class UrlRequest(BaseModel):
    url: str = Field(min_length=3, max_length=2048)

class UrlResponse(BaseModel):
    domain: str
    protocol: str
    hostname: str
    page_title: str | None = None
    redirects: list[str] = []
    suspicious_indicators: list[Signal]
    risk_indicators: list[str]
    ai_interpretation: str
    fetch_status: str
