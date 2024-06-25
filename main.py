import math
import numpy as np
# Freddie ;)
def CsvToArray():
  sigmalabels = []
  data = []
  with open("train.csv", "r") as file:
    training_data = file.reader(file)
    for row in data:
      sigmalabels.append(row[0])
      data.append(row[1:])
  return sigmalabels, data
      

# JOsh
def InitialiseParams():
  pass

# TEmi
def RELU():
  pass

# TEmI
def SoftMax(weightsum):
  e_weightsum = np.exp(weightsum - n)
  return e_weightsum /
    
  pass

# Ollie
def SigmaWeight(fredinfoalpha, fredinfolots):
  fredtemp = 0
  fredfinal = []
  fredconstant1 = 0
  for fred in range(0, 9):
    for fred2 in range(0, 783):
      for fred3 in range(0, 783):
        fredtemp = fredtemp + fredinfoalpha[fred2]*fredinfolots[fred][fred3]
      fredconstant1 = fredconstant1 + fredtemp
      fredtemp = 0
    fredfinal.append(fredconstant1)
    fredconstant1 = 0
  return fredfinal
  
  
  
def ForwardPropagation():
  pass

def Train():
  pass
