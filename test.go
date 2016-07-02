package main
import (
    "fmt"
    "io/ioutil"
)
func main() {
  a, _ := ioutil.ReadFile("rosalind_prot.txt")
  as := string(a)
  fmt.Println(as)
}
