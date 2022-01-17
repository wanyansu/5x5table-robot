def placement(position_x, position_y, facing, robot):
    directions = ["EAST", "SOUTH", "WEST", "NORTH"]
    try:
        if isinstance(int(position_x), int) and isinstance(int(position_y), int) and facing in directions:
            robot = {"X": int(position_x), "Y": int(
                position_y), "Facing": facing}
            return robot
        elif isinstance(int(position_x), int) and isinstance(int(position_y), int) and facing not in directions:
            print("Your input of facing directions is not valid")
            return
        else:
            print("Invalid command.")
            return
    except:
        print("Your command needs to include a starting position for a robot and its facing direction.")
        return


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
        elif next_command.split(" ")[0] == "PLACE" and len(next_command.split(" ")) == 2:
            command = next_command.split(" ")[1]
            if len(command.split(",")) == 3:
                position_x = command.split(",")[0]
                position_y = command.split(",")[1]
                facing = command.split(",")[2]
                active_robot = placement(
                    position_x, position_y, facing, active_robot)
            else:
                print(
                    "You will need to nominate a starting position after the \"PLACE\" command.")
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
    Robot = dict()
    while True:
        response = input("Please enter your command: ")
        if response.split(" ")[0] == "PLACE" and len(response.split(" ")) == 2:
            command = response.split(" ")[1]
            if len(command.split(",")) == 3:
                position_x = command.split(",")[0]
                position_y = command.split(",")[1]
                facing = command.split(",")[2]
                Robot = placement(position_x, position_y, facing, Robot)
                if Robot:
                    action(Robot)
                    break
                else:
                    print(
                        "Invalid command. You need to initiate a starting position first.")
            else:
                print(
                    "You will need to nominate a starting position after the \"PLACE\" command.")
        else:
            print("Invalid command. You need to initiate a starting position first.")
