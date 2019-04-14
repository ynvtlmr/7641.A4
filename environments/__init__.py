import gym
from gym.envs.registration import register

from .cliff_walking import *
from .frozen_lake import *

__all__ = ['RewardingFrozenLakeEnv']  # , 'WindyCliffWalkingEnv']

# register(
#     id='RewardingFrozenLake-v0',
#     entry_point='environments:RewardingFrozenLakeEnv',
#     kwargs={'map_name': '4x4'},
# )

register(
    id='RewardingFrozenLake4x4-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '4x4'}
)

register(
    id='RewardingFrozenLakeNoRewards4x4-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '4x4', 'rewarding': False}
)

register(
    id='DeterministicFrozenLakeNoRewards4x4-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '4x4', 'rewarding': False, 'is_slippery': False}
)

register(
    id='DeterministicFrozenLakeRewarding4x4-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '4x4', 'rewarding': True, 'is_slippery': False}
)
# ----

register(
    id='RewardingFrozenLake11x11-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '11x11'}
)

register(
    id='RewardingFrozenLakeNoRewards11x11-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '11x11', 'rewarding': False}
)

register(
    id='DeterministicFrozenLakeNoRewards11x11-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '11x11', 'rewarding': False, 'is_slippery': False}
)

register(
    id='DeterministicFrozenLakeRewarding11x11-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '11x11', 'rewarding': True, 'is_slippery': False}
)

# ----

register(
    id='RewardingFrozenLake22x23-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '22x23', 'rewarding': True}
            # ,'step_reward': -0.001, 'hole_reward': -0.01, 'goal_reward': 1}
)

register(
    id='RewardingFrozenLakeNoRewards22x23-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '22x23', 'rewarding': False}
)

register(
    id='DeterministicFrozenLakeNoRewards22x23-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '22x23', 'rewarding': False, 'is_slippery': False}
)

# ----

register(
    id='RewardingFrozenLake88x94-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '88x94'}
)

register(
    id='RewardingFrozenLakeNoRewards88x94-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '88x94', 'rewarding': False}
)

register(
    id='DeterministicFrozenLakeNoRewards88x94-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '88x94', 'rewarding': False, 'is_slippery': False}
)

register(
    id='DeterministicFrozenLakeRewarding88x94-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '88x94', 'rewarding': True, 'is_slippery': False,
            'step_reward': -0.00001, 'hole_reward': -0.001, 'goal_reward': 1}
)

def get_rewarding_frozen_lake_environment():
    return gym.make('RewardingFrozenLake4x4-v0')


def get_rewarding_no_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeNoRewards4x4-v0')


def get_deterministic_no_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeNoRewards4x4-v0')


def get_deterministic_rewarding_frozen_lake_environment():
    return gym.make('DeterministicFrozenLakeRewarding4x4-v0')

# ---

def get_large_rewarding_frozen_lake_environment():
    return gym.make('RewardingFrozenLake11x11-v0')


def get_large_rewarding_no_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeNoRewards11x11-v0')


def get_large_deterministic_no_reward_frozen_lake_environment():
    return gym.make('DeterministicFrozenLakeNoRewards11x11-v0')

def get_large_deterministic_rewarding_frozen_lake_environment():
    return gym.make('DeterministicFrozenLakeRewarding11x11-v0')

# ---

def get_complex_rewarding_frozen_lake_environment():
    return gym.make('RewardingFrozenLake22x23-v0')


def get_complex_rewarding_no_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeNoRewards22x23-v0')


def get_complex_deterministic_no_reward_frozen_lake_environment():
    return gym.make('DeterministicFrozenLakeNoRewards22x23-v0')


# ---

def get_88_rewarding_frozen_lake_environment():
    return gym.make('RewardingFrozenLake88x94-v0')


def get_88_rewarding_no_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeNoRewards88x94-v0')


def get_88_deterministic_no_reward_frozen_lake_environment():
    return gym.make('DeterministicFrozenLakeNoRewards88x94-v0')


def get_88_deterministic_rewarding_frozen_lake_environment():
    return gym.make('DeterministicFrozenLakeRewarding88x94-v0')