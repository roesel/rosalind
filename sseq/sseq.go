// http://rosalind.info/problems/sseq/

package main
import (
    "fmt"
    "io/ioutil"
    "strings"
  )
func main() {
    as, _ := ioutil.ReadFile("C:/Users/roese/Downloads/rosalind_sseq.txt")
    lines := strings.Split(string(as), "\n")
    for j := 0; j <= len(lines)-2; j++ {  // -2 b/c of newline@EOF
        if string(lines[j][0]) == ">" {
            lines[j] = "-"
        }
    }

    lin := strings.Join(lines,"")
    lin = strings.Replace(lin, "\r", "", -1)
    lin = lin[1:]
    lines = strings.Split(lin, "-")

    var a string = lines[0]
    var b string = lines[1]

    var pozice = make([]int,len(b))
    i := 0
    for j := 0; j <= len(a); j++ {
        if a[j] == b[i] {
          pozice[i] = j
          if i == len(b)-1 {
            break
          } else {
            i++
          }
        }
    }

    //fmt.Printf("%#v\n", pozice)

    for j := 0; j<len(pozice); j++ {
      fmt.Print(pozice[j]+1, " ")
    }
}
