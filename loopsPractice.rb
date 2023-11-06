counter = 0

until counter == 11
    puts(counter)
    counter += 1
end


for x in 1 .. 10            # this tells loop to equal to 10
    puts(x)
end

for i in 1 ... 10           # this tells loop to be up to 10, but not included
    puts(i)
end

v = 20                          # new loop concept seen
loop do
    puts "#{v}"
    v += 1
    break if v >= 26
end

b = 10                  # prints out every integer that's not a factor of 2
loop do
    b -= 1
    next if b % 2 != 0
    puts "#{b}"
    break if b <= 0
end


15.times{puts"school"}