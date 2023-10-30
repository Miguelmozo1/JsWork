puts("Any string to change")
string = gets.chomp
string.downcase!
if string.include? "s"
    string.gsub!(/s/, "th")
    puts("#{string}")
else
    print "Nothing to change here\n"
end