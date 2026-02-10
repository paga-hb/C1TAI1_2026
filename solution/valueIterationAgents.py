import mdp, util, math
import numpy as np

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        for iteration in range(iterations):
            values = self.values.copy()
            # Loop over all states and update each state based on the Bellman equation
            for state in self.mdp.getStates():
                q_values = []
                if not self.mdp.isTerminal(state):
                    # V(s) = max_a Q(s,a) = max_a sum_{s'} P(s'|s,a) [R(s,a,s') + gamma * V(s')]
                    for action in self.mdp.getPossibleActions(state):
                        q_values.append(self.getQValue(state, action)) # Q(s,a)
                    values[state] = max(q_values) # V(s) = max_a Q(s,a)
            self.values = values

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()

        gamma = self.discount
        q_value = 0

        # Q(s,a) = sum_{s'} P(s'|s,a) [R(s,a,s') + gamma * V(s')]
        for next_state, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            r = self.mdp.getReward(state, action, next_state)
            v = self.getValue(next_state)
            q_value += prob * (r + gamma * v) # Q(s,a) += P(s'|s,a) [R(s,a,s') + gamma * V(s')]
        return q_value


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()

        values = util.Counter()

        # PI(s) = a* = argmax_a Q(s,a)
        for action in self.mdp.getPossibleActions(state):
            values[action] = self.getQValue(state, action) # Q(s,a)
        try:
            return values.argMax() # argmax_a Q(s,a)
        except Exception as e:
            return None

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
