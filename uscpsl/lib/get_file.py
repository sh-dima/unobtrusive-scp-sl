import os

def get_file(directory: str, file: str, fallback="en") -> str:
	if os.path.exists(f"{directory}/{file}"):
		with open(f"{directory}/{file}") as file:
			return file.read()
	else:
		with open(f"{fallback}/{file}") as file:
			return file.read()
