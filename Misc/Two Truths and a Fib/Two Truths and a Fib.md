# Two Truths and a Fib

## Desciption

Can you catch the fibber?

nc umbccd.io 6000

Author: Trashcanna

## Approach

I visited `umbccd.io:6000` with netcat:

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

So the task is to figure out which number is the fionacci number. Sounds like it's scripting time.

I looked into [pwntools connections](https://es7evam.gitbook.io/security-studies/exploitation/sockets/03-connections-with-pwntools).

[script.py](script.py) connects to the netcat server, parses the stuff sent, then sends back the fibonacci number. It does this 100 times and after the 100th time, the shell gives a flag.

## Flag

DawgCTF{jU$T_l1k3_w3lc0me_w33k}
