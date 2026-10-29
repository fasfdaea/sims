#!/usr/bin/env python3
import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
            return
        if self.satiety >= 100:
            self.satiety = 100
            return
        self.satiety = min(100, self.satiety + 5)
        self.home.food -= 5

    def work(self):
        if not self.car.drive():
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if not self.car.drive():
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return

        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness = min(100, self.gladness + 10)
            self.satiety = min(100, self.satiety + 2)
            self.money -= 15

    def chill(self):
        self.gladness = min(100, self.gladness + 10)
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        title = f" Today the {day} of {self.name}'s life "
        print(f"{title:=^50}\n")
        human_indexes = f"{self.name}'s indexes"
        print(f"{human_indexes:^50}")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        print(f"{'Home indexes':^50}")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        print(f"{self.car.brand + ' car indexes':^50}")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}\n")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False

        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            if self.job is not None:
                print(
                    f"I don't have a job, I'm going to get a job "
                    f"{self.job.job} with salary {self.job.salary}"
                )

        self.days_indexes(day)
        dice = random.randint(1, 4)

        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("There is too much mess, so I will clean the house")
                self.clean_home()
            else:
                print("Let's chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let's chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        else:
            print("Time for treats!")
            self.shopping(manage="delicacies")

        return self.is_alive()


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        print("The car cannot move")
        return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


class Pet:
    def __init__(self, name="Pet"):
        self.name = name
        self.satiety = 50
        self.energy = 60
        self.mood = 60

    def eat(self, human=None):
        if human is not None and human.home is not None and human.home.food > 0:
            human.home.food -= 5
            print(f"{self.name} eats from the house pantry")
        else:
            print(f"{self.name} is eating")
        self.satiety = min(100, self.satiety + 15)
        self.mood = min(100, self.mood + 5)

    def play(self, human):
        if self.satiety <= 0:
            print(f"{self.name} is hungry and cannot play")
            return
        human.gladness = min(100, human.gladness + 10)
        self.satiety = max(0, self.satiety - 8)
        self.energy = max(0, self.energy - 10)
        self.mood = min(100, self.mood + 12)
        print(f"{human.name} is playing with {self.name}")

    def walk(self, human):
        if self.energy <= 0:
            print(f"{self.name} is too tired for a walk")
            self.sleep()
            return
        human.gladness = min(100, human.gladness + 5)
        self.energy = max(0, self.energy - 12)
        self.satiety = max(0, self.satiety - 4)
        self.mood = min(100, self.mood + 8)
        print(f"{self.name} and {human.name} went for a walk")

    def sleep(self):
        self.energy = min(100, self.energy + 25)
        self.mood = min(100, self.mood + 5)
        print(f"{self.name} is sleeping")

    def status(self):
        print(f"{self.name} status: satiety={self.satiety}, energy={self.energy}, mood={self.mood}")

    def act(self, human):
        if self.satiety <= 10:
            print(f"{self.name} is very hungry")
            if human.home is not None and human.home.food > 0:
                self.eat(human)
            else:
                human.gladness = max(0, human.gladness - 5)
                self.mood = max(0, self.mood - 10)
            return

        dice = random.randint(1, 5)
        if self.energy < 20:
            self.sleep()
        elif self.mood < 25:
            self.play(human)
        elif dice == 1:
            self.play(human)
        elif dice == 2:
            self.walk(human)
        elif dice == 3:
            self.eat(human)
        elif dice == 4:
            self.sleep()
        else:
            print(f"{self.name} is sitting on the sofa and watching the owner")
            self.mood = min(100, self.mood + 5)

        self.satiety = max(0, self.satiety - 3)
        self.energy = max(0, self.energy - 2)
        self.mood = max(0, min(100, self.mood - 1))
        self.status()


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}


if __name__ == "__main__":
    nick = Human(name="Nick")
    pet = Pet("Barsik")

    for day in range(1, 8):
        if not nick.live(day):
            break

        print(f"--- Pet routine for day {day} ---")
        pet.act(nick)
        print()