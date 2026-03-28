colors_tuple = ("red", "green", "blue")

colors_list = list(colors_tuple)

colors_list[1] = "yellow"

colors_tuple = tuple(colors_list)
print("Modified tuple:", colors_tuple)
