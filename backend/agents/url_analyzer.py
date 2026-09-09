import ipaddress
from urllib.parse import urlparse
import tldextract
from models.schemas import Signal, UrlResponse

async def analyze_url(value: str) -> UrlResponse:
    url = value.strip() if value.startswith(('http://','https://')) else 'https://' + value.strip()
    parsed = urlparse(url)
    if not parsed.hostname: raise ValueError('Please provide a valid URL with a hostname.')
    host=parsed.hostname.lower(); indicators=[]
    def add(key,severity,title,description): indicators.append(Signal(key=key,severity=severity,title=title,description=description,source='url'))
    try: ipaddress.ip_address(host); add('ip_hostname','high','IP address used as hostname','The link uses a numeric IP address instead of a named domain.')
    except ValueError: pass
    if 'xn--' in host: add('punycode','high','Punycode domain','The hostname contains encoded internationalized labels; inspect carefully for lookalikes.')
    if parsed.scheme != 'https': add('insecure_protocol','medium','No HTTPS encryption','This link uses HTTP, so browser-to-site traffic may not be encrypted.')
    if host.count('.') >= 4: add('excessive_subdomains','medium','Excessive subdomains','Many subdomains can obscure the registered domain.')
    if len(url)>120 or '@' in url or url.count('-')>=4: add('suspicious_url_shape','medium','Unusual URL structure','The URL is unusually long or uses a deceptive-looking structure.')
    x=tldextract.extract(host); domain='.'.join(p for p in [x.domain,x.suffix] if p) or host
    return UrlResponse(domain=domain,protocol=parsed.scheme,hostname=host,suspicious_indicators=indicators,risk_indicators=[x.title for x in indicators],ai_interpretation='Structural indicators warrant caution; they do not by themselves prove a site is malicious.' if indicators else 'No strong structural indicators were detected. This is not verification of legitimacy.',fetch_status='not_fetched')
