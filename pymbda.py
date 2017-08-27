# Pymbda interpreter in Python
# Created by LyricLy

import re
import sys

if len(sys.argv) < 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
else:
    try:
        with open(sys.argv[1]) as f:
            program = f.read()
    except FileNotFoundError:
        print("That file couldn't be found.")
    else:
        # split on a lone equals sign
        split = re.split("(?<!=)=(?!=)", program)
        if len(split) < 2:
            params = []
            code = split[0]
        else:
            params = split[0].split(",")
            code = split[1]
        env = {}
        for param in params:
            if "=" in param:
                split_param = param.split("=")
                env[split_param[0]] = eval(split_param[1])
            else:
                env[param] = eval(input())
        result = eval(code, env)
        print(result)