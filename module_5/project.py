print("Activity Holiday Planner")
holiday=input("choose your holiday place:(Beach/Mountains) - ")
if holiday=="beach":
    activity=input("Do you like swimming? - (yes/no)")
    if activity=="yes":
        print("Great! Enjoy your swimming!")
    else:
        print("Relax on the beach then!!!")
else:
    activity=input("Do you like trekking? - (yes/no)")
    if activity=="yes":
        print("Great! Enjoy your trek!")
    else:
        print("No worries!Just visit some villages and enjoy nature!")