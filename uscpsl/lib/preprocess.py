import re

def preprocess(text: str) -> str:
	return re.sub(r"SCP-0(\d{2})", r"SCP-\1", text)
