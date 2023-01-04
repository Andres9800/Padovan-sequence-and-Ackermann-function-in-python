# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:21:05 2022

@author: adsc9
"""

print("------#Ejercicio 1.1 ------")
def A ( n, m ) :
  if (m == 0): 
    return (0)
  if (n == 0): 
    return (2 * m)
  if (m == 1):
    return (2)
  else:
    return (A (n-1, A(n , m - 1)))

print("------#Ejercicio 1.2 ------")

def Pad ( n ) :
  if (n < 3):
    return (1)
  else:
      return (Pad (n - 2) + Pad (n - 3) )

def Padpr ( i, n ) :
  if (i < n):
    print(Pad (i)) 
    Padpr (i+1, n)    
  
def Padprf ( n ) :
  Padpr(0, n) 
  
def Plinealiter ( tras, ant, result, i , n ):
  if (i >= n):
    return (tras)
  return (Plinealiter (ant, result, (ant+tras), (i+1), n) )

def PadLin ( n ) :
    return (Plinealiter (1, 1, 1, 0, n)) 
  
def PadLinR ( i, n ):
  if (i < n):
    print(PadLin (i)) 
    PadLinR (i+1, n)    
  
def PadLinF ( n ) :
  PadLinR (0, n)
  
