import random

class Chef:
    def __init__(self, name, skill, speed, creativity):
        self.name = name
        self.skill = skill
        self.speed = speed
        self.creativity = creativity
        self.score = 0
        self.active = True

    def compete(self, opponent):
        points = self.skill + self.creativity - opponent.speed
        if points < 1:
            points = 1

        print(f"Chef {self.name} competes with {opponent.name}")

        self.score += points
        opponent.take_points(points)

    def take_points(self, points):
        self.score -= points
        print(f"{self.name} takes {points} points. Score: {self.score}")

        if self.score < 0:
            self.score = 0
            self.active = False
            print(f"{self.name} has been eliminated!")

    def is_active(self):
        return self.active

    def show_stats(self):
        print(
            f"Name: {self.name}, "
            f"Skill: {self.skill}, "
            f"Speed: {self.speed}, "
            f"Creativity: {self.creativity}, "
            f"Score: {self.score}, "
            f"Active: {self.active}"
        )


class CookingContest:
    def __init__(self):
        self.chefs = []

    def add_chef(self, chef):
        self.chefs.append(chef)

    def get_active_chefs(self):
        return [chef for chef in self.chefs if chef.active]

    def start_contest(self):
        print("Contest started!")

        while len(self.get_active_chefs()) > 1:
            active_chefs = self.get_active_chefs()

            chef1 = random.choice(active.chefs)
            chef2 = random.choce([c for c in active_chefs if c !=chef1])

            chef1.compete(shef2)

            if chef2.active:
                chef2.compete(shef1)

            print("Current state of all chefs:")
            for chef in self.chefs:
                chef.show_stats()
            print()

    def show_winner(self):
        active_chefs = self.get_active_chefs()
        if len(active_chefs) == 1:
            print(f"Winner: {active_chefs[0].name}")

chef1 = Chef("Alice", 10, 5, 7)
chef2 = Chef("Bob", 8, 6, 6)
chef3 = Chef("Carol", 9, 4, 8)

contest = CookingContest()
contest.add_chef(chef1)
contest.add_chef(chef2)
contest.add_chef(chef3)

contest.start_contest()
contest.show_winner()

        