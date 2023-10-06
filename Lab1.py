def chuyengio(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    DoiGio = f"{hours}:{minutes}:{seconds}"
    return DoiGio


soGiay = int(input("Nhập số giây: "))
ketQua = chuyengio(soGiay) 
print("Kết quả:", ketQua)
