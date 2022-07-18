def throws(): 
    return 5/0 
try: 
    throws() 
except ZeroDivisionError: 
    print ("Chia một số cho 0!") 
except Exception as problem: 
    print ('Phát hiện phép tính lỗi') 
finally:
    print ('Phép tính bị hủy')