user_signup_list = []
final_user_signup_list=[]
user_access_id=[]
star_count=0
#this function helps us to get the user id from file and it is convert into list
def final_user_list():
    f=open("user_signup_file", "r")
    for user in f:
        user_signup_list.append(user)
    for user in user_signup_list:
        for char in user:
            if char == '\n' :
                user__name=user[:-1]
                final_user_signup_list.append(user__name)
    for user in user_signup_list:
        if user[-1:] != '\n':
          final_user_signup_list.append(user)
    f.close()
    return(final_user_signup_list)
line='_'*78
star='*'*78
str="Python code for admin and user login"
print(line,str.center(80),line)
while 1:
    star_count+=1
    if star_count > 1:
      print(star)
    print("""\nEnter
    1  user signup
    2  user login
    3  admin login
    4  exit  """)
    choice=int(input("\n\nenter your choice :"))
    if choice==1:
       def user_signup():
           user_name=input("\nenter the new user id :")
           def check_username():
              user_acess_id=final_user_list()
              if user_name in user_acess_id:
                 print("user id already exists")
                 user_signup()
              else:
                  f=open("user_signup_file", "a+")
                  f.write(user_name)
                  f.write("\n")
                  user_password=input("enter the password :")
                  f.write(user_password)
                  f.close()
              return()
           check_username()
           return()
       user_signup()
    if choice ==2:
        def user_login():
            user_login_name=input("login id :")
            user_login_password=input("password :")
            user_acess_id=final_user_list()
            if (user_login_name and user_login_password) in  user_acess_id:
                str1='user program code'
                print(str1.center(80))
            else:
                print("wrong user id or password please try again")
                user_login()
            return()
        user_login()
    if choice == 3:
        def admin_login():
            admin_id="github"
            admin_password="githubgithub"
            admin_name=input("admin id: ")
            admin_pwd=input("admin password")
            if admin_name==admin_id and admin_password==admin_pwd:
                str1='admin program code'
                print(str1.center(80))
            else:
                print("wrong admin id or admin password")
                admin_login()
            return
        admin_login()
    if choice == 4:
        break
    choice_cont=int(input("n\n\nEnter \n 1  continue \n 0  exit"))
    if choice_cont==0:
        break
    
	
	   
