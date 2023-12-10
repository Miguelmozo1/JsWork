# book_1 = "Searching for Schrodinger's cat"

# book_2 = "The island at the center of the World"

# puts(book_1 <=> book_2)     # the combined comparison operator, return 1 if first(book_1) operand comes first than the second(book_2)


    # sorting from Z - A

books = ["Charlie and the Chocolate Factory", "War and Peace", "Utopia", "A Brief History of Time", "A Wrinkle in Time"]

# To sort our books in ascending order, in-place
books.sort! { |firstBook, secondBook| firstBook <=> secondBook }

# Z - A
puts(books.sort! { |firstBook, secondBook|
secondBook <=> firstBook})


list = [5,6,7,8,9,10]
list.each do |m|
    puts m * m
    end