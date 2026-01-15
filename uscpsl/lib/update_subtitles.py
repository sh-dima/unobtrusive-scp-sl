def update_subtitles(subtitles: str, names: dict[str, str]) -> str:
	lines = subtitles.splitlines()

	lines[15] = "⚡ [current]/[max]"

	return "\n".join(lines)
