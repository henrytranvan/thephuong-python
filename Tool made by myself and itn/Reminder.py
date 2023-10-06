import os
def ghichep() :
    
    vieclam = input('What to do ?\n ')
    ngay = input('Ngày \n ')
    thang = input('Tháng \n')
    nam = input('Năm \n')
    print('Bạn sẽ ' + vieclam +" vào " + ngay+'-'+thang+'-'+nam)
    confirm = input('Bạn chắc chứ ? \n [1] : Có \n [2] : Không \n')
    if confirm == '1' :
        print('Việc của bạn đã được ghi nhớ.')
        os.system('pause')
        with open ('./dat.txt',mode='a+', encoding='utf-8') as f :
            f.write(vieclam+ "\n" + ngay +'\n' + thang+ '\n'+ nam)
    else :
        pass
def reminder() :
    import datetime 
    from datetime import date
    today=date.today()
reminder()