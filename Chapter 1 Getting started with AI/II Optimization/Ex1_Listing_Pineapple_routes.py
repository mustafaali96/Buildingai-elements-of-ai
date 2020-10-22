#Beginner: 6

#Intermediate:
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            if port2 != port3:
                for port4 in range(1, 5):
                    if port2 != port4 and port3 != port4:
                        for port5 in range(1, 5):
                            if port2 != port5 and port3 != port5 and port4 != port5:
                                route = [port1, port2, port3, port4, port5]

                                # do not modify the print statement
                                print(' '.join([portnames[i] for i in route]))

main()


#Advanced
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
def permutations(route, ports):
    # write the recursive function here
    # remember to print out the route as the recursion ends
    for i in ports:
        route = ports[:i]+ports[i+1:]
#        print(route)

# this will start the recursion with 0 as the first stop
permutations([0], list(range(0, len(portnames))))
