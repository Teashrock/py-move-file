import os


def move_file(cmd: str) -> None:
    cmd_split = cmd.split(" ")
    if len(cmd_split) != 3:
        return
    if cmd_split[0] != "mv":
        return
    path = "/".join(cmd_split[2].split("/")[:-1])
    if path and not os.path.exists(path):
        os.makedirs(path)
    print(cmd_split[2])
    with open(cmd_split[1], "r") as inf:
        with open(f"{cmd_split[2]}", "w") as of:
            of.write(inf.read())
    os.remove(cmd_split[1])
