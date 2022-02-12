# %% [markdown]
# # If Statment with Odd and even

# %%
UserNum = int(input("Please enter your num: "))

if UserNum % 2==1:
    print("your num is odd !")
# you have to use == to get right answer
if UserNum %2 == 0:
    print("Your num is even ")


# %%
UserNum = int(input("Please enter your num: "))

if UserNum % 2==1: # % means mod
    print("your num is odd !")
# you have to use == as compariosn operqator to get right answer
else:
    print("your num is even !")


# %% [markdown]
# # Nested if structure

# %% [markdown]
# run first if, if passed it will run into the second if before goes else which is part of the first if Block
# 
# if condition:
#     if another condition:
#     do this
#     else:
#     do this
# else:
#     do this

# %%
print("Welcome to the rollercoaster !")
height= int(input("What is your age: "))

if height>=120:
    print("You can ride the rollercoaster !")

    age = int(input("Please enter your age: "))

    if age<=18:
        print("Please pay $7")
    else: 
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller")

# %% [markdown]
# # If and Elif Block

# %%
print("Welcome to BMI calculator !")

height= float(input("What is your height: "))
weight= float(input("What is your weight: "))

BMI = round(weight/height*height)

if BMI<18.5:
    print( "Your BMI is " + str(BMI) + " you are underwight !")

elif BMI<25:
    print("Your BMI is " + str(BMI) + " you have normal BMI !")

elif BMI>25<50:

    print("Your BMI is " + str(BMI)+ " you have different BMI !")
# if all conditions of if and elif are not met, then the code will reach else of the first block.
else:
    print("You are at risk ! ")


# %% [markdown]
# # Leap Year Excercise

# %%
Year = int(input("Please enter the year: "))

if Year % 4 ==0:
# IF DEIVISBLE IF 4, THEN CHECK NEXT IF CONDITION
  if Year %100 ==0:
  # IF IF DEIVISBLE IF 100=0, THEN CHECK NEXT IF CONDITION
    if Year% 400 ==0:
      print("Leap Year")
    else:
      # SECOND PART OF THIRD IF 
      print("Not leap year")
  else:
    # SECOND PART OF SECOND IF 
    print("leap year")
else:
  # SECOND PART OF FIRST IF
  print("Not leap year")

# %%
print("Welcome to the rollercoaster !")
height= int(input("What is your height in cm: "))

if height>=120:
    print("You can ride the rollercoaster !")

    age = int(input("Please enter your age: "))

    if age<12:
        bill=5
        print("Child tickets are $5")
       
    elif age <=18:
        bill = 7
        print("Youth tickets are $7 ")
    else:
        bill= 12
        print("Adults tickets are $12.")
    wantsPhoto = input("Do you want your photo taken? Y or N.")
    #if wantsPhoto =="y":
    #    if wantsPhoto =="no":
            #wantsPhoto.capitalize()

    if wantsPhoto =="Y":
      # add three dollars
      bill += 3
    print(f"your final bill is {bill}")
else:
    print("Sorry, you have yp grow taller before you can ride ")

# %% [markdown]
# # Pizza Shop with if

# %% [markdown]
# # Instruction
# Make sure that size of pizza has all if,elif and else indented under IF
# Make sure that add pepproni has all if,elif and else indented under IF
# Make sure that add cheese has all if,elif and else indented under IF
# keep bill under each if,elif and else indented under IF

# %%
size= input("Please select your pizza size:")
bill =0

if size.upper()== "S":
  bill +=15
elif size.upper()=="M":
  bill+=20
elif size.upper()=="L":
  bill +=25

Add=input("Add pepperoni, Y Or N ")

if Add.upper()=="Y":
  if size.upper()=="S":
    bill+=2
  else:
    bill+=5
cheese =input("Add Cheese: Y or N")
if cheese.upper()=="Y":
  bill +=1

# use f" {}" to keep text and variable value in one sentence
print(f"your ginal bill is ${bill}")



