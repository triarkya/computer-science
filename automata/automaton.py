class State:
    def __init__(self, name="q0", accepting=False):
        self.name = name
        self.accepting = accepting
        self.transitions = {}
