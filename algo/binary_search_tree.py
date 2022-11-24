""""Binary search tree implementation."""

from __future__ import annotations

from typing import Generator
from dataclasses import dataclass

from binary_tree import BinaryTreeNode, TraversalMethod


@dataclass
class BinarySearchTreeNode(BinaryTreeNode):
    """Binary Search Tree Node."""

    value: int | None = None
    left: BinarySearchTreeNode | None = None
    right: BinarySearchTreeNode | None = None

    def add(self, value: int) -> None:
        """Add new element to the tree."""
        if self.value is None:
            self.value = value
            return

        if value == self.value:
            return

        if value < self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinarySearchTreeNode(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinarySearchTreeNode(value)

    def __iter__(self) -> Generator[int, None, None]:
        """Generate values in acsending order."""
        return self.traverse(TraversalMethod.IN_ORDER)

    def __reversed__(self) -> Generator[int, None, None]:
        """Generate values in decsending order."""
        return self.traverse(TraversalMethod.IN_ORDER, reverse=True)

    def __contains__(self, value: int) -> bool:
        """Check if tree contains value."""
        if self.value == value:
            return True

        if value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def __str__(self) -> str:
        return str([i for i in self])

    def min(self) -> int:
        if self.left:
            return self.left.min()
        return self.value

    def max(self) -> int:
        if self.right:
            return self.right.max()
        return self.value

    # def delete(self, value: int) -> None:
    #     if value < self.value:
    #         if self.left:
    #             self.left = self.left.delete(value)
    #     elif value > self.value:
    #         if self.right:
    #             self.right = self.right.delete(value)
    #     else:
    #         # no children
    #         if self.left is None and self.right is None:  # leaf node
    #             return None

    #         # have only right child
    #         if self.left is None:
    #             return self.right

    #         # have only left child
    #         if self.right is None:
    #             return self.right

    #         # have both children
    #         min_value = self.right.min()
    #         self.value = min_value
    #         self.right = self.right.delete(min_value)

    #     return self


def make_tree(x: list) -> BinarySearchTreeNode:
    root = BinarySearchTreeNode()

    for i in x:
        root.add(i)

    return root


def main():
    root = make_tree([5, 4, 6, 1, 3, -88, -90])
    print(root)


if __name__ == "__main__":
    main()
