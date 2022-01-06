from eventsourcing.application import Application
from dotenv import load_dotenv

from aggregations import Dog

load_dotenv()


class Zoo(Application):
    def create_dog(self, name):
        dog = Dog(name)
        self.save(dog)
        return dog.id

    def add_dog_trick(self, dog_id, trick):
        dog = self.repository.get(dog_id)
        dog.add_trick(trick)
        self.save(dog)

    def get_dog_history(self, dog_id):
        dog = self.repository.get(dog_id)
        return dog.tricks
