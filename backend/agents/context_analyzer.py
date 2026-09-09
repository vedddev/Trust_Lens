import re

CONTEXTS = {'job_or_internship':['internship','job','hiring','recruiter','offer letter','इंटर्नशिप','नौकरी','नोकरी'], 'banking_or_account':['bank','account','otp','kyc','बैंक','खाता'], 'scholarship':['scholarship','grant','fellowship','शिष्यवृत्ती'], 'delivery':['delivery','parcel','courier','shipment','package'], 'investment':['investment','crypto','returns','trading'], 'social_media':['instagram','facebook','whatsapp','telegram'], 'government':['government','tax','aadhaar','pan','police']}

def detect_language(text: str) -> str:
    if re.search(r'[\u0900-\u097F]', text): return 'mr' if any(x in text for x in ['आहे','तुम्ही','करा']) else 'hi'
    return 'en'

def analyze_context(text: str) -> dict:
    for name, words in CONTEXTS.items():
        if any(word in text.lower() for word in words): return {'context':name,'intent':'request_or_notification'}
    return {'context':'general_communication','intent':'unknown'}
