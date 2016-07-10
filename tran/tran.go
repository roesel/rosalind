// http://rosalind.info/problems/tran/

package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	as, _ := ioutil.ReadFile("C:/Users/roese/Downloads/rosalind_tran.txt")
	lines := strings.Split(string(as), "\n")
	for j := 0; j <= len(lines)-2; j++ { // -2 b/c of newline@EOF
		if string(lines[j][0]) == ">" {
			lines[j] = "-"
		}
	}

	lin := strings.Join(lines, "")
	lin = strings.Replace(lin, "\r", "", -1)
	lin = lin[1:]
	lines = strings.Split(lin, "-")

	var a string = lines[0]
	var b string = lines[1]

	var transitions float64 = 0
	var transversions float64 = 0

	for j := 0; j <= len(a)-1; j++ {
		if a[j] != b[j] {
			if (string(a[j]) == "A" && string(b[j]) == "G") || (string(a[j]) == "G" && string(b[j]) == "A") || (string(a[j]) == "T" && string(b[j]) == "C") || (string(a[j]) == "C" && string(b[j]) == "T") {
				transitions += 1
			} else {
				transversions += 1
			}
		}
	}
	fmt.Printf("%.11f", transitions/transversions)

}
