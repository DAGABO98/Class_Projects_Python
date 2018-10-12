import matrices_code as mc

ts = mc.BaseMatrix(int, 4, 4)
ts.set(0, 0, 1)
ts.get(0, 0)
ts.get(0, 1)
print(ts)

gg = mc.MySparseMatrix(int, 4, 4)
gg.set(0, 0, 1)
print(gg)
print(ts==gg)
c = ts+gg
print(c)

tt = mc.MySparseMatrix(int, 2, 2)
tt.set(0,0,11)
tt.set(0,1,5)
tt.set(1,0,2)
print(tt.get(0,1))
print("tt = ", tt)

t1 = mc.BaseMatrix(int, 2, 2)
t1.set(0,1,-11)
t1.set(1,1,11)
print("t1 = ", t1)

print("tt + t1 =", tt + t1)

t3 = mc.BaseMatrix(float, 3, 3)
t4 = mc.BaseMatrix(float, 3,3)
print("t3 = ", t3)
print("t4 = ", t4)
print("t3 == t4 resolves to ", t3 == t4)

t5 = mc.BaseMatrix(float, 3, 3)
t6 = mc.MySparseMatrix(float, 3,3)
print("t5 = ", t5)
print("t6 = ", t6)

print("t5 == t6 is ", t5 == t6)
print("t5 is t6 evaluates to ", t5 is t6)

t5.set(0,0,3.4)
t5.set(1,1,4.0)
print("updated t5 = ", t5)


t6.set(1,1,11.0)
print("updated t6 = ", t6)

print("after updated, t5 == t6 is ", t5 == t6)


print("t5 + t6 = ", t5+t6)