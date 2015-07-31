__author__ = 'jonatahn fugate'
import sys


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
    x = prompt_user("Please enter the length of your Square (whole number): ")
    print "The area of your Square is: %i" % (int(x) * int(x))


def compute_rectangle():
    x = prompt_user("Please enter the height of your Rectangle (whole number):  ")
    y = prompt_user("Please enter the length of your Rectangle (whole number):  ")
    print "The area of your Rectangle is: %i" % (int(x) * int(y))


def compute_right_tri():
    x = prompt_user("Please enter the height of your Right Triangle (whole number): ")
    y = prompt_user("Please enter the length of your Right Triangle (whole number): ")
    print "The area of your Right Triangle is: %f" % ((int(x) * int(y)) / int(2))


def compute_circle():
    x = prompt_user("Please enter the radius of your Circle: ")
    print "The area of your Circle is: %f" % (3.14159 * ((float(x) * float(x))))


def compute_cylinder():
    x = prompt_user("Please enter the radius of your Cylinder: ")
    y = prompt_user("Please enter the height of your Cylinder: ")
    print "The area of your Cylinder is: %f" % (2 * 3.14159 * float(x) * float(y) + 2 * 3.14159 * (float(x) * float(x)))


def do_computation(choice, user_name):
    if choice == 1:
        compute_square()
    elif choice == 2:
        compute_rectangle()
    elif choice == 3:
        compute_right_tri()
    elif choice == 4:
        compute_circle()
    elif choice == 5:
        compute_cylinder()
    elif choice == 6:
        print "Good bye %s" % (user_name)
        sys.exit(0)
    else:
        print "Please Choose a valid option!\n"


def main():
    print "Hello and welcome my name is Area-O-tron-9000"
    user_name = raw_input("What is your name? : ")
    print "Hello %s, I am here to calculate the area of different shapes.\nChose any of these choices" % user_name

    while True:
        print "#1 Area of a Square.\n#2 Area of a Rectangle.\n#3 Area of a Right Triangle.\n#4 Area of a Circle."
        print "#5 Area of a Cylinder.\n#6 Exit. "
        user_choice = raw_input("\nChoice: ")
        if check_valid_number(user_choice):
            do_computation(int(user_choice), user_name)
            print "\nI like problems, give me another!!\n"
        else:
            print "Please Choose a valid option!\n"


if __name__ == "__main__":
    main()