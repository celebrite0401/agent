from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()

@app.api_route("/twilio/webhook", methods=["GET", "POST"])
async def twilio_webhook(request: Request):
    twiml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say language="hi-IN">नमस्ते, मैं सेंटियो से बोल रहा हूँ। क्या आप ठीक हैं?</Say>
</Response>
"""
    return Response(content=twiml, media_type="application/xml")
