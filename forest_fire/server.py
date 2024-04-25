import mesa

from .model import ForestFire
from .agent import WindPackage

COLORS = {
    "On Fire": "#FF4500",  # Bright red for burning trees
    "Burned Out": "#808080",  # Dark gray for burned-out trees
}

combustibility_COLORS = {
    "Flammable": "#008000",  # Green for Flammable
    "Resistant": "#A52A2A",  # Brown for Resistant
}


# def forest_fire_portrayal(tree):
#     if tree is None:
#         return
#     portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
#     (x, y) = tree.pos
#     portrayal["x"] = x
#     portrayal["y"] = y
    
#     # Use combustibility colors for healthy trees, distinct colors for other states
#     if tree.condition == "On Fire":
#         portrayal["Color"] = COLORS["On Fire"]
#     elif tree.condition == "Burned Out":
#         portrayal["Color"] = COLORS["Burned Out"]
#     else:  # If the tree is fine, use combustibility color
#         portrayal["Color"] = combustibility_COLORS[tree.combustibility]

#     return portrayal
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
            portrayal["Color"] = "#0000FF"  # Blue for active wind packages
            portrayal["Shape"] = "circle"  # Circular shape to denote the wind's area of effect
        else:
            portrayal["Color"] = "#ADD8E6"  # Light blue for inactive wind packages
    else:
        # Use existing color coding for trees
        if tree.condition == "On Fire":
            portrayal["Color"] = COLORS["On Fire"]
        elif tree.condition == "Burned Out":
            portrayal["Color"] = COLORS["Burned Out"]
        else:  # If the tree is fine, use combustibility color
            portrayal["Color"] = combustibility_COLORS[tree.combustibility]

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
}
server = mesa.visualization.ModularServer(
    ForestFire, [canvas_element, tree_chart, pie_chart], "Forest Fire", model_params
)
