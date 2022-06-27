import pytest
from stack_queue_pseudo.stack_queue_pseudo import Pseudo_Queue

def test_pseudoqueue_enqueue_one():
  q = Pseudo_Queue()
  q.enqueue(1)
  actual = q.s1.peek()
  expected = 1
  assert actual == expected

def test_pseudoqueue_enqueue_many():
  q = Pseudo_Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  q.enqueue(4)
  q.enqueue(5)
  actual = q.s1.peek()
  expected = 5
  assert actual == expected

def test_pseudoqueue_dequeue_one():
  q = Pseudo_Queue()
  q.enqueue(1)
  actual = q.dequeue()
  expected = 1
  assert actual == expected

def test_pseudoqueue_dequeue_many():
  q = Pseudo_Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  q.dequeue()
  q.dequeue()
  actual = q.dequeue()
  expected = 1
  assert actual == expected