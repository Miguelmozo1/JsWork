class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    def display_info(self):
        if self.is_rewards_member == True:
            print(f"No stranger to us {self.first_name}")
        # used multiple f strings since like calling different attributes, you have to list them one by one and not all at once. Ex. user_1.age has to be called individually
        # can possibly use one large f string as long as we format it with dot notation and list out the attributes in order
        print(f"User first name: {self.first_name}\n" + f"User last name: {self.last_name}\n" + f"User email: {self.email}\n" + f"User age: {self.age}\n" + 
                f"Rewards Member: {self.is_rewards_member}\n" + f"Gold Points: {self.gold_card_points}\n")
        return self
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"Insufficient funds")
        else:
            self.gold_card_points -= amount
            print(f"Updated Amount: {self.gold_card_points}")
        return self


user_1 = User("Miguel", "Mozo", "mmozo", "22")
user_1.enroll().display_info().spend_points(267)


