# Calculate Compound Interest 

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Annual Interest Rate: "))
time = float(input("Enter Time: "))
n = int(input("Enter Compounding Frequency per year: "))
amount = principal * (1 + (rate / 100) / n) ** (n * time)
compound_interest = amount - principal
print(f"\nCompound Interest = {compound_interest:.2f}")
print(f"Total Amount = {amount:.2f}")
