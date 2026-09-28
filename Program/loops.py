# loop of entry
def loop_service(service):
    option = False
    while option is False:
        service=input("\nSelect your Option in numbrs:")
        try:
            if int(service) <= n and int(service) > 0:
                option = True
                break
            else:
                print("invalid input")
        except:
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
    a=loop_service("2")
    return a
