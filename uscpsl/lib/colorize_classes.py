def colorize_classes(classes: str, names: dict[str, str]) -> str:
	lines = classes.splitlines()

	scps = [
		0, 3, 5, 7, 9, 10, 16, 23, 25, 26, 27
	]

	for scp in scps:
		if scp >= len(lines):
			continue
		lines[scp] = f"<color=#F00>{lines[scp]}</color>"

	# Source for class colors: https://en.scpslgame.com/index.php?title=Data/Color&action=edit
	lines[1] = f"<color=#FF8E00>{lines[1]}</color>" # Class D
	lines[15] = f"<color=#5B6370>{lines[15]}</color>" # Facility guards

	return "\n".join(lines)
