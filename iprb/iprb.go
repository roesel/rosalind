// http://rosalind.info/problems/iprb/
package main
import (
    "fmt"
    "strings"
    "strconv"
)
func main() {
  a := "18 24 17"
  s := strings.Split(a, " ")
  fmt.Print(s[0])

  k, err := strconv.ParseFloat(s[0], 64)
  m, err := strconv.ParseFloat(s[1], 64)
  n, err := strconv.ParseFloat(s[2], 64)

  if err != nil {
    print("Error.")
  }

  t := k+m+n

  k1 := k/t
  m1 := m/t
  n1 := n/t

  k2 := k/(t-1)
  m2 := m/(t-1)
  n2 := n/(t-1)

  kk := k1 * (k-1)/(t-1)
  mm := m1 * (m-1)/(t-1)
  //nn := n1 * (n-1)/(t-1)
  km := k1*m2
  mk := m1*k2
  kn := k1*n2
  nk := n1*k2
  mn := m1*n2
  nm := n1*m2

  p := kk + mm*0.75 + (mn+nm)*0.5 + (km+mk) + (kn+nk)

  fmt.Printf("%.5f", p)
}
