# The solution was tested locally for:
#   A. Scenario 1 and 2

# Running the code (The code was developed using Python 3.12.6)
# Via command line: simply run the file using the python or python3 command followed by the file name.
# Via IDE: open the file and click run.

# Assumptions: Only valid inputs are provided by the user.

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Car:
    directions = ['N', 'E', 'S', 'W']

    def __init__(self, name="", x="", y="", direction=""):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = []
        self.result = ""

    def add_commands(self, commands):
        self.commands.extend(commands)

    def turn_left(self):
        current_index = Car.directions.index(self.direction)
        self.direction = Car.directions[(current_index - 1) % 4]

    def turn_right(self):
        current_index = Car.directions.index(self.direction)
        self.direction = Car.directions[(current_index + 1) % 4]

    def move_forward(self, field):
        if self.direction == 'N' and self.y < field.height - 1:
            self.y += 1
        elif self.direction == 'E' and self.x < field.width - 1:
            self.x += 1
        elif self.direction == 'S' and self.y > 0:
            self.y -= 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1

    def execute_command(self, command, field):
        if command == 'L':
            self.turn_left()
        elif command == 'R':
            self.turn_right()
        elif command == 'F':
            self.move_forward(field)


def main():
    start_over = True
    while start_over is True:
        print("Welcome to Auto Driving Car Simulation!\n")
        
        width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
        field = Field(width, height)
        print(f"You have created a field of {width} x {height}.")
        cars = []
    
        while True:
            print("\nPlease choose from the following options:")
            print("[1] Add a car to field")
            print("[2] Run simulation")
            choice = input()

            if choice == '1':
                name = input("Please enter the name of the car: ")
                x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format: ").split()
                car = Car(name, int(x), int(y), direction)
                commands = input(f"Please enter the commands for car {name}: ")
                car.add_commands(commands)
                cars.append(car)
                print("\nYour current list of cars are:")
                for c in cars:
                    print(f"- {c.name}, ({c.x},{c.y}) {c.direction}, {''.join(c.commands)}")
            
            elif choice == '2':
                print("\nYour current list of cars are:")
                for c in cars:
                    print(f"- {c.name}, ({c.x},{c.y}) {c.direction}, {''.join(c.commands)}")
                previous_car = Car()
                for step in range(max(len(car.commands) for car in cars)):
                    for car in cars:
                        if step < len(car.commands):
                            car.execute_command(car.commands[step], field)
                            if car.name != previous_car.name and car.x == previous_car.x and car.y == previous_car.y:
                                car.commands = car.commands[0:step]
                                previous_car.commands = previous_car.commands[0:step]
                                car.result = f"- {car.name}, collides with {previous_car.name} at ({car.x},{car.y}) at step {step + 1}"
                                previous_car.result = f"- {previous_car.name}, collides with {car.name} at ({car.x},{car.y}) at step {step + 1}"
                        if "collides" not in car.result:
                            car.result = f"- {car.name}, ({car.x},{car.y}) {car.direction}"
                        previous_car = car

                print("\nAfter simulation, the result is:")
                for car in cars:
                    print(car.result)
                
                print("\nPlease choose from the following options:")
                print("[1] Start over")
                print("[2] Exit")
                end_choice = input()
                if end_choice == '1':
                    break
                elif end_choice == '2':
                    print("Thank you for running the simulation. Goodbye!")
                    start_over = False
                    break
        

if __name__ == "__main__":
    main()
