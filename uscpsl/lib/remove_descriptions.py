def remove_descriptions(items: str, names: dict[str, str]) -> str:
	lines = items.splitlines()

	split = [line.split("~") for line in lines]
	for i in range(len(split)):
		split_line = split[i]
		if len(split_line) >= 3:
			split_line[2] = ""

		split[i] = "~".join(split_line)

	return "\n".join(split)
