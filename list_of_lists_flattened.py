l = [1, 2, 3, 4]

ll = [l, l, l, l]

print(ll)

flattned_list = [e for e in l for l in ll]

print(type(flattned_list))
print(flattned_list)