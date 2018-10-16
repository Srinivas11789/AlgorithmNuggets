puts "Enter starting year:"
        starting_year = gets.chomp.to_i
puts "Enter ending year:"
      ending_year = gets.chomp.to_i
year = starting_year
while true
      if year%4==0
          if year%100!=0 || year%400 ==0
              puts year.to_s + ' is a Leap Year'
          end
      end
    year = year +1
      break if year >= ending_year
end
