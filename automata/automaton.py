class State:
    def __init__(self, name="q0", initial=False, accepting=False):
        self.name = name
        self.inital = initial
        self.accepting = accepting
        self.transitions = {}


class DFAutomaton:
    def __init__(self, name, states):
        self.name = name
        self.states = {}
        for s in states:
            self.states[s] = State(s)

    def add_transition(self, firststate, edge, nextstate):
        self.states[firststate].transitions[edge] = nextstate

    def next_state(self, state, edge):
        return self.states[state.transitions[edge]]

    def simulate(self, initial, word, verbose=False):
        initial_state = self.states[initial]
        next_state = self.next_state(initial_state, word[0])
        if verbose:
            print(f"starting at state {initial_state.name}")
            print(f"going to state {next_state.name} with transition {word[0]}")
        for i in range(1, len(word)):
            next_state = self.next_state(initial_state, word[i])
            if verbose:
                print(f"going to state {next_state.name} with transition {word[i]}")
        if verbose:
            if next_state.accepting:
                print(f"accepting at state {next_state.name}")
            else:
                print(f"not accepting at state {next_state.name}")
        return next_state.accepting


if __name__ == '__main__':
    A = DFAutomaton("test", [1, 2, 3])
    A.states[1].inital = True
    A.states[3].accepting = True
    A.add_transition(1, "a", 3)
    A.add_transition(1, "b", 1)
    A.add_transition(2, "a", 2)
    A.add_transition(2, "b", 1)
    A.add_transition(3, "b", 3)
    A.add_transition(3, "a", 2)
    print(A.simulate(1, "bbbbbabaaabababababbbbbaababbaaababbaaaaabaaabababaaababa", True))
