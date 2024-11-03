import random

class AI:
    def __init__(self, max_turns):
        """
        Initialize any data structures or variables needed before the simulation starts.
        """
        self.turn = -1
        self.explored_cells = set()
        self.goals_found = set()
        self.teleport_locations = {}
    
    def update(self, percepts, msg):
        """
        Update called each turn to process percepts, communicate, and determine movement.
        """
        self.turn += 1
        current_cell = percepts['X'][0]
        self.explored_cells.add(current_cell)

        # Parse received message for data from Agent B
        if msg:
            data = msg.get("goals", [])
            for goal in data:
                self.goals_found.add(goal)
            self.teleport_locations.update(msg.get("teleports", {}))

        # Check if on a goal or teleport cell and use it
        if current_cell in "0123456789rboyp":
            return 'U', {"goals": list(self.goals_found), "teleports": self.teleport_locations}

        # Choose next movement direction to avoid explored cells and prioritize new areas
        options = ["N", "E", "S", "W"]
        move = random.choice(options)

        return move, {"goals": list(self.goals_found), "teleports": self.teleport_locations}
