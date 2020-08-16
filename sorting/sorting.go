package sorting

import (
	"runtime"
	"sync"
)

type none struct{}

const max = 1 << 11

func merge(v []int, mid int) {
	l, r, t := 0, mid, 0
	len := len(v)
	temp := make([]int, len, len)
	for l < mid && r < len {
		if v[l] < v[r] {
			temp[t] = v[l]
			l++
		} else {
			temp[t] = v[r]
			r++
		}
		t++
	}
	for l < mid {
		temp[t] = v[l]
		l++
		t++
	}
	for r < len {
		temp[t] = v[r]
		r++
		t++
	}
	copy(v, temp)
}

func mergesort(v []int) {
	len := len(v)
	if len <= 1 {
		return
	}
	mid := len / 2

	mergesort(v[:mid])
	mergesort(v[mid:])

	merge(v, mid)
}

func goMergesort1(v []int) {
	ch := make(chan none, runtime.NumCPU())
	defer close(ch)
	_goMergesort1(v, ch)
}

func _goMergesort1(v []int, ch chan none) {
	len := len(v)
	if len <= 1 {
		return
	}
	if len <= max {
		mergesort(v)
		return
	}
	mid := len / 2

	wg := sync.WaitGroup{}

	wg.Add(1)

	select {
	case ch <- none{}:
		go func(v []int, mid int, ch chan none) {
			_goMergesort1(v[:mid], ch)
			wg.Done()
			<-ch
		}(v, mid, ch)
	default:
		wg.Done()
		_goMergesort1(v[:mid], ch)
	}

	_goMergesort1(v[mid:], ch)

	wg.Wait()

	merge(v, mid)
}

func goMergesort2(v []int) {
	len := len(v)
	if len <= 1 {
		return
	}

	if len <= max {
		mergesort(v)
		return
	}
	mid := len / 2

	var wg sync.WaitGroup

	wg.Add(2)

	go func() {
		goMergesort2(v[:mid])
		wg.Done()
	}()

	go func() {
		goMergesort2(v[mid:])
		wg.Done()
	}()

	wg.Wait()

	merge(v, mid)
}
