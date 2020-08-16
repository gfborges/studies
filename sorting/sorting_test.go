package sorting

import (
	"fmt"
	"math/rand"
	"testing"
	"time"
)

const size int = 1_000_000

// utils
func issorted(v []int) bool {
	len := len(v)
	for i := 1; i < len; i++ {
		if v[i-1] > v[i] {
			return false
		}
	}
	return true
}

func random(n int) []int {
	rand.Seed(time.Now().UnixNano())
	return rand.Perm(n)
}

func TestMergesort(t *testing.T) {
	v := []int{5, 2, 4, 3, 0, 1, 9, 6, 8, 7}
	mergesort(v)
	if !issorted(v) {
		t.Errorf("mergesort is not working properly")
	}

}

func TestGoMergesort1(t *testing.T) {
	v := []int{5, 2, 4, 3, 0, 1, 9, 6, 8, 7}
	goMergesort1(v)
	if !issorted(v) {
		fmt.Println(v)
		t.Errorf("goMergesort1 is not working properly")
	}
}
func TestGoMergesort2(t *testing.T) {
	v := []int{5, 2, 4, 3, 0, 1, 9, 6, 8, 7}
	goMergesort2(v)
	if !issorted(v) {
		fmt.Println(v)
		t.Errorf("goMergesort1 is not working properly")
	}
}

func BenchmarkMergesort(b *testing.B) {
	for i := 0; i < b.N; i++ {
		v := random(size)
		b.StartTimer()
		mergesort(v)
		b.StopTimer()
	}
}

func BenchmarkGoMergesort1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		v := random(size)
		b.StartTimer()
		goMergesort1(v)
		b.StopTimer()
	}
}

func BenchmarkGoMergesort2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		v := random(size)
		b.StartTimer()
		goMergesort2(v)
		b.StopTimer()
	}
}
