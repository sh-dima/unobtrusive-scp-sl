import re

def preprocess(directory: str, name: str, text: str) -> str:
	text = re.sub(r"SCP-0(\d{2})", r"SCP-\1", text)

	if directory.endswith("vi_uo"):
		text = text.replace(" – ", "~")

	if name.endswith("Legacy_Interfaces.txt"):
		lines = text.splitlines()
		lines[0] = "ㅤ"
		lines[1] = "ㅤ"
		lines[2] = "ㅤ"
		text = "\n".join(lines)

	if name.endswith("Class_Descriptions.txt"):
		lines = text.splitlines()
		lines = ["ㅤ" for line in lines]
		text = "\n".join(lines)

	if name.endswith("HumanBio.txt"):
		lines = text.splitlines()
		lines = ["ㅤ" for line in lines]
		text = "\n".join(lines)

	return text
