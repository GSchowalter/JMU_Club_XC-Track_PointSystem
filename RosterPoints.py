import Points
"""
Author: Grant Schowalter
Date Started: 3/21/2020
Version: 0.0.1

This module is part of the JMU_Club_XC-Track_PointSystem package

This module serves as the underlying data structure for the points system. 
The each member of the roster is entered as a string into a dict called roster.
Points object is assigned as the value for each of these enteries (See Points). 

"""
class RosterPoints:
    def __init__(self, roster = [], cs_requirement = 3, fr_requirement = 3):
        self.cs_requirement = cs_requirement
        self.fr_requirement = fr_requirement
        self.pointsOf = dict()
        for participant in roster:
            self.pointsOf[participant] = Points.Points()

    # add a specified number of points to the participant's cs total
    def add_cs_event(self, participants, event_name, points=1):
        for participant in participants:
            if participant not in self.pointsOf.keys():
                self.pointsOf[participant] = Points.Points()
            self.pointsOf[participant].add_cs(event_name, points)

    # add a specified number of points to the participant's fr total
    def add_fr_event(self, participants, event_name, points=1):
        for participant in participants:
            if self.pointsOf[participant] == None:
                self.pointsOf[participant] = Points.Points()
            self.pointsOf[participant].add_cs(event_name, points)

    def toString(self):
        str = ""
        for participant in self.pointsOf.keys():
            str += "Participant: {name}\thas {cs_points} community service and {fr_points} fundraising points\n".format(name = participant, cs_points = self.pointsOf[participant].cs_points, fr_points = self.pointsOf[participant].fr_points)
        return str

