print("Starting pynterpreter v.1.1, the most useless project ever...")

print("Creating internal functions...", end="\r")
class Builtins:
    def sync():
        print("Running commands...", end="\r")
        global commands
        exec(commands)
        commands = ""
sync = Builtins.sync
print("Setting up metadata...", end="\r")
class Metadata:
    pass
print("Creating blank command string...", end="\r")
commands = ""
print("All done.                        \n", end="\r")
print("NOTE: Commands will not be run until you use command `sync()'.")
while True:
    command = input(">>> ")
    if "sync()" in command:
        sync()
    print("Adding command to string...", end="\r")
    commands += command
    commands += "\n"
    print("                             ", end="\r")
    del command
