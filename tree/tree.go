// http://rosalind.info/problems/tree/

package main
import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
  )

func main() {
    as, _ := ioutil.ReadFile("C:/Users/roese/Downloads/rosalind_tree.txt")
    lines := strings.Split(string(as), "\n")

    number_of_nodes, _ := strconv.Atoi(lines[0][:len(lines[0])-1])
    var number_of_lines int = len(lines)
    fmt.Println(number_of_nodes-number_of_lines+1)
}
