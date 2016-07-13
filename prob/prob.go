// http://rosalind.info/problems/prob/

package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

func main() {
	as, _ := ioutil.ReadFile("C:/Users/roese/Downloads/rosalind_prob.txt")
	lines := strings.Split(string(as), "\n")

	var a string = lines[0]
	var b string = lines[1]

	probs_str := strings.Split(b, " ")
	probs := make([]float64, len(probs_str))

	for i := range probs_str {
		p := probs_str[i][:5]
		g, _ := strconv.ParseFloat(p, 64)
		probs[i] = g
	}

	for j := 0; j < len(probs); j++ {
		outprob := 0.0
		prob := probs[j]
		for i := 0; i < len(a)-1; i++ {
			if a[i] == 'A' || a[i] == 'T' {
				outprob += math.Log10((1 - prob) / 2)
			} else {
				outprob += math.Log10(prob / 2)
			}
		}
		fmt.Printf("%0.3f ", outprob)
	}

}
