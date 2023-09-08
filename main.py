#Made by: Manav Bharath and Teja Koduru
#11/17/2020
import numpy as np
"""Makes the equation of a polynomial p given a set of points.
"""
def polySolver(matrix): #Initializes all matrices, and creates variable matrix
  highDeg = len(matrix)-1
  #Initialization of matrices
  xMatrix = []
  yMatrix = []
  coefMatrix = []
  resultsMatrix=[]
  #Loading matrices with values
  loadMatrices(matrix, xMatrix, yMatrix, resultsMatrix)
  fillCoefMatrix(coefMatrix, xMatrix, highDeg)
  #Converting matrices to numpy matrices to find variable matrix
  A = np.matrix(coefMatrix)
  B = np.matrix(resultsMatrix)
  #Gives error if matrix is singular
  if np.linalg.det(A) == 0:
    print("ERROR! Matrix is singular. Enter another set of points.")
    return
  #Makes final equation using variable matrix
  A_inv = np.linalg.inv(A)
  varMatrix = A_inv * B
  equationMaker(varMatrix, highDeg)

def loadMatrices(matrix, xMatrix, yMatrix, resultsMatrix):
  #Splits up matrix of points to create a matrix of x variables and a matrix of y variables
  for subset in matrix:
    xVar = subset[0]
    yVar = subset[1]
    xMatrix.append(xVar)
    yMatrix.append(yVar)
  #Turns the y matrix into a results matrix, which is a 2d array
  for y in range(0, len(yMatrix)):
    newList = [] #Necessary because each y variable should be contained in its own list to form the proper size array
    newList.append(yMatrix[y])
    resultsMatrix.append(newList)

def fillCoefMatrix(coefMatrix, xMatrix, highDeg): 
  #Turns each x variable into a list of coefficients, where each x variable is raised to the power of each degree. Adds each list into a matrix of coefficients
  for x in xMatrix:
    equatList=[]
    for deg in range(highDeg, -1, -1):
      equatList.append(x**deg)
    coefMatrix.append(equatList)

def equationMaker(varMatrix, highDeg): #Uses variable matrix to form the equation
  equatString = ""
  for deg in range(highDeg, -1, -1): #Goes through each degree from highest to 0
    coef = round(varMatrix.item(highDeg-deg), 3) #Selects a coefficient and rounds it to 2 places
    varStr = ""
    """
    Rules for coefficients stated through if statements:
    1: If coefficient is 0, don't bother writing it (not having 0x for exp.)
    2: If the coefficient is 1, but the degree is not 0, don't write the coefficient (not having the 1 in 1x, for exp.)
    3: If degree is not the highest degree and the coefficient is positive, add a + sign in front of it and turn the coefficient into a string (+2.5 for exp.)
    4: If the degree is negative or the degree is the highest, turn the coefficient into a string.  
    """
    if coef != 0: 
      if coef!=1 or deg == 0:
        if deg!=highDeg and coef > 0:
          varStr = f"+{coef}"
        else:
          varStr = str(coef)
      # If the degree is greater than 1, then follow the coefficient with the string "x^degree". Else, if the degree is 1, just print the coefficient followed by "x". Finally, if the degree is 0, just make the coefficient what you print out. 
      if deg > 1:
        equatString += f"{varStr}x^{deg} "
      elif deg == 1:
        equatString += f"{varStr}x "
      else:
        equatString += varStr
  print(equatString)
#Input your points here (The ones below are examples, feel free to remove them.)
polySolver([[1, 3/2], [-2, -39], [1/2, -11/4], [-1, -25/2]])
polySolver([[2, 8], [-1/2, 3], [5/6, 3/4]])
polySolver([[10, 23], [51, 16], [44, 22], [15.5, 17.25]])
