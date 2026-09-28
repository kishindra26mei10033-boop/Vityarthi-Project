from Program.core_loops import print_service
from Program.cost_calculators import pbike_service_cost, nbike_service_cost, SUV_service_cost, MUV_service_cost

# loop for multiple service pbike
def loop_multi_pbike(opt, temp_c, c_list):
    option = False
    while option is False:
        opt = input("\ndo you want to add more service (yes or no):")
        if opt.lower() == "no":
            option = True
            break
        elif opt.lower() == "yes":
            i = 1
            s = print_service(i)
            if s in temp_c:
                print("You have already added this service!")
            else:
                temp_c.append(s) 
                if s == "4":
                    print("\nFull service selected. Replacing previous services and proceeding to bill.")
                    c_list.clear()
                    c_list.append(pbike_service_cost("4"))
                    option = True
                    break
                else:
                    c_list.append(pbike_service_cost(s))
            i += 1
        else:
            print("invalid input")
    return opt

# loop for multiple service nbike
def loop_multi_nbike(opt, temp_c, c_list):
    option = False
    while option is False:
        opt = input("\ndo you want to add more service (yes or no):")
        if opt.lower() == "no":
            option = True
            break
        elif opt.lower() == "yes":
            i = 1
            s = print_service(i)
            if s in temp_c:
                print("You have already added this service!")
            else:
                temp_c.append(s) 
                if s == "4":
                    print("\nFull service selected. Replacing previous services and proceeding to bill.")
                    c_list.clear()
                    c_list.append(nbike_service_cost("4"))
                    option = True
                    break
                else:
                    c_list.append(nbike_service_cost(s))
            i += 1
        else:
            print("invalid input")
    return opt

# loop for multiple service SUV
def loop_multi_SUV(opt, temp_c, c_list):
    option = False
    while option is False:
        opt = input("\ndo you want to add more service (yes or no):")
        if opt.lower() == "no":
            option = True
            break
        elif opt.lower() == "yes":
            i = 1
            s = print_service(i)
            if s in temp_c:
                print("You have already added this service!")
            else:
                temp_c.append(s) 
                if s == "4":
                    print("\nFull service selected. Replacing previous services and proceeding to bill.")
                    c_list.clear()
                    c_list.append(SUV_service_cost("4"))
                    option = True
                    break
                else:
                    c_list.append(SUV_service_cost(s))
            i += 1
        else:
            print("invalid input")
    return opt

# loop for multiple service MUV
def loop_multi_MUV(opt, temp_c, c_list):
    option = False
    while option is False:
        opt = input("\ndo you want to add more service (yes or no):")
        if opt.lower() == "no":
            option = True
            break
        elif opt.lower() == "yes":
            i = 1
            s = print_service(i)
            if s in temp_c:
                print("You have already added this service!")
            else:
                temp_c.append(s) 
                if s == "4":
                    print("\nFull service selected. Replacing previous services and proceeding to bill.")
                    c_list.clear()
                    c_list.append(MUV_service_cost("4"))
                    option = True
                    break
                else:
                    c_list.append(MUV_service_cost(s))
            i += 1
        else:
            print("invalid input")
    return opt
