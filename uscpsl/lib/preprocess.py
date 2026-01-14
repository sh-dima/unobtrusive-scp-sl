import re

def preprocess(directory: str, name: str, text: str) -> str:
	text = re.sub(r"SCP-0(\d{2})", r"SCP-\1", text)

	if directory.endswith("vi_uo"):
		text = text.replace(" – ", "~")

	if name.endswith("Legacy_Interfaces.txt"):
		lines = text.splitlines()
		lines[0] = ""
		lines[1] = ""
		lines[2] = ""
		text = "\n".join(lines)

	if name.endswith("Class_Descriptions.txt"):
		lines = text.splitlines()
		lines = ["" for line in lines]
		text = "\n".join(lines)

	return text
