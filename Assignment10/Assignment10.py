class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_animal_tpe(self):
        return self.animal_type


def main():
    pet_name = input('Please enter the name of your pet: ')
    pet_type = input('What type of pet do you have? ')   
    pet_age = float(input('How old is your pet? '))

    pet_specs = Pet(pet_name, pet_type, pet_age)

    print('pet name is ', pet_specs.get_name())
    print('pet type is ', pet_specs.get_animal_tpe())
    print('pet age is ', pet_specs.get_age())
    
if __name__ == '__main__':
    main()
    

# pet = {'name': ' ', 'age': ' ', 'type': ' '}  
pet1 = {'name': 'Anna', 'age': '7', 'type': 'cat'}
pet2 = {'name': 'Jackie', 'age': '5', 'type': 'cat'}
pet3 = {'name': 'Jillian', 'age': '5', 'type': 'cat'}
pet4 = {'name': 'Kiwi', 'age': '8', 'type': 'dog'}
pet5 = {'name': 'Watson', 'age': '9', 'type': 'cat'}
print('\n', pet1, '\n', pet2, '\n', pet3, '\n', pet4, '\n', pet5)
# print(pet)