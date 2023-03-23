from faker import Faker

fake = Faker()

random_words = []
for _ in range(100_000):
    random_words.append(fake.word())
random_words = " ".join(random_words)

with open("random_words.txt", mode="wt") as text_file:
    text_file.write(random_words)