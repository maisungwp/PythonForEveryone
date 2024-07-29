sumup = {}
actions = [
    "jim++", "john--", "jim++",
    "jim++", "john--", "john--",
    "jim++", "john--", "john--",
    "jim++", "jim++", "jim++",
    "bear++",
]

for action in actions:
    name = action[:-2]
    karma = action[-2:]
    print(name, karma)
    if name in sumup:
        sumup[name] = sumup[name] + 1 if karma == "++" else sumup[name] - 1
    else:
        sumup[name] = 1 if karma == "++" else -1

print(sumup)
print(sumup['jim'])
