def sum_of_lists(num):
    total = 0
    for i in range(5):
        l = [j ^ (j >> i) for j in range(num)]
        total += sum(l)
        del l # remove reference to l
    return total

# %mprun only can use in the module not in notebook(lab)
# use %%file <filename>.py
# then use %mprun
