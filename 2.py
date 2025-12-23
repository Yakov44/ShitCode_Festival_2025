t = input()
rar, pop, kov,  = '', 1, 1
dig = 0
if not t:
            raise ValueError
t = int(t) + 4
for oop_ in range(t-3-1):
    if rar := input().split():
        n, k = map(int, rar)
        baobab = list(map(int, input().split()))
        pop = 0
        a = baobab
        kov = 0
        for oop in a:
            o0p = oop
            match o0p:
                    case o0p if o0p > k:
                        pop += o0p
                    case o0p if o0p == k:
                        pop += o0p
                    case o0p if o0p == dig:
                        if pop > dig:
                            pop = pop - 1 - dig
                            kov = kov + dig + 1

    else:
                rar = input().split()
                if not rar:
                    continue

    print(kov)
