from agents.context_analyzer import analyze_context, detect_language
from agents.message_analyzer import analyze_message
from agents.risk_engine import calculate_risk
from models.schemas import AnalyzeResponse, Claim

def analyze_text(text: str, language: str = 'auto') -> AnalyzeResponse:
    signals, entities = analyze_message(text)
    score, level, classification = calculate_risk(signals)
    context = analyze_context(text)
    claims = [Claim(text=s.evidence or s.title, type=s.key, status='unverified', reasoning='This observation was derived from the submitted message and was not independently verified.') for s in signals[:3]]
    summary = ('The message contains multiple patterns associated with social-engineering attempts. Verify all claims independently before acting.' if score >= 50 else 'The message contains caution indicators. This is not proof of fraud, but independent verification is recommended.' if score >= 25 else 'Few common scam indicators were found. This is not proof that the message is legitimate.')
    advice = ['Do not send money or share OTPs, passwords, or financial details.', 'Verify the sender through the organization’s official website or published contact details.', 'Keep screenshots and report suspected fraud through the relevant platform or cybercrime channel.'] if score >= 50 else ['Verify unexpected requests through an independent channel before acting.', 'Avoid sharing sensitive information until you confirm the sender.']
    return AnalyzeResponse(risk_score=score, risk_level=level, classification=classification, summary=summary, detected_language=detect_language(text) if language == 'auto' else language, context=context['context'], intent=context['intent'], signals=signals, entities=entities, claims=claims, recommendations=advice, confidence=round(min(.93,.5+len(signals)*.075),2), limitations=['TrustLens assesses patterns in supplied content; it cannot guarantee fraud or legitimacy.', 'Claims are unverified unless independently corroborated.', 'User messages are not persisted.'])
