# Task 2

A program is needed to calculate the numbers on each level of a number tree.

The bottom row of the number tree has the numbers 1 to x.

The row above has the result of the addition of the two numbers directly below it. This repeats in pairs until there is only one number left at the top of the number tree. This creates the number tree.

### Example 1:
This number tree has 2 levels. The first level has the numbers 1 to 2.  
The next level adds together these numbers to give 3. There is only 1 number on this level, so the number tree is complete.

<pre>
  3
 / \
1   2
</pre>


### Example 2:
This number tree has 3 levels. The first level has the numbers 1 to 4.  
The second level adds together these numbers in pairs to give 1 + 2 = 3 and 3 + 4 = 7.  
The third level adds together the pair on the second level, 3 + 7 = 10.  
There is now only one number at this level, so the number tree is complete.

<pre>
    10
   /  \
  3    7
 / \  / \
1   2 3  4
</pre>


The number of levels is input into the program.  
The program will need to generate and output the number tree for the given number of levels.

The program uses object-oriented programming. Each number in the number tree is a node. The nodes are stored in a list. Each node has the integer number (for example, 1), the index of the left node below it, and the index of the right node below it.

The program needs to use local variables throughout.

The class `Node` contains three attributes:
- `data_value` the node's integer data, initialised to -1
- `left_node` the index of the number below it to the left, initialised to -1
- `right_node` the index of the number below it to the right, initialised to -1

`-1` represents no data present in `data_value`.

`-1` represents a null value in a pointer.

The class `Node` has the following methods:
- a constructor that initialises the three attributes
- `set_data()` that assigns a value to `data_value`
- `set_left()` that assigns a value to `left_node`
- `set_right()` that assigns a value to `right_node`
- `get_data()` that returns `data_value`
- `get_left()` that returns `left_node`
- `get_right()` that returns `right_node`

For each of the sub-tasks, add a comment statement at the beginning of the code, using the hash symbol `#`, to indicate the sub-task the program code belongs to, for example:

<pre>
# Task 2.1
Program code
</pre>

## Task 2.1

Write program code to declare the class `Node`, its constructor, and its methods.

[4]

---

## Task 2.2

This table shows the total number of nodes for number trees with levels 1 to 5.

| Number of levels | Total number of nodes |
|------------------|-----------------------|
| 1                | 1                     |
| 2                | 3                     |
| 3                | 7                     |
| 4                | 15                    |
| 5                | 31                    |

Write the function `calculate_nodes()` that takes the number of levels as a parameter. It calculates, outputs, and returns the number of nodes for that number tree.

The output must be in an appropriate message, for example:

`A 3 level number tree has 7 nodes`


You do not need to validate the parameter. The function must calculate the number of nodes for any number of levels greater than 0.

[3]

---

## Task 2.3

Test your program four times with the following levels:
- 1
- 3
- 5
- 10

Show the output for each test.

[2]

---

## Task 2.4

The function `create_empty_tree()` takes 2 parameters: the list of nodes and the number of levels.

The function creates a list of `Node` objects in their initial state with all attributes set to `-1`. The function returns the list.

The list is zero-indexed.

Write the function `create_empty_tree()`.

[3]

---

## Task 2.5

The function `assign_leaf_nodes()` sets the data for the lowest level of nodes. The function takes 2 parameters: the list of nodes and the number of levels.

Each leaf node in the first layer is assigned a number starting with 1 in the left-most node and then incrementing by 1 for each subsequent node.

For example, the first level of nodes in this number tree contains the data 1, 2, 3, 4.

<pre>
      10
    /    \
   3      7
  / \    / \
 1   2  3   4
</pre>


This table shows the number of leaf nodes for up to 5 levels in a number tree. The function must calculate the number of leaf nodes for any number of levels greater than 0.

| Number of levels | Number of leaf nodes |
|------------------|----------------------|
| 1                | 1                    |
| 2                | 2                    |
| 3                | 4                    |
| 4                | 8                    |
| 5                | 16                   |

For example, if the list of nodes is named `nodes`, then `assign_leaf_nodes(nodes, 3)` would return a list of 7 `Node` objects with the following attributes:

```plaintext
Index 0: data_value: 1, left_node: -1, right_node: -1
Index 1: data_value: 2, left_node: -1, right_node: -1
Index 2: data_value: 3, left_node: -1, right_node: -1
Index 3: data_value: 4, left_node: -1, right_node: -1
Index 4: data_value: -1, left_node: -1, right_node: -1
Index 5: data_value: -1, left_node: -1, right_node: -1
Index 6: data_value: -1, left_node: -1, right_node: -1
```

Write the function `assign_leaf_nodes()`.

[3]


---

## Task 2.6

The data for each parent node in the number tree is calculated by adding the data from its two lower nodes.

The function `create_number_tree()`:
- takes 2 parameters: the list of nodes (with the first level of nodes already assigned their data) and the number of levels
- calculates the data for each node in each level in the number tree
- stores the data in each node
- assigns the left pointer of each node to its left lower node
- assigns the right pointer of each node to its right lower node.

For example, if the list of nodes is named `nodes`, then `create_number_tree(nodes, 3)` would return a list of 7 `Node` objects with the following attributes:

```plaintext
Index 0: data_value: 1, left_node: -1, right_node: -1
Index 1: data_value: 2, left_node: -1, right_node: -1
Index 2: data_value: 3, left_node: -1, right_node: -1
Index 3: data_value: 4, left_node: -1, right_node: -1
Index 4: data_value: 3, left_node: 0, right_node: 1
Index 5: data_value: 7, left_node: 2, right_node: 3
Index 6: data_value: 10, left_node: 4, right_node: 5
```
Write the function `create_number_tree()`.

[4]

---

## Task 2.7

Amend the program to call the functions `calculate_nodes()`, `create_empty_tree()`, `assign_leaf_nodes()`, and `create_number_tree()`.

Output the content of each node in the array in the format:

<pre>
left pointer      data       right pointer
</pre>
[3]

Test your program with levels 1, 3, and 5 and show the output for each test.

[2]

Save your Jupyter Notebook for Task 2.
