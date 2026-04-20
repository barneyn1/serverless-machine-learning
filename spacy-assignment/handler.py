import json
import en_core_web_sm
from spacy import displacy

MODEL = en_core_web_sm.load()

def tag_and_parse(text):
    doc = MODEL(text)
    return displacy.parse_deps(doc)

def handle_request(event, context):
    request_body = event.get("body")
    text = json.loads(request_body)["text"] if request_body else None
    response_body = tag_and_parse(text) if text else {"words": [], "arcs": []}

    return {
        "statusCode": 200,
        "body": json.dumps(response_body),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    }
