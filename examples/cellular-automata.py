from random import randint

class Automata:
  def __init__(self, children, generations):
      self.parent_cells_length =  children
      self.generations = generations

  # Return a random binary
  def __random_binary(self):
      return randint(0,1)

  # Wolfram's Rule 110
  def __rule_110(self, current, left, right):
      if(left == 1 and current == 1 and right == 1):
          return 0
      elif(left == 1 and current == 1 and right == 0):
          return 1
      elif(left == 1 and current == 0 and right == 1):
          return 1
      elif(left == 1 and current == 0 and right == 0):
          return 0
      elif(left == 0 and current == 1 and right == 1):
          return 1
      elif(left == 0 and current == 1 and right == 0):
          return 1
      elif(left == 0 and current == 0 and right == 1):
          return 1
      elif(left == 0 and current == 0 and right == 0):
          return 0
      else:
          return current

  # Rule switcher
  def __apply_rule(self, current, left, right, rule):

      if rule == "110":
          return self.__rule_110(current, left, right)
      else:
          return current

  def __next_generation(self, old_generation, rule):
      new_generation = []

      for x in range(0, len(old_generation)):
          left_neighbor = old_generation[x - 1]

          if(x < (len(old_generation) -1 )):
              right_neighbor = old_generation[x + 1]
          else:
              right_neighbor = old_generation[x]

          new_generation.append(self.__apply_rule(old_generation[x], left_neighbor, right_neighbor, rule))

      return new_generation

  # Return the final array of generations
  def calc(self, rule):
      self.parent_cells = []
      self.cells = []
      self.final_cells = []

      for x in range(0, self.parent_cells_length):
          self.parent_cells.append(self.__random_binary())

      for y in range(0, self.generations):
          self.cells = self.__next_generation(self.parent_cells, rule)
          self.final_cells.append(self.cells)
          self.parent_cells = self.cells

      return self.final_cells

  #Print line in a beautiful way
  def print_line(self, lines):
      for x in lines:
          line = ""
          for y in x:
              if y == 1:
                  line += " # "
              else:
                  line += "   "

          print(line)

automata = Automata(71, 300)
automata_result = automata.calc("110")
automata.print_line(automata_result)