"""
Modify the system path so pytest finds the train_model.py module.
"""
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent))
