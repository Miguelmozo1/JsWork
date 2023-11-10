def welcome
    puts("Hello Ruby")
end

# welcome()



def puts_1_to_10
    (1 .. 10).each { |i| puts i}
end

# puts_1_to_10        # this is calling the method/ function to run


def array_of_10
    puts (1..10).to_a             # space between puts and parenthesis is a large difference in expected output
end

# array_of_10


def cubertino(n)                    # introducing parameters, and arguments into methods
    puts n ** 3
end

# cubertino(8)


def what_up(greeting, *friends)         # intro to splat arguments, its the * that allows a value to story multiple arguments
    friends.each { |friend| puts "#{greeting}, #{friend}!"}
end

what_up("Yo", "Marley", "Ian", "Bob", "Zach")
