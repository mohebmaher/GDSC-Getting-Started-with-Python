from faker import Faker

fake = Faker()
names = [fake.name() for _ in range(10)]
