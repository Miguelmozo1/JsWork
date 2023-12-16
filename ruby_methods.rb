def alphabatize(arr, rev = false)   # rev is an actual function within ruby, not a variable
    if rev
            # sort returns sorted array
            # sort! modifies original array
        arr.sort { |item1,item2| item2 <=> item1}
    else
        arr.sort { |item1,item2| item1 <=> item2 }
    end
end

books = ["Einsteins dreams", "Ruby", "Python", "The Sinner", "Green Eggs and Ham"]

puts(alphabatize(books))

puts(alphabatize(books, true))

# another way would be .reverse or .reverse! much like .sort or .sort!



# another example
def alphabetize(arr, rev = false)
    arr.sort!
    if rev
        arr.reverse!
    else
        return arr
    end
end

numbers = [1,45,23,89]
puts(alphabetize(numbers))