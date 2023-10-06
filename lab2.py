from datetime import datetime


class Sinhvien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoten = hoTen
        self.__ngaySinh = ngaySinh

        @property
        def maSo(self):
            return self.__maSo

        @maSo.setter
        def maSo(self, maso):
            if self.laMaSoHopLe(maso):
                self.__maSo = maSo

        @staticmethod
        def lamaSoHopLe(maso: int):
            return len(str(maso)) == 7

        @classmethod
        def doiTenTruong(self, tenmoi):
            self.truong = tenmoi

        def __str__(self) -> str:
            return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"

        def xuat(self):
            print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")


class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: Sinhvien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSinhVienTheoMSSV(self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv]

    def timVTSinhVientheoMSSV(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1

    def xoaSinhVientheoMSSV(self, maSo: int) -> bool:
        vt = self.timVTSinhVienTheoMSSV(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    def timSinhVienTheoTen(self, ten: str):
        return [sv for sv in self.dssv if ten in sv.hoTen]
     
    def timSVSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]


ngay_gioi_han = datetime(2000, 6, 15)
ket_qua_tim_kiem = DanhSachSV.timSVSinhTruocNgay(ngay_gioi_han)

if ket_qua_tim_kiem:
    print("Danh sách sinh viên sinh trước ngày 15/6/2000:")
    for sv in ket_qua_tim_kiem:
        print(sv)
else:
    print("Không có sinh viên nào sinh trước ngày 15/6/2000")

