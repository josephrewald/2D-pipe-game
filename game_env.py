import gym
import numpy as np
from pixel_game import PixelGame

class PixelLineGameEnv(gym.Env):
    def __init__(self):
        super(PixelLineGameEnv, self).__init__()
        self.game = PixelGame()
        self.action_space = gym.spaces.Discrete(4)  # Up, Down, Left, Right
        self.observation_space = gym.spaces.Box(low=0, high=max(self.game.width, self.game.height), shape=(4,), dtype=np.float32)

    def reset(self):
        self.game.reset()
        return self._get_observation()

    def step(self, action):
        self.game.step(action)
        done = self.game.current_pos == self.game.end_pos #TODO: add this back into the game itself
        reward = -np.linalg.norm(np.array(self.game.current_pos) - np.array(self.game.end_pos)) / 100
        self.game.render()
        return self._get_observation(), reward, done, {}

    def _get_observation(self):
        return np.array(self.game.current_pos + self.game.end_pos)

    def render(self):
        self.game.render()
