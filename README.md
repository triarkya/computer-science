# computer-science
just a collection of different things in computer science

# content:
Automata:

- [DFA](#dfa) (Deterministic Finite Automaton)

Data Structures:

- [BST](#bst) (Binary Search Tree)
- [Treap](#treap) (Binary Search Tree)
- [Searching Algorithms](#search_alg) (Binary Search, Bilinear Search)
- [Sorting Algorithms](#sort_alg) (Insertion Sort, Bubble Sort, Counting Sort, Heap Sort, Merge Sort)

[Network Technology](#net_tech)



# Automata

## DFA <a name="dfa"></a>
from automata.automaton import *

|Description | Method |
|------------|----------------|
|init DFA with name "test" | A = DFAutomaton("test") |
| add state 2 as final state to DFA A | A.add_state(2, is\_final=True) |
| add state 3 as nonfinal state to DFA A | A.add_state(3, is\_final=False) |
| state 1 will be the initial state of A | A.set\_initial(1) |
| add new transition from state 1 to state 2 with input "a" | A.add\_transition(1, "a", 2) |
| simulate A on word "aabaaba" (verbose mode) | A.simulate("aabaaba", verbose=True) |
| import states from file "states.csv" | A.import\_states("states.csv") |
| import transitions from file "transitions.csv" | A.import\_transitions("transitions.csv") |

As mentioned above all transitions as well as states can be imported from a file (csv-like format). The file-syntax should be similar to the input parameters of add\_state and add\_transition. The default separator is ",". If you need another separator just pass it to the respective import method as second parameter. Keep in mind that the initial state has to be set manually!


# Data Structures

## BST (Binary Search Tree) <a name="bst"></a>
In a binary search tree, the left child is a smaller node than the current node and the right child is a larger node. A node is only inserted as a child if the currently visited node does not have a right or left child. Otherwise, the respective child is set as the new current node until the respective child does not exist.

| Description | Method |
| ------------|--------|
| initialize the BST B with root 8 | B = BinarySearchTree(8)|
| insert new node 3 into B | B.insert_node(3) |
| print out B in nested parenthesis syntax | B.print_tree() |
| generate .png version of B in "images" (graphviz needed!) | B.gen\_graph\_tree() | 
| check if node 2 is in B and how many comparisons were necessary | B.search\_node(2) |
| print the previous values as a readable sentence | B.search\_node\_print(2)

![](datastructures/images/BST.png?raw=true)
    
## Treap <a name="treap"></a>
A treap is similar to a binary search tree with the difference that the nodes are inserted in ascending priority order.

    - create Treap from set af priority: key combinations
    - modify Treap by deleting/adding Treap nodes
    - print the Treap
    - image generation as .png (graphviz package needed)
![](datastructures/images/Treap.png?raw=true)
    
## Searching Algorithms <a name="search_alg"></a>
    - Binary Search
    - Bilinear Search
    
## Sorting Algorithms <a name="sort_alg"></a>
    - Insertion Sort
    - Bubble Sort
    - Counting Sort
    - Heap Sort
    - Merge Sort
    
# Network Technology <a name="net_tech"></a>

## Data Rates

    - Nyquist (frequency in Hz, modulation (64 if 64-QAM))
    - ODFM (quantity of subcarriers, modulation (64 if 64-QAM), total time interval per signal)