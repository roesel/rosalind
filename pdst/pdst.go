// http://rosalind.info/problems/pdst/

package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func dist(s1, s2 string) float64 {
	var matches float64
	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			matches++
		}
	}
	return matches / float64(len(s1))
}

func main() {
	as, _ := ioutil.ReadFile("C:/Users/roese/Downloads/rosalind_pdst.txt")
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

	// not optimized for speed, but prety OK for memory
	for i := 0; i < len(lines); i++ {
		for j := 0; j < len(lines); j++ {
			fmt.Printf("%.5f ", dist(lines[i], lines[j]))
		}
		fmt.Println("")
	}

}
