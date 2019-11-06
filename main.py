import valerie

def main():

    test_name = "Numbers"
    service_name = "valerie_pymongo"
    network_name = "aarxn_net"

    hey_val = valerie.valTest(test_name, service_name, network_name)
    output = hey_val.Run()
    print(output)

main()