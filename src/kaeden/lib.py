from importlib import import_module

from kaeden.util import patch_all_functions


def foo(x):
    return x * 2


def bar(x):
    return [x]


patch_all_functions(import_module(__name__))
