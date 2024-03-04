import search_problem
import heapq

from search import Search, SearchNode


class UniformCostSearch(Search):
  def __init__(self, search_problem, print_statistics=False):
    super().__init__(search_problem, print_statistics)
    self.name = "Uniform Cost"

  def search(self):
    frontier = [SearchNode(self.search_problem.initial_state, None, 0)]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
      node = heapq.heappop(frontier)
      

      if node.state not in explored:
        explored.add(node.state)
        self.expanded += 1
        if self.search_problem.is_goal(node.state):
          return self.extract_path(node), node.g
        for action in self.search_problem.actions(node.state):
          succ, action_cost = self.search_problem.result(node.state, action)
          child_node = SearchNode(succ, node, node.g + action_cost)
          self.generated += 1
          heapq.heappush(frontier, child_node)

    return None, None


if __name__ == "__main__":
  problem = search_problem.generate_random_problem(8, 2, 3, max_cost=10)
  problem.dump()
  ucs = UniformCostSearch(problem, True)
  ucs.run()


