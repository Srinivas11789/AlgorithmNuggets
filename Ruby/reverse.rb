#program to reverse the string
#! /usr/bin/ruby
#Function to reverse the string
def reverse(word_arr)
  reverse = []
#Assinging the length of the dtring to the variable index
  index = word_arr.length
#Pushing the last character to the reverse array and loop to repeat it until the length is 0
  until index == 0 do
    reverse << word_arr[index - 1]
    index -= 1
  end
#Returning the reverse string
  reverse
end
#Getting the string from console
puts "Enter the string"
string = gets
#call the Reverse function to reverse the string
reversedstring = reverse(string)
#print the reversed string
puts reversedstring
