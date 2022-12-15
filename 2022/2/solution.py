from aoc_lib.aoc_read_input import read_input

ROCK_POINTS = 1
PAPER_POINTS = 2
SCISSORS_POINTS = 3

LOSE = 0
DRAW = 3
WIN = 6

LOSE_SYMBOL = "X"
DRAW_SYMBOL = "Y"
WIN_SYMBOL = "Z"

LOSE_NUMBER = 2
WIN_NUMBER = 1
DRAW_NUMBER = 0

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

PLAYER_ROCK = "X"
PLAYER_PAPER = "Y"
PLAYER_SCISSORS = "Z"


def get_points_based_on_choose(choose: str) -> int:
    points = {
        PLAYER_ROCK: ROCK_POINTS,
        PLAYER_PAPER: PAPER_POINTS,
        PLAYER_SCISSORS: SCISSORS_POINTS,
    }
    return points.get(choose, 0)


get_opponent_int = lambda opponent: {ROCK: 0, PAPER: 1, SCISSORS: 2}.get(opponent)
get_player_play = lambda player: {
    0: PLAYER_ROCK,
    1: PLAYER_PAPER,
    2: PLAYER_SCISSORS,
}.get(player)
get_player_int = lambda player: {
    PLAYER_ROCK: 0,
    PLAYER_PAPER: 1,
    PLAYER_SCISSORS: 2,
}.get(player)
get_outcome_int = lambda outcome: {
    LOSE_SYMBOL: LOSE_NUMBER,
    DRAW_SYMBOL: DRAW_NUMBER,
    WIN_SYMBOL: WIN_NUMBER,
}.get(outcome)


def get_points_based_on_outcome(opponent: str, player: str) -> int:
    opponent_int = get_opponent_int(opponent)
    player_int = get_player_int(player)
    result = (3 + player_int - opponent_int) % 3
    return {DRAW_NUMBER: DRAW, WIN_NUMBER: WIN, LOSE_NUMBER: LOSE}.get(result)


def choose_players_play(opponent: str, outcome: str) -> str:
    """
    (3 + o - x)Mod3 = r
    (3 + o)Mod3 - xMod3= rMod3
    (3 + o)Mod3 - rMod3 = xMod3 ??
    """
    # opponent_int = get_opponent_int(opponent)
    # result_int = get_outcome_int(outcome)
    # player_int = ((3 + opponent_int) % 3) - (result_int % 3)
    # return get_player_play(player_int % 3)
    if ROCK == opponent and DRAW_SYMBOL == outcome:
        return PLAYER_ROCK
    elif ROCK == opponent and WIN_SYMBOL == outcome:
        return PLAYER_PAPER
    elif ROCK == opponent and LOSE_SYMBOL == outcome:
        return PLAYER_SCISSORS
    elif PAPER == opponent and DRAW_SYMBOL == outcome:
        return PLAYER_PAPER
    elif PAPER == opponent and WIN_SYMBOL == outcome:
        return PLAYER_SCISSORS
    elif PAPER == opponent and LOSE_SYMBOL == outcome:
        return PLAYER_ROCK
    elif SCISSORS == opponent and DRAW_SYMBOL == outcome:
        return PLAYER_SCISSORS
    elif SCISSORS == opponent and WIN_SYMBOL == outcome:
        return PLAYER_ROCK
    elif SCISSORS == opponent and LOSE_SYMBOL == outcome:
        return PLAYER_PAPER


def get_total_point_per_round(opponent: str, player: str) -> int:
    return get_points_based_on_choose(player) + get_points_based_on_outcome(
        opponent, player
    )


def get_total_point_per_round_choose(opponent: str, outcome: str) -> int:
    player = choose_players_play(opponent, outcome)
    return get_points_based_on_choose(player) + get_points_based_on_outcome(
        opponent, player
    )


if __name__ == "__main__":
    lines = data = read_input(2022, 2).splitlines()
    points = 0
    point_choose_outcome = 0
    for line in lines:
        opponent, player = line.split(" ")
        points += get_total_point_per_round(opponent, player)
        point_choose_outcome += get_total_point_per_round_choose(opponent, player)

    print(points)
    print(point_choose_outcome)
