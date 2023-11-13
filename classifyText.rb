puts "Copy and Paste text:"
text = gets.chomp
print "Words to Redact?: "
redact = gets.chomp
words = text.split(" ")             # w/o this, it seems like str becomes undefined since assuming there needs to be a temporary variable to hold new text, which
                                    # is then called "words"
words.each do |word|
    if word != redact
        print word + " "
    else
        print "REDACTED "
    end
end