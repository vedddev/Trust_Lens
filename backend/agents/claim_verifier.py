import re
from models.schemas import Claim
PATTERNS=[('selection_or_offer',r'[^.\n]{0,80}\b(selected|offer|internship|job|scholarship)\b[^.\n]{0,120}'),('payment',r'[^.\n]{0,80}\b(pay|payment|fee|deposit|₹|upi)\b[^.\n]{0,120}'),('account_status',r'[^.\n]{0,80}\b(account|blocked|suspended|otp)\b[^.\n]{0,120}')]
def extract_and_verify_claims(text: str) -> list[Claim]:
 return [Claim(text=m.group(0).strip(),type=kind,status='unverified',reasoning='This claim is present in the submitted message but was not independently verified by TrustLens.') for kind,pattern in PATTERNS if (m:=re.search(pattern,text,re.I))]
