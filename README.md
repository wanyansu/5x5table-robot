## Robot Challenge

#### Description

This application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units.

There are no other obstructions on the table surface.

The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.

Commands are in the following form:

```
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
```

Where PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0) can be considered to be the SOUTH WEST most corner.

It is required that the first command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed.

Where MOVE will move the toy robot one unit forward in the direction it is currently facing.

Where LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.

Where REPORT will announce the X,Y and facing of the robot. This can be in any form, but standard output is sufficient.

A robot that is not on the table can choose the ignore the MOVE, LEFT, RIGHT and REPORT commands.

#### Expected Outcomes

a)

```
PLACE 0,0,NORTH
MOVE
REPORT

Output: 0,1,NORTH
```

b)

```
PLACE 0,0,NORTH
LEFT
REPORT

Output: 0,0,WEST
```

c)

```
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT

Output: 3,3,NORTH
```

_Refer to the **main.py** file for the code to solve the problem._

_Refer to the **answer.txt** file for the printed outputs from the program._

#### Testings

a) Test if the robot will move out of the 5 x 5 tabletop:

```
PLACE 4,5,EAST
MOVE
MOVE
LEFT
MOVE
REPORT

Output: 5,5,NORTH
```

b) Test if the robot can be placed outside of the tabletop:

```
PLACE 5,6,SOUTH
MOVE

Output: Your robot is not on the tabletop.
```

c) Test error handling:

```
ASD

Output: Invalid command. You need to initiate a starting position first.

PLACE 1,2,3

Output: Your input of facing directions is not valid
Invalid command. You need to initiate a starting position first.

PLACE 1,2,EAST
LEFT
MOVE
ACTION

Output: Invalid

REPORT

Output: 1,3,NORTH
```

#### Extension

Multiple robots will operate on the table

The existing system above should continue to work as-is. REPORT will also now report on how many robots are present and which robot is active (see the ROBOT command later).

PLACE will add a new robot to the table with incrementing number identifier, i.e. the first placed robot will be 'Robot 1', then the next placed robot will be 'Robot 2', then 'Robot 3', etc.

A ROBOT <number> command will make the robot identified by active i.e. subsequent commands will affect that robot's position/direction. Any command that affects position/direction (e.g. MOVE, LEFT, RIGHT...) will affect only the active robot.

By default the first robot placed will become the active robot.

_Refer to the **extension.py** file for the code to solve the extension problem._

_Refer to the **extension_answer.txt** file for the printed outputs from the program._
