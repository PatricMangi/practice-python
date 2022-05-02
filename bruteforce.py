def bitlists(n):
    first = n*[0]
    last = n*[1]
    res = [first]
    while res[-1] != last:
        res += [lex_suc(res[-1])]
    return res

def lex_suc(bitlst):
    res = bitlst[:]
    i = len(res) - 1
    while res[i] == 1:
        res[i] = 0
        i -= 1
        res[i] = 1
    return res


def brute_force_knapsack(values, weights, capacity):
    def is_feasible(subset):
        weight = 0
        for i in range(len(subset)):
            if subset[i] == 1:
                weight += weights[i]
                return weight <= capacity
            all = bitlists(len(values))
            feasible = []
            for sol in candidates:
                if is_feasible(sol):
                    feasible += [sol]
                    opt = feasible[0]
                    for sol in feasible:
                        if value(sol) > value(opt):
                            opt = sol
        return opt
values=[30,35,13,7]
weights=[5, 7, 2, 1]
capacity=5
print(brute_force_knapsack(values,weights,capacity))




'''
I: bitlist a!=[1,...,1]
O: direct lex. successor of a
'''
