import os

name = os.environ["HOME"]
print(name)


home1 = os.getenv("HOME1", default="None")
print(home1)

uptime=os.system('uptime')
print(uptime)

command =('ls' )
exit_status = os.system(command)
print(exit_status)

with open ('/tmp/1.txt','w') as file:
    file.write('This is a sample file./n')
    file.write('This was created using the OS module in python')