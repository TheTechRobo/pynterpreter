print("Starting pynterpreter v.1.1, the most useless project ever...")
def p(*args):
    print(*args, end="\r", sep="")

p("Creating internal functions...")
class Builtins:
    def sync():
        p("Running commands...")
        global commands
        exec(commands)
        commands = ''''''
sync = Builtins.sync
p("Setting up metadata...")
class Metadata:
    pass
p("Creating blank command string...")
commands = ''''''
p("All done.                        \n")
print("NOTE: Commands will not be run until you use command `sync()'.")
while True:
    command = input(">>> ")
    if "sync()" in command:
        sync()
    p("Adding command to string...")
    commands += command
    commands += "\n"
    p("                             ")
    del command
