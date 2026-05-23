class Calculator:
    
    
    def _init_(self):
        
        self.history = []

    def add(self, a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        result = a + b
        self._record_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Returns the difference of two numbers."""
        result = a - b
        self._record_history(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Returns the product of two numbers."""
        result = a * b
        self._record_history(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """
        Returns the quotient of two numbers.
        Applies defensive programming to prevent ZeroDivisionError.
        """
        if b == 0:
            raise ValueError("Execution Blocked: Division by zero is mathematically undefined.")
        
        result = a / b
        self._record_history(f"{a} / {b} = {result}")
        return result

    def _record_history(self, operation: str):
        """Internal helper method to track operations."""
        self.history.append(operation)

    def get_history(self):
        """Returns all operations performed in this session."""
        return self.history


def run_interface():
    """Runs a clean, robust command-line interface for the user."""
    calc = Calculator()
    print("=== OO-Architecture Calculator Engine initialized ===")
    print("Available operations: +, -, *, /, history, exit")
    
    while True:
        try:
            choice = input("\nEnter operation sign (+, -, *, /) or keyword: ").strip().lower()
            
            if choice == 'exit':
                print("Shutting down engine. Goodbye!")
                break
                
            if choice == 'history':
                history = calc.get_history()
                if not history:
                    print("No operations recorded yet.")
                else:
                    print("\n--- Session History ---")
                    for record in history:
                        print(record)
                continue

            if choice not in ['+', '-', '*', '/']:
                print("Invalid input. Please choose a valid operator.")
                continue

            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            
            if choice == '+':
                print(f"Result: {calc.add(num1, num2)}")
            elif choice == '-':
                print(f"Result: {calc.subtract(num1, num2)}")
            elif choice == '*':
                print(f"Result: {calc.multiply(num1, num2)}")
            elif choice == '/':
                print(f"Result: {calc.divide(num1, num2)}")

        except ValueError as error:
            
            print(f"Application Error: {error}")
        except Exception as general_error:
            
            print(f"An unexpected system exception occurred: {general_error}")


if _name_ == "_main_":
    run_interface()