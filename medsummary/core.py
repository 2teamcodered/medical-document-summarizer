import re
def extract_sections(text: str) -> dict:
    labels=["history","medications","assessment","plan"]
    result={k:[] for k in labels}
    for line in text.splitlines():
        low=line.lower()
        for label in labels:
            if low.startswith(label+":"):
                result[label].append(line.split(":",1)[1].strip())
    return result
def summary(text: str) -> dict:
    return {"sections":extract_sections(text),"review_flags":["verify dates, dosages, and patient identity"],"human_review_required":True}
