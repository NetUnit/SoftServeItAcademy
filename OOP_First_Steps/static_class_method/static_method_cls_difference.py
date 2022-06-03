### 3
### @ classmethod 
### @ staticmethod
#####################################
class Human:
    # Атрибут класу
    species = "Homosapiens"
    name = 'Jacky'
    # Конструктор
    def __init__(self, name=name):
        self.name = name
    
    #метод екземпляру класу
    def say(self, msg):
        return "{name}>>> {message}".format(name=self.name, message=msg)
    
    # Метод класу
    @classmethod
    def get_species(cls):
        return cls.species
        
    # Статичний метод викликається без посилання на класс чи екземпляр
    @staticmethod
    def grunt():
        return "*Static*"

instance = Human()

# classmethod
# @classmethod - це звичайний метод класу, що має доступ до всіх атрибутам класу, 
# через який він був викликаний. Следовательно, classmethod - це метод, який прив'язується
# до класу, а не до екземпляру класу
print(Human.get_species())

# staticmethod - метод без параметру self, можна викликати поза класом за допомогою будь-якого instance
# @staticmethod використовується, коли ми хочемо повернтуи одне і те ж, незалежно від викликаного дочірнього класу
print(Human.grunt()) ## функція всередині класу котру можна викликати як від екз так і від самого класу
print(instance.grunt())

# method say
print(instance.say('say something'))