"""
# forcing path implementation

import importlib.util
spec = importlib.util.spec_from_file_location("module.name", "/path/to/file.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
foo.MyClass()
"""

import os
import sys
import pathlib

this_folder = pathlib.Path(__file__).parent.resolve()
package_folder = os.path.join(this_folder, 'dev')
print("ThisFolder:", this_folder, "\nPackageFolder:", package_folder)
sys.path.append(package_folder)

from Pointer import Point
import random

limit  = 20
points = 5
points_collector = []

for i in range(points):
    x = random.randint(-(limit), limit)
    y = random.randint(-(limit), limit)
    p = Point(x,y)
    print("Point:", p, "Quad:", p.quad())
    points_collector.append(p)


pa = points_collector[0].add(points_collector[2])
print("Adding:", points_collector[0], "and", points_collector[2], "to get ", pa, "in", pa.quad(), "quadrant.")

ps = points_collector[1].add(points_collector[3])
print("Subtracting:", points_collector[3], "from", points_collector[1], "to get ", ps, "in", ps.quad(), "quadrant.")
