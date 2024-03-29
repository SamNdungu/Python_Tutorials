### Scientific Computing with Python Projects

It's time to put your Python skills to the test. By completing these projects, you'll demonstrate that you have a strong foundational knowledge of Python. And you'll qualify for freeCodeCamp's Scientific Computing with Python Certification.


1. **Arithmetic Formatter**
   

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

[See full instructions here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter)


See the full solution on replit [Here](https://replit.com/@WsNdungu/boilerplate-arithmetic-formatter-3)


2. **Time Calculator**
   

Write a function named add_time that takes in two required parameters and one optional parameter:

- A start time in the 12-hour clock format (ending in AM or PM)
- A duration time that indicates the number of hours and minutes
- A starting day of the week, case insensitive (optional) 

The function should add the duration time to the start time and return the result.


[See full instructions here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator)


See the full solution on replit [Here](https://replit.com/@WsNdungu/boilerplate-time-calculator-2#time_calculator.py)


3. **Budget App**
    

Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:

- A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
- A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
- A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
- A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
- A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.


[See full instructions here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app)


See the full solution on replit [Here](https://replit.com/@WsNdungu/boilerplate-budget-app#budget.py)


4. **Polygon Area Calculator**
   

In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.

*`Rectangle class`*
When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

- set_width
- set_height
- get_area: Returns area (width * height)
- get_perimeter: Returns perimeter `(2 * width + 2 * height)`
- get_diagonal: Returns diagonal `((width ** 2 + height ** 2) ** .5)`
- get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line `(\n`) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
- get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.


[See full instructions here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator)


See the full solution on replit [Here](https://replit.com/@WsNdungu/boilerplate-polygon-area-calculator#shape_calculator.py)



5. **Probability Calculator**
   

Suppose there is a hat containing` 5 blue balls, 4 red balls, and 2 green balls`. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.

First, create a Hat class in prob_calculator.py. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:


[See full instructions here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator)


See the full solution on replit [Here](https://replit.com/@WsNdungu/boilerplate-probability-calculator#prob_calculator.py)