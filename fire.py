import firebase_admin
from firebase_admin import credentials, db

def initialize_firebase():
    # Initialize the Firebase Admin SDK
    cred = credentials.Certificate('Cre.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://hello-90594-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

def save_calculation(operation, num1, num2, result):
    # Reference to the database
    ref = db.reference('/calculations')
    new_entry = ref.push()
    new_entry.set({
        'operation': operation,
        'num1': num1,
        'num2': num2,
        'result': result
    })
    print("Calculation saved successfully!")

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = num1 + num2
            operation = 'Addition'
        elif choice == '2':
            result = num1 - num2
            operation = 'Subtraction'
        elif choice == '3':
            result = num1 * num2
            operation = 'Multiplication'
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = 'Division'
        
        print(f"Result: {result}")
        save_calculation(operation, num1, num2, result)
    else:
        print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    initialize_firebase()
    calculator()
