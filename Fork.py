import os

pid = os.fork()

if pid > 0:
    
    print(f"Parent process with PID: {os.getpid()}")
    print(f"Child process PID: {pid}")
else:
    
    print(f"Child process with PID: {os.getpid()}")
    print(f"Parent PID: {os.getppid()}")
