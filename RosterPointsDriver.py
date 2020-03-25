import RosterPoints, Points

roster = ["Grant Schowalter", "Alex Connolly", "John Fritz"]
PointTracker = RosterPoints.RosterPoints(roster)
print("\n" + PointTracker.toString() + "\n" + "\n")
roster.append("Tyler Groves")
PointTracker.add_cs_event(roster, "love packs")
print(PointTracker.toString())

