# Vehicle sevice calculator

print("="*41)
print(" "*5,"# Vehicle sevice calculator # ")
print("="*41)
print()

# cost table
from tabulate import tabulate
data = [
    ["break Service",700,300,9000,5000],
    ["full service",2500,1000,25000,15000],
    ["oil change",1000,400,12000,8000],
    ["engine check",500,200,3000,1200]
]
headers = ["PRICE","Premium bike","Normal bike","SUV","MUV"]
print(tabulate(data, headers=headers, tablefmt="grid"))

# loop of entry
def loop_service(service):
    option = False
    while option is False:
        service=int(input("\nSelect Option:"))
        if service <= n and service > 0:
            option = True
            break
        else:
            print("invalid input")
    return service

# service cost of Premium bike
def pbike_service_cost(sel):
    if sel == 1:
        return 700
    elif sel == 2:
        return 2500
    elif sel == 3:
        return 1000
    elif sel == 4:
        return 500

# service cost of Normal bike
def nbike_service_cost(sel):
    if sel == 1:
        return 300
    elif sel == 2:
        return 1000
    elif sel == 3:
        return 400
    elif sel == 4:
        return 200

# service cost of SUV
def SUV_service_cost(sel):
    if sel == 1:
        return 9000
    elif sel == 2:
        return 25000
    elif sel == 3:
        return 12000
    elif sel == 4:
        return 3000

# service cost of MUV
def MUV_service_cost(sel):
    if sel == 1:
        return 5000
    elif sel == 2:
        return 15000
    elif sel == 3:
        return 8000
    elif sel == 4:
        return 1200
# printing bill
def print_bill(bill):
    tax=b*(9/100)
    print()
    print("="*25)
    print("Service charges:",float(b))
    print("         + CGST:",tax)
    print("         + SGST:",tax)
    print("-"*25)
    print("  TOTAL CHARGES:",b+2*tax)
    print("="*25)

# entry of vehicle type
print("""\n# Vehicle choice
1. Bike
2. Car""")
n=2
choice=loop_service(0)

# choosing bike type
if choice == 1:
    print("""\n# Bike type choice
1. Premium bike
2. Normal bike""")
    n=2
    choice1=loop_service(1)
    print("""\n# Service required
1. break Service
2. full service
3. oil change
4. engine check""")
    n=4
    a=loop_service(2)
    if choice1 == 1:
        b=pbike_service_cost(a)
        print_bill(b)
    elif choice1 == 2:
        b=nbike_service_cost(a)
        print_bill(b)
    else:
        print()
                   
# choosing car type
elif choice == 2:
    print("""\n# car type choice
1. SUV
2. MUV""")
    n=2
    choice2=loop_service(1)
    print("""\n# Service required
1. break Service
2. full service
3. oil change
4. engine check""")
    n=4
    a=loop_service(2)
    if choice2 == 1:
        b=SUV_service_cost(a)
        print_bill(b)
    elif choice2 == 2:
        b=MUV_service_cost(a)
        print_bill(b)
    else:
        print()
    
else:
    print()
