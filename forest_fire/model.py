import mesa

from .agent import TreeCell


class ForestFire(mesa.Model):
    """
    Simple Forest Fire model.
    """

    def __init__(self, width=100, height=100, density=0.65,Flammable_ratio=50):
        """
        Create a new forest fire model.

        Args:
            width, height: The size of the grid to model
            density: What fraction of grid cells have a tree in them.
        """
        super().__init__()
        # Set up model objects
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, torus=False)

        self.datacollector = mesa.DataCollector(
            {
                "On Fire": lambda m: self.count_type(m, "On Fire"),
                "Burned Out": lambda m: self.count_type(m, "Burned Out"),
                "Fine Flammable": self.count_fine_Flammable,  # Counting fine Flammable trees
                "Fine Resistant": self.count_fine_Resistant,  # Counting fine Resistant trees
            }
        )

        # Place a tree in each cell with Prob = density
        for contents, (x, y) in self.grid.coord_iter():
            if self.random.random() < density:
                # Determine combustibility based on Flammable_ratio
                combustibility = "Flammable" if self.random.random() < (Flammable_ratio / 100.0) else "Resistant"
                new_tree = TreeCell((x, y), self, combustibility)
                if x == 0:   # Set the condition of all trees in the first column to "On Fire"
                    new_tree.condition = "On Fire"
                self.grid.place_agent(new_tree, (x, y))
                self.schedule.add(new_tree)


        self.running = True
        self.datacollector.collect(self)

    def step(self):
        """
        Advance the model by one step.
        """
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

        # Halt if no more fire
        if self.count_type(self, "On Fire") == 0:
            self.running = False

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
