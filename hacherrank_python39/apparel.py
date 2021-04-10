class Apparel:
    def init(self, ab, typ, price, inStock):
        self.ab, self.typ, self.price, self.inStock = ab, typ, price, inStock


class Store:
    def init(self, aplist):
        self.aplist = aplist

    def caa(self, brand, typ, size, num):
        st1 = False
        st2 = False
        st3 = False
        demp = None
        for i in self.aplist:
            if i.ab == brand and i.typ == typ:
                st1 = True
                demp = i.inStock


        if demp is not None:
            if size in demp.keys():
                st2 = True
                if num < demp[size]:
                    st3 = True
                    demp[size] = num
                    if st1 == True and st2 == True and st3 == True:
                        print("Size Available")
                        for k, v in demp.items():
                            print(k, ":", v)
                        return True
        return False


li = []
n = int(input())

for i in range(n):
    brand = input()
    typ = input()
    price = int(input())
    count = int(input())
    di = {}
    for i in range(count):
        k = input()
        v = int(input())
        di[k] = v
    li.append(Apparel(brand, typ, price, di))

ab = input()
at = input()
asize = input()
c = int(input())
store = Store(li)
st = store.caa(ab, at, asize, c)
if st == False:
    print("Size is not available")
status = False
for i in li:
    if i.ab == ab and i.typ==at:
        status = True
        break
if status == False:
    print("Apparel not Found")