""" Init for findoutlie module
"""
__version__ = '0.1a0'

from .outfind import find_outliers
from .detectors import iqr_detector, z_score_detector, dvars, dvars_detector