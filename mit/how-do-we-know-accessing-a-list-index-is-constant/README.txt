Lecture 10: Understanding Program Efficiency, Part 1.

https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-10-understanding-program-efficiency-part-1/

Support material: https://stackoverflow.com/questions/7297916/why-does-accessing-an-element-in-an-array-take-constant-time.

"constant time" really means "time that doesn't depend on the 'problem size'". For the 'problem' "get something out of a container", the 'problem size' is the size of the container.

Accessing an array element takes basically the same amount of time (this is a simplification) regardless of the container size, because a fixed set of steps is used to retrieve the element: its location in memory (this is also a simplification) is calculated, and then the value at that location in memory is retrieved.

A linked list, for example, can't do this, because each link indicates the location of the next one. To find an element you have to work through all the previous ones; on average, you'll work through half the container, so the size of the container obviously matters.