from automaton import State


class NFAutomaton:
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

    # import states from file
    def import_states(self, filepath, separator=','):
        states_file = open(filepath, 'r')
        states_data = states_file.read().splitlines()
        states_file.close()
        for state in states_data:
            name, is_final = state.rstrip().split(separator)
            self.add_state(name, is_final)

    # return list of accepting states
    def get_accepting_states(self):
        return [name for name, state in self.states.items() if state.accepting]

    # set the initial state to an existing state of the automaton
    def set_initial(self, state):
        self.initial_state = self.states[state]

    # first_state --- edge ---> next_state
    # NOTE: first_state and next_state have to exist
    def add_transition(self, first_state, edge, next_state):
        if edge not in self.states[first_state].transitions.keys():
            self.states[first_state].transitions[edge] = [next_state]
        else:
            self.states[first_state].transitions[edge].append(next_state)

    # import transitions from file
    def import_transitions(self, filepath, separator=','):
        transitions_file = open(filepath, 'r')
        transitions_data = transitions_file.read().splitlines()
        transitions_file.close()
        for transition in transitions_data:
            first, edge, second = transition.rstrip().split(separator)
            self.add_transition(first, edge, second)

    # returns the list of next reachable states if the value of "edge" is passed to "state"
    def get_next_states(self, state, edge):
        if edge in self.states[state].transitions.keys():
            return self.states[state].transitions[edge]
        else:
            return []

    # simulate the automaton on a given word
    def simulate(self, word):
        current = self.get_next_states(self.initial_state.name, word[0])
        print(f'starting at state {self.initial_state.name}')
        for i in range(1, len(word)):
            next_states_after = [self.get_next_states(state, word[i]) for state in current]
            current = []
            for state_list in next_states_after:
                current = list(set(current).union(state_list))
        if any(state in self.get_accepting_states() for state in current):
            print("accepting")
            return True
        else:
            print("rejecting")
            return False


if __name__ == '__main__':
    N = NFAutomaton("test")
    N.add_state(1, False)
    N.set_initial(1)
    N.add_state(2, False)
    N.add_state(3, True)
    N.add_transition(1, "a", 1)
    N.add_transition(1, "a", 2)
    N.add_transition(2, "a", 2)
    N.add_transition(2, "b", 2)
    N.add_transition(2, "b", 3)
    N.add_transition(3, "a", 2)
    print(N.simulate("abaaabababababbbbbaababbaaababbaaaaabaaabababaaabab"))
