# app.py

# Task 6: Final Cleanup - Global variable for the exchange rate
# NOTE: Using a hardcoded rate for simplicity as per assignment scope
# 1 USD equals approximately 17.15 MXN (rate is for example only)
MXN_RATE = 17.15 

# Task 1: Welcome message
print("🇲🇽 Welcome to the Simple USD to MXN Converter!")

# Task 2: Ask for input (USD amount)
usd_input = input("Enter the amount in USD ($) you wish to convert: ")

# Task 5: Error handling around conversion and calculation
try:
    # Task 3: Convert input & perform calculation
    usd_amount = float(usd_input)
    
    # Check for negative input (optional but good practice)
    if usd_amount < 0:
        print("Please enter a non-negative amount.")
        exit()
        
    # Perform the conversion
    mxn_amount = usd_amount * MXN_RATE  

    # Task 4: Display result clearly
    print(f"\n--- Conversion Result ---")
    print(f"Original USD Amount: ${usd_amount:,.2f}")
    print(f"Exchange Rate Used: 1 USD = {MXN_RATE} MXN")
    print(f"Converted MXN Amount: ${mxn_amount:,.2f} Pesos") # Note: MXN uses the $ symbol too
    print(f"-------------------------")

except ValueError:
    # Task 5: Basic error handling for non-numeric input
    print("❌ Invalid Input: Please enter a valid number for the USD amount. Program will exit now.")
    # exit() or sys.exit() are fine for early exit on error
    
# Task 6: Final Cleanup and Comments are present throughout the file.