// http://rosalind.info/problems/subs/

package main

import "fmt"

func main() {
	var n int = 21
	var k int = 7
	var s int = 1

	for i := 0; i < k; i++ {
		s = (s * (n - i)) % 1000000
	}

	fmt.Println(s)
	// possible issues with size of int? problem with n=100, k=10
}
