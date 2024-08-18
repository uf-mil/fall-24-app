class Topic:
    """
    1. Define the constructor for this class with the name of the topic and an empty array of publisher callback functions.
    2. Define the publish function to call all the callback functions that do something with the data being published to the topic.
    3. Define the subscribe function. This function should register a callback function into the array of callback functions associated with this topic.
    """
    def __init__(self, name):
        pass

    async def publish(self, data):
        pass

    def subscribe(self, callback):
        pass

class Publisher:
    """
    1. Initialize the publisher by storing the topic it is publishing to.
    2. Define the publish function. The publish function should call the publish function in the publisher.
    """
    def __init__(self, topic):
        pass

    async def publish(self, data):
        pass

class Subscriber:
    """
    1. Initialize the subscriber by passing the topic it is subscribing to as well as the callback function associated with this subscriber.
    2. Define the callback method inside the subscriber to call the callback_func associated with the subscriber.
    """
    def __init__(self, topic, callback_func):
        pass

    async def callback(self, data):
        pass
