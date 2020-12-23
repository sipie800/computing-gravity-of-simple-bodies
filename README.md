# computing-gravity-of-simple-bodies
Computing gravity and gravity gradient tensor of a cuboid or a sphere.
Aim to present the simple python interface with high computing efficiency as well,which benefits gravity modeling or inversion routine.  
The kernel algothm was written in **c** to obtain highest speed,with optimizing in programming and mathe,and compiled into x64 dll with windows gcc(gcc with better compatibility than intel cpp compiler though the latter provide higher speed on intel cpu).
Python interface wrap it into simple functions.

## Usage:
put all .py and libgravity_forward.dll together.Import the python functions in your own python program(example.py here).
for more information see example.py.

