"""
Author: Grant Schowalter
Date Started: 3/21/2020
Version: 0.0.1

This module is part of the JMU_Club_XC-Track_PointSystem package.

This module holds the class that is the value for the RosterPoints dictionary entries.

"""

def __init__(self, cs_points = 0, f_points = 0):
    self.cs_points = cs_points
    self.f_points = f_points

def add_f(self, points):
    self.f_points += points

def add_cs(self, points):
    self.cs_points += points


