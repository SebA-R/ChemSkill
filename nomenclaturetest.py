import json
import random
import math

with open("chem_json.json", "r") as f:
    dict = json.loads(f.read())

def test1():
    #simple ionic stuff
    total=0
    correct=0
    for i in range(10):
        cation, dict2 = random.choice(list(dict["cation"].items()))
        anion, dict3 = random.choice(list(dict["anion"].items()))
        answer=cation + " "+ anion
        if int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1 and int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]     
        elif int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]                       
        elif int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))        
        else:
            question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
        user=input(question)
        if user==answer:
            correct+=1
            total+=1
            print("correct, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))

def test2():
    #solely multivalent + normal anion
    total=0
    correct=0
    for i in range(10):
        cation, dict2 = random.choice(list(dict["multivalent cation"].items()))
        anion, dict3 = random.choice(list(dict["anion"].items()))
        answer=cation + " "+ anion
        if int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1 and int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]     
        elif int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]                       
        elif int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))        
        else:
            question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
        user=input(question)
        if user==answer:
            correct+=1
            total+=1
            print("correct, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))

def test3():
    #solely polyatomics + normal cations
    total=0
    correct=0
    for i in range(10):
        choices=["polyatomic cation", "cation", "cation", "cation", "cation", "cation", "cation", "cation" ]
        rand=random.randint(0,7)
        cation, dict2 = random.choice(list(dict[choices[rand]].items()))
        anion, dict3 = random.choice(list(dict["polyatomic anion"].items()))
        answer=cation + " "+ anion
        if int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1 and int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]     
        elif int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            if rand!=0:
                question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"] 
            else:
                question="("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]                                       
        elif int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))        
        else:
            if rand!=0:
                question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
            else:
                question="("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
        user=input(question)
        if user==answer:
            correct+=1
            total+=1
            print("correct, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))

def test4():
    #solely multivalent and polyatomic
    total=0
    correct=0
    for i in range(10):
        choices=["polyatomic cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation"]
        rand=random.randint(0,7)
        cation, dict2 = random.choice(list(dict[choices[rand]].items()))
        anion, dict3 = random.choice(list(dict["polyatomic anion"].items()))
        answer=cation + " "+ anion
        if int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1 and int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]     
        elif int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            if rand!=0:
                question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"] 
            else:
                question="("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]                                       
        elif int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))        
        else:
            if rand!=0:
                question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
            else:
                question="("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
        user=input(question)
        if user==answer:
            correct+=1
            total+=1
            print("correct, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))
        
def test5():
    #everything thats ionic
    total=0
    correct=0
    for i in range(10):
        choices1=["polyatomic cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "cation", "cation", "cation", "cation", "cation", "cation", "cation", "cation", "cation"]
        rand=random.randint(0,16)
        choices2=["polyatomic anion", "polyatomic anion", "polyatomic anion", "polyatomic anion", "anion", "anion", "anion", "anion", "anion"]
        rand2=random.randint(0, 8)
        cation, dict2 = random.choice(list(dict[choices1[rand]].items()))
        anion, dict3 = random.choice(list(dict[choices2[rand2]].items()))
        answer=cation + " "+ anion
        if int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1 and int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]     
        elif int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            if rand!=0:
                question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"] 
            else:
                question="("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]                                       
        elif int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            if rand2>=4:
                question=dict2["Periodic table name"]+dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))  
            else:
                question=dict2["Periodic table name"]+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))  
        else:
            if rand!=0:
                question+=(dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"])))))
            else:
                question+=("("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"])))))
            if rand2>=4:
                question+=(dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))))
            else:
                question+=("("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))))
        user=input(question)
        if user==answer:
            correct+=1
            total+=1
            print("correct, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))

def test6():
    #solely covalent
    total=0
    correct=0
    for i in range(10):
        cation, dict2 = random.choice(list(dict["nonmetal"].items()))
        anion, dict3 = random.choice(list(dict["anion"].items()))
        rand1=random.randint(1, 10)
        rand2=random.randint(1, 10)
        question=dict2["Periodic table name"]+str(rand1)+dict3["Periodic table name"]+str(rand2)
        user=input(question)
        answer=(dict["prefix"][rand1-1]+cation+" ")
        answer2=(dict["prefix"][rand1-1]+cation+" ")
        if anion=="oxide":
            if rand2==1:
                answer+="monoxide"
                answer2+="monoxide"
            elif rand2==2:
                answer+="dioxide"
                answer2+="dioxide"
            elif rand2==3:
                answer+="trioxide"
                answer2+="trioxide"
            elif rand2==4:
                answer+="tetraoxide"
                answer2+="tetroxide"
            elif rand2==5:
                answer+="pentaoxide"
                answer2+="pentoxide"
            elif rand2==6:
                answer+="hexaoxide"
                answer2+="hexoxide"
            elif rand2==7:
                answer+="heptaoxide"
                answer2+="heptoxide"
            elif rand2==8:
                answer+="octoxide"
                answer2+="octoxide"
            elif rand2==9:
                answer+="nonoxide"
                answer2+="nonoxide"
            elif rand2==10:
                answer+="decaoxide"
                answer2+="decoxide"
        else:
            answer+=(dict["prefix"][rand2-1]+anion)
            answer2+=(dict["prefix"][rand2-1]+anion)
        x=answer.lower()
        y=answer2.lower()
        answer=x[0:1].upper()+x[1:]
        answer2=y[0:1].upper()+y[1:]
        if user==answer or user==answer2:
            correct+=1
            total+=1
            if answer == answer2:
             print("correct, the answer is "+str(answer))
            else:
              print("correct, the answers could be "+str(answer)+" or "+ str(answer2))

            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            if answer == answer2:
             print("no, the answer is "+str(answer))
            else:
              print("no, the answers could be "+str(answer)+" or "+ str(answer2))
            print("your score is "+str(correct)+"/"+str(total))
def test7():
    #acids: name to formula
    correct=0
    total=0
    for i in range(10):
        name, answer = random.choice(list(dict["acid"].items()))
        user=input(name)
        if user==answer:
            correct+=1
            total+=1
            print("correct, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))
def test8():
    #acids: formula to name
    correct=0
    total=0
    for i in range(10):
        answer, formula = random.choice(list(dict["acid"].items()))
        user=input(formula)
        if user==answer:
            correct+=1
            total+=1
            print("correct, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))

def test9():
    #simple ionic stuff name to formula
    total=0
    correct=0
    for i in range(10):
        cation, dict2 = random.choice(list(dict["cation"].items()))
        anion, dict3 = random.choice(list(dict["anion"].items()))
        answer=cation + " "+ anion
        if int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1 and int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]     
        elif int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]                       
        elif int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))        
        else:
            question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
        user=input(answer)
        if user==question:
            correct+=1
            total+=1
            print("correct, the answer is "+str(question))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(question))
            print("your score is "+str(correct)+"/"+str(total))

def test10():
    #solely multivalent + normal anion name to formula
    total=0
    correct=0
    for i in range(10):
        cation, dict2 = random.choice(list(dict["multivalent cation"].items()))
        anion, dict3 = random.choice(list(dict["anion"].items()))
        answer=cation + " "+ anion
        if int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1 and int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]     
        elif int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]                       
        elif int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))        
        else:
            question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
        user=input(answer)
        if user==question:
            correct+=1
            total+=1
            print("correct, the answer is "+str(question))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(question))
            print("your score is "+str(correct)+"/"+str(total))

def test11():
    #solely polyatomics + normal cations name to formula
    total=0
    correct=0
    for i in range(10):
        choices=["polyatomic cation", "cation", "cation", "cation", "cation", "cation", "cation", "cation" ]
        rand=random.randint(0,7)
        cation, dict2 = random.choice(list(dict[choices[rand]].items()))
        anion, dict3 = random.choice(list(dict["polyatomic anion"].items()))
        answer=cation + " "+ anion
        if int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1 and int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]     
        elif int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            if rand!=0:
                question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"] 
            else:
                question="("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]                                       
        elif int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))        
        else:
            if rand!=0:
                question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
            else:
                question="("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
        user=input(answer)
        if user==question:
            correct+=1
            total+=1
            print("correct, the answer is "+str(question))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(question))
            print("your score is "+str(correct)+"/"+str(total))

def test12():
    #solely multivalent and polyatomic name to formula
    total=0
    correct=0
    for i in range(10):
        choices=["polyatomic cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation"]
        rand=random.randint(0,7)
        cation, dict2 = random.choice(list(dict[choices[rand]].items()))
        anion, dict3 = random.choice(list(dict["polyatomic anion"].items()))
        answer=cation + " "+ anion
        if int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1 and int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]     
        elif int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            if rand!=0:
                question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"] 
            else:
                question="("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]                                       
        elif int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))        
        else:
            if rand!=0:
                question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
            else:
                question="("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))
        user=input(answer)
        if user==question:
            correct+=1
            total+=1
            print("correct, the answer is "+str(question))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(question))
            print("your score is "+str(correct)+"/"+str(total))
        
def test13():
    #everything thats ionic name to formula
    total=0
    correct=0
    for i in range(10):
        choices1=["polyatomic cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "multivalent cation", "cation", "cation", "cation", "cation", "cation", "cation", "cation", "cation", "cation"]
        rand=random.randint(0,16)
        choices2=["polyatomic anion", "polyatomic anion", "polyatomic anion", "polyatomic anion", "anion", "anion", "anion", "anion", "anion"]
        rand2=random.randint(0, 8)
        cation, dict2 = random.choice(list(dict[choices1[rand]].items()))
        anion, dict3 = random.choice(list(dict[choices2[rand2]].items()))
        answer=cation + " "+ anion
        if int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1 and int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            question=dict2["Periodic table name"]+dict3["Periodic table name"]     
        elif int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            if rand!=0:
                question=dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"] 
            else:
                question="("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"]))))+dict3["Periodic table name"]                                       
        elif int(abs(dict3["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))==1:
            if rand2>=4:
                question=dict2["Periodic table name"]+dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))  
            else:
                question=dict2["Periodic table name"]+"("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"]))))  
        else:
            if rand!=0:
                question+=(dict2["Periodic table name"]+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"])))))
            else:
                question+=("("+dict2["Periodic table name"]+")"+str(int(abs((dict3["Charge"])/math.gcd(dict3["Charge"], dict2["Charge"])))))
            if rand2>=4:
                question+=(dict3["Periodic table name"]+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))))
            else:
                question+=("("+dict3["Periodic table name"]+")"+str(int(abs(dict2["Charge"]/math.gcd(dict3["Charge"], dict2["Charge"])))))
        user=input(question)
        if user==answer:
            correct+=1
            total+=1
            print("correct, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(answer))
            print("your score is "+str(correct)+"/"+str(total))

def test14():
    #solely covalent name to formula
    total=0
    correct=0
    for i in range(10):
        cation, dict2 = random.choice(list(dict["nonmetal"].items()))
        anion, dict3 = random.choice(list(dict["anion"].items()))
        rand1=random.randint(1, 10)
        rand2=random.randint(1, 10)
        question=dict2["Periodic table name"]+str(rand1)+dict3["Periodic table name"]+str(rand2)
        answer=(dict["prefix"][rand1-1]+cation+" ")
        answer2=(dict["prefix"][rand1-1]+cation+" ")
        if anion=="oxide":
            if rand2==1:
                answer+="monoxide"
                answer2+="monoxide"
            elif rand2==2:
                answer+="dioxide"
                answer2+="dioxide"
            elif rand2==3:
                answer+="trioxide"
                answer2+="trioxide"
            elif rand2==4:
                answer+="tetraoxide"
                answer2+="tetroxide"
            elif rand2==5:
                answer+="pentaoxide"
                answer2+="pentoxide"
            elif rand2==6:
                answer+="hexaoxide"
                answer2+="hexoxide"
            elif rand2==7:
                answer+="heptaoxide"
                answer2+="heptoxide"
            elif rand2==8:
                answer+="octoxide"
                answer2+="octoxide"
            elif rand2==9:
                answer+="nonoxide"
                answer2+="nonoxide"
            elif rand2==10:
                answer+="decaoxide"
                answer2+="decoxide"
        else:
            answer+=(dict["prefix"][rand2-1]+anion)
            answer2+=(dict["prefix"][rand2-1]+anion)
        x=answer.lower()
        y=answer2.lower()
        answer=x[0:1].upper()+x[1:]
        answer2=y[0:1].upper()+y[1:]
        user=input(answer)
        if user==question:
            correct+=1
            total+=1
            print("correct, the answer is "+str(question))
            print("your score is "+str(correct)+"/"+str(total))
        else:
            total+=1
            print("no, the answer is "+str(question))
            print("your score is "+str(correct)+"/"+str(total))



