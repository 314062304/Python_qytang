import random

Section1 = random.randint(1, 255)
Section2 = random.randint(1, 255)
Section3 = random.randint(1, 255)
Section4 = random.randint(1, 255)

random_ip = str(Section1) + '.' + str(Section2) + '.' + str(Section3)+'.' + str(Section4)

print(random_ip)