import os

name = os.environ["HOME"]
print(name)


home1 = os.getenv("HOME1", default="None")
print(home1)

uptime=os.system('uptime')
print(uptime)

command ="ls-l"
exit_status = os.system(command)
print(exit_status)