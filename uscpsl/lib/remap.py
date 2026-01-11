import os
import logging
import json

from uscpsl.lib.preprocess import preprocess

def remap(directory: str):
	files = os.listdir(directory)

	if os.path.exists(f"{directory}/manifest.json"):
		with open(f"{directory}/manifest.json") as manifest_file:
			manifest_text = manifest_file.read()
		
		manifest = json.loads(manifest_text)
		manifest["Name"] = f"{manifest["Name"]} (Unobtrusive)"

		with open(f"{directory}/manifest.json", "w") as manifest_file:
			manifest_file.write(json.dumps(manifest))

	logging.debug(f"Preprocessing {len(files)} files in directory {directory}:")

	for file in files:
		with open(f"{directory}/{file}") as f:
			text = f.read()

		with open(f"{directory}/{file}", "w") as f:
			f.write(preprocess(text))
