p_rod = {
    "name": "Paul Rodriguez",
    "age": 38,
    "stance": "Goofy",
    "sponosor": "Primitive"
}

y_horigome = {
    "name": "Yuto Horigome",
    "age": 24,
    "stance": "Goofy",
    "sponsor": "April"
}

players = [
    {
    "name": "Kevin Durant", 
	"age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
	"name": "Jason Tatum", 
    "age":24, 
	"position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
	"age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    }
]

# player_list = []
# for i in players:
#     player_list.append(i)
# print(player_list)


class Pro:
    def __init__(self, pro):
        self.name = pro["name"]
        self.age = pro["age"]
        self.stance = pro["stance"]
        self. sponsor = pro["sponsor"]

class Players:
    def __init__(self, list):
        self.name = list["name"]
        self.age = list["age"]
        self.team = list["team"]
    @classmethod
    def get_all(cls, team_list):
        team = []
        for mate in team_list:
            player = Players(mate)
            team.append(player)
        print(team)

Players.get_all(players)


c_joslin = {
    "name": "Chris Joslin",
    "age": 27,
    "stance": "Regular",
    "sponsor": "Zero"
}



# first_pro = Pro(c_joslin)
# print(first_pro.sponsor)
