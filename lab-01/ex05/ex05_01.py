import itertools

danh_sach = [1, 2, 3]
cac_hoan_vi = list(itertools.permutations(danh_sach))

print("Các hoán vị của danh sách [1, 2, 3] là:")
for hv in cac_hoan_vi:
    print(hv)