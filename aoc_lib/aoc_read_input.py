import aocd


def read_input(year: int, day: int, local=False):
    if local:
        with open(f"{year}/{day}/test.in", "r") as fp:
            input = fp.read()
        return input
    else:
        return aocd.get_data(day=day, year=year)
