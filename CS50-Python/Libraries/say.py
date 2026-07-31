import cowsay
import sys

from sayings import goodbye
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])