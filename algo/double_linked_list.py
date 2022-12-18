"""Double linked list implementation."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    """Double linked list node."""

    value: Any
    prev: Node | None = None
    next: Node | None = None

    def delete(self) -> None:
        """Delete this node from list."""
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoubleLinkedList:
    """Double linked list."""

    def __init__(self, *args: Any) -> None:
        """Initialize DL list"""
        self._head = None
        self._tail = None
        self._size = 0

        for e in args:
            self.push(e)

    @property
    def head(self) -> Node | None:
        """Get head node of list."""
        return self._head
    
    @property
    def tail(self) -> Node | None:
        """Get tail node of list."""
        return self._tail

    def __len__(self) -> int:
        """Get length of list."""
        return self._size

    def empty(self) -> bool:
        """Check if list is empty."""
        return self._size == 0

    def push(self, value: Any) -> Node:
        """Push value to the end of the list."""
        node = Node(value)

        if self.empty():
            self._head = node            
        else:
            self._tail.next = node
            node.prev = self._tail

        self._tail = node
        self._size += 1
        return node

    def lpush(self, value: Any) -> Node:
        """Push value to the start of the list."""
        node = Node(value)

        if self.empty():
            self._tail = node    
        else:
            self._head.prev = node
            node.next = self._head

        self._head = node
        self._size += 1
        return node

    def pop(self) -> Any:
        """Pop value from the end of the list."""
        if self.empty():
            return None

        value = self._tail.value

        self._tail = self._tail.prev
        if self._tail:
            self._tail.next = None
        else:
            self._head = None

        self._size -= 1
        return value

    def lpop(self) -> Any:
        """Pop value from the start of the list."""
        if self.empty():
            return None

        value = self._head.value
        self._head = self._head.next
        
        if self._head:
            self._head.prev = None
        else:
            self._tail = None

        self._size -= 1
        return value

    def __iter__(self) -> Generator[Any, None, None]:
        """Generate list values."""
        current = self._head
        while current:
            yield current.value
            current = current.next

    def __reversed__(self) -> Generator[Any, None, None]:
        """Generate list value in reverse order."""
        current = self._tail
        while current:
            yield current.value
            current = current.prev

    def __repr__(self) -> str:
        """Get list representation."""
        return "[" + ", ".join(str(i) for i in self) + "]"

    def __str__(self) -> str:
        """Get list string form."""
        return self.__repr__()


def main():
    x = DoubleLinkedList(1,2,3)
    print(x, "size ", len(x), x.head, x.tail); x.pop()
    print(x, "size ", len(x), x.head, x.tail); x.pop()
    print(x, "size ", len(x), x.head, x.tail); x.pop()
    print(x, "size ", len(x), x.head, x.tail)
    print(x.pop())


if __name__ == "__main__":
    main()
