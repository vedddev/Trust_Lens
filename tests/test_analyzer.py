from backend.services.analysis_service import analyze_text

def test_payment_scam_is_high_risk():
    result = analyze_text('Google internship selected. Pay ₹3,999 within 30 minutes.')
    assert result.risk_score >= 50
    assert result.classification == 'potential_scam'

def test_credential_phishing_is_detected():
    result = analyze_text('Your bank account is blocked. Send OTP immediately.')
    assert any(signal.key == 'credential_request' for signal in result.signals)

def test_legitimate_message_stays_low():
    assert analyze_text('Your team meeting is scheduled for Tuesday.').risk_level == 'LOW'
