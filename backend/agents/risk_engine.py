from models.schemas import Signal

WEIGHTS = {'payment_request': 22, 'credential_request': 25, 'artificial_urgency': 15, 'impersonation': 14, 'suspicious_employment': 18, 'threat_language': 10, 'ip_hostname': 15, 'punycode': 15, 'excessive_subdomains': 8, 'insecure_protocol': 6, 'suspicious_url_shape': 10}

def calculate_risk(signals: list[Signal]) -> tuple[int, str, str]:
    score = min(100, sum(WEIGHTS.get(s.key, {'high': 12, 'medium': 7, 'low': 3}[s.severity]) for s in signals))
    if score >= 75: return score, 'CRITICAL', 'potential_scam'
    if score >= 50: return score, 'HIGH', 'potential_scam'
    if score >= 25: return score, 'MODERATE', 'caution'
    return score, 'LOW', 'likely_legitimate'
