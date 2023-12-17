from tkinter import *
import mysql.connector
sqlobj=mysql.connector.connect(user="root",host="localhost",password="1234")
cur=sqlobj.cursor()
#cur.execute("create database if not exists library")
cur.execute("use library")

Student_ID = 0
cost = idr = 0
cd = dop = []

'''
cur.execute("use library")
cur.execute("create table if not exists cust(Student_ID int primary key, Student_name varchar(80), Student_address varchar(200), Password varchar(15))")
cur.execute("drop table if exists admin ")
cur.execute("create table admin(Admin_ID int primary key, Admin_name varchar(80), Admin_adress varchar(200), Password varchar(15))")
cur.execute("insert into admin values(0001, 'Abhinaya','Bishop Garden Avenue, Gandhi nagar,Chennai','Abhi24@baby9001'),(0002, 'Abhay', 'Cathedral Road, Rosary Church street, Adambakkam, Chennai', '$12iAMRICHBOY&!')")
cur.execute("drop table if exists books ")
cur.execute("create table books(id int primary key,bookname varchar(100),author varchar(100),genre varchar(100),availability varchar(30),price int)")
cur.execute("insert into books values(001,'magic treehouse','enid blyton','kids fantasy','yes',150)")
cur.execute("insert into books values(002,'summer days','enid blyton','kids fantasy','yes',200)")
cur.execute("insert into books values(003,'matilda','roald dahl','kids fantasy','yes',250)")
cur.execute("insert into books values(004,'the bfg','roald dahl','kids fantasy','yes',300)")
cur.execute("insert into books values(005,'the twits','roald dahl','kids fantasy','yes',200)")
cur.execute("insert into books values(006,'harry potter:1','j k rowling','fantasy','yes',1000)")
cur.execute("insert into books values(007,'harry potter:2','j k rowling','fantasy','yes',1100)")
cur.execute("insert into books values(008,'harry potter:3','j k rowling','fantasy','yes',1020)")
cur.execute("insert into books values(009,'harry potter:4','j k rowling','fantasy','yes',1200)")
cur.execute("insert into books values(010,'harry potter:5','j k rowling','fantasy','yes',1200)")
cur.execute("insert into books values(011,'harry potter:6','j k rowling','fantasy','yes',1200)")
cur.execute("insert into books values(012,'harry potter:7','j k rowling','fantasy','yes',1200)")
cur.execute("insert into books values(013,'harry potter:half blood prince','j k rowling','fantasy','yes',1300)")
cur.execute("insert into books values(014,'percy jackson:The Lightning Thief ','rick riordan','fantasy','yes',1800)")
cur.execute("insert into books values(015,'percy jackson:The Sea Of Monsters ','rick riordan','fantasy','yes',1300)")
cur.execute("insert into books values(016,'percy jackson:The Titan’s Curse','rick riordan','fantasy','yes',1500)")
cur.execute("insert into books values(017,'percy jackson:The Battle Of The Labyrinth ','rick riordan','fantasy','yes',1000)")
cur.execute("insert into books values(018,'percy jackson:The Last Olympian ','rick riordan','fantasy','yes',1500)")
cur.execute("insert into books values(019,'percy jackson:The Demigod Files','rick riordan','fantasy','yes',1300)")
cur.execute("insert into books values(020,'percy jackson:the Singer of Apollo','rick riordan','fantasy','yes',1100)")
cur.execute("insert into books values(021,'Frankenstein','Mary Shelley ','sci fi','yes',1000)")
cur.execute("insert into books values(022,'Foundation','Isaac Asimov ','sci fi','yes',1400)")
cur.execute("insert into books values(023,'Dune','Frank Herbert','sci fi','yes',600)")
cur.execute("insert into books values(024,'Ice','Anna Kavan','sci fi','yes',2000)")
cur.execute("insert into books values(025,'Kindred','Octavia E. Butler ','sci fi','yes',1500)")
cur.execute("insert into books values(026,'Neuromancer','William Gibson ','sci fi','yes',1800)")
cur.execute("insert into books values(027,'Consider Phlebas','Iain Banks ','sci fi','yes',1340)")
cur.execute("insert into books values(028,'Hyperion','Dan Simmons','sci fi','yes',1750)")
cur.execute("insert into books values(029,'Jurassic Park','Michael Crichton','sci fi','yes',1450)")
cur.execute("insert into books values(030,'Snow Crash','Neal Stephenson ','sci fi','yes',1700)")
cur.execute("insert into books values(031,'Under The Skin','Michel Faber ','sci fi','yes',1450)")
cur.execute("insert into books values(032,'Metro','Dmitry Glukhovsky','sci fi','yes',1790)")
cur.execute("insert into books values(033,'Oryx and Crake','Margaret Atwood ','sci fi','yes',1800)")
cur.execute("insert into books values(034,'The Martian','Andy Weir ','sci fi','yes',400)")
cur.execute("insert into books values(035,'The Power','Naomi Alderman ','sci fi','yes',550)")
cur.execute("insert into books values(036,'ULYSSES','James Joyce','novel','yes',800)")
cur.execute("insert into books values(037,'THE GREAT GATSBY','Scott Fitzgerald','novel','yes',900)")
cur.execute("insert into books values(038,'A PORTRAIT OF THE ARTIST AS A YOUNG MAN','James Joyce','novel','yes',1010)")
cur.execute("insert into books values(039,'LOLITA','Vladimir Nabokov','novel','yes',1000)")
cur.execute("insert into books values(040,'BRAVE NEW WORLD','Aldous Huxley','novel','yes',2000)")
cur.execute("insert into books values(041,'THE SOUND AND THE FURY','William Faulkner','novel','yes',2780)")
cur.execute("insert into books values(042,'CATCH-22','Joseph Heller','novel','yes',3000)")
cur.execute("insert into books values(043,'DARKNESS AT NOON','Arthur Koestler','novel','yes',4000)")
cur.execute("insert into books values(044,'THE GRAPES OF WRATH','John Steinbeck','novel','yes',3400)")
cur.execute("insert into books values(045,'UNDER THE VOLCANO','Malcolm Lowry','novel','yes',890)")
cur.execute("insert into books values(046,'THE WAY OF ALL FLESH','Samuel Butler','novel','yes',1000)")
cur.execute("insert into books values(047,'TO THE LIGHTHOUSE','Virginia Woolf','novel','yes',2090)")
cur.execute("insert into books values(048,'AN AMERICAN TRAGEDY','Theodore Dreiser','novel','yes',3450)")
cur.execute("insert into books values(049,'THE HEART IS A LONELY HUNTER','Carson McCullers','novel','yes',890)")
cur.execute("insert into books values(050,'SLAUGHTERHOUSE-FIVE','Kurt Vonnegut','novel','yes',897)")
cur.execute("insert into books values(051,'INVISIBLE MAN','Ralph Ellison','novel','yes',999)")
cur.execute("insert into books values(052,'NATIVE SON','Richard Wright','novel','yes',1999)")
cur.execute("insert into books values(053,'HENDERSON THE RAIN KING','Saul Bellow','novel','yes',1299)")
cur.execute("insert into books values(054,'APPOINTMENT IN SAMARRA','John O’Hara','novel','yes',1399)")
cur.execute("insert into books values(055,'A PASSAGE TO INDIA','E.M. Forster','novel','yes',1599)")
cur.execute("insert into books values(056,'THE WINGS OF THE DOVE','Henry James','novel','yes',1689)")
cur.execute("insert into books values(057,'THE AMBASSADORS','Henry James','novel','yes',1799)")
cur.execute("insert into books values(058,'LORD OF THE FLIES','William Golding','novel','yes',2000)")
cur.execute("insert into books values(059,'THE SUN ALSO RISES','Ernest Hemingway','novel','yes',1345)")
cur.execute("insert into books values(060,'THE SECRET AGENT','Joseph Conrad','novel','yes',897)")
cur.execute("insert into books values(061,'NOSTROMO','Joseph Conrad','novel','yes',678)")
cur.execute("insert into books values(062,'THE RAINBOW','D.H. Lawrence','novel','yes',5678)")
cur.execute("insert into books values(063,'LIGHT IN AUGUST','William Faulkner','novel','yes',1300)")
cur.execute("insert into books values(064,'ON THE ROAD','Jack Kerouac','novel','yes',345)")
cur.execute("insert into books values(065,'PARADE’S END','Ford Madox Ford','novel','yes',678)")
cur.execute("insert into books values(066,'THE AGE OF INNOCENCE','Edith Wharton','novel','yes',890)")
cur.execute("insert into books values(067,'FROM HERE TO ETERNITY','James Jones','novel','yes',1000)")
cur.execute("insert into books values(068,'THE WAPSHOT CHRONICLES','John Cheever','novel','yes',888)")
cur.execute("insert into books values(069,'THE CATCHER IN THE RYE','J.D. Salinger','novel','yes',899)")
cur.execute("insert into books values(070,'A CLOCKWORK ORANGE','Anthony Burgess','novel','yes',1230)")
cur.execute("insert into books values(071,'OF HUMAN BONDAGE','W. Somerset Maugham','novel','yes',897)")
cur.execute("insert into books values(072,'MAIN STREET','Sinclair Lewis','novel','yes',2200)")
cur.execute("insert into books values(073,'THE ALEXANDRIA QUARTET','Lawrence Durrell','novel','yes',1356)")
cur.execute("insert into books values(074,'Hamlet','William Shakespeare','play','yes',2000)")
cur.execute("insert into books values(075,'Macbeth','William Shakespeare','play','yes',8790)")
cur.execute("insert into books values(076,'Arcadia','Tom Stoppard','play','yes',768)")
cur.execute("insert into books values(077,'Pygmalion','George Bernard Shaw','play','yes',900)")
cur.execute("insert into books values(078,'The Mysterious Affair at Styles','agatha christie','crime thriller','yes',890)")
cur.execute("insert into books values(079,'The Murder on the Links','agatha christie','crime thriller','yes',1000)")
cur.execute("insert into books values(080,'The Murder of Roger Ackroyd','agatha christie','crime thriller','yes',198)")
cur.execute("insert into books values(081,'The Big Four','agatha christie','crime thriller','yes',340)")
cur.execute("insert into books values(082,'The Mystery of the Blue Train','agatha christie','crime thriller','yes',780)")
cur.execute("insert into books values(083,'Peril at End House','agatha christie','crime thriller','yes',786)")
cur.execute("insert into books values(084,'Lord Edgware Dies','agatha christie','crime thriller','yes',999)")
cur.execute("insert into books values(085,'House of Leaves','Mark Z. Danielewski','horror','yes',7800)")
cur.execute("insert into books values(086,'The Haunting of Hill House','Shirley Jackson','horror','yes',4500)")
cur.execute("insert into books values(087,'Ring','Koji Suzuki','horror','yes',5000)")
cur.execute("insert into books values(088,'Penpal','Dathan Auerbach','horror','yes',3400)")
cur.execute("insert into books values(090,'The Fault in Our stars','John green','novel','yes',1300)")
cur.execute("insert into books values(091,'Looking for Alaska','John green','novel','yes',2340)")
cur.execute("insert into books values(092,'Paper Towns','John green','novel','yes',1300)")
cur.execute("insert into books values(093,'You Are Not Alone','John green','novel','yes',789)")
cur.execute("insert into books values(094,'Let it Snow','John green','novel','yes',1200)")
sqlobj.commit()
'''
#cur.execute("drop table if exists borrow")
#cur.execute("create table borrow(student_id int , book_id int primary key, name char(50) , price int , currentdate int)")


#cur.execute("drop table if exists help")
#cur.execute("create table help(student_id int, name_of_book char(50), author char(50))") 
total_rows = total_columns = 0            
def browse():
    global total_row, total_colums
    
    def options():
        if name.get()=="alphebetical":
            cur.execute("select * from books order by bookname")
        elif name.get()=="reverse alphabetical":
            cur.execute("select * from books order by bookname desc")
        elif name.get()=="price low to high":
            cur.execute("select * from books order by price ")
        elif name.get()=="price high to low":
            cur.execute("select * from books order by price desc")
        elif name.get()=="availability":
            cur.execute("select * from books where availability = 'yes'")
        else:
            cur.execute("select *from books")
        
        rec=cur.fetchall()
        
        print ("{:<3} {:<50} {:<20} {:<10} {:<12} {:<5}".format('BookID','Name','Author','Genre','Availability','Cost'))
        for i in rec:
            print ("{:<3} {:<50} {:<20} {:<15} {:<11} {:<5}".format(i[0],i[1],i[2],i[3],i[4],i[5] ))
    root = Tk()
    root.geometry('500x500')
    root.configure(bg = "#DBAE58")
    root.title("view")    
    name = StringVar(root)
    name.set('SORT')
    choice = ["alphebetical","reverse alphabetical","price low to high", "price high to low","availability"]
    menu = OptionMenu(root, name,*choice)
    menu.config(font=('Helvetica',15,'bold'),width=20)
    menu.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    button = Button(root, text = "SHOW", command = options,padx = 15, pady = 15, font = ("Helvetica",12)).pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    button_quit = Button( root, text = "Back" , command = root.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
    button_quit.pack()
    root.mainloop()   
    

#USER LOGIN

def login_as_user():
    
    global Student_ID
    root = Tk()
    root.geometry('1000x1000')
    root.configure(bg = "#DBAE58")
    root.title("User login")
    label = Label(root, text = "", bg ="#DBAE58").pack()
    label = Label(root, text = "REGISTRATION NUMBER",padx = 15, pady = 15, font = ("Helvetica",12)).pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    entryid = Entry(root,font = ("Helvetica",12), width =   40, borderwidth =2)
    entryid.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    pwdlabel = Label(root, text = "PASSWORD",padx = 15, pady = 15, font = ("Helvetica",12)).pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    entrypwd = Entry(root, show ="*",font = ("Helvetica",12), width =   40, borderwidth =2)
    entrypwd.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    def collect():
        global Student_ID
        dbobj=mysql.connector.connect(user="root",host="localhost",password="1234")
        cursor=dbobj.cursor()
        cursor.execute("use Library")
        
        Student_ID = entryid.get()
        pwd = entrypwd.get()
        
        uname = (Student_ID,)
        
        try:
            cursor.execute("select * from cust where Student_ID like %s ", uname)
            L = cursor.fetchall()
            if L[0][-1] == pwd:
                        RPWindow()
            else:
                label = Label(root, text = " Invalid credentials ", font = ("Helvetica",12),bg ="#DBAE58").pack()
        except :
                label = Label(root, text = " Invalid credentials ", font = ("Helvetica",12),bg ="#DBAE58").pack()

    

    button = Button(root, text = "LOGIN",padx = 15, pady = 15, font = ("Helvetica",12), command = collect).pack()
    label = Label(root, text = "", bg ="#DBAE58",font = ("Helvetica",12)).pack()
    button_quit = Button(root, text = "Exit" , command = root.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
    button_quit.pack()
    root.mainloop()
    return Student_ID



# STUDENT/CUSTOMER CONTROLS borrow return help :

def Return():  
    global Student_ID, fine,cd,dop

    def Returntk():
        global Student_ID
        ret =Tk()
        ret.geometry( '1000x1000' )
        ret.configure(bg = "#DBAE58")
        ret.title("Return")
        
        
     
        
        returnidlabel = Label(ret, text ="Enter id of book you want to return  ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
        
        returnidlabel.pack()
        label = Label(ret, text = "", bg ="#DBAE58").pack()

        returnid = Entry(ret,font = ("Helvetica",12), width =   40, borderwidth =2)
        returnid.pack()
        
      
 
               
        fine = 0   
        def Returnsql():
                global Student_ID
                global fine ,cd,dop
                try :
                    idr = returnid.get()
                    data = (idr,)
                    mydb = mysql.connector.connect( host = 'localhost' , user = ' root ', password ='1234')
                    mycursor = mydb.cursor()
                    mycursor.execute( " use library")
                    
                
                    command = ( " select currentdate from borrow  where book_id =  %s")
                    mycursor.execute(command,data)
                    dop = mycursor.fetchall()
                    cd = mycursor.execute(" select day(current_date) ")
                    cd = mycursor.fetchall()
                    com = ( " update books set availability = 'yes'  where id = %s")
                    d = (data)
                    mycursor.execute(com, d)
                    mydb.commit()                                                                
                    c = ( " delete from borrow where book_id = %s")
                    mycursor.execute(c,data)
                    mydb.commit()
                
                               
                    label = Label(ret, text = "", bg ="#DBAE58").pack()
                    returnlabel = Label(ret, text = "Returned",padx = 15, pady = 15, font = ("Helvetica",12))
                    returnlabel.pack()
                except :
                    errorlabel = Label(ret, text = "Please enter a valid id ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
                    errorlabel.pack()
        def fine_calc():
            global fine, cd, dop
            ret =Tk()
            ret.geometry( '1000x1000' )
            ret.configure(bg = "#DBAE58")
            ret.title("FINE")
            print(cd,dop)
            if int(cd[0][0]) - int(dop[0][0]) > 7 :
                                fine =1 * int(cd - dop)
            else: fine = 0
            message = "your fine is Rs " + str(fine)
            label = Label(ret, text = message,padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58").pack()
            button_quit = Button(ret, text = "OK" , command = ret.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
            button_quit.pack()

        label = Label(ret, text = "", bg ="#DBAE58").pack()
        mybuttonr = Button(ret, text =" Return ", command =Returnsql,padx = 15, pady = 15, font = ("Helvetica",12))
        label = Label(ret, text = "", bg ="#DBAE58").pack()
        mybuttonr.pack()
        label = Label(ret, text = "", bg ="#DBAE58").pack()
        mybuttonrm = Button(ret, text =" Return More ", command =Return,padx = 15, pady = 15, font = ("Helvetica",12))
        label = Label(ret, text = "", bg ="#DBAE58").pack()
        mybuttonrm.pack()
        label = Label(ret, text = "", bg ="#DBAE58").pack()
        mybuttonshow = Button(ret, text =" Show my purchase list ", padx = 15, pady = 15, font = ("Helvetica",12))
        label = Label(ret, text = "", bg ="#DBAE58").pack()
        mybuttonshow.pack()
        label = Label(ret, text = "", bg ="#DBAE58").pack()
        mybuttonco = Button(ret, text =" Check Out ",padx = 15, pady = 15, font = ("Helvetica",12),command = fine_calc)
        label = Label(ret, text = "", bg ="#DBAE58").pack()
        mybuttonco.pack()
        label = Label(ret, text = "", bg ="#DBAE58").pack()
        button_quit = Button( ret, text = "Back" , command = ret.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
        button_quit.pack()
       
        ret.mainloop()
    Returntk()
   
   
def Borrow():
              global Student_ID
              def Borrowtk():
                        global Student_ID
                        bor =Tk()
                        bor.geometry( '1000x1000' )
                        bor.configure(bg = "#DBAE58")
                        bor.title(" Borrow")
                        
                        
                        
                       
                        boridlabel = Label(bor, text = "Enter id of book you want to borrow  ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
                        boridlabel.pack()
                        label = Label(bor, text = "", bg ="#DBAE58").pack()
                        borid = Entry(bor,font = ("Helvetica",12), width =   40, borderwidth =2)
                        borid.pack()
                       

      
                                 
    
                      
                       
                               
                       
                        def Borrowsql():
                            global Student_ID
                            try:
                                mydb = mysql.connector.connect( host = 'localhost' , user = ' root ', password ='1234')
                                mycursor = mydb.cursor()
                                mycursor.execute( " use library ")
                                
                                mycursor.execute( " select day(current_date) " )
                                r = mycursor.fetchall()
                                dt = ()
                                for i in r :
                                    dt = (i,)
                            
                                idr = borid.get()
                                bookid = (idr, )
                                mycursor.execute(" select * from books where id = %s ",bookid )
                                book = mycursor.fetchall()
                                L = []
                                for i in book :
                                    L = L + [i]
                                
                                if L[0][-2]=="Unavailable":
                                    label = Label(bor, text = "", bg ="#DBAE58").pack()
                                    borrowlabel = Label(bor, text = " Unavailable at the moment ",padx = 15, pady = 15, font = ("Helvetica",12)).pack()
                                else :
                                    
                                    
                                    

                                    com = ( " update books set availability = 'Unavailable'  where id = %s")
                                    d = (bookid)
                                    mycursor.execute(com, d)
                                    mydb.commit()
                                
                                    data = (Student_ID ,L[0][0] , L[0][1] , L[0][-1], dt[0][0])
                                    command =( " insert into borrow(student_id , book_id, name  , price  , currentdate )values(%s,%s,%s,%s,%s)" )
                                    mycursor.execute(command,data)
                                    mydb.commit()
                                    label = Label(bor, text = "", bg ="#DBAE58").pack()
                                    borrowlabel = Label(bor, text = "Borrowed",padx = 15, pady = 15, font = ("Helvetica",12))
                                    borrowlabel.pack()
                            except  :
                                errorlabel2 = Label(bor, text = "Please enter a valid id  ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
                                errorlabel2.pack()
                        def total_cost():
                            global Student_ID
                            global cost
                            global idr
                            mydb = mysql.connector.connect( host = 'localhost' , user = ' root ', password ='1234')
                            mycursor = mydb.cursor()
                            mycursor.execute( " use library ")
                            data = (idr,)

                            command = ("select book_id,price from borrow where student_id = %s")
                            Studid = (Student_ID,)
                            mycursor.execute(command,Studid)
                            cost_current = mycursor.fetchall()
                            
                        
                         
                                
                            print ("{:<8} {:<15} ".format('BookID','Cost'))
                            for i in cost_current:
                                    
                                    print ("{:<8} {:<15} ".format(i[0],i[1] ))
    
                                         
                           


                        label = Label(bor, text = "", bg ="#DBAE58").pack()
                        mybuttonr = Button(bor, text =" Borrow", command = Borrowsql,padx = 15, pady = 15, font = ("Helvetica",12))
                        mybuttonr.pack()
                        label = Label(bor, text = "", bg ="#DBAE58").pack()
                        mybuttonrbm = Button(bor, text =" Borrow More", command = Borrow,padx = 15, pady = 15, font = ("Helvetica",12))
                        mybuttonrbm.pack()
                        label = Label(bor, text = "", bg ="#DBAE58").pack()
                        mybuttonco = Button(bor, text =" Check Out",padx = 15, pady = 15, font = ("Helvetica",12),command=total_cost)
                        mybuttonco.pack()
                        label = Label(bor, text = "", bg ="#DBAE58").pack()
                        button_quit = Button( bor, text = "Back" , command = bor.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
                        button_quit.pack()
                       
                        bor.mainloop()
              Borrowtk()



# Help : Suggest, Notif, Contact 
def helppage():
    global Student_ID
    help = Tk()
    help.geometry( '1000x1000' )
    help.configure(bg = "#DBAE58")
    help.title(" Help ")
    def suggestion():
        global Student_ID
        sugg = Tk()
        sugg.geometry( '1000x1000' )
        sugg.configure(bg = "#DBAE58")
        sugg.title("Suggest")
        suglabel = Label(sugg, text = " Enter name of the book ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
        suglabel.pack()
        label = Label(sugg, text = "", bg ="#DBAE58").pack()
        sugn = Entry(sugg,font = ("Helvetica",12), width =   40, borderwidth =2)
        sugn.pack()
        suglabel = Label(sugg, text = " Enter author of the book ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
        suglabel.pack()
        label = Label(sugg, text = "", bg ="#DBAE58").pack()
        suga= Entry(sugg,font = ("Helvetica",12), width =   40, borderwidth =2)
        suga.pack()
        
        def suggestions():
                    global Student_ID
                    name = sugn.get()
                    author = suga.get()
                    mydb = mysql.connector.connect( host = 'localhost' , user = ' root ', password ='1234')
                    mycursor = mydb.cursor()
                    mycursor.execute( " use library ")
                    command = (" insert into help values (%s,%s,%s)")
                    data = (Student_ID, name, author)
                    mycursor.execute(command,data)
                    mydb.commit()
                    suggestion = Tk()
                    suggestion.geometry( '1000x1000' )
                    suggestion.configure(bg = "#DBAE58")
                    suggestion.title(" Thank you ")
                    sugglabel = Label(suggestion, text = " Suggestion Added. Thank you !  ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
                    sugglabel.pack()
                    label = Label(suggestion, text = "", bg ="#DBAE58").pack()
                    button_quit = Button( suggestion, text = "Ok" , command = suggestion.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
                    button_quit.pack()
        
        label = Label(sugg, text = "", bg ="#DBAE58").pack()
        mybuttonsug = Button(sugg, text =" Add suggestion  ",command = suggestions,padx = 15, pady = 15, font = ("Helvetica",12))
        label = Label(sugg, text = "", bg ="#DBAE58").pack()
        mybuttonsug.pack()
        label = Label(sugg, text = "", bg ="#DBAE58").pack()
        button_quit = Button( sugg, text = "Exit" , command = sugg.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
        button_quit.pack()
        
        
        
    def notif():
         notiff = Tk()
         notiff.geometry( '1000x1000' )
         notiff.configure(bg = "#DBAE58")
         notiff.title(" Thank you ")
         notiflabel = Label(notiff, text = " Enter id of the book you want notification for   ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
         notiflabel.pack()
         label = Label(notiff, text = "", bg ="#DBAE58").pack()
         notifid = Entry(notiff,font = ("Helvetica",12), width =   40, borderwidth =2)
         notifid.pack()
         def notifed():
            notifc = Tk()
            notifc.geometry( '1000x1000' )
            notifc.configure(bg = "#DBAE58")
            notifc.title(" Done")
            notiflabel = Label(notifc, text = " You will now be notified when the book is available!  ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
            notiflabel.pack()
            label = Label(notifc, text = "", bg ="#DBAE58").pack()
            button_quit = Button( notifc, text = "Ok" , command = notifc.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
            button_quit.pack()
         mybuttonnotif = Button(notiff, text =" Add notification  ",command = notifed,padx = 15, pady = 15, font = ("Helvetica",12))
         label = Label(notiff, text = "", bg ="#DBAE58").pack()
         mybuttonnotif.pack()
         label = Label(notiff, text = "", bg ="#DBAE58").pack()
         button_quit = Button( notiff, text = "Exit" , command = notiff.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
         button_quit.pack()
         
         
    def contact():
        
         cont = Tk()
         cont.geometry( '1000x1000' )
         cont.configure(bg = "#DBAE58")
         cont.title(" Thank you ")
         contlabel = Label(cont, text = " Contact us at :   ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
         contlabel.pack()
         label = Label(cont, text = "", bg ="#DBAE58").pack()
         contlabel = Label(cont, text = " 044 2345 1267 ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
         contlabel.pack()
         label = Label(cont, text = "", bg ="#DBAE58").pack()
         contlabel = Label(cont, text = " Virtuallibrary@gmail.com   ",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58")
         contlabel.pack()
         label = Label(cont, text = "", bg ="#DBAE58").pack()
         button_quit = Button( cont, text = "Back" , command = cont.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
         button_quit.pack()
         
        
    helpsugglabel = Label(help, text = " Do we not have the book you want ? Suggest it !  ",padx = 15, pady = 15, font = ("Helvetica",14),bg ="#DBAE58")
    helpsugglabel.pack()
    label = Label(help, text = "", bg ="#DBAE58").pack()
    mybuttonhelp = Button(help, text =" Suggest a book to add to our collection ", command = suggestion,padx = 15, pady = 15, font = ("Helvetica",12))
    mybuttonhelp.pack()
    label = Label(help, text = "", bg ="#DBAE58").pack()
    helpnotiflabel = Label(help, text = " Book unavailable at the moment ? We can notify you when its available ! ",padx = 15, pady = 15, font = ("Helvetica",14),bg ="#DBAE58")
    helpnotiflabel.pack()
    mybuttonhelpnotif = Button(help, text =" Notify me  ", command = notif,padx = 15, pady = 15, font = ("Helvetica",12))
    mybuttonhelpnotif.pack()
    label = Label(help, text = "", bg ="#DBAE58").pack()
    helpsugglabel = Label(help, text = " We are always here for you !  ",padx = 15, pady = 15, font = ("Helvetica",14),bg ="#DBAE58")
    helpsugglabel.pack()
    mybuttonhelpcontact = Button(help, text =" Contact us ", command = contact,padx = 15, pady = 15, font = ("Helvetica",12))
    mybuttonhelpcontact.pack()
    label = Label(help, text = "", bg ="#DBAE58").pack()
    button_quit = Button( help, text = "Back" , command = help.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
    button_quit.pack()
    




# STUDENT / CUSTOMER WINDOW FOR BOOK PURCHASE OR RETURN :





def RPWindow():

    root = Tk()
    root.geometry( '1000x1000' )
    root.title("Library")
    root.configure(bg = "#DBAE58")

   
    



    mylabelpr = Label(root, text = "Return / Borrow",padx = 15, pady = 15, font = ("Helvetica",15),bg ="#DBAE58" )
    mylabelpr.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    mybutton1b = Button(root, text =" Browse BookList ",command = browse,padx = 15, pady = 15, font = ("Helvetica",12))
    mybutton1b.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    mybutton1b = Button(root, text =" Borrow Books",command = Borrow,padx = 15, pady = 15, font = ("Helvetica",12))
    mybutton1b.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    mybutton2r = Button(root, text =" Return Books",command = Return,padx = 15, pady = 15, font = ("Helvetica",12))
    mybutton2r.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    mybutton2h = Button(root, text =" Help ",command = helppage ,padx = 15, pady = 15, font = ("Helvetica",12))
    mybutton2h.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    button_quit = Button( root, text = "Log Out" , command = root.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
    button_quit.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    root.mainloop()





# ADMIN CONTROLS add remove : 


def Add():

   
   
   

    def Addtk():
        add =Tk()
        add.geometry( '1000x1000' )
        add.configure(bg = "#DBAE58")
        add.title("Add")  

        
        addidlabel = Label(add, text = "Enter id of the book you want to add : ",font = ("Helvetica",10))
        addidlabel.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()
        addid = Entry(add,font = ("Helvetica",12), width =40, borderwidth =2)
        addid.pack()
            
        label = Label(add, text = "", bg ="#DBAE58").pack()

        addnamelabel = Label(add, text = "Enter name of the book you want to add : ",font = ("Helvetica",10))
        addnamelabel.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()
        addname = Entry(add,font = ("Helvetica",12), width =40, borderwidth =2)
        addname.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()

        addauthorlabel = Label(add, text = "Enter the name of the author of the book you want to add : ", font = ("Helvetica",10))
        addauthorlabel.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()
        addauthor = Entry(add,font = ("Helvetica",12),width =40, borderwidth =2)
        addauthor.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()

        addgenrelabel  = Label(add, text =  "Enter the genre of the book you want to add : ",font = ("Helvetica",10))
        addgenrelabel.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()
        addgenre = Entry(add,font = ("Helvetica",12),width =40, borderwidth =2)
        addgenre.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()

        addpricelabel = Label(add, text =  "Enter price of the book you want to add : ", font = ("Helvetica",10))
        addpricelabel.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()
        addprice = Entry(add,font = ("Helvetica",10),width =40, borderwidth =2)
        addprice.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()

        addavaillabel = Label(add, text =  "Enter the status of availability of the book you want to add : ", font = ("Helvetica",10))
        addavaillabel.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()
        
        addavail = Entry(add,font = ("Helvetica",10),width =40, borderwidth =2)
        addavail.pack()
        label = Label(add, text = "", bg ="#DBAE58" ).pack()
           
       
        def Addsql():
            try :
                idadd = int(addid.get())
                nameadd = addname.get()
                authoradd = addauthor.get()
                genreadd = addgenre.get()
                priceadd = int(addprice.get())
                availadd = addavail.get()
            except :
                errorlabel3 = Label(add, text = "Please enter valid details  ",font = ("Helvetica",10),bg = "#DBAE58")
                
            try :
                    mydb = mysql.connector.connect( host = 'localhost' , user = ' root ', password ='1234')
                    mycursor = mydb.cursor()
                    mycursor.execute( " use library")
                    data = ( idadd, nameadd, authoradd, genreadd, availadd,priceadd)
                    command = ( " insert into books(id,bookname,author,genre,availability,price)values(%s,%s,%s,%s,%s,%s) " )
                    mycursor.execute(command,data)
                    mydb.commit()
                    label = Label(add, text = "", bg ="#DBAE58").pack()
                    addlabel = Label(add, text = "Added")
                    addlabel.pack()
            except :
                    errorlabel3 = Label(add, text = "Please enter valid details  ",font = ("Helvetica",10),bg = "#DBAE58")
                    errorlabel3.pack()
        
        mybuttonadd = Button(add, text =" Add ", command = Addsql,font = ("Helvetica",10))
        mybuttonadd.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()
        mybuttonaddm = Button(add, text =" Add More ", command = Add,font = ("Helvetica",10))
        mybuttonaddm.pack()
        label = Label(add, text = "", bg ="#DBAE58").pack()
        button_quit = Button( add, text = "Back" , command = add.destroy,font = ("Helvetica",10))
        button_quit.pack()
        add.mainloop()
    Addtk()
   




















def Remove():

   
   
   

    def Removetk():
        
        rem =Tk()
        rem.geometry( '1000x1000' )
        rem.configure(bg = "#DBAE58")
        rem.title("Remove")
        
        removeidlabel= Label(rem, text = "Enter id of the book you want to remove : ",padx = 15, pady = 15, font = ("Helvetica",12), bg ="#DBAE58")
        removeidlabel.pack()
        label = Label(rem, text = "", bg ="#DBAE58").pack()
        removeid = Entry(rem,width = 40, borderwidth =2)
        
        
        

        
        
        removeid.pack()
        
           
        
        def Removesql():
                 
                try :
                    mydb = mysql.connector.connect( host = 'localhost' , user = ' root ', password ='1234')
                    mycursor = mydb.cursor()
                    mycursor.execute( " use library ")
                    idrm = int(removeid.get())
                    data = (idrm,)
                    mycursor.execute( "delete from books where id = %s",data )
                    mydb.commit()
                    label = Label(rem, text = "", bg ="#DBAE58").pack()
                    removelabel = Label(rem, text = "Removed",font = ("Helvetica",12), bg ="#DBAE58")
                    removelabel.pack()
                
                except  :
                    errorlabel4 = Label(rem, text = "Please enter a valid id that you want to remove  ",font = ("Helvetica",12), bg ="#DBAE58")
                    errorlabel4.pack()
                                    
        label = Label(rem, text = "", bg ="#DBAE58").pack()
        mybuttonrm = Button(rem, text =" Remove ", command =Removesql,padx = 15, pady = 15, font = ("Helvetica",12))
        mybuttonrm.pack()
        label = Label(rem, text = "", bg ="#DBAE58").pack()
        mybuttonrm = Button(rem, text =" Browse ",command = browse,padx = 15, pady = 10, font = ("Helvetica",12))
        mybuttonrm.pack()
        label = Label(rem, text = "", bg ="#DBAE58").pack()
        mybuttonrmm = Button(rem, text =" Remove More ", command =Remove,padx = 15, pady = 15, font = ("Helvetica",12))
        mybuttonrmm.pack()
        label = Label(rem, text = "", bg ="#DBAE58").pack()
        button_quit = Button( rem, text = "Back" , command = rem.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
        button_quit.pack()
       
        rem.mainloop()
        
    Removetk()
   


# ADMIN WINDOW TO ADD BOOKS OR REMOVE THEM :
def student_list():
    mydb = mysql.connector.connect( host = 'localhost' , user = ' root ', password ='1234')
    mycursor = mydb.cursor()
    mycursor.execute("use library")
    mycursor.execute("select * from cust")
    print ("{:<10} {:<25} {:<60} {:<20}".format('StudentID','Name','Address','Password'))
    for i in mycursor:
        print ("{:<10} {:<25} {:<60} {:<20}".format(i[0],i[1],i[2],i[3]))
def borrow_list():
    mydb = mysql.connector.connect( host = 'localhost' , user = ' root ', password ='1234')
    mycursor = mydb.cursor()
    mycursor.execute("use library")
    mycursor.execute("select *from borrow")
    print ("{:<10} {:<5} {:<50} {:<10} {:<5}".format('StudentID','BookID','Name','Price','Date'))
    for i in mycursor:
        print ("{:<10} {:<5} {:<50} {:<10} {:<5}".format(i[0],i[1],i[2],i[3],i[4]))
def sugg():
    mydb = mysql.connector.connect( host = 'localhost' , user = ' root ', password ='1234')
    mycursor = mydb.cursor()
    mycursor.execute("use library")
    mycursor.execute("select *from help")
    print ("{:<10} {:<50} {:<40}".format('StudentID','Name','Author'))
    for i in mycursor:
        print ("{:<10} {:<50} {:<40}".format(i[0],i[1],i[2]))

def manage_admin():
    root = Tk()
    root.geometry('1000x1000')
    root.configure(bg = "#DBAE58")
    label = Label(root, text = "", bg ="#DBAE58").pack()
    button = Button(root, text = "VIEW STUDENT'S LIST",padx = 15, pady = 15, font = ("Helvetica",12), command = student_list).pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    button = Button(root, text = "VIEW BORROWED LIST",padx = 15, pady = 15, font = ("Helvetica",12), command = borrow_list).pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    button = Button(root, text = "VIEW SUGGESTIONS",padx = 15, pady = 15, font = ("Helvetica",12), command = sugg).pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    button_quit = Button(root, text = "Back" , command = root.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
    button_quit.pack()
    root.mainloop()


def ARWindow():
    adminwin = Tk()
    adminwin.geometry( '1000x1000' )
    adminwin.title("Library")
    adminwin.configure(bg = "#DBAE58")

    


    mylabelar = Label(adminwin, text = " Admin Options :  Add Record / Remove Record ",font = ("Helvetica",12),bg ="#DBAE58")
    mylabelar.pack()
    label = Label(adminwin, text = "", bg ="#DBAE58").pack()
    mybutton1a = Button(adminwin, text =" Add Book Record ", command = Add,padx = 15, pady = 15, font = ("Helvetica",12))
    mybutton1a.pack()
    label = Label(adminwin, text = "", bg ="#DBAE58").pack()
    mybutton2rv = Button(adminwin, text =" Remove Book Record", command = Remove,padx = 15, pady = 15, font = ("Helvetica",12))
    mybutton2rv.pack()
    label = Label(adminwin, text = "", bg ="#DBAE58").pack()
    mybutton2rv = Button(adminwin, text =" View Booklist", command = browse,padx = 15, pady = 15, font = ("Helvetica",12))
    mybutton2rv.pack()
    label = Label(adminwin, text = "", bg ="#DBAE58").pack()
    mybutton2rv = Button(adminwin, text =" Manage library", command = manage_admin,padx = 15, pady = 15, font = ("Helvetica",12))
    mybutton2rv.pack()
    label = Label(adminwin, text = "", bg ="#DBAE58").pack()
    button_quit = Button( adminwin, text = "log out" , command = adminwin.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
    button_quit.pack()
    adminwin.mainloop() 


# admin username pwd 


               
def login_as_admin():
    root = Tk()
    root.geometry('1000x1000')
    root.configure(bg = "#DBAE58")
    label = Label(root, text = "", bg ="#DBAE58",font = ("Helvetica",15)).pack()
    root.title("Admin login")
    label = Label(root,text = "USERNAME",padx = 15, pady = 15, font = ("Helvetica",12)).pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    entryname = Entry(root,font = ("Helvetica",15), width =   40, borderwidth =2)
    entryname.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    pwdlabel = Label(root, text = "PASSWORD",padx = 15, pady = 15, font = ("Helvetica",12)).pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    entrypwd = Entry(root, show ="*",font = ("Helvetica",15), width =   40, borderwidth =2)
    entrypwd.pack()
    label = Label(root, text = "", bg ="#DBAE58",font = ("Helvetica",12)).pack()
    


    def collect():
        dbobj=mysql.connector.connect(user="root",host="localhost",password="1234")
        cursor=dbobj.cursor()
        cursor.execute("use Library")
        
        username = str(entryname.get())
        pwd = entrypwd.get()
        
        uname = (username,)
        try:
            cursor.execute("select * from admin where Admin_name like %s ", uname)
            L = cursor.fetchall()
            if L[0][-1] == pwd:
                        ARWindow()
            else:
                label = Label(root, text = " Invalid credentials ", font = ("Helvetica",12),bg ="#DBAE58").pack()
        except :
                label = Label(root, text = " Invalid credentials ",font = ("Helvetica",12), bg ="#DBAE58").pack()
    button = Button(root, text = "LOGIN",padx = 15, pady = 15, font = ("Helvetica",12), command = collect).pack()
    label = Label(root, text = "", bg ="#DBAE58",font = ("Helvetica",12)).pack()
    button_quit = Button(root, text = "Exit" , command = root.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
    button_quit.pack()
    root.mainloop()



#registername, id, adress, pwd
    
def register():
    root = Tk()
    root.geometry('1000x1000')
    root.configure(bg = "#DBAE58")
    root.title("register")
    label = Label(root, text = "", bg ="#DBAE58").pack()
    label2 = Label(root, text = "NAME",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58").pack()
    entry2 = Entry(root,font = ("Helvetica",15), width =   40, borderwidth =2)
    entry2.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    label1 = Label(root, text = "ADMISSION NUMBER",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58").pack()
    entry1 = Entry(root,font = ("Helvetica",15), width =   40, borderwidth =2)
    entry1.pack()
    label = Label(root, text = "", bg ="#DBAE58")
    label3 = Label(root, text = "ADDRESS",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58").pack()
    entry3 = Entry(root,font = ("Helvetica",15), width =   40, borderwidth =2)
    entry3.pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()
    label4 = Label(root, text = "PASSWORD",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58").pack()
    entry4= Entry(root, show ="*",font = ("Helvetica",15), width =   40, borderwidth =2)
    entry4.pack()


    def register_mysql():
        try:
            
            dbobj=mysql.connector.connect(user="root",host="localhost",password="1234")
            cursor=dbobj.cursor()
            cursor.execute("use Library")
            name = entry2.get()
            adm_no = entry1.get()
            address = entry3.get()
            password = entry4.get()
            l = (adm_no,name,address,password)

            command =("insert into cust(student_id,student_name, student_address, password) values(%s,%s,%s,%s)")
            cursor.execute(command,l)
            dbobj.commit()
            RPWindow()
        except  :
            label = Label(root, text = "Invalid! try again",padx = 15, pady = 15, font = ("Helvetica",12),bg ="#DBAE58").pack()
            
    label = Label(root, text = "", bg ="#DBAE58").pack()
    button = Button(root, text = "register",padx = 15, pady = 15, font = ("Helvetica",12), command = register_mysql ).pack()
    label = Label(root, text = "", bg ="#DBAE58").pack()  
    button_quit = Button(root, text = "Exit" , command = root.destroy,padx = 15, pady = 15, font = ("Helvetica",12))
    button_quit.pack()
        

    root.mainloop()


def main():
    root = Tk()
    root.geometry('1000x1000')
    root.configure(bg = "#DBAE58")
    root.title("Entry")
    label = Label("", bg ="#DBAE58").pack()
    label = Label(root, text = "WELCOME TO OUR VIRTUAL LIBRARY! \n \n HAPPY READING! ",padx = 50, pady = 50,font = ("Arial Black",18),fg = "green",bg = "#DBAE58").pack()
    button1 = Button(root, text = "LOGIN AS A USER", command = login_as_user,padx = 20, pady = 20, font = ("Helvetica",15),fg = "red").pack()
    label = Label(text = "",bg = "#DBAE58").pack()
    button2 = Button(root,text = "LOGIN AS AN ADMIN", command = login_as_admin,padx = 20, pady = 20, font = ("Helvetica",15), fg = "red").pack()
    label = Label(text = "", bg = "#DBAE58").pack()
    button3 = Button(root,text = "REGISTER", command = register, padx = 20, pady = 20,font = ("Helvetica",15), fg = "red").pack()
    label = Label("", bg ="#DBAE58").pack()
    button_quit = Button(root, text = "EXIT" , command = root.destroy,padx = 20, pady = 20, font = ("Helvetica",15),fg = "red")
    button_quit.pack()
    root.mainloop()
    
main()

    
    
