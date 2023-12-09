import periodictable
import random
from decimal import Decimal, getcontext 

def metal():
    rand = random.randint(0,11)
    metals = [2,3,10,11,18,19,36,37,54,55,86,87]
    return metals[rand]

def nonmetal():
    rand = random.randint(0,8)
    nonmetals = [6,7,8,14,15,16,33,34,52]
    return nonmetals[rand]

def charge(elm):
    metals = [2,3,10,11,18,19,36,37,54,55,86,87]
    nonmetals = [6,7,8,14,15,16,33,34,52]
    for i in range (11):
        if (metals[i]==elm):
            return -(i%2+1)
    if (elm == 6 or elm ==14):
        return 3
    elif (elm == 7 or elm ==15 or elm == 33):
        return 2
    else:
        return 1

Elements = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P",
    "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", 
    "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce",
    "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf",
    "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
    "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", 
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Uut",
    "Fl", "Uup", "Lv", "Uus", "Uuo"]


Molar_mass = {element.symbol: element.mass for element in periodictable.elements}


def find_mass():
    elm = random.randint(0,117)
    mol = random.randint(1,5)
    print("What is the mass of "+str(mol)+Elements[elm]+"?(round to the tenth decimal place)")
    
    ans = mol*Molar_mass[Elements[elm]]
    ans = round(ans,1)
    #ans input here
    user_input = float(input())
    if (user_input==ans):
        print("correct")
    else:
        print("incorrect, the answer is: "+str(ans)+"g")

def find_mol():
    elm = random.randint(0,117)
    m1 = Molar_mass[Elements[elm]]*random.randint(1,5)+random.randint(1,40)
    print("How many mols of "+Elements[elm]+" are present if there is "+str(m1)+"g?(round to the tenth decimal place)")
    
    ans = m1/Molar_mass[Elements[elm]]
    ans = round(ans,1)
    #ans input here
    user_input = float(input())
    if (user_input==ans):
        print("correct")
    else:
        print("incorrect, the answer is: "+str(ans)+" mols.")
    
def lim_reag():
    elm1 = metal()
    elm2 = nonmetal()
    chg1 = charge(elm1)
    chg2 = charge(elm2)
    m1 = random.randint(1,5)*Molar_mass[Elements[elm1]]+random.randint(1,50)
    m2 = random.randint(1,5)*Molar_mass[Elements[elm2]]+random.randint(1,50)
    count1 = 1
    count2 = 1
    while (count1*chg1+count2*chg2!=0):
        if (abs(count1*chg1)<abs(count2*chg2)):
            count1+=1
        else:
            count2+=1
    print ("If "+str(m1)+" grams of "+Elements[elm1]+" reacted with "+str(m2)+" grams of "+Elements[elm2]+" creates "+Elements[elm1]+"("+str(count1)+")"+Elements[elm2]+"("+str(count2)+") which element is the limiting reageant?")
    user_input = input()
    if (m1/Molar_mass[Elements[elm1]]>m2/Molar_mass[Elements[elm2]]):
        ans = Elements[elm1]
    elif (m1/Molar_mass[Elements[elm1]]==m2/Molar_mass[Elements[elm2]]):
        ans = "N/A"
    else:
        ans = Elements[elm2]

    if (user_input==ans):
        print("correct")
    else:
        print("incorrect, the answer is: "+ans)

find_mass()
find_mol()
lim_reag()