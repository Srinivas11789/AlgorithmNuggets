#Program to find if the year is a leap year or not

#Get the starting year from user
puts "Enter starting year:"


        starting_year = gets.chomp.to_i
#Get the ending year from user
puts "Enter ending year:"
      ending_year = gets.chomp.to_i
#variable assignment with user input
year = starting_year
while true
#checks to find if its a leap year or not
      if year%4==0
          if year%100!=0 || year%400 ==0
              puts year.to_s + ' is a Leap Year'
          end
      end
#Incrementing year
    year = year +1
#Breaking the loop once the end year has been reached
      break if year >= ending_year
end
