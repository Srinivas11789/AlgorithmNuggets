#Fibonacci program 
/**
 * @param {number} N
 * @return {number}
 */

var fib = function(N) {
  f = [0,1];                   //Storing the known values in array
  for (var i = 2; i <= N; i++) {
      f[i] = f[i -1] + f[i - 2]; //Logic to find the fibonacci of the given number 
  }
    return f[N];
};

fib(9);
