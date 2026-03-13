# 1. Description
## PDA pizzeria
This is a simple PDA application for a pizzeria written in Python. The user might place orders, modify them and print receipts. Directions are provided when the application starts.

# 2. Features
* The application has a simple built-in menu of a pizzeria.
* Processes orders using Python lists
* Displays the current state of the order, after each modification of it
* The user has the ability to modify any item in the order, in case they made a mistake
* Updates automatically the quantity of an item, if the item is added again in the order
* Print the ordrer 's receipt

# 3. Technologies
* Python3
* Lists
* Parallel Lists
* Loops

# 4. Execute the program
1. Save the script as:
   pizzeria_PDA.py
2. Run the program:
   python pizzeria_PDA.py

# 5. Structure
PDA-pizzeria/    

├── foodMenu.py         # Main program
└── README.md           # Project Documentation

# 6. Example Output

``` plaintext

* * * * * * Menu * * * * * *
----------------------------
1  Margherita          6.5       
2  Farm House          6         
3  Peppy Paneer        7.5       
4  Mexican Green Wave  7         
5  Deluxe Veggie       8         
6  Veg Extravaganza    8.5       
7  Cheese n Corn       5         
8  Fresh Veggie        5.5       
9  Veggie Paradise     6.5       
10 Special             9         
----------------------------
Would you like to place an order? yes/no: yes
Place your order, Pick a number to choose a pizza and after that type the quantity of that product.
If you like to stop, type -1
Press 0 to modify your order
Choose a number between 1 and 10: 1
Type the quantity of that product: 2
2  Margherita          13.0      
----------------------------
13.0
Choose a number between 1 and 10: 7
Type the quantity of that product: 1
2  Margherita          13.0      
1  Cheese n Corn       5         
----------------------------
18.0
Choose a number between 1 and 10: 0
2  Margherita          13.0      
1  Cheese n Corn       5         
----------------------------
18.0
Which row would you like to modify? 1
Type the new quantity: 1
1  Margherita          6.5       
1  Cheese n Corn       5         
----------------------------
11.5
Choose a number between 1 and 10: 0
1  Margherita          6.5       
1  Cheese n Corn       5         
----------------------------
11.5
Which row would you like to modify? 2
Type the new quantity: 0
1  Margherita          6.5       
----------------------------
6.5
Choose a number between 1 and 10: 10
Type the quantity of that product: 2
1  Margherita          6.5       
2  Special             18        
----------------------------
24.5
Choose a number between 1 and 10: -1
1  Margherita          6.5       
2  Special             18        
----------------------------
24.5
1  Margherita          6.5       
2  Special             18        
----------------------------
Checkout:              24.5

Process finished with exit code 0

```

# 7. Future Improvements
Some future improvements I keep in mind are:
* Keep track of orders using a database
* Make the program flexible by creating a non-stable menu
* Re-write the program using object-oriented programming
  
# 8. Author
Nikos Misailidis 
GitHub: https://github.com/NiMisa179
