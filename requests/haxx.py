from subprocess import run, PIPE, check_output, call
from os import system
from os.path import join

for i in range(1000):
    with open('/tmp/haxxorzzz', 'a') as f:
        msg = "I AM A HAXX0RR, BEWARE!!"
        print(msg, file=f)
        print(msg)

        if not i % 100:
            out = run("ls -l", shell=True, stdout=PIPE).stdout
            print(out, file=f)
            print(out)
            system('ls -l')
            system('ls -la')
            check_output()
            call()
            system('ls -lard')
            system('ls -ltard')
            join('a', 'b')  # innocent comment here ... continued
            system('ls -l')
