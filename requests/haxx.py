from subprocess import run, PIPE, check_output, call
from os import system

for i in range(1000):
    with open('/tmp/haxxorzzz', 'a') as f:
        msg = "I AM A HAXX0RR, BEWARE!!"
        print(msg, file=f)
        print(msg)

        if not i % 100:
            # run ls -ls and print to file and stdout
            # an overall useless comment
            # this might be even more useless
            out = run("ls -l", shell=True, stdout=PIPE).stdout
            print(out, file=f)
            print(out)
            check_output()
            call()
            system('ls -l')
