print("Starting pynterpreter...")
def p(*args):
    print(*args, end="\r", sep="")

p("Creating internal functions...")
class Builtins:
    def sync():
        p("Running commands...")
        global commands
        for item in commands:
            exec(item)
        commands = []
sync = Builtins.sync
p("Setting up metadata...")
class Metadata:
    pass
p("Creating blank command list...")
commands = []
p("All done.                        \n")
print("NOTE: Commands will not be rum until you use command `sync()'.")
while True:
    command = input(">>> ")
    if "sync()" in command:
        sync()
    p("Adding command to list...")
    commands.append(command)
    p("                             ")
    del command
