import subprocess
import random

target = input("Enter your target: ") 

proxiesfile = "proxies.txt"

f = open(proxiesfile, "r")

num_lines = sum(1 for line in open(proxiesfile))
print(num_lines)

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

for x in f:
    proxy = random_line(proxiesfile)
    outfile = target + "_" + proxy
    subprocess.run(["curl", target, "--proxy", proxy, "--output", outfile])
    print("/n")
    
print(f.read())
