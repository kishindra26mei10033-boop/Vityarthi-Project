import main

# printing bill
def print_bill(bill):
    print()
    print("=" * 27)
    print("        INVOICE ITEMS")
    print("-" * 27)
    
    subtotal = 0
    for price in main.c:
        print(f"service charge:  {float(price):.2f}")
        subtotal += price
        
    tax = subtotal * (9 / 100)
    total_charges = subtotal + (2 * tax)
    
    print("=" * 27)
    print(f"Subtotal:        {subtotal:.2f}")
    print(f"         + CGST: {tax:.2f}")
    print(f"         + SGST: {tax:.2f}")
    print("-" * 27)
    print(f"  TOTAL CHARGES: {total_charges:.2f}")
    print("=" * 27)
