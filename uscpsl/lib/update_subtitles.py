def update_subtitles(subtitles: str, names: dict[str, str]) -> str:
	lines = subtitles.splitlines()

	lines[15] = "⚡ [current]/[max]"
	lines[29] = f"+ [number] {names["chaos"]}"
	lines[30] = f"+ [number] {names["chaos"]}"

	return "\n".join(lines)
