import numpy as np
import random
from collections import defaultdict

class QLearning:
  def __init__(self, actions):
    self.ACTIONS = np.array(actions)
    self.step_size = 0.01
    self.discount_factor = 0.9
    self.epsilon = 0.1
    self.q_table = defaultdict(lambda:[0.0 for _ in range(len(actions))])

  def get_action(self, state):
    if np.random.rand() < self.epsilon:
        action = np.random.choice(self.ACTIONS)
    else:
        q_list = self.q_table[str(state)]
        action = self.ACTIONS[np.random.choice(np.argwhere(q_list == np.amax(q_list)).flatten().tolist())]
    return action

  def learn(self, state, action, reward, next_state):
    
    state, next_state = str(state), str(next_state)
    
    current_q = self.q_table[state][np.argwhere(self.ACTIONS==action)[0][0]]
    next_state_q = max(self.q_table[next_state])

    td = reward + self.discount_factor * next_state_q - current_q
    new_q = current_q + self.step_size * td
    self.q_table[state][np.argwhere(self.ACTIONS==action)[0][0]] = new_q