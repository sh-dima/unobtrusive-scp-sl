import re

def preprocess(directory: str, text: str) -> str:
	text = re.sub(r"SCP-0(\d{2})", r"SCP-\1", text)

	if directory.endswith("vi_uo"):
		text = text.replace(" – ", "~")

	return text
