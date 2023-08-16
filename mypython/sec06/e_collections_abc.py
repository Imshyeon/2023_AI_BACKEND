from functools import singledispatch
from collections.abc import Mapping

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

@fun.register
def _(arg: Mapping, verbose=False):
    if verbose:
        print("Keys & Values")
    for key, value in arg.items():
        print(key, "=>", value)     #a => b
fun({"a" : "b"})