import mesa
from mesa.space import MultiGrid

from .agent import TreeCell
from .agent import WindPackage
from random import randint


class ForestFire(mesa.Model):
    """
    Simple Forest Fire model.
    """

    def __init__(self, width=100, height=100, density=0.65,Flammable_ratio=50, wind_chance=100):
        """
        Create a new forest fire model.

        Args:
            width, height: The size of the grid to model
            density: What fraction of grid cells have a tree in them.
        """
        super().__init__()
        # Set up model objects
        super().__init__()
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = MultiGrid(width, height, torus=False)  # Using MultiGrid instead of SingleGrid
        self.wind_chance = wind_chance  # Probability of wind package activation per step

        self.datacollector = mesa.DataCollector(
            {
                "On Fire": lambda m: self.count_type(m, "On Fire"),
                "Burned Out": lambda m: self.count_type(m, "Burned Out"),
                "Fine Flammable": self.count_fine_Flammable,  # Counting fine Flammable trees
                "Fine Resistant": self.count_fine_Resistant,  # Counting fine Resistant trees
            }
        )

        for contents, (x, y) in self.grid.coord_iter():
            # Check for tree placement with density probability
            if randint(0, 100) < density * 100:
                # Determine combustibility based on Flammable_ratio
                combustibility = "Flammable" if randint(0, 100) < Flammable_ratio else "Resistant"
                new_tree = TreeCell((x, y), self, combustibility)
                if x == 0:  # Set the condition of all trees in the first column to "On Fire"
                    new_tree.condition = "On Fire"
                self.grid.place_agent(new_tree, (x, y))
                self.schedule.add(new_tree)

                
        self.running = True
        self.datacollector.collect(self)


    def step(self):
        if randint(0, 100) < self.wind_chance:
            x, y = randint(0, self.grid.width - 1), randint(0, self.grid.height - 1)
            wind = WindPackage((x, y), self)
            self.grid.place_agent(wind, (x, y))

            # Check for nearby trees that are "On Fire" before activating
            nearby_trees_on_fire = any(tree.condition == "On Fire" for tree in self.grid.get_neighbors((x, y), moore=True, include_center=False, radius=wind.radius) if isinstance(tree, TreeCell))
            if nearby_trees_on_fire:
                wind.activate()
                print(f"Wind package activated at ({x}, {y}) due to nearby fire")
            else:
                self.grid.remove_agent(wind)
                print(f"Wind package placed at ({x}, {y}) but not activated")

        self.schedule.step()
        print('1')

        self.datacollector.collect(self)
        print('2')

        if self.count_type(self, "On Fire") == 0:
            self.running = False
        else:
            self.running = True
            print("still has tree on fire")


    # def step(self):
    #     """
    #     Advance the model by one step.
    #     """
    #     self.schedule.step()
    #     # collect data
    #     self.datacollector.collect(self)

    #     # Halt if no more fire
    #     if self.count_type(self, "On Fire") == 0:
    #         self.running = False

    @staticmethod
    def count_type(model, tree_condition):
        """
        Helper method to count trees in a given condition in a given model.
        """
        count = 0
        for tree in model.schedule.agents:
            if tree.condition == tree_condition:
                count += 1
        return count
    

    @staticmethod
    def count_fine_Flammable(model):
        """Count fine Flammable trees."""
        return sum(1 for tree in model.schedule.agents if tree.combustibility == "Flammable" and tree.condition == "Fine")

    @staticmethod
    def count_fine_Resistant(model):
        """Count fine Resistant trees."""
        return sum(1 for tree in model.schedule.agents if tree.combustibility == "Resistant" and tree.condition == "Fine")
    
