from uscpsl.lib.get_file import get_file

def get_names(directory: str) -> dict[str, str]:
	names = {}

	names_file = get_file(directory, "Class_Names.txt")
	names_list = list(map(lambda n: n.strip(), names_file.splitlines()))

	names["49"] = names_list[5]
	names["49-2"] = names_list[10]
	names["96"] = names_list[9]
	names["173"] = names_list[0]
	names["939"] = names_list[16]

	return names
