def double(n)
    return n * 2
end

output = double(6)
output += 2
# puts output



def sum(x, y)
    return x + y
end

add = sum(3, 5)
# puts add





def by_five(n)
    return n % 5 == 0
end

is_it = by_five(46)
# puts is_it



def greeter(name)
    return "Hello #{name}"
end

choose_name = greeter("Miguel")
# puts choose_name



# working with Blocks now

# instead of writing methods(functions) and invoking them to capitalize whatever argument we want
["sushi", "pizza", "burger"].each {|string| puts "#{string[0].upcase}#{string[1..-1]}"}

4.times do
    puts("I love Ruby")
end
# or
4.times{puts "I also love Ruby"}


# prints out the array's values and multiplies them by 5
[1,2,3,4,5].each { |i| puts i * 5}

