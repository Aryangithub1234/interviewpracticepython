import pyttsx3
eg = pyttsx3.init()
voice = eg.getProperty("voices")
rate = eg.getProperty("rate")
eg.setProperty("rate",rate+1)
eg.setProperty("voice",voice[1].id)

eg.say("welcome to my private limited organisation")
welcome = "__***__welcome to my private limited organisation__***__"
print(welcome)
eg.runAndWait()

eg.say("dear intern first enter your name here")
eg.runAndWait()
name = input("dear intern first enter your name here: ")
# print(name)

eg.say(f"hello {name} how are you? (are you ready for your python interview yes or no?)")
eg.runAndWait()
say = (f"hello {name} how are you? are you ready for your python interview yes or no?:")
print(say)
ready = "yes"
options = input("enter yes or no: ")
if options != ready:
    eg.say("okay prepare more & try for next chance")
    print("okay...prepare more & try for next chance")
    eg.runAndWait()
    exit()
if __name__ == '__main__':

    def fresherinterview():
        eg.say("so my first question is")
        eg.say("what is python")
        Q1 = "Q1 What is Python?"
        print(Q1)
        eg.runAndWait()
        eg.say("python is low level language")
        a = "(a) python is low level language"
        print(a)
        eg.runAndWait()
        eg.say("Python is a high-level, interpreted, general-purpose programming language")
        b = "(b) Python is a high-level, interpreted, general-purpose programming language"
        print(b)
        eg.runAndWait()
        eg.say("It is like c language")
        c = "(c) It is like c language"
        print(c)
        eg.runAndWait()
        ans = "b"
        option = input("enter your ans here: ")
        if option != ans:
            eg.say(f"your are wrong{b}")
            eg.runAndWait()
            print("your are wrong",b)
        else:
            eg.say(f"your are correct{b}")
            eg.runAndWait()
            print("you are correct",b)

        eg.say("my next question is")
        eg.say("What are the benefits of using Python")
        Q2 = "Q2 What are the benefits of using Python?"
        print(Q2)
        eg.runAndWait()
        eg.say("it is simple, easy-to-learn syntax that emphasizes readability")
        a = "(a) it is simple, easy-to-learn syntax that emphasizes readability"
        print(a)
        eg.runAndWait()
        eg.say("python is not easy")
        b = "(b) python is not easy"
        print(b)
        eg.runAndWait()
        eg.say("python is worst to learn for everyone")
        c = "(c) python is worst to learn for everyone"
        print(c)
        eg.runAndWait()
        ans = "a"
        option = input("enter your ans here: ")
        if option == ans:
            eg.say(f"your are correct{a}")
            eg.runAndWait()
            print("your are correct", a)
        else:
            eg.say(f"you are wrong because{a}")
            eg.runAndWait()
            print("you are wrong because",a)

        eg.say("my third question is")
        eg.say("What are lists and tuples")
        Q3 = "Q3 What are lists and tuples?"
        print(Q3)
        eg.runAndWait()
        eg.say("they are same objects in python")
        a = "(a) they are same objects in python"
        print(a)
        eg.runAndWait()
        eg.say("lists and tuples are user defined function")
        b = "(b) lists and tuples are user defined functions"
        print(b)
        eg.runAndWait()
        eg.say("Lists and Tuples are both sequence data types that can store a collection of objects in Python")
        c = "(c) Lists and Tuples are both sequence data types that can store a collection of objects in Python"
        print(c)
        eg.runAndWait()
        eg.say("Lists are represented with square brackets and tuples are represented with parantheses")
        d = "(d) Lists are represented with square brackets and tuples are represented with parantheses"
        print(d)
        eg.runAndWait()
        ans1 , ans2 = "c" , "d"
        option = input("enter your ans here: ")
        if option == ans1 or option == ans2:
            eg.say(f"your are correct{c} or {d}")
            eg.runAndWait()
            print("your are correct",c,"and",d)
        else:
            eg.say(f"you are wrong because{c}or{d}")
            eg.runAndWait()
            print("you are wrong because",c,"and",d)

        eg.say("my fourth question is")
        eg.say("Why python is most popular to Data Science")
        Q4 = "Q4 Why python is most popular to Data Science?"
        print(Q4)
        eg.runAndWait()
        eg.say("because it is a object oriented language")
        a = "(a) because it is a object oriented language"
        print(a)
        eg.runAndWait()
        eg.say("or it is mostly used in gamedevelopement")
        b = "(b) or it is mostly used in gamedevelopement"
        print(b)
        eg.runAndWait()
        eg.say("it is comparitable to angular javascript")
        c = "(c) it is comparitable to angular javascript"
        print(c)
        eg.runAndWait()
        eg.say("it has such machine learning libraries")
        d = "(d) it has such machine learning libraries"
        print(d)
        eg.runAndWait()
        ans = "d"
        option = input("write your ans here: ")
        if option == ans:
            eg.say("your are correct it has such machine learning libraries like(numpy) ,(matplotlib) ,(pandas)etc")
            print("your are correct it has such machine learning libraries like(numpy) ,(matplotlib) ,(pandas)etc")
            eg.runAndWait()
        else:
            eg.say("you are wrong")
            print("you are wrong")
            eg.runAndWait()

        eg.say("my fivth question is")
        eg.say("Which operator is right-associative in python programming")
        Q5 = "Q5 Which operator is right-associative in python programming?"
        print(Q5)
        eg.runAndWait()
        eg.say("multiplication operator")
        a = "(a) *"
        print(a)
        eg.runAndWait()
        eg.say("equal to = operator")
        b = "(b) ="
        print(b)
        eg.runAndWait()
        eg.say("add operator")
        c = "(c) +"
        print(c)
        eg.runAndWait()
        eg.say("modular operator")
        d = "(d) %"
        print(d)
        eg.runAndWait()
        ans = "b"
        option = input("enter your ans here: ")
        if option == ans:
            eg.say("correct answer = operator is right associative as assignment operators are right associative")
            print("your are correct", b,"operator is right associative as assignment operators are right associative.")
            eg.runAndWait()
        else:
            eg.say("you are wrong because operator is right associative as assignment operators are right associative")
            print("you are wrong because",b,"operator is right associative as assignment operators are right associative.")
            eg.runAndWait()

        eg.say("my sixth question is")
        eg.say("What is a correct syntax to output 'Hello World' in Python")
        Q6 = "Q6 What is a correct syntax to output 'Hello World' in Python?"
        print(Q6)
        eg.runAndWait()
        eg.say("p('hello world')")
        a = "(a) p('hello world')"
        print(a)
        eg.runAndWait()
        eg.say("print('hello world')")
        b = "(b) print('hello world')"
        print(b)
        eg.runAndWait()
        eg.say("echo(hello world)")
        c = "(c) echo(hello world);"
        print(c)
        eg.runAndWait()
        ans = "b"
        option = input("enter your ans here: ")
        if option == ans:
            eg.say(f"you are correct{b}")
            eg.runAndWait()
            print("you are correct")
        else:
            eg.say(f"you are wrong the  correct way is{b}")
            eg.runAndWait()
            print("you are wrong",b)

        eg.say("my next question is")
        eg.say("what is oops in python")
        Q7 = "Q7 what is oops in python?"
        print(Q7)
        eg.runAndWait()
        eg.say("it is a gaming module")
        a = "(a) it is gaming module"
        print(a)
        eg.runAndWait()
        eg.say("it is a machine learning algorithm")
        b = "(b) it is a machine learning algorithm"
        print(b)
        eg.runAndWait()
        eg.say("it is a python package")
        c = "(c) it is a python package"
        print(c)
        eg.runAndWait()
        eg.say("In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming")
        d = "(d) In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming"
        print(d)
        eg.runAndWait()
        ans = "d"
        option = input("write the ans here: ")
        if option == ans:
            eg.say("correct answer")
            print("correct ans")
            eg.runAndWait()
        else:
            eg.say(f"wrong answer because{d}")
            eg.runAndWait()
            print("wrong answer",d)

        eg.say("my last question is")
        eg.say("name the four pillars in oops in python")
        Q8 = "Q8 Name the four pillars in oops in python?"
        print(Q8)
        eg.runAndWait()
        eg.say("(abstraction, inheritance, encapsulation, and polymorphism)")
        a = "(a) abstraction, inheritance, encapsulation, and polymorphism"
        print(a)
        eg.runAndWait()
        eg.say("list (tuple) set & (dictionary)")
        b = "(b) list , tuple , set & dictionary"
        print(b)
        eg.say("def , for loop , (data collections) , (user inputs)")
        c = "(c) def , for loop , data collections , user inputs"
        print(c)
        eg.runAndWait()
        ans = "a"
        option = input("write ans here: ")
        if option == ans:
            eg.say("right answer")
            print("rigth answer")
            eg.runAndWait()
        else:
            eg.say(f"wrong answer because {a}")
            eg.runAndWait()
            print("wrong answer",a)
        eg.say(f"okay {name}your interview is overed now")
        eg.runAndWait()
        print("okay" ,name, "your interview is overed now")
        eg.say("Good byee")
        print("Good byee...")
        eg.runAndWait()

    f = fresherinterview()
