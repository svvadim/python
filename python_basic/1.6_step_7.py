graf = {}


def isAncestor(ancestor, parent):
    # print(f'{parent} - >', end=' '),
    if parent == ancestor:
        return True
    if parent is None:
        return False
    for anc in graf[parent]:
        if anc == ancestor or isAncestor(ancestor, anc):
            return True
        else:
            continue


for i in range(int(input())):
    inp = input().split()
    graf[inp[0]] = [None] if len(inp) == 1 else inp[2:]

for i in range(int(input())):
    ancestor, parent = input().split()
    if isAncestor(ancestor, parent):
        print('Yes')
    else:
        print('No')
