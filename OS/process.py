import os


def fork_process():
    """Function to fork a process,
    Behvaior of the function is non-determinism
    """
    print(f"Hello World: PID: {os.getpid()}")
    n = os.fork()
    if n < 0:
        print("fork failed")
    elif n == 0:
        print(f"I am child: PID:{os.getpid()}")
    else:
        print(f"I am parent: PID: {os.getpid()}")


def fork_and_wait():
    print(f"Hello World: PID: {os.getpid()}")
    n = os.fork()
    if n < 0:
        print("fork failed")
    elif n == 0:
        print(f"I am child: PID:{os.getpid()}")
    else:
        child_wait = os.wait()
        print(
            f"I am parent: PID: {os.getpid()} of child: {n} and wait status: {child_wait}")


# print(fork_process())
print(fork_and_wait())
