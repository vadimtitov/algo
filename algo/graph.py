"""Graph implementation."""

import enum
import queue
from typing import Union, Dict, Set, Generator, List, Optional

NodeVal = Union[int, float, str]


class TraverseMethod(enum.Enum):
    """Traverse method enum."""

    BFS = enum.auto()
    DFS = enum.auto()


class Graph:
    """Adjacency dict graph."""

    _nodes: Dict[NodeVal, Set[NodeVal]] = {}

    def __init__(self, directed: bool = False) -> None:
        """Init."""
        self._directed = directed

    def __len__(self) -> int:
        """Get number of nodes."""
        return len(self._nodes)

    def __contains__(self, node: NodeVal) -> bool:
        """Check if node is in graph."""
        return node in self._nodes

    def __repr__(self) -> str:
        """Get graph string representation."""
        return (
            "\n".join(
                f"{k.rjust(15)}: {', '.join(i for i in v)}"
                for k, v in self._nodes.items()
            )
            + f"\nSize: {len(self)}"
        )

    def __str__(self) -> str:
        """Get graph string representation."""
        return self.__repr__()

    @property
    def directed(self) -> bool:
        """Indicate if graph is directed."""
        return self._directed

    def neighbours(self, node: NodeVal) -> Set[NodeVal]:
        """Get neighbours of a given node."""
        return self._nodes[node]

    def add_node(self, node: NodeVal) -> None:
        """Add node to graph."""
        if not node in self:
            self._nodes[node] = set()

    def add_neighbour(self, node: NodeVal, neighbour: NodeVal) -> None:
        """Add node if does not exists and neighbour to that node."""
        self.add_node(node)
        neighbours = self.neighbours(node)

        if neighbour in neighbours:
            return

        neighbours.add(neighbour)

        if self.directed:
            self.add_node(neighbour)
        else:
            self.add_neighbour(neighbour, node)

    def traverse(
        self, node: NodeVal, method: TraverseMethod
    ) -> Generator[NodeVal, None, None]:
        """Traverse graph nodes using given method."""
        if method is TraverseMethod.BFS:
            container = queue.Queue()
        elif method is TraverseMethod.DFS:
            container = queue.LifoQueue()
        else:
            raise ValueError("Invalid traverse method")

        discovered: Set[NodeVal] = set()
        container.put(node)

        while not container.empty():
            value = container.get()
            if value not in discovered:
                yield value
                discovered.add(value)
                for neighbour in self.neighbours(value):
                    container.put(neighbour)


def main():
    g = Graph(directed=True)

    adj_list = (
        ("Stratford", ("Bank", "Kings Cross")),
        ("Manor House", ("Kings Cross",)),
        ("Kings Cross", ("Bank", "Baker Street")),
    )

    for node, neighbours in adj_list:
        for neighbour in neighbours:
            g.add_neighbour(node, neighbour)

    print(g)

    print("\nBFS:")
    for i in g.traverse("Baker Street", TraverseMethod.BFS):
        print(i)

    print("\nDFS:")
    for i in g.traverse("Stratford", TraverseMethod.DFS):
        print(i)

    print("Stratford" in g)


if __name__ == "__main__":
    main()
