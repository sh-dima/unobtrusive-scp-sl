def update_subtitles(subtitles: str, names: dict[str, str]) -> str:
	lines = subtitles.splitlines()

	lines[1] = f"[count] {names["scps"]}"
	lines[15] = "⚡ <color=yellow>[current]</color>/<color=yellow>[max]</color>"
	lines[16] = ""
	lines[29] = f"+[number] <color=#008F1e>{names["chaos"]}</color>"
	lines[30] = f"+[number] <color=#008F1e>{names["chaos"]}</color>"

	return "\n".join(lines)
