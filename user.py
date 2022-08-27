import admin as ad

class Application:
        login_info = {}
        def __init__(self,email,name,phone_no,address,password):
            self.email = email
            self.name = name
            self.phone_no = phone_no
            self.password = password
            Application.login_info[self.email] ={"Email":self.email,
                                               "Full_Name":self.name,
                                               "Phone_no":self.phone_no,
                                               "Address":self.addresss,
                                               "Password":self.password,
                                               }
            self.order_history = {}

        def place_new_order(self):
            print("What you want to order ")
            ad.show_inven()
          #   print(ad.inven)
            choice_user = int(input("If you want to order then select 1.YES 2.NO"))
            if choice_user ==1:
                n=int(input("How many Item do You Want to Order"))
                total_bill=0
                total_discount=0
                for i in range(n):
                    itemid = int(input("Enter the Item id here:"))
                    quan = int(input("Enter the quantity of the item:"))
                    total_bill = total_bill + ad.inven[itemid]["Price"] * quan
                    total_discount += ad.inven[itemid]["Discount"]
                    ad.inven[itemid]["Stock"] = ad.inven[itemid]["Stock"]-quan

                    self.order_history[itemid] = {
                        "Name": ad.inven[itemid]["Name"],
                        "Price": ad.inven[itemid]["Price"],
                        "Quantity":quan
                    
                    }
                    print(self.order_history)
                again_ask = int(input("Confirmed ??1 for Yes Otherwise 2 NO"))
                if again_ask ==1:
                    print(f"Total Discount Allowed is {total_discount} ")
                    print(F"After Deduced Discount It costs is {total_discount}")
                    print("You're order is successfully placed...")

                elif again_ask==2:
                    print("Your Order has Cancelled Now...")
                    self.order_history.clear()

                else:
                    print("Invalid no   !!! ")

            def order_history_see(self):
               print(self.order_history)

            def update_profile(self):
                email=input("Enter Your Mail_id for confirmation ")
                if email in Application.login_info.keys():
                    print("Email Matched ,YOU CAN UPDATE NOW")
                    del Application.login_info[email]
                    new_email = input("Enter new Email ")
                    new_name =  input("Enter new Name")
                    new_phone_no = int(input("Enter new Phone No"))
                    new_Address = input("Enter new Address ")
                    new_password = input("Enter new Password ")

                    Application.login_info[new_email] = {'Email': new_email,'Full_Name': new_name,'Phone_no': new_phone_no,'Address': new_Address,'Password': new_password,}
                    print("Profile Update")

                else:
                    print("Email not Registered  <---Please Try Again ")

            @classmethod
            def login(cls, email, password):
                if  email in cls.login_info.keys():
                    if cls.login_info.get(email)['Password'] == password:
                       print(f"logged in  -------Successfully------- {cls.login_info.get(email)['Full_Name']}")
                       return True
                    else:
                        print("Sorry! These are the Wrong Credentails")
                        return False
                else:
                    print(f"{email} Not Registerd Yet.. First Register then Come Again !!!!! ")
                    return False
                                                        
            
        

                    


            

                                  

        
        
          

