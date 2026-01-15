def update_facility(facility: str, names: dict[str, str]) -> str:
	lines = facility.splitlines()

	lines[32] = "➜] [escape_minutes]:[escape_seconds]"
	lines[34] = "ℹ️ <color=yellow><b>F1</b></color>"

	return "\n".join(lines)
