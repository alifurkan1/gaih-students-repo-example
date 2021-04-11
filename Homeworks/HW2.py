data_base={"aslan":12344,"kaplan":59234,"ayı":94224,"kedi":532665}

user_id=input("Kullanıcı adınızı giriniz:")

while not user_id in data_base:
        user_id=input("Terar kullanıcı adınızı giriniz:")
        
user_pw=input("Sifrenizi girin:")

try:  
    user_pw_new=int(user_pw)
except (ValueError,NameError):
    print("Şifreniz sadece sayılardan oluşabilir !!")
    user_pw_new=input("Tekrar şifrenizi girin:")
    
if user_pw_new==data_base[user_id]:
    print("Successfull login !!")
    
else:
    print("Unsuccessfull login !!")

    