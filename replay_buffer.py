class ReplayBuffer:
    pass
class Trajectory:
    def __init__(self):
        self.states = []
        self.actions = []
        self.rewards = []
    
    def add(self, state, action, reward):
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)