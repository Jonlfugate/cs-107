__author__ = 'jonatahn fugate'
import sys
x = 0
z_valid = False
q_valid = False
w_valid = False
e_valid = False
x_valid = False
while True:
    if x == 0:
        x = raw_input(
            "Welcome. Please select a Option: \n#1 Area of a sqaure. \n#2 Area of a right triangle. \n#3 Area of a circle. \n#4 Exit. \nChoice: ")
        while not x_valid:
            try:
                t = int(x)
                x_valid = True
            except:
                x = raw_input("Enter a valid number: ")
                x_valid = False
    elif x < 5:
        x = raw_input("Ener a valid number: ")

    elif int(x) == 1:
        z = raw_input("Please enter the length of your square (whole number) : ")
        while not z_valid:
            try:
                t = int(z)
                z_valid = True
            except:
                z = raw_input("Enter a valid number: ")

        print "your area is", int(z) * int(z)
        x = 0
        z_valid = False
        x_valid = False
    elif int(x) == 2:
        q = raw_input("Please enter the height of your triangle (whole number): ")
        while not q_valid:
            try:
                t = int(q)
                q_valid = True
            except:
                q = raw_input("Enter a valid number: ")
        w = raw_input("Please enter the base of your triangle (whole number): ")
        while not w_valid:
            try:
                t = int(w)
                w_valid = True
            except:
                w = raw_input("Enter a valid number: ")

        print "your area is", .5 * int(w) * int(q)
        x = 0
        q_valid = False
        w_valid = False
        x_valid = False

    elif int(x) == 3:
        e = raw_input("Please enter the radi of your circle (whole number): ")
        while not e_valid:
            try:
                t = int(e)
                e_valid = True
            except:
                e = raw_input("Enter a valid number: ")

        print "your area is", 3.14159 * (float(e) * float(e))
        x = 0
        e_valid = False
        x_valid = False

    elif int(x) == 4:
        exit


def check_valid_number(number):
    try:
        number = int(number)
        return True
    except:
        return False


def prompt_user(prompt):
    while True:
        user_choice = raw_input(prompt)
        if check_valid_number(user_choice):
            return user_choice
        else:
            print "Invalid Choice!\n"


def compute_square():
    x = prompt_user("Please enter the length of your square (whole number): ")
    print "The area of your square is: %i" % (int(x)*int(x))


def do_computation(choice):
    if choice == 1:
        compute_square()
    elif choice == 2:
        compute_right_tri()
    elif choice == 3:
        compute_circle()
    elif choice == 4:
        sys.exit(0)
    else:
        print "Please Choose a valid option!\n"


def main():
    print "Welcome. Please select a Option: \n"
    while True:
        user_choice = raw_input(
            "#1 Area of a sqaure. \n#2 Area of a right triangle. \n#3 Area of a circle. \n#4 Exit. \nChoice: ")
        if check_valid_number(user_choice):
            do_computation(int(user_choice))
        else:
            print "Please Choose a valid option!\n"

if __name__ == "__main__":
    main()

#Add Area of Rectangle and Area of Cylinder