from numpy import array, linspace
from itertools import chain

def get_probability_vectors(dimension, probability_range):
  def convexify(*args):
    vector = [el for el in args]
    return tuple(vector + [1 - sum(vector)])
  
  vector = [[p] for p in probability_range]
  for n in range(dimension - 2):
    vector = [el + [p] for el in vector for p in probability_range]
  vector = [el for el in vector if sum(el) <= 1.0]
  return [convexify(*el) for el in vector]

def multiply_probability_vectors(vector_1, vector_2):
  return [v1*v2 for v1 in vector_1 for v2 in vector_2]

def solve_msne_2(payoff_matrix_p1, payoff_matrix_p2, granularity=5):
  # Construct list of probability values
  probability_range = linspace(0.0, 1.0, granularity).tolist()
  # Construct probability vectors for each bidder
  vector_p1 = get_probability_vectors(len(payoff_matrix_p1), probability_range)
  vector_p2 = get_probability_vectors(len(payoff_matrix_p1[0]), probability_range)
  # Construct utility vectors for each bidder
  probability_vectors = [multiply_probability_vectors(v1, v2) for v1 in vector_p1 for v2 in vector_p2]
  print(probability_vectors)
  # Other...
  # probability_vectors = {(p,q): [p*q, p*(1-q), (1-p)*q, (1-p)*(1-q)] for p in probability_range for q in probability_range}
  # payoff_vector_1 = list(chain.from_iterable(payoff_matrix_p1))
  # payoff_vector_2 = list(chain.from_iterable(payoff_matrix_p2))
  # utilities_1 = {pair: sum(list(map(lambda x, y: x*y, probability_vectors[pair], payoff_vector_1))) for pair in probability_vectors}
  # utilities_2 = {pair: sum(list(map(lambda x, y: x*y, probability_vectors[pair], payoff_vector_2))) for pair in probability_vectors}
  # # print(utilities_1)
  # # print(utilities_2)
  # matched = list(map(lambda x, y: (x[0], abs(x[1] - y[1])), sorted(utilities_1.items()), sorted(utilities_2.items())))
  # minimum = min(matched, key=lambda x: x[1])
  # print(sorted([x for x in matched if x[1] == minimum[1]], key=lambda x: x[0]))
  return None

def test(condition):
  try:
    assert condition
  except AssertionError as e:
    print("Test failed")
  else:
    print("Test successful")

if __name__ == '__main__':
  ### Test get_probability_vectors(...)
  # Create probability range
  probability_range = linspace(.0, 1.0, 5).tolist()
  # Test output
  # Dimension of 2
  vector = set(get_probability_vectors(2, probability_range))
  other = set(((.0, 1.0), (.25, .75), (.5, .5), (.75, .25), (1.0, .0)))
  test(other == vector)
  # Should test higher dimensions as well...
  ### Test scenario1: Matching pennies
  # Create payoff matrices for two players
  p_matrix_p1 = [[-1, 1], [1, -1]]
  p_matrix_p2 = [[1, -1], [-1, 1]]
  # Solve for MSNE
  msne = solve_msne_2(p_matrix_p1, p_matrix_p2)
  ### Test scenario2: Example 4.16 from Carter's book
  # Create payoff matrices for two players
  p_matrix_p1 = [[1, 4, 2], [4, 0, 4]]#, [2, 3, 5]]
  p_matrix_p2 = [[3, 2, 2], [0, 3, 1]]#, [5, 4, 6]]
  # Solve for MSNE
  msne = solve_msne_2(p_matrix_p1, p_matrix_p2)
