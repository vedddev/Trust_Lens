from fastapi.testclient import TestClient
from backend.main import app
client = TestClient(app)
def test_health(): assert client.get('/api/health').json() == {'status':'ok'}
def test_analyze_validation(): assert client.post('/api/analyze',json={'text':''}).status_code == 422
