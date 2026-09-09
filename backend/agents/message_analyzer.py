import re
from models.schemas import Entity, Signal
RULES = [
 ('payment_request','high','Upfront payment request','The message asks for money before the claimed benefit is provided.',r'\b(pay|payment|fee|deposit|₹|rs\.?|inr|upi|wallet)\b'),
 ('artificial_urgency','high','Artificial urgency','The message pressures you to act quickly, reducing time to verify.',r'\b(within|urgent|immediately|today|minutes?|hours?|last chance|expire|जल्दी|तुरंत)\b'),
 ('credential_request','high','Sensitive information request','The message appears to request credentials or verification codes.',r'\b(otp|password|pin|cvv|login|credential|aadhaar number|pan number)\b'),
 ('impersonation','high','Possible organization impersonation','A recognizable organization is invoked, but the message cannot establish the sender represents it.',r'\b(google|microsoft|amazon|bank|government|rbi|sbi|flipkart|govt)\b'),
 ('threat_language','medium','Threat or consequence language','The message mentions a negative consequence to pressure action.',r'\b(blocked|suspended|arrest|penalty|legal action|lose access|बंद|निलंबित)\b'),
 ('suspicious_employment','high','Employment scam pattern','An opportunity is paired with payment or immediate action; verify independently.',r'\b(internship|job|hiring|recruiter|offer letter|इंटर्नशिप|नौकरी|नोकरी)\b')]
def analyze_message(text: str) -> tuple[list[Signal], list[Entity]]:
 signals=[]
 for key,severity,title,description,pattern in RULES:
  match=re.search(pattern,text,re.I)
  if match: signals.append(Signal(key=key,severity=severity,title=title,description=description,evidence=text[max(0,match.start()-42):min(len(text),match.end()+52)].strip()))
 entities=[]
 for org in re.findall(r'\b(Google|Microsoft|Amazon|SBI|RBI|Flipkart|WhatsApp|Instagram)\b',text,re.I): entities.append(Entity(text=org,type='organization'))
 for amount in re.findall(r'(?:₹\s?\d[\d,]*|(?:Rs\.?|INR)\s?\d[\d,]*)',text,re.I): entities.append(Entity(text=amount,type='money'))
 for url in re.findall(r"https?://[^\s<>'\"]+|www\.[^\s<>'\"]+",text,re.I): entities.append(Entity(text=url,type='url'))
 return signals,entities
import re
from models.schemas import Entity, Signal

RULES = [('payment_request','high','Upfront payment request','The message asks for money before a claimed benefit.',r'\b(pay|payment|fee|deposit|₹|rs\.?|inr|upi)\b'),('artificial_urgency','high','Artificial urgency','The message pressures quick action.',r'\b(within|urgent|immediately|today|minutes?|hours?|last chance|expire)\b'),('credential_request','high','Sensitive information request','The message appears to request credentials or codes.',r'\b(otp|password|pin|cvv|login|credential)\b'),('impersonation','high','Possible organization impersonation','A known organization is invoked but the sender cannot be established.',r'\b(google|microsoft|amazon|bank|government|rbi|sbi|flipkart)\b'),('threat_language','medium','Threat language','A negative consequence is used to pressure action.',r'\b(blocked|suspended|arrest|penalty|legal action|lose access)\b'),('suspicious_employment','high','Employment scam pattern','An opportunity paired with payment or urgency warrants verification.',r'\b(internship|job|hiring|recruiter|offer letter)\b')]

def analyze_message(text: str) -> tuple[list[Signal], list[Entity]]:
    signals=[]
    for key,severity,title,description,pattern in RULES:
        if m:=re.search(pattern,text,re.I): signals.append(Signal(key=key,severity=severity,title=title,description=description,evidence=text[max(0,m.start()-42):min(len(text),m.end()+52)].strip()))
    entities=[]
    for org in re.findall(r'\b(Google|Microsoft|Amazon|SBI|RBI|Flipkart|WhatsApp|Instagram)\b',text,re.I): entities.append(Entity(text=org,type='organization'))
    for amount in re.findall(r'(?:₹\s?\d[\d,]*|(?:Rs\.?|INR)\s?\d[\d,]*)',text,re.I): entities.append(Entity(text=amount,type='money'))
    return signals,entities
