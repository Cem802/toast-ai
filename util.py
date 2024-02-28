import heapq

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
class HNode():
    def __init__(self, state, parent, action, cost=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost if cost is not None else 0

    def __lt__(self, other):
        return self.cost < other.cost


class QueueFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class StackFrontier(QueueFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class HeapFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, cost, node):
        heapq.heappush(self.frontier, (cost, node))

    def contains_state(self, state):
        return any(node.state == state for _, node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            _, node = heapq.heappop(self.frontier)
            return node