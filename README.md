1. # MC.py - Mathematical Calculator
def calculator():
    print("=== MATHEMATICAL CALCULATOR [MC] ===")
    print("Operators: +  -  *  /  %  ^   |   C = Clear   |   OFF = Exit")
    
    while True:
        expr = input("\nEnter calculation: ").strip()
        
        if expr.upper() == "OFF":
            print("Calculator OFF. Goodbye!")
            break
        elif expr.upper() == "C":
            print("Cleared.")
            continue
        
        try:
            # Replace ^ with ** for Python power
            expr = expr.replace('^', '**')
            result = eval(expr)  # eval is fine here for a simple school task
            print(f"Result = {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception:
            print("Error: Invalid input. Use numbers and + - * / % ^ only.")

if __name__ == "__main__":
    calculator()



    2.# PPC.py - Personal Pocket CGPA Calculator
def grade_to_point(grade):
    grade = grade.upper().strip()
    if grade == "A":
        return 5
    elif grade == "B":
        return 4
    elif grade == "C":
        return 3
    elif grade == "D":
        return 2
    elif grade == "E":
        return 1
    elif grade == "F":
        return 0
    else:
        return None  # invalid grade

def cgpa_calculator():
    print("=== PERSONAL POCKET CGPA CALCULATOR [PPC] ===")
    print("Enter courses. Type 'DONE' when finished.\n")
    
    total_quality_points = 0
    total_units = 0
    
    while True:
        course = input("Course code or name [or DONE]: ").strip()
        if course.upper() == "DONE":
            break
        
        try:
            units = float(input(f"  Units for {course}: "))
            grade = input(f"  Grade for {course} [A-F]: ")
        except ValueError:
            print("  Invalid units. Try again.")
            continue
        
        gp = grade_to_point(grade)
        if gp is None:
            print("  Invalid grade. Use A, B, C, D, E, F.")
            continue
        
        quality_point = units * gp
        total_quality_points += quality_point
        total_units += units
        print(f"  -> {units} x {gp} = {quality_point}\n")
    
    if total_units > 0:
        cgpa = total_quality_points / total_units
        print("\n=== RESULT ===")
        print(f"Total Units: {total_units}")
        print(f"Total Quality Points: {total_quality_points}")
        print(f"Your CGPA: {cgpa:.2f} / 5.00")
    else:
        print("No courses entered.")

if __name__ == "__main__":
    cgpa_calculator()
    
