#Ruby Factorial program 

def fact(n)
 if n == 0
  1
 else
  if n> 0
   n * fact(n-1)
   
  else 
   puts "no factorial for -ve number"
  end
end   
end

puts fact(ARGV[0].to_i)
