
last_result = ""   # global variable

def set_result(text: str):
    global last_result
    last_result = text

def get_result() -> str:
    return last_result
