import json
import en_core_web_sm

MODEL = en_core_web_sm.load()

def create_ner_spans(text):
    doc = MODEL(text)
    return [
        {
            "start": ent.start_char,
            "end": ent.end_char,
            "type": ent.label_
        }
        for ent in doc.ents
    ]

def handle_request(event, context):
    text = event.get("body")
    spans = create_ner_spans(text) if text else []

    return {
        "statusCode": 200,
        "body": json.dumps({"spans": spans}),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    }
