

This repository contains Python implementations of a singly linked list, a circular singly queue, and a doubly linked queue. The code demonstrates various operations such as adding elements, deleting elements, swapping nodes, and more.

## Classes and Methods

### `singly_linked_list`

- **`add_first(data)`**: Adds an element to the beginning of the list.
- **`add_last(data)`**: Adds an element to the end of the list.
- **`find_index_from_first(index)`**: Finds the value at a specific index starting from the first node.
- **`find_index_from_last(index)`**: Finds the value at a specific index starting from the last node.
- **`__add__(second)`**: Concatenates two singly linked lists.
- **`add(second)`**: Concatenates two singly linked lists without modifying the original lists.
- **`swap_index(first_index, second_index)`**: Swaps the nodes at the given indices.

### `circular_singly_queue`

- **`add(data)`**: Adds an element to the queue.
- **`delete()`**: Removes and returns the first element in the queue.
- **`retrive()`**: Returns the first element in the queue without removing it.
- **`swap(first, second)`**: Swaps the values of two nodes at the given positions.
- **`swap_nodes(first, second)`**: Swaps the positions of two nodes in the queue.
- **`nodes_belonging(first, second)`**: Checks if two nodes belong to the same circular queue.

### `doubly_linked_queue`

- **`add(data)`**: Adds an element to the end of the queue.
- **`mid_without_counter()`**: Finds the middle element of the queue without using a counter.

### `cirular_singly_stack`

- **`add(data)`**: Adds an element to the stack.
- **`delete()`**: Removes and returns the top element from the stack.
- **`retrive()`**: Returns the top element without removing it.
- **`swap(first, second)`**: Swaps the values of two nodes at the given positions.
- **`swap_nodes(first, second)`**: Swaps the positions of two nodes in the stack.

## Usage

To use the classes and methods, simply import the script and create instances of the desired classes. Here is an example:

```python
from training_2 import singly_linked_list, circular_singly_queue, doubly_linked_queue, cirular_singly_stack

# Example usage of singly_linked_list
sll = singly_linked_list()
sll.add_first(10)
sll.add_last(20)
print(sll)

# Example usage of circular_singly_queue
csq = circular_singly_queue(5)
csq.add(10)
csq.add(15)
print(csq)

# Example usage of doubly_linked_queue
dlq = doubly_linked_queue()
dlq.add(10)
dlq.add(20)
print(dlq.mid_without_counter())

# Example usage of cirular_singly_stack
css = cirular_singly_stack(5)
css.add(10)
css.add(15)
print(css)
```

## Notes

- The `singly_linked_list` class supports basic operations like adding elements, finding elements by index, and swapping nodes.
- The `circular_singly_queue` class implements a circular queue with operations like adding, deleting, and swapping nodes.
- The `doubly_linked_queue` class implements a doubly linked queue with a method to find the middle element without using a counter.
- The `cirular_singly_stack` class implements a circular stack with operations similar to the circular queue.
