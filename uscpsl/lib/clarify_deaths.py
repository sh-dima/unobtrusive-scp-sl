def clarify_deaths(deaths: str) -> str:
	lines = deaths.splitlines()
	lines[0] = "<b>[user]</b> - [class]\\n\\n💀 [cause]"
	return "\n".join(lines)
