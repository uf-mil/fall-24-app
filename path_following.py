from classes import Topic


class PathFollowing:
    # Start Position
    x = 0
    y = 15

    def __init__(
        self, position_topic: Topic, down_cam_topic: Topic, delay: float = 0.1,
    ):
        """
        Args:
            position_topic: The topic for the robot's position.
            down_cam_topic: The topic for the color camera, which you can use
                to coordinate the robot's movement along the path.
            delay: The delay between each position update that your path following
                algorithm should respect, in seconds.
        """
        pass

    async def main(self):
        """
        The main function to handle the path following and position updates.
        This function should return once done!
        """
        pass
