import subprocess

proc = subprocess.run( argv: ["ls", "-l"],capture_output=True)
print(proc)
