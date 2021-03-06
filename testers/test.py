#!/bin/env python3
import os


path = os.path.dirname(__file__)
import sys
sys.path.insert(0,f"{path}/..")
import dynamic_load

# Load Module from string
t = dynamic_load.dynamic_load("datetime")
print(t.datetime.now())

# Load function from string
t = dynamic_load.dynamic_load("datetime.datetime.now")
print(t())

# Execute function with no argument
y = dynamic_load.dynamic_execute("testers.funcs.func1")
print(y)

# Execute function with arguments
y = dynamic_load.dynamic_execute("testers.funcs.func2", 3)
print(y)

# Execute function with arguments
y = dynamic_load.dynamic_execute("testers.funcs.func2", x=7)
print(y)


# String
def testing(f):
  return f
import datetime
y = dynamic_load.dynamic_string(testing(dynamic_load.dynamic_load("datetime.datetime.now")))
print(y)

@dynamic_load.tail_call_optimized
def factorial(n, acc=1):
  "calculate a factorial"
  if n == 0:
    return acc
  return factorial(n-1, n*acc)

factorial(4)

@dynamic_load.tail_call_optimized
def fibo(n : int) -> int:
  if (n < 2):
    return 1
  else:
    return fibo(n-1) + fibo(n+2)