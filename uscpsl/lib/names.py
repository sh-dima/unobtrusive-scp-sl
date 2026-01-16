from uscpsl.lib.get_file import get_file

def get_names(directory: str) -> dict[str, str]:
	names = {}

	names_file = get_file(directory, "Class_Names.txt")
	names_list = list(map(lambda n: n.strip(), names_file.splitlines()))

	teams_file = get_file(directory, "Teams.txt")
	teams_list = list(map(lambda n: n.strip(), teams_file.splitlines()))

	items_file = get_file(directory, "Items.txt")
	items_list = list(map(lambda i: i.strip().split("~"), items_file.splitlines()))

	names["49"] = names_list[5]
	names["49-2"] = names_list[10]
	names["96"] = names_list[9]
	names["106"] = names_list[3]
	names["173"] = names_list[0]
	names["939"] = names_list[16]
	names["3114"] = names_list[23]
	names["1507"] = names_list[25]

	names["127"] = items_list[56][1]
	names["207"] = items_list[18][1]
	names["1509"] = items_list[57][1]

	names["chaos"] = teams_list[2]

	return names
