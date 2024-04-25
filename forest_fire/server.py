import mesa

from .model import ForestFire
from .agent import WindPackage

COLORS = {
    "On Fire": "#EB5406",  # Bright red for burning trees
    "Burned Out": "#EEEEEE",  # Dark gray for burned-out trees
}

combustibility_COLORS = {
    "Flammable": "#90EE90",  # Green for Flammable
    "Resistant": "#4CC552",  # Brown for Resistant
}

def forest_fire_portrayal(tree):
    if tree is None:
        return
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
    (x, y) = tree.pos
    portrayal["x"] = x
    portrayal["y"] = y
    
    # Check if the agent is a WindPackage
    if isinstance(tree, WindPackage):
        if tree.active:
            portrayal["Color"] = "#93FFE8" if tree.visual_state_changed else "#93FFE8" # Blue for active wind packages
            portrayal["Shape"] = "circle"  # Circular shape to denote the wind's area of effect
            portrayal["Layer"] = 2  # Ensure wind is on top
            print(f"Drawing active wind package at ({x}, {y}) with color {portrayal['Color']}")
        else:
            portrayal["Color"] = "#93FFE8" if tree.visual_state_changed else "#3B2F2F" # Light blue for inactive wind packages
            portrayal["Layer"] = 2  # Ensure wind is on top
            print(f"Drawing inactive wind package at ({x}, {y}) with color {portrayal['Color']}")
        # Reset visual change flag
        tree.visual_state_changed = False 
    else:  
        # Use existing color coding for trees
        if tree.condition == "On Fire":
            portrayal["Color"] = COLORS["On Fire"]
        elif tree.condition == "Burned Out":
            portrayal["Color"] = COLORS["Burned Out"]
        else:  # If the tree is fine, use combustibility color
            portrayal["Color"] = combustibility_COLORS[tree.combustibility]
            # print(f"Drawing fine tree at ({x}, {y}) with color {portrayal['Color']}")
        portrayal["Layer"] = 1  
        

    return portrayal

    

canvas_element = mesa.visualization.CanvasGrid(
    forest_fire_portrayal, 100, 100, 500, 500
)
tree_chart = mesa.visualization.ChartModule(
    [
        {"Label": "On Fire", "Color": "red"},
        {"Label": "Burned Out", "Color": COLORS["Burned Out"]},
        {"Label": "Fine Flammable", "Color": combustibility_COLORS["Flammable"]},  
        {"Label": "Fine Resistant", "Color": combustibility_COLORS["Resistant"]},  
    ],
    data_collector_name='datacollector'
)
pie_chart = mesa.visualization.PieChartModule(
    [
        {"Label": "On Fire", "Color": "red"},
        {"Label": "Burned Out", "Color": COLORS["Burned Out"]},
        {"Label": "Fine Flammable", "Color": combustibility_COLORS["Flammable"]},
        {"Label": "Fine Resistant", "Color": combustibility_COLORS["Resistant"]},
    ],
    data_collector_name='datacollector'
)

model_params = {
    "height": 100,
    "width": 100,
    "density": mesa.visualization.Slider("Tree density", 0.65, 0.01, 1.0, 0.01),
    "Flammable_ratio": mesa.visualization.Slider("Flammable Tree Ratio", 50, 0, 100, 1),  #new slider of combustibility added
    "wind_chance": mesa.visualization.Slider("Wind Chance", 10, 0, 100, 1),  # Probability in %
    "wind_radius": mesa.visualization.Slider("Wind Radius", 15, 1, 30, 1)  # Radius in grid cells
}
server = mesa.visualization.ModularServer(
    ForestFire, [canvas_element, tree_chart, pie_chart], "Forest Fire", model_params
)
