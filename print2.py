import subprocess

proc = subprocess.run(["ls", "-l", "dev/null"] capture_output=True)
print(proc)