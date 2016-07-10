// http://rosalind.info/problems/pmch/

package main

import (
	"fmt"
	"io/ioutil"
	"math/big"
	"strings"
)

func content(s string, l byte) int64 {
	var count int64 = 0
	for j := 0; j < len(s); j++ {
		if s[j] == l {
			count++
		}
	}
	return count
}

func factorial(n *big.Int) (result *big.Int) {
	//fmt.Println("n = ", n)
	b := big.NewInt(0)
	c := big.NewInt(1)

	if n.Cmp(b) == -1 {
		result = big.NewInt(1)
	}
	if n.Cmp(b) == 0 {
		result = big.NewInt(1)
	} else {
		// return n * factorial(n - 1);
		result = new(big.Int)
		result.Set(n)
		result.Mul(result, factorial(n.Sub(n, c)))
	}
	return
}

func main() {
	as, _ := ioutil.ReadFile("C:/Users/roese/Downloads/rosalind_pmch.txt")
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

	f1 := big.NewInt(content(a, 'A'))
	f2 := big.NewInt(content(a, 'C'))
	result := new(big.Int)
	fmt.Println(result.Mul(factorial(f1), factorial(f2)))

}
