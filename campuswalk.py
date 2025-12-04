import turtle
import sys


#print("argv:", sys.argv)  # DEBUG

if len(sys.argv) > 1:
        n = int(sys.argv[1])

##else:
##      n = int(input("Enter the path number (1 to 20): "))
#print("Using path number:", n) #debug


#n = int(input("Enter the path number (1 to 20): "))

 # --- 1. Set up the drawing screen ---
screen = turtle.Screen()
screen.bgpic("pes.gif") # Using the exact uploaded filename
screen.setup(width=800, height=600)
screen.title("PES Campus Map")


 # --- 2. Initialize the Path Tracer Turtle (x) ---
x = turtle.Turtle()
x.speed(2)
x.pensize(3)
x.color("blue")
x.shape("triangle")
x.shapesize(0.5)


 # --- 3. Initialize the Label Turtle (label_turtle) ---
 # We use a separate turtle for writing text so it doesn't interfere with the path drawing.
label_turtle = turtle.Turtle()
label_turtle.speed(0)  # Fastest speed, since we just need to place the text once
label_turtle.penup()   # Important: Do not draw while moving the label
label_turtle.hideturtle()  # Make the turtle icon invisible


#--F-BLOCK--
text_x, text_y = -55, -175 #Coordinates
# Move the label turtle to the desired location and write the text
label_turtle.goto(text_x, text_y)
label_turtle.color("brown")# Use a striking color for the label
# Write the text "F Block" with a clear font and size
label_turtle.write("F Block", align="center", font=("Inter", 10,"bold" ))

#--GJBC--
text_x, text_y = 0,-100#coordinates
 # Move the label turtle to the desired location and write the text
label_turtle.goto(text_x, text_y)
label_turtle.color("brown")# Use a striking color for the label
 # Write the text "GJBC" with a clear font and size
label_turtle.write("GJBC", align="center", font=("Inter", 10,"bold" ))

#--MRD--
text_x, text_y = 130,-100#coordinates
# Move the label turtle to the desired location and write the text
label_turtle.goto(text_x, text_y)
label_turtle.color("brown")# Use a striking color for the label
# Write the text " M.R.D Auditorium" with a clear font and size
label_turtle.write("M.R.D Auditorium", align="center", font=("Inter", 5,"bold" ))




# --- 4. Path Tracing Logic  ---

# Starting Position Adjustment
def start_point_MainGate():
	x.hideturtle()
	x.penup()
	x.goto(70, -250) # Start near the main entrance
	x.setheading(90) # Face North (up)
	x.pendown()
	x.showturtle()

def start_point_GJBC():
	x.hideturtle()
	x.penup()
	x.goto(60,-110) # Start near the GJBC Block
	x.setheading(90) # Face North (up)
	x.pendown()
	x.showturtle()

def start_point_OpenTheater():
	x.hideturtle()
	x.penup()
	x.goto(60,-75) # Start near the Open Theater
	x.setheading(90) # Face North (up)
	x.pendown()
	x.showturtle()

def start_point_FBlock():
	x.hideturtle()
	x.penup()
	x.goto(-80, -150) # Start near the F Block
	x.setheading(90) # Face North (up)
	x.pendown()
	x.showturtle()

def start_point_BEBlock():
	x.hideturtle()
	x.penup()
	x.goto(85,-55) # Start near the B Block--
	x.setheading(90) # Face North (up)
	x.pendown()
	x.showturtle()


#---------------5. Path Tracing----------------------------

#FROM MAIN GATE

if n == 1:
    start_point_MainGate()
    print("Tracing path from Main Gate to F block.")
    #to F block
    x.forward(119)
    x.left(100) # Turn 100 degrees left
    x.forward(140)

elif n == 2:
    start_point_MainGate()
    print("Tracing path from Main Gate to GJBC block .")
    # to GJBC block 1
    x.forward(140)
    x.left(90)
    x.forward(15)

elif n == 3:
    start_point_MainGate()
    print("Tracing path from Main Gate to BE block.")
    # to BE block (Moving North, then around B-Block)
    x.forward(194)
    x.right(90) # Turn 90 degrees right (East)
    x.forward(30)
    x.left(90) # Turn 90 degrees left (North)

elif n == 4:
    start_point_MainGate()
    print("Tracing path from Main Gate to Open Air Theater.")
    # open air theater 
    x.forward(180)
    x.right(90) # Turn 90 degrees right (East)
    x.forward(20)




#FROM F BLOCK
elif n == 5:
    start_point_FBlock()
    print("Tracing path from F block to GJBC block .")
    # to GJBC block 1 
    x.right(83) 
    x.forward(147)
    x.left(90) 
    x.forward(20)

elif n == 6:
    start_point_FBlock()
    print("Tracing path from F block to Main Gate.")
    # to Main Gate
    x.right(83)
    x.forward(142)
    x.right(90)
    x.forward(110)

elif n == 7:
    start_point_FBlock()
    print("Tracing path from F block to Open air theater.")
    # to Open air Theater
    x.right(83) 
    x.forward(147)
    x.left(90) 
    x.forward(50)

elif n == 8:
    start_point_FBlock()
    print("Tracing path from F block to BE Block.")
    # to BE Block
    x.right(83)
    x.forward(147)
    x.left(90) 
    x.forward(72)
    x.right(90)
    x.forward(20)
    



#FROM GJBC BLOCK
elif n == 9:
    start_point_GJBC()
    print("Tracing path from  GJBC block  to Main Gate.")
    # to Main Gate
    x.setheading(276) 
    x.forward(140)

elif n == 10:
    start_point_GJBC()
    print("Tracing path from  GJBC block  to F block.")
    # to F block  
    x.setheading(270)
    x.forward(20)
    x.right(84)
    x.forward(140)
    
elif n == 11:
    start_point_GJBC()
    print("Tracing path from  GJBC block  to  BE Block .")
    # to  BE Block
    x.forward(47)
    x.right(80)
    x.forward(17)

elif n == 12:
    start_point_GJBC()
    print("Tracing path from  GJBC block  to Open air theater .")
    # to GJBC block Open air theater
    x.forward(30)
   




# FROM BE BLOCK
elif n == 13:
    start_point_BEBlock()
    print("Tracing path from BE Block to Main Gate.")
    # to Main Gate
    x.forward(1)
    x.left(90)
    x.forward(30)
    x.left(95)
    x.forward(194)
    
  
elif n == 14:
    start_point_BEBlock()
    print("Tracing path from BE Block to F block.")
    # to F block
    x.left(90)
    x.forward(25)
    x.left(89)
    x.forward(75)
    x.right(82)
    x.forward(147)

elif n == 15:
    start_point_BEBlock()
    print("Tracing path from BE Block to GJBC block .")
    # to GJBC block 1
    x.forward(1)
    x.left(105)
    x.forward(25)
    x.left(83)
    x.forward(47)

elif n == 16:
    start_point_BEBlock()
    print("Tracing path from BE Block to Open air theater.")
    # to Open air theater
    x.forward(1)
    x.left(105)
    x.forward(25)
    x.left(83)
    x.forward(15)




#FROM OPEN AIR THEATER
elif n == 17:
    start_point_OpenTheater()
    print("Tracing path from Open air theater to Main Gate.")
    # to Main Gate 
    x.setheading(275)
    x.forward(160)
    

elif n == 18:
    start_point_OpenTheater()
    print("Tracing path from Open air theater to F block.")
    # to F block
    x.setheading(270)
    x.forward(55)
    x.right(83)
    x.forward(140)

elif n == 19:
    start_point_OpenTheater()
    print("Tracing path from Open air theater to GJBC block .")
    # to GJBC block 1
    x.setheading(270)
    x.forward(30)

elif n == 20:
    start_point_OpenTheater()
    print("Tracing path from Open air theater to  BE Block.")
    # to  BE Block
    x.forward(15)
    x.right(80)
    x.forward(17)



else:
    print(f"Path number {n} is not defined (Please enter 1 to 20).")


# Keeps the turtle graphics window open until manually closed
turtle.done()
