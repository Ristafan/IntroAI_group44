# Liam Kontopulos, Gabriel Stegmaier, Martin Fähnrich
import pancake_problem
from pancake_problem import PancakeProblem
from queue import PriorityQueue
from search import Search, SearchNode
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


class WeightedAStarSearch(Search):
  name = "weighted-astar"

  def __init__(self, search_problem, weight, **kwargs):
    super().__init__(search_problem, **kwargs)
    self.w = weight
    if weight == 0:
      self.name = "uniform-cost"
    elif weight == 1:
      self.name = "astar"

  def search(self):
    # early goal test for initial state
    p = self.search_problem
    if p.is_goal(p.initial_state):
      return [p.initial_state], 0

    # enqueue initial state
    frontier = PriorityQueue()
    frontier.put(PrioritizedItem(0, SearchNode(p.initial_state, None, 0)))
    self.generated += 1
    reached = {p.initial_state}

    while not frontier.empty():
      node = frontier.get().item
      self.expanded += 1

      for action in p.actions(node.state):
        h_cost = p.h(node.state)
        succ, cost = p.result(node.state, action)
        new_g = node.g + cost + self.w * h_cost
        succ_node = SearchNode(succ, node, new_g)

        # early goal test
        if p.is_goal(succ):
          return self.extract_path(succ_node), new_g

        # mark reached to avoid cycles
        if succ not in reached:
          reached.add(succ)

          # enqueue successor
          frontier.put(PrioritizedItem(succ_node.g, succ_node))
          self.generated += 1

        if self.generated == self.max_generations:
          print("Aborting search after generating " +
            f"{self.max_generations} states without finding a solution.")
          return None, None

    # no solution found
    print("Explored entire search problem, no solution exists.")
    return None, None

if __name__ == "__main__":
  problem = pancake_problem.generate_random_problem(5)
  problem = PancakeProblem((1, 5, 6, 2, 4, 3))
  problem.dump()
  astar = WeightedAStarSearch(problem, 1, print_statistics=True)
  astar.run()



