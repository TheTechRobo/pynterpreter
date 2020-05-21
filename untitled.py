print("A Completely Useless Project -- pynterpreter 1.0")
while True:
    command = input(">")
    if "if" in command:
        cmd2 = input("...")
        cmd3 = input("...")
        if cmd3 == "":
            cmd4 = input("...")
    exec(command)