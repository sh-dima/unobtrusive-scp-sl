import os
import sys
import shutil
import logging

from pathlib import Path

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from uscpsl.lib.remap import remap

def main():
	parser = ArgumentParser(
		formatter_class=lambda prog: ArgumentDefaultsHelpFormatter(prog, width=120, max_help_position=50)
	)

	parser.add_argument("-l", "--log-level", type=str, choices=[level for level in logging._nameToLevel.keys()], default="INFO", metavar="level", help="set logging level")
	parser.add_argument("-d", "--directory", type=str, default=f"{Path.home()}/.local/share/Steam/steamapps/common/SCP Secret Laboratory/Translations/", metavar="directory", help="set translations directory")
	parsed = parser.parse_args()

	logging.basicConfig(level=getattr(logging, parsed.log_level))

	os.chdir(parsed.directory)

	logging.info(f"Remapping translations in directory {os.getcwd()}")
	
	languages = os.listdir(os.getcwd())
	logging.debug(f"Found the following {len(languages)} existing translations: {languages}")

	languages = list(filter(lambda l: not l.endswith("_uo"), languages))

	logging.debug(f"{len(languages)} remain after filtering: {languages}")

	for language in languages:
		name = f"{language}_uo"

		if os.path.exists(name):
			shutil.rmtree(name)

		shutil.copytree(language, name)
		remap(f"{os.getcwd()}/{name}")

if __name__ == "__main__":
	main()
