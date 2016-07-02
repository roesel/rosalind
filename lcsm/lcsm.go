// http://rosalind.info/problems/lcsm/

package main
import (
    "fmt"
    "io/ioutil"
    "strings"
  )

func allhave(s string, lines []string) bool {
    for i := 1; i<len(lines); i++ {  // pro kazdy dalsi string
        if !strings.Contains(lines[i], s) {
          return false
        }
    }
    return true
}

func main() {
    as, _ := ioutil.ReadFile("C:/Users/roese/Downloads/rosalind_lcsm.txt")
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

    g_max := 0
    lcsm := ""

    for j := 0; j < len(lines[0]); j++ {  // pro každou pozici z prvniho stringu
         for i := 0; i < len(lines[0])-j; i++ { // pro každou délku
             if !allhave(lines[0][j:j+i], lines) {
                 if i>g_max {
                      g_max = i
                      lcsm = lines[0][j:j+i-1]
                 }
                 break
             }
         }
    }


    fmt.Println(lcsm)

}
