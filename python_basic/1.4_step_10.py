builin = {'global': [None]}

for i in range(int(input())):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        builin.update({namesp: [arg]})
    if cmd == 'add':
        builin[namesp].append(arg)
    if cmd == 'get':
        while namesp != None and arg not in builin[namesp][1:]:
            namesp = builin[namesp][0]
        print(namesp)
