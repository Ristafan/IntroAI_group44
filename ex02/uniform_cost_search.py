import search_problem

from search import Search, SearchNode


class UniformCostSearch(Search):
  name = "uniform-cost"

  def search(self):
    raise NotImplementedError


if __name__ == "__main__":
  problem = search_problem.generate_random_problem(8, 2, 3, max_cost=10)
  problem.dump()
  ucs = UniformCostSearch(problem, True)
  ucs.run()


