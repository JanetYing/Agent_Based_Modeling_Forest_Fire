import mesa

from .model import ForestFire

COLORS = {
    "Fine": "#00AA00",  # Green for fine trees
    "On Fire": "#FF4500",  # Bright red for burning trees
    "Burned Out": "#696969",  # Dark gray for burned-out trees
}

TEXTURE_COLORS = {
    "softwood": "#008000",  # Green for softwood
    "hardwood": "#A52A2A",  # Brown for hardwood
}


def forest_fire_portrayal(tree):
    if tree is None:
        return
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
    (x, y) = tree.pos
    portrayal["x"] = x
    portrayal["y"] = y
    
    # Use texture colors for healthy trees, distinct colors for other states
    if tree.condition == "On Fire":
        portrayal["Color"] = COLORS["On Fire"]
    elif tree.condition == "Burned Out":
        portrayal["Color"] = COLORS["Burned Out"]
    else:  # If the tree is fine, use texture color
        portrayal["Color"] = TEXTURE_COLORS[tree.texture]

    return portrayal
    

canvas_element = mesa.visualization.CanvasGrid(
    forest_fire_portrayal, 100, 100, 500, 500
)
tree_chart = mesa.visualization.ChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)
pie_chart = mesa.visualization.PieChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)

model_params = {
    "height": 100,
    "width": 100,
    "density": mesa.visualization.Slider("Tree density", 0.65, 0.01, 1.0, 0.01),
    "softwood_ratio": mesa.visualization.Slider("Softwood Ratio", 50, 0, 100, 1),  #new slider of texture added
}
server = mesa.visualization.ModularServer(
    ForestFire, [canvas_element, tree_chart, pie_chart], "Forest Fire", model_params
)
