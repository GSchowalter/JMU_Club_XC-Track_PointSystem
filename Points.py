"""
Author: Grant Schowalter

Date Started: 3/21/2020
Version: 0.0.1

This module is part of the JMU_Club_XC-Track_PointSystem package.

This module holds the class that is the value for the RosterPoints dictionary entries.

"""
class Points:
    def __init__(self):
        self.cs_points = 0
        self.fr_points = 0
        self.events = []

    def add_fr(self, name, points):
        self.fr_points += points
        self.events += name

    def add_cs(self, name, points):
        self.cs_points += points
        self.events += name


