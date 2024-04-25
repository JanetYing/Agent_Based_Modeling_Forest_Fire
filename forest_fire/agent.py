import mesa
import random 

class WindPackage(mesa.Agent):
    """
    A wind package that can influence fire spread.

    Attributes:
        pos: Grid coordinates
        radius: The effective radius of the wind
        active: Whether the wind package is currently active
        visual_state_changed: Flag to track when the visual representation needs updating
    """
    def __init__(self, pos, model, radius=15):
        super().__init__(pos, model)
        self.pos = pos
        self.radius = radius
        self.active = False  # Wind packages activate randomly
        self.need_visual_update = True
        self.visual_state_changed = True  # Initialize this attribute

    def activate(self):
        if not self.active:
            self.active = True
            self.need_visual_update = True
            self.visual_state_changed = True

    def deactivate(self):
        if self.active:
            self.active = False
            self.need_visual_update = True
            self.visual_state_changed = True

    def step(self):
        # Assuming some logic for auto-activation
        if not self.active:  
            self.activate()
        # Reset the visual state change flag after it's been used for visualization
        if self.visual_state_changed:
            self.visual_state_changed = False



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
            # Collect all active winds first to assess their combined effect.
            active_winds = [wind for wind in self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius=15)
                            if isinstance(wind, WindPackage) and wind.active]

            if active_winds:
                spread_radius = 15  # Increase spread radius due to wind

            # Apply fire spread logic
            for neighbor in self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius=spread_radius):
                if isinstance(neighbor, TreeCell) and neighbor.condition == "Fine":
                    fire_chance = 0.8 if neighbor.combustibility == "Flammable" else 0.5
                    if random.random() < fire_chance:
                        neighbor.condition = "On Fire"

            self.condition = "Burned Out"  # Tree burns out after spreading fire

            # Deactivate wind that were active this step
            for wind in active_winds:
                wind.deactivate()
                print(f"Wind package at {wind.pos} deactivated after influencing fire spread.")




