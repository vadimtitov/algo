"""Binary tree implementation."""

from __future__ import annotations

import enum
from typing import Generator, Union
from dataclasses import dataclass

NodeVal = Union[int, float]
NodeValGen = Generator[NodeVal, None, None]


class TraversalMethod(enum.Enum):
    """Binary tree traversal nethods."""

    PRE_ORDER = enum.auto()
    IN_ORDER = enum.auto()
    POST_ORDER = enum.auto()


@dataclass
class BinaryTreeNode:
    """Binary Search Tree Node."""

    value: NodeVal | None = None
    left: BinaryTreeNode | None = None
    right: BinaryTreeNode | None = None

    def add(self, value: NodeVal) -> None:
        """Add value to this tree."""
        raise NotImplementedError

    def traverse(self, method: TraversalMethod, reverse: bool = False) -> NodeValGen:
        methods = {
            (TraversalMethod.PRE_ORDER, False): self._traverse_pre_order,
            (TraversalMethod.IN_ORDER, False): self._traverse_in_order,
            (TraversalMethod.POST_ORDER, False): self._traverse_post_order,
            (TraversalMethod.PRE_ORDER, True): self._r_traverse_pre_order,
            (TraversalMethod.IN_ORDER, True): self._r_traverse_in_order,
            (TraversalMethod.POST_ORDER, True): self._r_traverse_post_order,
        }
        return methods[(method, reverse)]()

    # PRE ORDER
    def _traverse_pre_order(self) -> NodeValGen:
        yield self.value

        if self.left:
            for value in self.left._traverse_pre_order():
                yield value

        if self.right:
            for value in self.right._traverse_pre_order():
                yield value

    def _r_traverse_pre_order(self, method: TraversalMethod) -> NodeValGen:
        yield self.value

        if self.right:
            for value in self.right._r_traverse_pre_order():
                yield value

        if self.left:
            for value in self.left._r_traverse_pre_order():
                yield value

    # IN ORDER
    def _traverse_in_order(self) -> NodeValGen:
        if self.left:
            for value in self.left._traverse_in_order():
                yield value

        yield self.value

        if self.right:
            for value in self.right._traverse_in_order():
                yield value

    def _r_traverse_in_order(self, method: TraversalMethod) -> NodeValGen:
        if self.right:
            for value in self.right._r_traverse_in_order():
                yield value

        yield self.value

        if self.left:
            for value in self.left._r_traverse_in_order():
                yield value

    # POST ORDER
    def _traverse_post_order(self) -> NodeValGen:
        if self.left:
            for value in self.left._traverse_post_order():
                yield value

        if self.right:
            for value in self.right._traverse_post_order():
                yield value

        yield self.value

    def _r_traverse_post_order(self, method: TraversalMethod) -> NodeValGen:
        if self.right:
            for value in self.right._r_traverse_post_order():
                yield value

        if self.left:
            for value in self.left._r_traverse_post_order():
                yield value

        yield self.value
