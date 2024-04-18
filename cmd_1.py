import subprocess

def cmd(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))

