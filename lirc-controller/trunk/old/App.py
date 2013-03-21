import daemon
from src import LircController


with daemon.DaemonContext():
    LircController