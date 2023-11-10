def what_up(greeting, *friends)
    friends.each { |friend| puts "#{greeting}, #{friend}!"}
end

what_up("Yo", "Marley", "Ian", "Bob", "Zach")