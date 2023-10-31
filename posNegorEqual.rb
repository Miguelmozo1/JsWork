puts("Please Choose any Integer")               # puts makes a new line after, whereas print continues on same line
int = Integer(gets.chomp)                       # Converts string into integar, case sensative!
if int > 0
    puts("You chose a positive!")
elsif int < 0
    puts("You chose a negative!")
else
    puts("You choose zero")
end
