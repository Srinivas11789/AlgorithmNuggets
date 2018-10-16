#! /usr/bin/ruby

def reverse(word_arr)
  reverse = []
  index = word_arr.length
  until index == 0 do
    reverse << word_arr[index - 1]
    index -= 1
  end
  reverse
end


string = gets

reversedstring = reverse(string)
puts "reversedstring"
