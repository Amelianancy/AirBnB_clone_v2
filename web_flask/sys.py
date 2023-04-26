import sys


import importlib

try:
    models = importlib.import_module('models')
except ImportError as e:
    print(f"Error importing 'models': {e}")
print(sys.path)
