def placement():
    while True:
        starting_position = input(
            "Please enter the starting position in the format of X(Integer),Y(Interger),F(Direction): ")
        if starting_position == 'PLACE':
            placement()
        try:
            if isinstance(int(starting_position.split(",")[0]), int) and isinstance(int(starting_position.split(",")[1]), int) and starting_position.split(",")[2] in ['EAST', 'SOUTH', 'WEST', 'NORTH']:
                Robot = {"X": int(starting_position.split(",")[0]), "Y": int(
                    starting_position.split(",")[1]), "Facing": starting_position.split(",")[2]}
                return Robot
        except:
            print("Invalid Input!")


def action(active_robot):
    while True:
        next_command = input("Please enter the next action or direction: ")
        if (active_robot["X"] < 0 or active_robot["X"] > 5) or (active_robot["Y"] < 0 or active_robot["Y"] > 5):
            print("Your robot is not on the table.")
            break
        if next_command == 'MOVE':
            active_robot = move(active_robot)
        elif next_command == 'LEFT' or next_command == 'RIGHT':
            active_robot["Facing"] = turn(active_robot, next_command)
        elif next_command == 'REPORT':
            print(
                f'{str(active_robot["X"])},{str(active_robot["Y"])},{active_robot["Facing"]}')
            break
        else:
            print('Invalid')


def move(active_robot):
    switch = {
        "EAST": active_robot["X"] + 1,
        "SOUTH": active_robot["Y"] - 1,
        "WEST": active_robot["X"] - 1,
        "NORTH": active_robot["Y"] + 1
    }
    if active_robot["Facing"] in ["EAST", "WEST"]:
        active_robot["X"] = switch.get(active_robot["Facing"], "Invalid")
    else:
        active_robot["Y"] = switch.get(active_robot["Facing"], "Invalid")

    if active_robot["X"] == -1:
        active_robot["X"] = active_robot["X"] + 1
    elif active_robot["X"] == 6:
        active_robot["X"] = active_robot["X"] - 1
    elif active_robot["Y"] == -1:
        active_robot["Y"] = active_robot["Y"] + 1
    elif active_robot["Y"] == 6:
        active_robot["Y"] = active_robot["Y"] - 1
    return active_robot


def turn(active_robot, direction):
    if direction == "LEFT":
        switch = {
            "EAST": "NORTH",
            "NORTH": "WEST",
            "WEST": "SOUTH",
            "SOUTH": "EAST"
        }
        active_robot["Facing"] = switch.get(active_robot["Facing"], "Invalid")
    else:
        switch = {
            "EAST": "SOUTH",
            "SOUTH": "WEST",
            "WEST": "NORTH",
            "NORTH": "EAST"
        }
        active_robot["Facing"] = switch.get(active_robot["Facing"], "Invalid")
    return active_robot["Facing"]


if __name__ == '__main__':
    while True:
        initiator = input("Please enter your first command: ")
        if initiator == "PLACE":
            Robot = dict()
            Robot = placement()
            action(Robot)
            break
        else:
            print("Invalid input!")
