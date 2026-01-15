import os
import logging
import json

from uscpsl.lib.names import get_names

from uscpsl.lib.preprocess import preprocess
from uscpsl.lib.clarify_deaths import clarify_deaths
from uscpsl.lib.update_facility import update_facility

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
		try:
			with open(f"{directory}/{file}") as f:
				text = f.read()

			with open(f"{directory}/{file}", "w") as f:
				f.write(preprocess(directory, f.name, text))
		except:
			logging.error(f"Failed to preprocess file {file}")
			exit(1)

	names = get_names(directory)
	
	if os.path.exists(f"{directory}/DeathReasons.txt"):
		with open(f"{directory}/DeathReasons.txt") as f:
			deaths = f.read()

		with open(f"{directory}/DeathReasons.txt", "w") as f:
			f.write(clarify_deaths(deaths, names))

	if os.path.exists(f"{directory}/Facility.txt"):
		with open(f"{directory}/Facility.txt") as f:
			facility = f.read()

		with open(f"{directory}/Facility.txt", "w") as f:
			f.write(update_facility(facility, names))
