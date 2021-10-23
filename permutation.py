def permutations(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in permutations(elements[1:]):
            #print(f'printing perm {perm}')
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
                
for i in permutations([1,2,3]):
    print(i)
