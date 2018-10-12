import cayley_groups as cg

def unit_test():
    f1 = cg.CayleyMod5(2)
    f2 = cg.CayleyMod5(3)
    f3 = cg.CayleyMod5(11)

    print("f1 = ", f1)
    print("f2 = ", f2)
    print("f3 = ", f3)

    print("f1 * f2 = ", f1 * f2)
    print("f3 * f2 = ", f3 * f2)

    x = cg.CayleyOneAndI(-1 - 0j)
    y = cg.CayleyOneAndI(-1 - 0j)
    print("x = ", x)
    print("y = ", y)
    print("x*y = ", x * y)
    z = cg.CayleyOneAndI(0 + 1j)
    print("z = ", z)
    print("x*z =", x * z)
    print("z*z =", z * z)

    print(x==y)

    print("Trying to make CayleyOneAndI(2)")
    ##f = cg.CayleyOneAndI(2)

unit_test()