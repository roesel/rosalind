// http://rosalind.info/problems/lgis/

package main
import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
  )

func lds(b string) {
    // Print longest decreasing subsequence.
    nums := strings.Split(b[:len(b)-1], " ")
    numvals := make([]int, len(nums))
    for i := range nums {
      numvals[i], _ = strconv.Atoi(nums[i])
    }
    size := len(nums)



    m := make([]int, size)

    max := 0
    max_pos := size-1

    for i := size-1; i >= 0; i-- {
      for j := i; j<size; j++ {
        if numvals[i]>numvals[j] && m[j]+1 > m[i] {
          m[i] = m[j]+1
          if m[i]>max {
            max = m[i]
            max_pos = i
          }
        }
      }
    }

    fmt.Print(nums[max_pos], " ")
    for i := max_pos+1; i < size; i++ {
        if m[i] == max-1 {
          fmt.Print(nums[i], " ")
          max = max-1
        }
    }
}

func lis(b string) {
    // Print longest increasing subsequence.
    nums := strings.Split(b[:len(b)-1], " ")
    numvals := make([]int, len(nums))
    for i := range nums {
      numvals[i], _ = strconv.Atoi(nums[i])
    }
    size := len(nums)

    m := make([]int, size)
    max := 0
    max_pos := size-1

    for i := size-1; i >= 0; i-- {
      for j := i; j<size; j++ {
        if numvals[i]<numvals[j] && m[j]+1 > m[i] {
          m[i] = m[j]+1
          if m[i]>max {
            max = m[i]
            max_pos = i
          }
        }
      }
    }

    fmt.Print("\n\n",nums[max_pos], " ")
    for i := max_pos+1; i < size; i++ {
        if m[i] == max-1 {
          fmt.Print(nums[i], " ")
          max = max-1
        }
    }
}

func main() {
    as, _ := ioutil.ReadFile("C:/Users/roese/Downloads/rosalind_lgis.txt")
    lines := strings.Split(string(as), "\n")

    // var a string = lines[0]
    var b string = lines[1]
    lis(b)
    fmt.Printf("\n")
    lds(b)
}
