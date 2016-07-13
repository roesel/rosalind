// http://rosalind.info/problems/rstr

package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

func main() {
	as, _ := ioutil.ReadFile("C:/Users/roese/Downloads/rosalind_rstr.txt")
	lines := strings.Split(string(as), "\n")

	var a string = lines[0]
	var b string = lines[1]

	first_line := strings.Split(a, " ")
	N, _ := strconv.Atoi(first_line[0])
	GC, _ := strconv.ParseFloat(first_line[1][:len(first_line[1])-1], 64)

	prob := 1.0
	for i := 0; i < len(b); i++ {
		if b[i] == 'A' || b[i] == 'T' {
			prob *= (1 - GC) / 2
		} else if b[i] == 'C' || b[i] == 'G' {
			prob *= GC / 2
		}
	}

	fmt.Printf("%.03f", 1-math.Pow(1-prob, float64(N)))

}
