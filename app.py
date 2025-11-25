# app.py
# Define the exchange rate for the calculation
MXN_RATE = 17.15

print("Welcome to the Simple USD to MXN Converter!")

# Task 2: Ask for input
usd_input = input("Enter the amount in USD ($) you wish to convert: ")

# Task 3: Convert input & perform calculation
usd_amount = float(usd_input)
mxn_amount = usd_amount * MXN_RATE  

# Task 4: Display result clearly
print("\n--- Conversion Result ---")
print(f"Original USD Amount: ${usd_amount:,.2f}")
print(f"Exchange Rate Used: 1 USD = {MXN_RATE} MXN")
print(f"Converted MXN Amount: ${mxn_amount:,.2f} Pesos") 
print("-------------------------\n")