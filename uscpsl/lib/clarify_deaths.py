def clarify_deaths(deaths: str, names: dict[str, str]) -> str:
	lines = deaths.splitlines()
	lines[0] = "<b>[user]</b> - [class]\\n\\n💀 [cause]"
	lines[3] = names["49"]
	lines[11] = names["106"]
	lines[15] = names["207"]
	lines[18] = "⚡"
	lines[19] = "💥"
	lines[21] = names["96"]
	lines[22] = names["173"]
	lines[23] = names["939"]
	lines[24] = names["49-2"] + " / " + names["1507"] + " / " + names["3114"]
	lines[34] = names["127"]
	lines[35] = names["1509"]
	return "\n".join(lines)
