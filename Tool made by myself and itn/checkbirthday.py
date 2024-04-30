import datetime 
import os
khongai = 0 
kct = ("Lê Xuân Đức An	05/18",
"Bùi Ngọc Trâm Anh	05/24",
"Bùi Thị Vy Anh	11/20",
"Lê Đức Anh	12/20",
"Nguyễn Nam Anh	04/08",

"Nguyễn Vũ Diệp Anh	06/09",

"Trần Ngọc Châm	12/15",

"Đoàn Trần Bảo Châu	09/08",

"Nguyễn Thị Quỳnh Chi	06/10",

"Đặng Trần Đức Dũng	09/19",

"Vũ Quang Dũng	11/25",

"Nguyễn Liên Hải	10/14",

"Nguyễn Nữ Việt Hạnh	04/07",

"Trương Quang Hiếu	06/19",

"Nguyễn Ngọc Phi Hùng	06/22",

"Nguyễn Thành Hưng	09/14",

"Nguyễn Vũ Khoa	09/16",

"Hoàng Thị Ngọc Lan	09/11",

"Nguyễn Phương Linh	08/09",

"Nguyễn Trà My	10/14",

"Lại Phú Bảo Nam	12/19",

"Nguyễn Ngọc Nam	03/22",

"Bùi Yến Nhi	10/14",

"Nguyễn Thị Kim Oanh	01/01",

"Cao Bá Phát	04/02",

"Nguyễn Hải Phong	10/06",

"Nguyễn Thế Phong	07/11",

"Hà Thế Phương	07/22",

"Hồ Việt Phương	03/10",

"Chu Anh Quốc	10/20",

"Lê Tiến Sơn	10/05",

"Ngô Đức Sơn	12/29",

"Trần Minh Sơn	08/05",

"Nguyễn Phương Thảo	12/03",

"Nguyễn Thanh Thảo	10/17",

"Trịnh Nguyên Thảo	05/06",

"Gia Quang Thắng	07/24",

"Trần Ngân Thu	04/09",

"Đỗ Bảo Trâm	10/05",

"Vũ Đức Trung	07/22",

"Nguyễn Như Tuấn	03/26",

"Phạm Hồng Vân	09/16",

"Lưu Đình Minh Vũ	09/14",
"AAAAA  04/30"
)
now = datetime.datetime.now()
checkdaymonth = now.strftime("%m/%d")
d = checkdaymonth.split()
for i in kct :
    b = i.split("\t")
    c = b[-1:]
    if c == d :
        print('Hôm nay là sinh nhật của : ' + str(i))
        os.system('pause')
    khongai = khongai + 1
if khongai == 0 :
    print("không ai sinh nhật hôm nay")
            
           
            
            


