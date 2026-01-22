def colorize_classes(classes: str, names: dict[str, str]) -> str:
	lines = classes.splitlines()

	scps = [
		0, 3, 5, 7, 9, 10, 16, 23, 27
	]

	for scp in scps:
		if scp >= len(lines):
			continue
		lines[scp] = f"<color=#F00>{lines[scp]}</color>"

	# Source for class colors: https://en.scpslgame.com/index.php?title=Data/Color&action=edit
	lines[1] = f"<color=#FF8E00>{lines[1]}</color>" # Class D
	lines[4] = f"<color=#00D9FF>{lines[4]}</color>" # NTF specialist
	lines[6] = f"<color=#FFFF7C>{lines[6]}</color>" # Scientist
	lines[8] = f"<color=#559101>{lines[8]}</color>" # Chaos conscript
	lines[11] = f"<color=#0096FF>{lines[11]}</color>" # NTF sergeant
	lines[12] = f"<color=#003DCA>{lines[12]}</color>" # NTF captain
	lines[13] = f"<color=#70C3FF>{lines[13]}</color>" # NTF private
	lines[14] = f"<color=#F700FD>{lines[14]}</color>" # Tutorial
	lines[15] = f"<color=#5B6370>{lines[15]}</color>" # Facility guards
	lines[18] = f"<color=#008F1C>{lines[18]}</color>" # CI rifleman
	lines[19] = f"<color=#066328>{lines[19]}</color>" # CI marauder
	lines[20] = f"<color=#15853D>{lines[20]}</color>" # CI repressor

	lines[25] = f"<color=#FF59CA>{lines[25]}</color>" # Flamingo
	lines[26] = f"<color=#E94CB7>{lines[26]}</color>" # Alpha flamingo

	return "\n".join(lines)
