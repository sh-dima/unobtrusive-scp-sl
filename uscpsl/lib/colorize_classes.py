def colorize_classes(classes: str, names: dict[str, str]) -> str:
	lines = classes.splitlines()

	scps = [
		0, 3, 5, 7, 9, 10, 16, 23, 25, 26, 27
	]

	for scp in scps:
		if scp >= len(lines):
			continue
		lines[scp] = f"<color=#F00>{lines[scp]}</color>"

	return "\n".join(lines)
