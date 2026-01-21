import os
import logging
import json

from uscpsl.lib.names import get_names

from uscpsl.lib.preprocess import preprocess
from uscpsl.lib.clarify_deaths import clarify_deaths
from uscpsl.lib.update_facility import update_facility
from uscpsl.lib.update_subtitles import update_subtitles
from uscpsl.lib.remove_descriptions import remove_descriptions
from uscpsl.lib.colorize_classes import colorize_classes

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

	if os.path.exists(f"{directory}/Subtitles.txt"):
		with open(f"{directory}/Subtitles.txt") as f:
			subtitles = f.read()

		with open(f"{directory}/Subtitles.txt", "w") as f:
			f.write(update_subtitles(subtitles, names))

	if os.path.exists(f"{directory}/Items.txt"):
		with open(f"{directory}/Items.txt") as f:
			items = f.read()

		with open(f"{directory}/Items.txt", "w") as f:
			f.write(remove_descriptions(items, names))

	if os.path.exists(f"{directory}/Class_Names.txt"):
		with open(f"{directory}/Class_Names.txt") as f:
			classes = f.read()

		with open(f"{directory}/Class_Names.txt", "w") as f:
			f.write(colorize_classes(classes, names))
