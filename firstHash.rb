my_hash = {
    "name" => "Miguel Mozo",
    "age" => 22,
    "hobbies" => ['snowboarding', 'hiking', 'coding'],
    "hungry" => true
}

puts(my_hash["name"])               # only works with brackets to be called upon, not based on index
puts(my_hash["hobbies"])



pets = Hash.new                    # setting up blank hash with a name
pets["Cat"] = "Benny"               # establishes key name, then value
puts pets["Cat"]
puts(pets)