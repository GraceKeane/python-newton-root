#! /usr/bin/env python3

# Grace Keane
# Calculating the square root of a number

def sqrt(x):
  """
  Calculate the square root of argument x.
  """

  # Check that x is positive
  if x < 0:
    print("Error: negative value supplied")
    return -1
  else:
    print("Here we go again...")

  # Initial guess for the square root.
  z = x / 2.0

  # Continuously improve the guess.
  # Adapted from https://tour.golang.org/flowcontrol/8
  while abs(x - (z*z)) > 0.0000001:
    z = z - (((z * z) - x) / (2 * z))
  
  return z

myVal = 63.0
print("The square root of", myVal, "is",  sqrt(myVal))











