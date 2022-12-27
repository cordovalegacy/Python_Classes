class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    

    def display_info(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member is False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"{self.is_rewards_member}: {self.first_name} is now a member!")
            print(f"Your new balance is {self.gold_card_points}")
        else:
            print(f"{self.first_name} {self.last_name} is already a member")
        return self

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print(f"{self.first_name} only has {self.gold_card_points} to spend")
        return self

user_id_1 = User("Brendan", "Cordova", "cordovalegacy19@gmail.com", 27)
user_id_2 = User("Tori", "Cordova", "t.mccullar@hotmail.com", 26)

user_id_1.enroll()

user_id_1.spend_points(200)

user_id_1.display_info()

user_id_2.enroll()

user_id_2.enroll() #again for falsey check

user_id_2.spend_points(500) #checking validation

user_id_2.display_info()