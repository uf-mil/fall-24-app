from collections.abc import Coroutine
from typing import Any, Callable, Protocol


class Serializable(Protocol):
    def __str__(self) -> str:
        ...


class Topic:
    """
    1. Define the constructor for this class with the name of the topic and an empty array of publisher callback functions.
    2. Define the publish function to call all the callback functions that do something with the data being published to the topic.
    3. Define the subscribe function. This function should register a callback function into the array of callback functions associated with this topic.
    """

    def __init__(self, name: str):
        pass

    async def publish(self, data: Serializable):
        pass

    def subscribe(self, callback: Callable[[Serializable], Coroutine[None, None, Any]]):
        pass


class Publisher:
    """
    1. Initialize the publisher by storing the topic it is publishing to.
    2. Define the publish function. The publish function should call the publish function in the publisher.
    """

    def __init__(self, topic: Topic):
        pass

    async def publish(self, data: Serializable):
        pass

class Subscriber:
    """
    1. Initialize the subscriber by passing the topic it is subscribing to as well as the callback function associated with this subscriber.
    2. Define the callback method inside the subscriber to call the callback_func associated with the subscriber.
    """

    def __init__(self, topic: Topic, callback_func: Callable[[Serializable], Coroutine[None, None, Any]]):
        pass

    async def callback(self, data: Serializable):
        pass
