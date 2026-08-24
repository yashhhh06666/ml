# ml
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

def Fact(n):
    if n== 0:
        return 1
    else:
        return n * Fact(n-1)

--------------------

Stack -> Lifo--500,99,77

--------------------------------------------
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
-> ML is the process in which a computer analyes data,learn patternfrom it,and make predicatoin or desicions automatically

# What is Learnig 
 -> Learnig is the process of gaining knowledge or improving performance by using experience by using experience, practice, or data.

# Day 5

Knowledge = information prodessing

infomation = raw data processing 

raw data = from the surrounding

<!-- What is AI -->

-------------

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

# ML Types -->
ML have Four Types 
 
1. Supervised Learing
and its learned from the past 
  mai mere pass input and output hota hai  
    1. Regression("Agar o/p no. mai arra hai to vo Reg.")
    2. Classification("Agar o/p word. mai arra hai to vo Classification.")
2. Un-Supervised Learing
  mai mere pass input and output nahi hota hai
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



 # linear Reg. -->
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

# Day 8
Today we make a new file called num_liner_reg.py 

"num_liner_reg.py" have to use prediect Marks 

<!-- ML Lib  -->
seaborn use for Advance Graph
pandas use for manuplation
NumPy use for Array 
matplotlib Use for make a Graph 

<!-- Get Dataset -->

# Day 9

# Linear Reg. -->

X kya hI INDEPENDENT Var.
Y kya hI DEPENDENT Var.

Eqn of Lin
# MSE  -->
MSE Squared Error (MSE) is a method us ed to measure how accurately a reg. Model predicts the traget Value 
EX 
suppose our model pre
how to cal. MSE:
 mse = 4+4+4+4/4
    =5.35

# Day 10 

# Logistic Reg.  -->
A superviesd ML algo. used for Classification problems. 
is not used for Predicting Contionus Values .
its predict the the probablity.

based on sigmod(logistic) fun.

-for ex 

 0.98 
 0.18 

 types of Logistic
 1. binary
 2. Multinomial
 3. Ordinal 

 # Day 11

# KNN (K Nearest Neibour)
 Euclidian Method used to calculate distance b\w two points 
 formula =\(\sqrt{(x_{1}+x_{2})^{2}+(y_{1}+y_{2})^{2}}\)

 # Day 12 

# Decision Tree -->
Decision Tree is a supervised ML Algo.used for classification and regression . It Make decision by Askin a series of que splitting the data into branches 

Process of cleaning Data is called 

have two criterion 
 1. Gini 
 2. Entropy

also make a file called Decision_tree.py


# Day 13 

overfiting and underfiting
# overfiting -->
Overfitting happens when a machine learning model learns the training data too well

 -- Reason 
    1. Noisy Garbage Data
    2. Complex Model 

How to Avoid 
1. Removing Features 
2. Early stopping the traning 
3. Complex Model
4. Traning the Model with Sufficient data
5. using cross-validation 

#  underfitting -->
Underfitting happens when a machine learning model is too simple to learn the true patterns in data

-- reason  
1. Noisy Garbage Data
2. Simple Data 

How to Avoid
1. More traning to the Model 
2. Increase the model Complexity 

# SVM  -->
A Support Vector Machine (SVM) is a powerful supervised machine learning algorithm use for classification, though it can also handle regression tasks. 

also called Hyperplane 

# DAY 14 
confusien matrix 
types 

<!-- Naive Bayes -->
Naive Bayes is a supervised ML Classification algo. based on Bayes' Theorm      

# Day 15

# Random Forest -->
Random Forest is a ml algo that uses for many decision trees to make better pred.

<!-- random forest effective  -->
1. high Accuracy 
2. handle missing valu e
3. reduse over fitting 

# Day 16 

basic Format of writing a code 

1. import lib 
like :-
    import pandas when u have a csv file
    import numpy when u matrix and array 
    import matplotlib when u have to create a Graph 
    import Seaborn its advance version of matplotlib 

    *import sklearn its change Acrdn to What Algo. u use 

2. Data set 
     means when u have a CSV file insert it and access it 
     then , 
    give X, Y values 
    X independent Vules
    Y dependent Vules

    When u did'nt have a CSV file 
    U have to make a own data Dictinory 
    then provide X and Y value 

3. Train dataset and Give Algo name 
    when u have a CSV file
     
     X_Train, X_Test, Y_Train,
     Y_Test = train_test_split(X, Y,test_size=0.2, random_state=42)
    <!-- Algo name  -->
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_Train, Y_Train)

    when u did'nt have a CSV file
    <!-- Algo name  -->
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_Train, Y_Train)

4. Predicte a Data  
    Now u have to make a var. that data pred. 
     
