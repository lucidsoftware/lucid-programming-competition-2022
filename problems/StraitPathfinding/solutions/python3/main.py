from typing import List, Tuple, TypeVar, Callable, Dict
from sys import stdin


# Generic type setup
A = TypeVar("A")
B = TypeVar("B")
Key = TypeVar("Key")
Value = TypeVar("Value")
InnerKey = TypeVar("InnerKey")


debug = False


class State:
    def __init__(
        self,
        length: int = None,
        width: int = None,
        obstacles: List[Tuple[int, int]] = None,
        down: List[Tuple[int, int]] = None,
        up: List[Tuple[int, int]] = None,
    ):
        self.width = width
        self.length = length
        self.down = down
        self.up = up
        self.obstacles = obstacles
        self.dynamic = len(up) + len(down) > 0

        self.__blocked = dict()
        for x, y in [*down, *up, *obstacles]:
            put_if_not_exists_and_get(self.__blocked, x, dict)[y] = True

        if debug:
            print_nested_dicts(self.__blocked)

    def is_blocked(self, x: int, y: int) -> bool:
        """
        Checks if a coordinate goes out of bounds.
        """
        return (
            x < 0
            or y < 0
            or y >= self.width
            or (x in self.__blocked and y in self.__blocked[x])
        )

    def print(self, boat = (None, None)):
        """
        Displays the current state, optionally displaying a boat at a given position
        """
        bx, by = boat
        for y in range(width):
            for x in range(length):
                if x == bx and y == by:
                    print("@", end="")
                elif self.is_blocked(x, y):
                    if (x, y) in self.up:
                        print("^", end="")
                    elif (x, y) in self.down:
                        print("v", end="")
                    else:
                        print("x", end="")
                else:
                    print("~", end="")
            print()


def put_if_not_exists_and_get(
    dict: Dict[Key, Value], key: Key, init: Callable[[], Value]
) -> Value:
    """
    Puts a value into a dictionary at the given key if a value does not already
    exist at that location. If it exists already, it's returned.

    Creates a new list when there's not one present:
    >>> my_dictionary = dict()
    >>> put_if_not_exists_and_get(my_dictionary, 'a', list)
    []

    Returns the existing list when there is one present:
    >>> my_dictionary = dict()
    >>> my_list = [0, 1]
    >>> my_dictionary['a'] = my_list
    >>> put_if_not_exists_and_get(my_dictionary, 'a', list)
    [0, 1]
    """
    if key not in dict:
        dict[key] = init()
    return dict[key]


def print_nested_dicts(dict: Dict[Key, Dict[InnerKey, A]]) -> None:
    """
    Prints key-keys and associated values.

    >>> my_dict = { 'a': { 5: 'hello' } }
    >>> print_nested_dicts(my_dict)
    a 5: hello
    """
    for x in dict.keys():
        for y in dict[x].keys():
            print(f"{x} {y}: {dict[x][y]}")


def find_coords_in_2d_list(
    list: List[List[A]], predicate: Callable[[A], bool]
) -> List[Tuple[int, int]]:
    """
    Flattens a 2D list into a singular list of x, y coordinates of any values
    that match the given predicate.

    :param list: A 2-dimensional list
    :param predicate: A predicate with which to check list items
    :return: List[Tuple[int, int]]

    >>> find_coords_in_2d_list([
    ...     [0, 0, 0, 1],
    ...     [1, 0, 0, 1],
    ...     [0, 1, 0, 0],
    ... ], lambda c: c == 1)
    [(3, 0), (0, 1), (3, 1), (1, 2)]
    """
    return [
        item
        for y in range(len(list))
        for item in [(x, y) for (x, c) in enumerate(list[y]) if predicate(c)]
    ]


def add_tuple(a: Tuple[A, B], b: Tuple[A, B]) -> Tuple[A, B]:
    """
    Adds two similarly-typed tuples together.

    >>> add_tuple((0, 0), (5, 5))
    (5, 5)

    >>> add_tuple((0, 1), (5, 5))
    (5, 6)

    >>> add_tuple((3, 'a'), (5, 'c'))
    (8, 'ac')
    """
    return (a[0] + b[0], a[1] + b[1])


def advance(state: State) -> State:
    """
    Moves the state forward a single move step.
    """
    # New lists to allow mutation of children
    obstacles = [(x, y) for x, y in state.obstacles]
    up = []
    down = []

    for (x, y) in state.down:
        if state.is_blocked(x, y + 1):
            up.append((x, y))
        else:
            down.append((x, y + 1))

    for (x, y) in state.up:
        if state.is_blocked(x, y - 1):
            down.append((x, y))
        else:
            up.append((x, y - 1))

    return State(state.length, state.width, obstacles, down, up)


def solve(next_state: State, start: Tuple[int, int]) -> int:
    """
    Slightly-optimized breadth-first search. Figures out if the given strait is
    dynamic, then either simulates the dynamic maze (more expensive) or uses a
    more optimal solution for static mazes.
    """
    # Useful aliases for directions and moves
    HOLD = (0, 0)
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, 1)
    DOWN = (0, -1)

    states = [next_state]  # states by time index
    dynamic = next_state.dynamic  # check if we need to simulate anything

    # We only need to stand still in dynamic mazes
    moves = [RIGHT, DOWN, UP, LEFT] + ([HOLD] if dynamic else [])
    queue = [(0, start, [])]

    while len(queue) > 0:
        state_idx, position, history = queue.pop(0)

        # create any states needed
        while dynamic and state_idx + 1 >= len(states):
            states.append(advance(states[-1]))

        next_state = states[state_idx + 1] if dynamic else next_state
        futures = [
            (state_idx + 1, add_tuple(position, move), [*history, move])
            for move in moves
            # no backtracking, but allow waiting
            if not next_state.is_blocked(*add_tuple(position, move))
        ]

        for future in futures:
            _, coord, history = future

            # we win
            if coord[0] >= next_state.length:
                if debug:
                    print(history)
                return len(history)

            if (
                len(history) > 1
                and history[-1][0] == -history[-2][0]
                and history[-1][1] == -history[-2][1]
                and not (history[-1][0] != 0 and history[-1][1] != 0)
            ):
                continue

            queue.append(future)

    return 0


def run(width: int, length: int, strait: List[List[str]]) -> int:
    """
    Deal with input then solve.
    """
    # Find the start using the same process
    start = find_coords_in_2d_list(strait, lambda c: c == "@")[0]

    # We're already nearly there
    if start[0] == length - 1:
        return 1

    # Do some slow stuff a single time
    # Unpack state into a more linear form
    down = find_coords_in_2d_list(strait, lambda c: c == "v")
    up = find_coords_in_2d_list(strait, lambda c: c == "^")
    obstacles = find_coords_in_2d_list(strait, lambda c: c == "x")

    # Create a nice state object to help us
    state = State(length, width, obstacles, down, up)
    return solve(state, start)


if __name__ == "__main__":
    # Run tests on util functions
    import doctest

    doctest.testmod()

    # Handle input
    width = int(stdin.readline())
    length = int(stdin.readline())
    strait = [list(stdin.readline()) for _ in range(width)]

    print(run(width, length, strait))
