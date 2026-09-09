import json
from pathlib import Path
from backend.services.analysis_service import analyze_text

root = Path(__file__).resolve().parents[1]
items = []
for filename in ('scam_examples.json', 'legitimate_examples.json'):
    items += json.loads((root / 'data' / 'examples' / filename).read_text())
tp = fp = tn = fn = 0
for item in items:
    predicted = analyze_text(item['text']).classification == 'potential_scam'
    actual = item['label'] == 'scam'
    tp += predicted and actual; fp += predicted and not actual; tn += not predicted and not actual; fn += not predicted and actual
precision = tp / (tp + fp) if tp + fp else 0
recall = tp / (tp + fn) if tp + fn else 0
print({'accuracy': (tp + tn) / len(items), 'precision': precision, 'recall': recall, 'f1': 2 * precision * recall / (precision + recall) if precision + recall else 0, 'false_positives': fp, 'false_negatives': fn})
