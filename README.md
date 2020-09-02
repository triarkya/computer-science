# computer-science
just a collection of different things in computer science

# Automata

## DFA
from automata.automaton import *

|Description | Method |
|------------|----------------|
|init DFA with name "test" | A = DFAutomaton("test") |
| add state 2 as final state to DFA A | A.add_state(2, is\_final=True) |
| add state 3 as nonfinal state to DFA A | A.add_state(3, is\_final=False) |
| state 1 will be the initial state of A | A.set\_initial(1) |
| add new transition from state 1 to state 2 with input "a" | A.add\_transition(1, "a", 2) |
| simulate A on word "aabaaba" (verbose mode) | A.simulate("aabaaba", verbose=True) |


# Data Structures 

## BST (Binary Search Tree)
In a binary search tree, the left child is a smaller node than the current node and the right child is a larger node. A node is only inserted as a child if the currently visited node does not have a right or left child. Otherwise, the respective child is set as the new current node until the respective child does not exist.

    - create BST by passing each node in the intended order
    - print the BST
    - image generation as .png (graphviz package needed)
![](datastructures/images/BST.png?raw=true)
    
## Treap
A treap is similar to a binary search tree with the difference that the nodes are inserted in ascending priority order.

    - create Treap from set af priority: key combinations
    - modify Treap by deleting/adding Treap nodes
    - print the Treap
    - image generation as .png (graphviz package needed)
![](datastructures/images/Treap.png?raw=true)
    
## Searching Algorithms
    - Binary Search
    - Bilinear Search
    
## Sorting Algorithms
    - Insertion Sort
    - Bubble Sort
    - Counting Sort
    - Heap Sort
    - Merge Sort
    
# Network Technology

## Data Rates

    - Nyquist (frequency in Hz, modulation (64 if 64-QAM))
    - ODFM (quantity of subcarriers, modulation (64 if 64-QAM), total time interval per signal)