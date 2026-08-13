# ml(Machine Learning with Python)
Internship 
-----------
Day 1 

Basic Functions - Group of block - 

Data Type Required:- Array

Need to Improve - Loops, types of loops
, Nested Loop ,Function, Type of Functions , Array , recursive functions 

--_-----_-----_----

Day2 ---

{• what is recursive functions •
-> recursive functions call it self unit the given condition is true }

formula :- fact(n)=n*fact(n-1)
           fact(0)=1

example:- fact(5)=?

n=5
fact(5)=5*fact(5-1)
fact(5)=5*fact(4)
fact(4)=5*fact(3)
.
.
.
n times 
until value met✅

fact5*4*3*2*1*1 = ?

------------------------------

recurcive

fact(n)=n*fact(n-1)
n=5
fact(5)=5*fact(5-1)  

fact(5)=5*fact(4)
fact(4)=4*fact(3)
fact(5)=5*fact(2)
fact(5)=5*fact(1)
fact(5)=5*fact(0)

back tracking -- return back 
function -> fun Def. -> Code of Block -> Activation record(Memory Address)

---------------------

facto(5)=5*4*3*2*1


loop - cycle - 
loop( k= 5 to 1)

result= result*k



<!-- WE Have to learn  -->
!.. (function , loop and Nested loop or array
, Recursion .)

-------------------------
     Day 3
     
def Fact(n):
    if n== 0:
        return 1
    else:
        return n * Fact(n-1)

--------------------

Stack -> LIFO--500,99,77
-------------

#       Day 4

we install Pandas or install Django 
or Sir nee nahi padhyai 

fact. ke hi program hai.....................

def add(n):
    if n == 0:
        return 0
    else:
        return n+add(n-1) 

n = int(input("enter a number: "))
z = add(n)

print(z)

iska output n number ko 
n+n+n+n...+0 
tak 



#  ML  

# What is Machine Learning 
-> ML is the process in which a computer analyes data,learn patternfrom it,and make predicatoin or desicions automatically.

# What is Learnig 
 -> Learnig is the process of gaining knowledge or improving performance by using experience by using experience, practice, or data.


# Day 5

Knowledge = information prodessing

infomation = raw data processing 

raw data = from the surrounding

<!-- What is AI -->

# Day 6 

Moduels 

first mak a  main file

and made anoter file called exe_mod
import Main file ame 
and another metod 
from Main file ame import * 
*("* this can imoprt all fun. from Main file ame ")

dir("pandas")

--------------------

we have to learn 
algebra, Static , Calculas , probelity

Duler Theorm 

<!-- topic Numpy  -->

NumPy Provides Two Fundamental Object 
1. N-dimensional Array Object 
2. A Universal Function Object 

zero= np.zeros((2, 3))
This create a 2x3 arr, and every value must be 0 
one= np.ones((3, 2))
This create a 3x2 arr, and every value must be 1
ranges= np.arange(0, 10, 2)
this use as Start , Stop , Skip 


# Day 7
<!-- ML  -->
first we give data to ML then analyses Past Data then trains , Then predicts Output 
- Application 
       Face rec. , Healthcare, alexa , swiggy, Weather Casting

<!-- ML Types -->
ML have Four Types 
 
1. Supervised Learing
    1. Regression("Agar o/p no. mai arra hai to vo Reg.")
    2. Classification("Agar o/p word ya text mai to vo hai to vo Classification.")
2. Un-Supervised Learing

3. reinforcement learning

4. semi-supervised learning

<!-- process involved in ML -->
1. Data Gathering 
2. Data pre-processing 
3. Choose Model
4. Train Model 
5. Test Model
6. Tune Model
7. prediction("*BEST FITLINE*")

<!-- Algorithms -->
1. linear Reg.
2. Logistic Reg.
3. Decision Tree
4. Random Forest 
5. K Nearest Neighbors 



 <!-- linear Reg. -->
 liner reg. is a linear modeling approch to find a realn btw one or more independent Varaible 
  .csv file = comma seprated value 
    name,age,add,
    aman,18,'bhopal'
  .tsv file = Tab seprated value
name    age     add 


<!-- Implementation of liner Reg. -->
1. Load the lib 
importing the lib 

2. Import the dataset 

3. Visualize the Data 
Visualize the dataset

4. split the data into traning and testing set
spliting the data into traning and testing set

5. Fit simple Linear reg.

6. predict the test set 

7. Visualize the train set result

8. Visualize the test set result 

9. Calculating the residuals
