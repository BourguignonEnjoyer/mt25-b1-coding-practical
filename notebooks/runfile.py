import sys
import os
modules = os.getcwd() + "/../uuv_mission"
sys.path = sys.path + [modules]
print(sys.path)
from terrain import *
from dynamic import *

sub = Submarine()
controller = Controller(sub)
closed_loop = ClosedLoop(sub, controller)
mission = Mission.from_csv("../data/mission.csv")
trajectory = closed_loop.simulate_with_random_disturbances(mission)
trajectory.plot_completed_mission(mission)
