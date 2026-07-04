# MC.py - Mathematical Calculator
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
    