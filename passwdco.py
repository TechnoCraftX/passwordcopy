try:
    import pyperclip
    import json
    import os
    def update():
        try:
            with open("password.txt","r") as f:
                nested_dict=json.load(f)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            nested_dict={}  

        with open("tmp.txt",'w') as p:
            json.dump(nested_dict,p,indent=4) 
        with open("tmp.txt",'r')  as w:
            nested_dict=json.load(w)  
        while True:
            a = input("Enter name of web or app (or 'exit' to quit): ").strip().lower()
            if a=='exit':
                break
            if a not in nested_dict:
                nested_dict[a]={}
            while True:
                b = input("Enter credential name (or 'exit' to go back): ").strip().lower()
                if b == 'exit':
                    break
                c=input(f"Enter {b} (or 'exit' to go back): ").strip()
                if c=='exit':
                    break
                if not b or not c:
                    print("❌ Empty fields not allowed. Try again.")
                    continue
                nested_dict[a][b]=c
        ask=input("Can you save it Yes or no:-").strip().lower()
        while True:

            if ask=='yes' or ask=='y':       
                with open("password.txt","w") as l:
                    json.dump(nested_dict,l,indent=4) 
                    break  
            elif ask=='no' or ask=='n':
                print("Not save")
                break
            else:
                continue       
        os.remove("tmp.txt")   
    
    def modify():
        with open("password.txt","r") as f:
            nested_dict=json.load(f)
        with open("tmp.txt","w") as g:
            json.dump(nested_dict, g, indent=4)  
        with open("tmp.txt","r") as h:
            x=json.load(h)   
        while True:
            a=input("Enter name of  web or app:('exit' to quit)):").strip().lower()
            if a=='exit':
                break

            if a in  x:
                b=input("delet or modify(m or d): ").strip().lower()
                if b!='m' and b!= 'd':
                    break
                elif b=="d":
                    del x[a]
                elif b=='m':
                    while True:
                        z=input("Enter your credential name :('exit' to back))").strip().lower()
                        if z=='exit':
                            break
                        if z in x[a]:
                             o=input("delet or modify:m or d ").strip().lower()
                             if o!='m' and o!='d':
                                 break
                             elif o=='d':
                                 del x[a][z]
                             elif o=='m':
                                 n=input("Enter your deta:-")  
                                 x[a][z]=n
        with open ("tmp.txt","w") as l:
            json.dump(x,l,indent=4) 
        #print(x)                           
        m=input("Can you want to save(y or n):").strip().lower()
        if m=='y':
            with open("tmp.txt","r") as c:
                rd=json.load(c)
            with open("password.txt","w") as g:
                json.dump(rd, g, indent=4) 
        elif m=='n':
            print("Your password not save") 

        os.remove("tmp.txt")                             

                                 








    
 

   
    
    
    
    def coped():
        with open("password.txt", "r") as f:
            nested_dict= json.load(f)
        with open("tmp.txt","w") as g:
            json.dump(nested_dict, g, indent=4)
        while True:
            a=input("Enter name of  web or app:(exit for quit)").strip().lower()
            if  a=="exit":
                os.remove("tmp.txt")
                break
            if a in nested_dict:
                b=input("What you want:").strip().lower()
                if b in nested_dict[a]:
                    pyperclip.copy(nested_dict[a][b]) 
                    print(f"{b} is coped to clipe bord")
                else:
                    print(f'{b} cannot find ')   
            elif a=='':
                os.remove("tmp.txt")


            elif a not in nested_dict:
                print(f"{a}cannot find ")
    
    while True:
        i=input("C forcopy and U for update and M for modify existing data:").strip().lower()  
        if i=='c':
            coped()
        elif i=='u':
            update()   
        elif i=='m':
            modify()    
        else:
            break
                 
except KeyboardInterrupt:
        a='tmp.txt'
        if os.path.exists(a):
            os.remove(a)
            pass
        else:
            pass

   
       
        
 

  
except ModuleNotFoundError as e:

  print(f"\n{e.name} not found")
  pass
except NameError as s:
    print(f"\n{s.name} not import it")
    

except FileNotFoundError:
    print("Update your passworddatabace")
except json.decoder.JSONDecodeError:
    print("Update your passworddatabace")   
