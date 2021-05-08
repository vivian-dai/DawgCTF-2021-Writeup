# Two Truths and a Fib

## Desciption

Can you catch the fibber?

nc umbccd.io 6000

Author: Trashcanna

## Approach

I connected to `umbccd.io:6000` with netcat:

```console
Welcome to two truths and a fib! You'll be given three numbers:
one of them will be a fibonacci number and two of them will not.
It's your job to tell which is which and send back the fibonacci.
Example:
12, 8, 4
Which number is a fib?
>> 8
Correct!


[18613250067381, 14930352, 25089646462807]
>>
Oof, too slow!
```

So the task is to figure out which number is the Fibonacci number, and we have to do it fast. We can write a script. 

First off, the best way to find out if a number is Fibonacci is to ~~hardcode every Fibonacci number in an array~~ realize (from some derivations of Binet's and some CP) that a number is Fibonacci if and only if one of 5N^2+4 or 5N^2-4 is a perfect square (theory explanation [here](https://math.stackexchange.com/questions/9999/checking-if-a-number-is-a-fibonacci-or-not))

Then, we need to connect to the server. I first looked into socket and telnet (because kali supremacy ~~and kevin's lessons~~) [here](https://pequalsnp-team.github.io/cheatsheet/socket-basics-py-js-rb), but it didn't work + was too slow 😭 (rip socket code + effort).

I then looked into [pwntools connections](https://es7evam.gitbook.io/security-studies/exploitation/sockets/03-connections-with-pwntools), and that worked so I decided to us that instead.

[script.py](script.py) is vivian's weird hardcode thing lol (ask her to explain it XD)

[script2.py](script2.py) connects to the netcat server and reads in the server header.
Then, for each iteration, it parses the information sent, then sends back the Fibonacci number by checking which value is a Fibonacci number. It does this 100 times and after the 100th time, the server should give us a flag.

## Flag

DawgCTF{jU$T_l1k3_w3lc0me_w33k}
