package main


import (
    "fmt"
    "valerie/valerie"
)

func main() {
  
    my_test := valerie.NewTest("Numbers")
    my_test.Service_name = "valerie_pymongo"
    my_test.Network_name = "aarxn_net"
    output := my_test.Run()
    fmt.Println(output)
 
}

