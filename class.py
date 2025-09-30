
# class assignment
class Hero:
    def __init__(self, name, secret_identity):
        self.name = name 
        self._secret_identity = secret_identity
        self._power_level = 100 
    
    def train(self):  
        self._power_level += 10
        print(f"{self.name} trained hard! Power level now: {self._power_level}")
    
    def get_power_level(self):
        return self._power_level
    
    def activate_power(self):
        print(f"{self.name} activates basic power!")

class Superhero(Hero):
    def __init__(self, name, secret_identity, superpower, weakness):
        super().__init__(name, secret_identity)  # Call parent constructor
        self.superpower = superpower  # Unique attribute
        self.weakness = weakness  # Unique attribute
    
    def activate_power(self): 
        print(f"{self.name} unleashes {self.superpower}! But watch out for {self.weakness}.")
    
    def reveal_identity(self): 
        print(f"Shh! {self.name}'s secret identity is {self._secret_identity}")

# Example usage - creating unique objects
if __name__ == "__main__":
    # Basic Hero
    basic_hero = Hero("Captain Courage", "Clark Kent")
    basic_hero.train()
    basic_hero.activate_power()
    
    # Superhero instances with unique values
    superman = Superhero("Superman", "Clark Kent", "Super Strength", "Kryptonite")
    batman = Superhero("Batman", "Bruce Wayne", "Gadgets", "No superpowers")
    
    superman.activate_power() 
    batman.activate_power()   
    batman.reveal_identity()
    print(f"Superman's power level: {superman.get_power_level()}")