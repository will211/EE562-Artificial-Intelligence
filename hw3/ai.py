import time
import random 
import io

class key:
    def key(self):
        return "10jifn2eonvgp1o2ornfdlf-1230"

class ai:
    def __init__(self):
        self.max_depth = 15
        self.limit_time  = 1
        self.heuristic_method = 'simple'
        # self.heuristic_method = 'advance'


    class state:
        def __init__(self, a, b, a_fin, b_fin):
            self.a = a
            self.b = b
            self.a_fin = a_fin
            self.b_fin = b_fin
            self.index_to_evaluate = {}

    # Kalah:
    #         b[5]  b[4]  b[3]  b[2]  b[1]  b[0]
    # b_fin                                         a_fin
    #         a[0]  a[1]  a[2]  a[3]  a[4]  a[5]
    # Main function call:
    # Input:
    # a: a[5] array storing the stones in your holes
    # b: b[5] array storing the stones in opponent's holes
    # a_fin: Your scoring hole (Kalah)
    # b_fin: Opponent's scoring hole (Kalah)
    # t: search time limit (ms)
    # a always moves first
    #
    # Return:
    # You should return a value 0-5 number indicating your move, with search time limitation given as parameter
    # If you are eligible for a second move, just neglect. The framework will call this function again
    # You need to design your heuristics.
    # You must use minimax search with alpha-beta pruning as the basic algorithm
    # use timer to limit search, for example:
    # start = time.time()
    # end = time.time()
    # elapsed_time = end - start
    # if elapsed_time * 1000 >= t:
    #    return result immediately 
    def move(self, a, b, a_fin, b_fin, t):
        # #For test only: return a random move
        # r = []
        # for i in range(6):
        #     if a[i] != 0:
        #         r.append(i)
        # # To test the execution time, use time and file modules
        # # In your experiments, you can try different depth, for example:
        # f = open('time.txt', 'a') #append to time.txt so that you can see running time for all moves.
        # # Make sure to clean the file before each of your experiment
        # for d in [3, 5, 7]: #You should try more
        #     f.write('depth = '+str(d)+'\n')
        #     t_start = time.time()
        #     self.minimax(depth = d)
        #     f.write(str(time.time()-t_start)+'\n')
        # f.close()
        # return r[random.randint(0, len(r)-1)]
        # #But remember in your final version you should choose only one depth according to your CPU speed (TA's is 3.4GHz)
        # #and remove timing code. 
        
        # #Comment all the code above and start your code here

        # f = open('time.txt', 'a')
        # for d in [3, 5, 7, 10, 15, 20]:
        for _ in range(1):
            # self.max_depth = d
            # f.write('depth =' + str(d)+'\n')
            # t_start = time.time()
            state = self.state(a, b, a_fin, b_fin)
            heuristic_val = self.minimax(state, 0, -float("inf"), float("inf"), True)
            for index in state.index_to_evaluate:
                if state.index_to_evaluate[index] == heuristic_val:
                    res = index
            # f.write(str(time.time() - t_start)+'\n')
        # f.close()

        return res
 
    """
    Minimax search with alpha-beta pruning implement

    Args:
        - state: the state of Kalah game
        - depth: the current state of depth
        - alpha: the alpha-beta pruining alpha value
        - beta: the alpha-beta pruining beta value
        - is_maximizing: to determine the level is max or min

    Returns:
        - The heuristic value
    """ 
    # calling function
    def minimax(self, state, depth, alpha, beta, is_maximizing):
        # #example: doing nothing but wait 0.1*depth sec
        # time.sleep(0.1*depth)

        if depth > self.max_depth or state.a_fin > 36 or state.b_fin > 36 or (state.a_fin + state.b_fin) == 72:
            return self.heuristic_function(state)

        evals = float("inf")
        if is_maximizing:
            evals = -float("inf")

        for index in range(6):
            if state.a[index] == 0:
                continue
            
            index_next_state = self.kalah_move(state, index)
            depth += 1

            if is_maximizing:
                evals = max(evals, self.minimax(index_next_state, depth, alpha, beta, False))
                # hash table of index the pit postion to the evaluation value
                state.index_to_evaluate[index] = evals
                if evals >= beta:
                    return evals
                alpha = max(alpha, evals)
            else:
                evals = min(evals, self.minimax(index_next_state, depth, alpha, beta, True))
                if evals <= alpha:
                    return evals
                beta = min(beta, evals)

        return evals

    """
    Compute the kalah move

    Args:
        - state: the current state of Kalah game
        - index: the position of the pits

    Returns:
        - The state of Kalah
    """ 
    def kalah_move(self, state, index):

        ao = state.a[:]
        kalah = state.a[index:] + [state.a_fin] + state.b + state.a[:index]
        count = state.a[index]
        kalah[0] = 0
        p = 1

        while count > 0:
            kalah[p] += 1
            p = (p + 1) % 13
            count -= 1
            
        a_fin = kalah[6 - index]
        a = kalah[13 - index:] + kalah[: 6 - index]
        b = kalah[7 - index : 13 - index]
        ceat = False

        p = (p - 1) % 13
        if p <= (5 - index) and ao[index] < 14:
            id = p + index
            if (ao[id] == 0 or p % 13 == 0) and (b[5 - id] > 0):
                ceat = True
        elif p >= (14 - index) and ao[index] < 14:
            id = p + index - 13
            if (ao[id] == 0 or p % 13 == 0) and (b[5 - id] > 0):
                ceat = True
            
        if ceat:
            a_fin += a[id] + b[5 - id]
            b[5 - id] = 0
            a[id] = 0
            
        b_fin = state.b_fin
        if sum(a) == 0:
            b_fin += sum(b)
        if sum(b) == 0:
            a_fin += sum(a)

        return self.state(a, b, a_fin, b_fin)
    
    """
    Compute the heuristic value base on which method

    Args:
        - state: the current state of Kalah game

    Returns:
        - The heuristic value
    """ 
    def heuristic_function(self, state):
        if self.heuristic_method == 'simple':
            return (state.a_fin - state.b_fin)
    
        elif self.heuristic_method == 'advance':
            return (state.a_fin - state.b_fin) + (sum(state.a) - sum(state.b)) * 0.3