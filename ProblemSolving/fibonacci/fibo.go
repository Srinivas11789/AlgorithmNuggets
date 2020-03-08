// Iterative Fibonacci - 0ms
func fib(N int) int {
    if N == 0 {
        return 0
    }
    if N == 1 {
        return 1
    }
    f0 := 0
    f1 := 1
    f2 := 0
    for i := 1;  i<N; i++  {
        f2 = f0 + f1
        f0 = f1
        f1 = f2
    }
    return f2
}

// Naive Recursive Fibonacci - 8ms
/*
func fib(N int) int {
    if N == 0 {
        return 0
    } else if N == 1 {
        return 1
    } else {
        return fib(N-1) + fib(N-2)
    }
}
*/
