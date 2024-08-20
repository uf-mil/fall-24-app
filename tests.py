import asyncio
import unittest
from collections.abc import Callable

import numpy as np
import pygame

from constants import BLUE, HEIGHT, ORANGE, WIDTH
from path_following import PathFollowing
from pubsub import Publisher, Subscriber, Topic

pygame.init()
pygame.display.set_caption("MIL's next big robot project")


class Test(unittest.IsolatedAsyncioTestCase):

    DOWN_CAM_TOPIC = Topic("/robot/camera")
    DOWN_CAM_PUBLISHER = Publisher(DOWN_CAM_TOPIC)

    async def test_multiple_subscribers(self):
        """
        Ensure that two subscribers will hear the same messages.
        """
        topic = Topic("/test")
        publisher = Publisher(topic)
        cb1_val, cb2_val = 0, 0

        async def cb1(x):
            nonlocal cb1_val
            cb1_val = x

        async def cb2(x):
            nonlocal cb2_val
            cb2_val = x

        Subscriber(topic, cb1)
        Subscriber(topic, cb2)
        for i in range(10):
            await publisher.publish(i)
            await asyncio.sleep(0.1)
            self.assertEqual(cb1_val, i)
            self.assertEqual(cb2_val, i)

    async def update_position(self, position):
        pygame.draw.circle(self.screen, (255, 0, 0), position, 10)
        pygame.display.flip()

    def down_cam_driver(self, center_x, center_y):
        """
        This function allows us to tap into the simulation and get a 10-by-10 square of colors near the robot. The name of this function is a tribute to how we collect data from our sensors in the lab.
        """
        half_size = 10  # 20x20 matrix, so half size is 10
        matrix = np.zeros(
            (20, 20, 3),
            dtype=np.uint8,
        )  # Initialize a 20x20 matrix with RGB channels

        for i in range(-half_size, half_size):
            for j in range(-half_size, half_size):
                x = center_x + i
                y = center_y + j
                if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                    matrix[i + half_size, j + half_size] = self.screen.get_at((x, y))[
                        :3
                    ]  # Get the color

        return matrix

    async def capture_matrix(self, position):
        # Sample publisher
        matrix = self.down_cam_driver(position[0], position[1])
        await self.DOWN_CAM_PUBLISHER.publish(matrix)
        await self.update_position(position)

    # Run the Pygame event loop in a separate task
    async def pygame_event_loop(self, topic: Topic, draw_path: Callable[[int, int], None]):
        x, y = 0, 15

        async def _set_vars(position):
            nonlocal x, y
            x, y = position

        Subscriber(topic, _set_vars)
        while True:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                draw_path(x, y)
                await self.capture_matrix((x, y))
                await asyncio.sleep(0)
            except asyncio.CancelledError:
                break

    async def test_path_1(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        PATH = [
            ((0, 15), (400, 15)),
            ((400, 15), (400, 200)),
            ((400, 200), (600, 400)),
            ((600, 400), (790, 200)),
            ((790, 200), (790, 600)),
        ]

        def _draw_path(x, y):
            self.screen.fill(BLUE)
            for start, end in PATH:
                pygame.draw.line(self.screen, ORANGE, start, end, 10)
            # Ensure that x and y are near the path
            on_path = False
            for start, end in PATH:
                min_x, max_x = min(start[0], end[0]), max(start[0], end[0])
                min_y, max_y = min(start[1], end[1]), max(start[1], end[1])
                if (min_x - 10) <= x <= (max_x + 10) and (min_y - 10) <= y <= (max_y + 10):
                    on_path = True
                    break
            self.assertTrue(on_path)

        topic = Topic("/robot/position")
        main_task = asyncio.create_task(
            PathFollowing(topic, self.DOWN_CAM_TOPIC, 0.1).main(),
        )
        game_task = asyncio.create_task(self.pygame_event_loop(topic, _draw_path))
        try:
            _, pending = await asyncio.wait(
                [main_task, game_task],
                timeout=60,
                return_when=asyncio.FIRST_COMPLETED,
            )
            for task in pending:
                task.cancel()
        except KeyboardInterrupt:
            pass
        finally:
            pygame.quit()


if __name__ == "__main__":
    unittest.main()
