# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

# check repeated elements in a list
# return True if there are a repeated element
def repeated_elements(lista) :

  aux = []

  for i in lista :

    if i not in aux :

      aux.append(i)

  if len(aux) < len(lista) :

    return True

  return False

# check there are some repeated elements in a specific row
# return True if there are repeated elements in a row
def check_row(lista) :

  aux = []

  for i in lista :
    aux.append(repeated_elements(i)) 

  for i in aux :

    if i == True :

      return True

  return False

#convert list into columns
def convert_row(lista) :
  cons = 0
  li = 0
  aux = []
  convertida = []

  while cons < len (lista) : 

     while li < len(lista) :

        aux.append(lista[li][cons])
        li = li + 1

     li = 0
     cons = cons + 1
     convertida.append(aux)
     aux = []

  return convertida

# convert list into columns and check it like a row
# return True if there are a repeated element in a specific column
def check_column(lista) :


  print lista

  lista = convert_row(lista)
  
  if check_row(lista) == True :

    return True

  else :

    return False


#check if the element is a integer
# return True if there number is not a integer
def check_float(lista):

  for i in lista :

    for j in i :

      if type(j) != int :

        return True

  return False

#check that elements in range to the numbers 1 to the len of the list
# return True if elements are not in range to the numbers 1 to the len of the list
def check_elements(lista) :

  for i in lista :

    for j in i :

      if j not in range(1, len(lista) + 1) :

        return True

  return False

# check if a square is A valid sudoku
# return True if is valid, else no
def check_sudoku(lista):

  if check_float(lista) == True :

    return False

  if check_row(lista) == True :

    return False
  if check_column(lista) == True :

    return False

  if check_elements(lista) == True :

    return False

  return True


#print check_sudoku(correct) 
#>>> True
            
#print check_sudoku(incorrect)
#>>> False



#print check_sudoku(incorrect2)
#>>> False

#print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False