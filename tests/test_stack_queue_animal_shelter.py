import pytest
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter

def test_animal_enqueue_one():
  animal_instance = AnimalShelter("cat", "F")
  shelter_instance = AnimalShelter()
  shelter_instance.enqueue(animal_instance)
  actual = shelter_instance.cats.peek()
  expected = animal_instance
  assert actual == expected

def test_animal_enqueue_several():
  animal_instance_one = AnimalShelter("dog", "D")
  animal_instance_two = AnimalShelter("cat", "K")
  shelter_instance = AnimalShelter()
  shelter_instance.enqueue(animal_instance_one)
  shelter_instance.enqueue(animal_instance_two)
  actual = shelter_instance.cats.peek()
  expected = animal_instance_two
  assert actual == expected

def test_animal_enqueue_invalid_type():
  animal_instance = AnimalShelter("cow", "Mo")
  shelter_instance = AnimalShelter()
  with pytest.raises(Exception):
    shelter.enqueue(animal_instance)

def test_animal_dequeue_one():
  animal_instance = AnimalShelter("cat", "C")
  shelter_instance = AnimalShelter()
  shelter_instance.enqueue(animal_instance)
  actual = shelter_instance.dequeue("cat")
  expected = animal_instance
  assert actual == expected

def test_animal_dequeue_several():
  animal_instance_one = AnimalShelter("dog", "T")
  animal_instance_two = AnimalShelter("dog", "I")
  shelter_instance = AnimalShelter()
  shelter_instance.enqueue(animal_instance_one)
  shelter_instance.enqueue(animal_instance_two)
  shelter_instance.dequeue("dog")
  actual = shelter_instance.dequeue("dog")
  expected = animal_instance_two
  assert actual == expected

def test_animal_dequeue_several_types():
  animal_instance_one = AnimalShelter("cat", "M")
  animal_instance_two = AnimalShelter("dog", "B")
  shelter_instance = AnimalShelter()
  shelter_instance.enqueue(animal_instance_one)
  shelter_instance.enqueue(animal_instance_two)
  shelter_instance.dequeue("cat")
  actual = shelter_instance.dequeue("dog")
  expected = animal_instance_two
  assert actual == expected
