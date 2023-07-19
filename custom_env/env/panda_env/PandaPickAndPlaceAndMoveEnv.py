import numpy as np
import random
import time

from panda_gym.envs.core import RobotTaskEnv
from panda_gym.envs.robots.panda import Panda
from custom_env.env.task.PandaPickAndPlaceAndMoveTask import PandaPickAndPlaceMoveTask
from panda_gym.pybullet import PyBullet
from typing import Any, Dict, Optional, Tuple, Union, Final
from panda_gym.utils import distance
import pybullet as p


class PandaPickAndPlaceAndMoveEnv(RobotTaskEnv):
    """Pick and Place task wih Panda robot.
    Args:
        render (bool, optional): Activate rendering. Defaults to False.
        reward_type (str, optional): "sparse" or "dense". Defaults to "sparse".
        control_type (str, optional): "ee" to control end-effector position or "joints" to control joint values.
            Defaults to "ee".
    """

    def __init__(self, render: bool = False, reward_type: str = "sparse", control_type: str = "ee") -> None:
        sim = PyBullet(render=render)
        robot = Panda(sim, block_gripper=False, base_position=np.array([-0.6, 0.0, 0.0]), control_type=control_type)
        task = PandaPickAndPlaceMoveTask(sim, reward_type="dense")
        super().__init__(robot, task)

    def step(self, action: np.ndarray) -> Tuple[Dict[str, np.ndarray], float, bool, Dict[str, Any]]:
        self.task.take_step()

        if self.ayhaga() == 0:
            self.robot.set_action(action)
        elif self.ayhaga() == 1:
            if not hasattr(self, "elapsed_time"):
                link_index = 6
                desired_position = np.array([0, 0, 0.5])
                desired_orientation = np.array([1, 0, 0, 0.001])

                joint_angles = self.robot.inverse_kinematics(link=link_index, position=desired_position,
                                                             orientation=desired_orientation)
                # Set the desired joint angles for the robot
                self.robot.set_joint_angles(joint_angles)
            if self.elapsed_time < 0.5:
                self.robot.set_action(action)
                self.elapsed_time += self.sim.dt

        '''    
        elif self.ayhaga() == 1:
            link_index = 6
            desired_position = np.array([0, 0, 0.5])
            desired_orientation = np.array([1, 0, 0, 0.001])

            joint_angles = self.robot.inverse_kinematics(link=link_index, position=desired_position,
                                                         orientation=desired_orientation)
            # Set the desired joint angles for the robot
            self.robot.set_joint_angles(joint_angles)
          '''


        self.sim.step()
        obs = self._get_obs()
        done = False
        info = {"is_success": self.task.is_success(obs["achieved_goal"], self.task.get_goal())}
        reward = self.task.compute_reward(obs["achieved_goal"], self.task.get_goal(), info)
        assert isinstance(reward, float)  # needed for pytype cheking
        return obs, reward, done, info

    def reset(self) -> Dict[str, np.ndarray]:
        self.task.moving_direction = random.randint(0, 1)
        self.elapsed_time = 0
        return super(PandaPickAndPlaceAndMoveEnv, self).reset()

    def ayhaga(self):
        return (self.task.is_success(self.sim.get_base_position('object'), self.sim.get_base_position('target')))
