from grid import *
from statistics import mean

import random
import copy
import collections

# Class that represents physical objects that can be shown at an environment.
# Each "thing" can have an attribute .__name__ used as an output.

class Thing(object):

    def __repr__(self):
        return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))

    def is_alive(self):
        "Things that are 'alive' must return True."
        return hasattr(self, 'alive') and self.alive

    def show_state(self):
        "Shows the internal state of the agent. Subclasses must replace."
        print("I don't know how to show the state.")

    def display(self, canvas, x, y, width, height):
        "Show an image of this 'thing' in screen."
        pass


class Agent(Thing):

    def __init__(self, program=None):
        self.alive = True
        self.bump = False
        self.holding = []
        self.performance = 0
        if program is None:
            def program(percept):
                return eval(input('Percept={}; action? ' .format(percept)))
        assert isinstance(program, collections.Callable)
        self.program = program

    def can_grab(self, thing):
        """Return True if this agent is able to catch this "thing".
        Replace for apropriate subclasses of Agent and Thing."""
        return False


def TraceAgent(agent):
    """Goes with the agent's program to print its input and output.
    This will let the user see what the agent is doing at the environment."""

    old_program = agent.program

    def new_program(percept):
        action = old_program(percept)
        print('{} notices {} and does {}'.format(agent, percept, action))
        return action
    agent.program = new_program
    return agent


def TableDrivenAgentProgram(table):
    """This agent selects an action based in a sequence of perceptions.
    For big domains it's not usable.
    To customize it, pass a dictionary as table for all the pairs.
    Ex.: {Percept_sequence: action}"""

    percepts = []

    def program(percept):
        percepts.append(percept)
        action = table.get(tuple(percepts))
        return action
    return program


def RandomAgentProgram(actions):
    "An agent who chooses an action randomly, ignoring all the perceptions."
    return lambda percept: random.choice(actions)


def SimpleReflexAgentProgram(rules, interpret_input):
    "This agent take actions only based in the perception."
    def program(percept):
        state = interpret_input(percept)
        rule = rule_match(state, rules)
        action = rule.action
        return action
    return program


def ModelBasedReflexAgentProgram(rules, update_state):
    "This agent take actions based in perception and state."
    def program(percept):
        program.state = update_state(program.state, program.action, percept)
        rule = rule_match(program.state, rules)
        action = rule.action
        return action
    program.state = program.action = None
    return program


def rule_match(state, rules):
    "Finds the first rule that matches the state."
    for rule in rules:
        if rule.matches(state):
            return rule


# Environment

class Environment(object):
    """Class that represents an environment.

    Percept: Defines the perceptions that an agent notices.
    Execute_action: Defines the effects of the execution of an action. Also update the agent.performance.

    The Environment keeps a list of .things and .agents.
    Each agent has a slot of performance that starts with 0. 
    Each thing has a slot of location, even those that don't need it."""

    def __init__(self):
        self.things = []
        self.agents = []

    # List of classes in Environment
    def thing_classes(self):
        return []  

    def percept(self, agent):
        '''
            Returns the perception that the agent sees. It can be implemented based in Environment.
        '''
        raise NotImplementedError

    def execute_action(self, agent, action):
        "Changes the world (Environment)."
        raise NotImplementedError

    def default_location(self, thing):
        "Standard location to add new 'Thing'."
        return None

    def exogenous_change(self):
        "Verifies if there are spontaneous changes in the 'world'."
        pass

    def is_done(self):
        "Ends the program when there is no alive agent avaiable."
        return not any(agent.is_alive() for agent in self.agents)

    def step(self):
        "Executing the Environment for one time step."
        if not self.is_done():
            actions = []
            for agent in self.agents:
                if agent.alive:
                    actions.append(agent.program(self.percept(agent)))
                else:
                    actions.append("")
            for (agent, action) in zip(self.agents, actions):
                self.execute_action(agent, action)
            self.exogenous_change()

    def run(self, steps=1000):
        "Eexcuting the Environment for a determined number of time steps"
        for step in range(steps):
            if self.is_done():
                return
            self.step()

    def list_things_at(self, location, tclass=Thing):
        "Returning all the things in the determined location"
        return [thing for thing in self.things
                if thing.location == location and isinstance(thing, tclass)]

    def some_things_at(self, location, tclass=Thing):
        """Returns True if at least one of the things in local 
        is an instance of class tclass."""
        return self.list_things_at(location, tclass) != []

    def add_thing(self, thing, location=None):
        """Add a new thing in Environment, defining its location."""

        if not isinstance(thing, Thing):
            thing = Agent(thing)
        assert thing not in self.things, "Don't add the same thing twice"
        thing.location = location if location is not None else self.default_location(thing)
        self.things.append(thing)
        if isinstance(thing, Agent):
            thing.performance = 0
            self.agents.append(thing)

    def delete_thing(self, thing):
        """Remove uma coisa no ambiente."""
        try:
            self.things.remove(thing)
        except ValueError as e:
            print(e)
            print("  in Environment delete_thing")
            print("  Thing to be removed: {} at {}" .format(thing, thing.location))
            print("  from list: {}" .format([(thing, thing.location) for thing in self.things]))
        if thing in self.agents:
            self.agents.remove(thing)

class Direction():
    """A direction class for agents who want to move in a 2D plan."""

    D = "right"
    A = "left"
    W = "up"
    S = "down"

    def __init__(self, direction):
        self.direction = direction

    def __add__(self, heading):
        if self.direction == self.D:
            return{
                self.D: Direction(self.S),
                self.A: Direction(self.W),
            }.get(heading, None)
        elif self.direction == self.L:
            return{
                self.D: Direction(self.W),
                self.A: Direction(self.A),
            }.get(heading, None)
        elif self.direction == self.W:
            return{
                self.D: Direction(self.D),
                self.A: Direction(self.A),
            }.get(heading, None)
        elif self.direction == self.S:
            return{
                self.D: Direction(self.A),
                self.A: Direction(self.D),
            }.get(heading, None)

    def move_forward(self, from_location):
        x, y = from_location
        if self.direction == self.D:
            return (x+1, y)
        elif self.direction == self.A:
            return (x-1, y)
        elif self.direction == self.W:
            return (x, y-1)
        elif self.direction == self.S:
            return (x, y+1)


class Obstacle(Thing):
    """Something that can represent a limit, preventing an agent from
    moving to the same space as it is now."""
    pass


class Wall(Obstacle):
    pass


def compare_agents(EnvFactory, AgentFactories, n=10, steps=1000):
    """Compares several agents in n instances in an Environment."""
    envs = [EnvFactory() for i in range(n)]
    return [(A, test_agent(A, steps, copy.deepcopy(envs)))
            for A in AgentFactories]


def test_agent(AgentFactory, steps, envs):
    "Returns the average score of execution (performance) of an agent in each of the Environments for each step."
    def score(env):
        agent = AgentFactory()
        env.add_thing(agent)
        env.run(steps)
        return agent.performance
    return mean(map(score, envs))
