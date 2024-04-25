import mesa
import random 

# define a new class wind packege to introduce wind
class WindPackage(mesa.Agent):
    """
    A wind package that can influence fire spread.

    Attributes:
        pos: Grid coordinates
        radius: The effective radius of the wind
        active: Whether the wind package is currently active
    """
    def __init__(self, pos, model, radius=3):
        super().__init__(pos, model)
        self.pos = pos
        self.radius = radius
        self.active = False  # Wind packages activate randomly

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def step(self):
        if not self.active:  
            self.activate()


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

    # def step(self):
    #     """
    #     If the tree is on fire, spread it to fine trees nearby.
    #     """
    #     if self.condition == "On Fire":
    #         for neighbor in self.model.grid.iter_neighbors(self.pos, True):
    #             # Introduce combustibility-based fire spread
    #             if neighbor.condition == "Fine":
    #                 if self.combustibility == "Flammable" or random.random() < 0.8:  # Assuming Flammable Wood burns and spreads easier
    #                     neighbor.condition = "On Fire"
    #                 elif self.combustibility == "Resistant" and random.random() < 0.5:  # Resistant Wood is less likely to catch fire
    #                     neighbor.condition = "On Fire"
    #         self.condition = "Burned Out"

    def step(self):
        if self.condition == "On Fire":
            spread_radius = 1  # Default spread radius without wind
            for wind in self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius=9):
                if isinstance(wind, WindPackage) and wind.active:
                    spread_radius = 9  # Increase the spread radius due to active wind
                    break

            for neighbor in self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius=spread_radius):
                if isinstance(neighbor, TreeCell) and neighbor.condition == "Fine":
                    if self.combustibility == "Flammable" and random.random() < 0.8:
                        neighbor.condition = "On Fire"
                    elif self.combustibility == "Resistant" and random.random() < 0.5:
                        neighbor.condition = "On Fire"
            self.condition = "Burned Out"






