def process_command(text, memory):
    text = text.lower()

    if "поллукс" in text or "лукси" in text:
        text = text.replace("поллукс","").replace("лукси","")

    if "запусти" in text:
        return {"type":"launch", "text":text}

    if "найди" in text:
        return {"type":"search", "text":text}

    if "помни" in text:
        return {"type":"memory"}

    return {"type":"chat", "text":text}