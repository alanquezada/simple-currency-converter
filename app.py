# app.py
#
# Simple USD to MXN Currency Converter
# Author: Alan Quezada
# Purpose: Converts USD amount tht you type into Mexican Pesos (MXN) using a fixed exchange rate, and includes basic error handling.
# --- Configuration --
MXN_RATE = 17.15 # Fixed exchange rate: 1 USD = 17.15 MXN

# --- Program Start ---
print("Welcome to the Simple USD to MXN Converter!")

# Prompt user for input
usd_input = input("Enter the amount in USD ($) you wish to convert: ")

# --- Conversion and Error Handling ---
try:
    # Convert input to a float for calculation
    usd_amount = float(usd_input) 
    
    # Do the the currency conversion calculation
    mxn_amount = usd_amount * MXN_RATE  
    
    # --- Display Result Clearly ---
    print("\n--- Conversion Result ---")
    print(f"Original USD Amount: ${usd_amount:,.2f}")
    print(f"Exchange Rate Used: 1 USD = {MXN_RATE} MXN")
    print(f"Converted MXN Amount: ${mxn_amount:,.2f} Pesos") 
    print("-------------------------\n")

except ValueError:
    # Handle non-numeric input correctly
    print("\n❌ Invalid Input: Please enter a valid number for the USD amount.")
    # Terminate the program cleanly after an error
    exit()