import math


class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def rutGon(self):
        gcd = math.gcd(self.tu_so, self.mau_so)
        self.tu_so = self.tu_so // gcd
        self.mau_so = self.mau_so // gcd

    def __add__(self, other):
        tu_so_moi = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau_so_moi = self.mau_so * other.mau_so
        result = PhanSo(tu_so_moi, mau_so_moi)
        result.rutGon()
        return result

    def __sub__(self, other):
        tu_so_moi = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau_so_moi = self.mau_so * other.mau_so
        result = PhanSo(tu_so_moi, mau_so_moi)
        result.rutGon()
        return result

    def __mul__(self, other):
        tu_so_moi = self.tu_so * other.tu_so
        mau_so_moi = self.mau_so * other.mau_so
        result = PhanSo(tu_so_moi, mau_so_moi)
        result.rutGon()
        return result

    def __truediv__(self, other):
        tu_so_moi = self.tu_so * other.mau_so
        mau_so_moi = self.mau_so * other.tu_so
        result = PhanSo(tu_so_moi, mau_so_moi)
        result.rutGon()
        return result

    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"


a = PhanSo(1, 5)
b = PhanSo(3, 3)
print(f"{a} + {b} = {a + b }")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")


class DanhSachPhanSo:
    def __init__(self) -> None:
        self.DSPS = [
            PhanSo(1, 2),
            PhanSo(5, 4),
            PhanSo(2, 3),
            PhanSo(3, 4),
            PhanSo(-2, 3),
            PhanSo(2, -3),
        ]

    def DemPSAm(self):
        return len((list(filter(lambda x: (x.tuSo * x.mauSo < 0), self.DSPS))))

    def TimDuongNN(self):
        m = list(filter(lambda x: (x.tuSo / x.mauSo) > 0, self.DSPS))
        a = []
        for i in m:
            if i != None:
                a.append((i.tuSo / i.mauSo))
        mina = min(a)
        return min(list(filter(lambda x: (x.tuSo / x.mauSo) == mina, self.DSPS)))
