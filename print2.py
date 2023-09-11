import subprocess

proc = subprocess.run(args: ["ls", "-l"],capture_output=True)
