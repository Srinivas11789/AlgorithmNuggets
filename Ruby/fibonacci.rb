#Fibonacci program
def fibonacci(n)
    a = 0
    b = 1

    # Compute Fibonacci number in the desired position.
    n.times do
        temp = a
        a = b
        # Add up previous two numbers in sequence.
        b = temp + b
    end

    return a
end

# Write Fibonacci numbers in sequence as per the userinput.
puts "Enter the number:"
userinput = gets.chomp.to_i
result = fibonacci(userinput)
puts result

