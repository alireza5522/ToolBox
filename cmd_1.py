import subprocess

def cmd(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return(result.stdout.decode('utf-8'))

