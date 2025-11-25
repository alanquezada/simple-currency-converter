# app.py
MXN_RATE = 17.15 

print("Welcome to the Simple USD to MXN Converter!")

usd_input = input("Enter the amount in USD ($) you wish to convert: ")

# Task 5: Add basic error handling
try:
    # Code that might fail (conversion)
    usd_amount = float(usd_input) 
    mxn_amount = usd_amount * MXN_RATE  

    # Display result clearly (inside try block)
    print("\n--- Conversion Result ---")
    print(f"Original USD Amount: ${usd_amount:,.2f}")
    # ... (rest of the print statements)
    print("-------------------------\n")

except ValueError:
    print("\n❌ Invalid Input: Please enter a valid number for the USD amount. Program will exit now.")
    exit() # Exits the program on error