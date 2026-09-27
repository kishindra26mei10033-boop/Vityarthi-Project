# Vehicle service cost calculator

print("="*47)
print(" "*5,"# Vehicle service cost calculator # ")
print("="*47)

# loop of entry
def loop_service(service):
    option = False
    while option is False:
        service=int(input("\nSelect your Option in numbrs:"))
        if service <= n and service > 0:
            option = True
            break
        else:
            print("invalid input")
    return service

# loop for printing service
def print_service(loop):
    print("""\n# Service required
1. brake Service
2. engine check
3. oil change
4. full service""")
    n=4
    a=loop_service(2)
    return a

# service cost of Premium bike
def pbike_service_cost(sel):
    if sel == 1:
        return 700
    elif sel == 2:
        return 500
    elif sel == 3:
        return 1000
    elif sel == 4:
        return 2500

# service cost of Normal bike
def nbike_service_cost(sel):
    if sel == 1:
        return 300
    elif sel == 2:
        return 200
    elif sel == 3:
        return 400
    elif sel == 4:
        return 1000

# service cost of SUV
def SUV_service_cost(sel):
    if sel == 1:
        return 9000
    elif sel == 2:
        return 3000
    elif sel == 3:
        return 12000
    elif sel == 4:
        return 25000

# service cost of MUV
def MUV_service_cost(sel):
    if sel == 1:
        return 5000
    elif sel == 2:
        return 1200
    elif sel == 3:
        return 8000
    elif sel == 4:
        return 15000

# loop for multiple service pbike
def loop_multi_pbike(opt, temp_c):
    option = False
    while option is False:
        opt=input("\ndo you want to add more service (yes or no):")
        if opt.lower() == "no":
            option = True
            break
        elif opt.lower() == "yes":
            i=1
            s=print_service(i)
            if s in temp_c:
                print("You have already added this service!")
            else:
                temp_c.append(s)
                if s == 4:
                    print("\nFull service selected. Replacing previous services and proceeding to bill.")
                    c.clear()
                    c.append(pbike_service_cost(4))
                    option = True
                    break
                else:
                    c.append(pbike_service_cost(s))
            i+=1
        else:
            print("invalid input")
    return opt

# loop for multiple service nbike
def loop_multi_nbike(opt, temp_c):
    option = False
    while option is False:
        opt=input("\ndo you want to add more service (yes or no):")
        if opt.lower() == "no":
            option = True
            break
        elif opt.lower() == "yes":
            i=1
            s=print_service(i)
            if s in temp_c:
                print("You have already added this service!")
            else:
                temp_c.append(s) 
                if s == 4:
                    print("\nFull service selected. Replacing previous services and proceeding to bill.")
                    c.clear()
                    c.append(nbike_service_cost(4))
                    option = True
                    break
                else:
                    c.append(nbike_service_cost(s))
            i+=1
        else:
            print("invalid input")
    return opt

# loop for multiple service SUV
def loop_multi_SUV(opt, temp_c):
    option = False
    while option is False:
        opt=input("\ndo you want to add more service (yes or no):")
        if opt.lower() == "no":
            option = True
            break
        elif opt.lower() == "yes":
            i=1
            s=print_service(i)
            if s in temp_c:
                print("You have already added this service!")
            else:
                temp_c.append(s) 
                if s == 4:
                    print("\nFull service selected. Replacing previous services and proceeding to bill.")
                    c.clear()
                    c.append(SUV_service_cost(4))
                    option = True
                    break
                else:
                    c.append(SUV_service_cost(s))
            i+=1
        else:
            print("invalid input")
    return opt

# loop for multiple service MUV
def loop_multi_MUV(opt, temp_c):
    option = False
    while option is False:
        opt=input("\ndo you want to add more service (yes or no):")
        if opt.lower() == "no":
            option = True
            break
        elif opt.lower() == "yes":
            i=1
            s=print_service(i)
            if s in temp_c:
                print("You have already added this service!")
            else:
                temp_c.append(s) 
                if s == 4:
                    print("\nFull service selected. Replacing previous services and proceeding to bill.")
                    c.clear()
                    c.append(MUV_service_cost(4))
                    option = True
                    break
                else:
                    c.append(MUV_service_cost(s))
            i+=1
        else:
            print("invalid input")
    return opt

# printing bill
def print_bill(bill):
    print()
    print("=" * 27)
    print("        INVOICE ITEMS")
    print("-" * 27)
    
    subtotal = 0
    for price in c:
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


# frontend program
while True:
    print("-"*21)
    print("1. Enter the program")
    print("2. Exit")
    print("-"*21)
    program_run = input("Select your option (1 or 2): ").strip()
    
    if program_run == "2":
        print("\nExiting the Vehicle Service Calculator. Thank you for using the program, Have a great day!")
        break 
    elif program_run == "1":
        # cost table
        from tabulate import tabulate
        data = [
    ["brake Service",700,300,9000,5000],
    ["engine check",500,200,3000,1200],
    ["oil change",1000,400,12000,8000],
    ["full service",2500,1000,25000,15000]
]
        headers = ["PRICE","Premium bike","Normal bike","SUV","MUV"]
        print(tabulate(data, headers=headers, tablefmt="grid"))


        
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
            n=4
            c=[]
            temp_c=[] 
            
            if choice1 == 1:
                b=print_service(0)
                temp_c.append(b) 
                c.append(pbike_service_cost(b))
                if b == 4:
                    print_bill(c)
                else:
                    loop_multi_pbike(0, temp_c) 
                    print_bill(c)
            elif choice1 == 2:
                b=print_service(0)
                temp_c.append(b) 
                c.append(nbike_service_cost(b))
                if b == 4:
                    print_bill(c)
                else:
                    loop_multi_nbike(0, temp_c) 
                    print_bill(c)
            else:
                print()
                          
        # choosing car type
        elif choice == 2:
            print("""\n# car type choice
1. SUV
2. MUV""")
            n=2
            choice1=loop_service(1)
            n=4
            c=[]
            temp_c=[] 
            
            if choice1 == 1:
                b=print_service(0)
                temp_c.append(b) 
                c.append(SUV_service_cost(b))
                if b == 4:
                    print_bill(c)
                else:
                    loop_multi_SUV(0, temp_c) 
                    print_bill(c)
            elif choice1 == 2:
                b=print_service(0)
                temp_c.append(b) 
                c.append(MUV_service_cost(b))
                if b == 4:
                    print_bill(c)
                else:
                    loop_multi_MUV(0, temp_c) 
                    print_bill(c)
            else:
                print()
        else:
            print()
    else:
        print("Invalid input. Please type 1 or 2.")
