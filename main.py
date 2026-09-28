import Program.loops.py
from Program.loops.py import loop_service, print_service
from Program.service_cost.py import pbike_service_cost, nbike_service_cost, SUV_service_cost, MUV_service_cost
from Program.multi_service_loops.py import loop_multi_pbike, loop_multi_nbike, loop_multi_SUV, loop_multi_MUV
from Program.invoicing.py import print_bill

print("="*47)
print(" "*5,"# Vehicle service cost calculator # ")
print("="*47)

c = []
temp_c = []

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
        Program.core_loops.n=2
        choice=loop_service("0")

        # choosing bike type
        if choice == "1":
            print("""\n# Bike type choice
1. Premium bike
2. Normal bike""")
            Program.core_loops.n=2
            choice1=loop_service("1")
            Program.core_loops.n=4
            c=[]
            temp_c=[] 
            
            if choice1 == "1":
                b=print_service("0")
                temp_c.append(b) 
                c.append(pbike_service_cost(b))
                if b == "4":
                    print_bill(c)
                else:
                    loop_multi_pbike("0", temp_c)
                    print_bill(c)
            elif choice1 == "2":
                b=print_service("0")
                temp_c.append(b) 
                c.append(nbike_service_cost(b))
                if b == "4":
                    print_bill(c)
                else:
                    loop_multi_nbike("0", temp_c)
                    print_bill(c)
            else:
                print()
                          
        # choosing car type
        elif choice == "2":
            print("""\n# car type choice
1. SUV
2. MUV""")
            Program.core_loops.n=2
            choice1=loop_service("1")
            Program.core_loops.n=4
            c=[]
            temp_c=[] 
            
            if choice1 == "1":
                b=print_service("0")
                temp_c.append(b) 
                c.append(SUV_service_cost(b))
                if b == "4":
                    print_bill(c)
                else:
                    loop_multi_SUV("0", temp_c)
                    print_bill(c)
            elif choice1 == "2":
                b=print_service("0")
                temp_c.append(b) 
                c.append(MUV_service_cost(b))
                if b == "4":
                    print_bill(c)
                else:
                    loop_multi_MUV("0", temp_c)
                    print_bill(c)
            else:
                print()
        else:
            print()
    else:
        print("Invalid input. Please type 1 or 2.")
