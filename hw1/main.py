from state import State

MISS_NUM = 3
CANN_NUM = 3

total_count = 0
illegal_count = 0
repeated_count = 0

"""
DFS function to solve the missionaries and cannibals problem.

Args:
    - cur_state (State): The current state.
    - pre_states (list of State): List of all previously visited states.
"""
def dfs(cur_state, pre_states):
    moves = ([0, 1], [0, 2], [1, 1], [1, 0], [2, 0])
    global total_count, illegal_count, repeated_count
    if cur_state in pre_states:
        repeated_count += 1
        return
        
    elif not is_valid(cur_state):
        illegal_count += 1
        return

    elif cur_state == State(0, 0, 0):
        total_count += 1
        print("Solution:")
        for state in (pre_states + [cur_state]):
            print(state)

    else:
        total_count += 1
        for move in moves:
            m, c = move
            if cur_state.side:
                next_state = State(cur_state.missionaries - m, cur_state.cannibals - c, 0)
                dfs(next_state, pre_states + [cur_state])
            else:
                next_state = State(cur_state.missionaries + m, cur_state.cannibals + c, 1)
                dfs(next_state, pre_states + [cur_state])

"""
Check if a given state is valid.

Args:
    - state (State): The state to be checked.

Returns:
    - bool: True if the state is valid, False otherwise.
"""
def is_valid(state):
        if state.missionaries < 0 or state.cannibals < 0 or state.missionaries > MISS_NUM or state.cannibals > CANN_NUM or (state.side != 0 and state.side != 1):
            return False
        
        elif (state.missionaries and state.missionaries < state.cannibals) or (MISS_NUM - state.missionaries and MISS_NUM - state.missionaries < CANN_NUM - state.cannibals):
            return False

        return True

def main():
    dfs(State(MISS_NUM, CANN_NUM, 1), [])
    print(f"totals: {total_count}, illegals: {illegal_count}, repeats: {repeated_count}")

if __name__ == "__main__":
    main()