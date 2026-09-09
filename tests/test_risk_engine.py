from backend.agents.risk_engine import calculate_risk
from backend.models.schemas import Signal

def signal(key, severity='high'):
    return Signal(key=key, severity=severity, title=key, description='test')

def test_no_signals_is_low(): assert calculate_risk([])[1] == 'LOW'
def test_single_signal_is_moderate(): assert calculate_risk([signal('payment_request')])[1] == 'MODERATE'
def test_multiple_signals_are_high(): assert calculate_risk([signal('payment_request'),signal('credential_request'),signal('artificial_urgency')])[1] in {'HIGH','CRITICAL'}
