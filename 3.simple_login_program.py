valid_username="technical"
valid_password="python@123"
for i in range(3):
    username=input("enter username")
    password=input("enter password")
    if(username==valid_username and password==valid_password):
        print("login successfull")
        break
    else:
        print("invalid username or password")
else:
    print("Account blocked for 24 hours")

