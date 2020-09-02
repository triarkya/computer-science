class State:
    def __init__(self, name="q0", accepting=False):
        self.name = name
        self.accepting = accepting
        self.transitions = {}


class DFAutomaton:
    def __init__(self, name):
        self.name = name
        self.states = {}
        self.initial_state = State()

    # add new (non)final state to automaton without transitions
    def add_state(self, label, is_final):
        self.states[label] = State(
            name=label,
            accepting=is_final
        )

    # set the initial state to an existing state of the automaton
    def set_initial(self, state):
        self.initial_state = self.states[state]

    # first_state --- edge ---> next_state
    # NOTE: first_state and next_state have to exist
    def add_transition(self, first_state, edge, next_state):
        self.states[first_state].transitions[edge] = next_state

    # returns the next state if the value of "edge" is passed to "state"
    def get_next_state(self, state, edge):
        return self.states[state.transitions[edge]]

    # simulate the automaton on a given word
    def simulate(self, word, verbose=False):
        next_state = self.get_next_state(self.initial_state, word[0])
        run_output = ''
        if verbose:
            run_output = f'[{self.initial_state.name}]---{word[0]}-->[{next_state.name}]---'
        for i in range(1, len(word)):
            next_state = self.get_next_state(next_state, word[i])
            if verbose:
                run_output += f'{word[i]}-->[{next_state.name}]---'
        if verbose:
            if next_state.accepting:
                run_output += '>ACCEPT'
                print(f"accepting at state {next_state.name}")
            else:
                print(f"rejecting at state {next_state.name}")
                run_output += '>REJECT'
            print(run_output)
        return next_state.accepting


if __name__ == '__main__':
    A = DFAutomaton("test")
    A.add_state(1, False)
    A.set_initial(1)
    A.add_state(2, False)
    A.add_state(3, True)
    A.add_transition(1, "a", 3)
    A.add_transition(1, "b", 1)
    A.add_transition(2, "a", 2)
    A.add_transition(2, "b", 1)
    A.add_transition(3, "b", 3)
    A.add_transition(3, "a", 2)
    print(A.simulate("bbbbbabaaabababababbbbbaababbaaababbaaaaabaaabababaaababa", True))
