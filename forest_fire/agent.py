import mesa
import random 

class TreeCell(mesa.Agent):
    """
    A tree cell.

    Attributes:
        x, y: Grid coordinates
        condition: Can be "Fine", "On Fire", or "Burned Out"
        unique_id: (x,y) tuple.

    unique_id isn't strictly necessary here, but it's good
    practice to give one to each agent anyway.
    """

    def __init__(self, pos, model,combustibility):
        """
        Create a new tree.
        Args:
            pos: The tree's coordinates on the grid.
            model: standard model reference for agent.
        """
        super().__init__(pos, model)
        self.pos = pos
        self.condition = "Fine"
        self.combustibility = combustibility  # New attribute for combustibility

    def step(self):
        """
        If the tree is on fire, spread it to fine trees nearby.
        """
        if self.condition == "On Fire":
            for neighbor in self.model.grid.iter_neighbors(self.pos, True):
                # Introduce combustibility-based fire spread
                if neighbor.condition == "Fine":
                    if self.combustibility == "Flammable" or random.random() < 0.8:  # Assuming Flammable Wood burns and spreads easier
                        neighbor.condition = "On Fire"
                    elif self.combustibility == "Resistant" and random.random() < 0.5:  # Resistant Wood is less likely to catch fire
                        neighbor.condition = "On Fire"
            self.condition = "Burned Out"
