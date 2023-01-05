import random
print("***WELCOME TO THE BEST PLATFORM FOR SAVING YOUR PASSWORD***")
with open("pass.txt","r+") as f:
  lines = f.read()
  if "password" in lines:
    print("You are signed in")
    view = input("Enter v to view your passwords or s to save your password")
    
    if view=="v":
      v_view = input("Enter all to view your all passwords or simply enter the subject to view it's password.")
      
      if v_view=="all":
        with open("pass.txt") as f:
          read = f.read()
          print(read)
      else:
          with open("pass.txt") as f:
                lines = f.read()

          
          sub_pwd = {}
          for line in lines:
            parsed = lines.split()
            ind = parsed.index(v_view)

          for i in range(ind,ind+1):
            sub_pwd[parsed[i]]=parsed[i+2]
          print(f"The password of {v_view} is {sub_pwd[v_view]}")
    
    elif view=="s":    
      main_sub = input("Enter the subject of the passwords :")
      main_pwd = input("Enter the password :")
      with open("pass.txt","a") as f:
        f.write("Subject: " + main_sub + "|" + "password: " + main_pwd + "\n")
        print("Your password is saved!")
      

  else:    
        c = input("Type c to continue:")
        def genr_pass():
            upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lower_case = "abcdeghijklmnopqrstuvwxyz"
            num = "1234567890"
            symbols="!@#$%^&*()_?"
            user_for = upper_case+lower_case+num+symbols
            lenght_for_pass = 10
            password = "".join(random.sample(user_for,lenght_for_pass))
            return password



        if c!="c":
          f = input("How can we improve this Manager that this platform should deserve you")
          if f!=None:
            print("Thank You for your Feedback!")

        elif c=="c": 
          sign_in = input("Continue wit signing in (yes/no)")
          if sign_in!="no":
            n =input("Enter your Full name")
            mail = input("Enter your E-mail")
            pwd = input("Enter your password or use recommended password if Yes type yes .")
          
            if pwd=="yes":
                pwd_genr = genr_pass()
                print("Your password is ",pwd_genr) 
                print("Now you are all setup up to take up adavantage of this password manager") 

                with open("pass.txt","w") as f:
                    f.write("name: " + n + "|" + "Email: " + mail + "|" + "password: " + pwd_genr + "\n")
            else:
                print("Your password is ",pwd)
                with open("pass.txt","w") as f:
                    f.write("name: " + n + "|" + "Email: " + mail + "|" + "password: " + pwd + "\n")
          else:
            print('You must be signed in')          

            
        

