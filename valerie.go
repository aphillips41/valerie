package valerie

import (
    "os/exec"
)

type val_x struct {
	Name string
    Service_name string
    Cluster_name string
    Network_name string
}

func NewTest (test_name string) val_x {
	my_test := val_x{Name:test_name}
	return my_test
}

func (val_test val_x) Run() []byte {
    cmdStr := "docker run -d --rm --network " + val_test.Network_name + " " + val_test.Service_name
    out, _ := exec.Command("/bin/sh", "-c", cmdStr).Output()
    return out
}
