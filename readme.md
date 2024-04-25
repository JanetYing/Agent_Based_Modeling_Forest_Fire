MACS 40550 1 Agent-Based Modeling
Assignment 2: Environment / Updating
Janet Cao
Word Counts: 842
Git link: https://github.com/JanetYing/Agent_Based_Modeling_Forest_Fire.git

Background:
The forest fire model is a grid-based simulation that illustrates how fires spread through a forest. Each grid cell can either be empty or contain a tree in one of three states: unburned, on fire, or burned out. Fire propagates from on-fire trees to adjacent unburned trees, which then transition to a burned state. The simulation persists until all fires are extinguished. Initially, the model was designed to explore fire dynamics across different forest densities.
In the first assignment, I enhanced the model by incorporating tree combustibility, categorizing trees as either "Highly Combustible" (Flammable) or "Less Combustible" (Resistant). This classification allows for varied fire spread behaviors based on tree properties. For this assignment, I have added further complexity and realism by introducing a new Wind class. This models how wind's various activation probability and influence radius impact fire spread dynamics.

Design Concepts:
In the updated model, wind serves as a dynamic external factor that significantly enhances fire spread among trees. Normally, an "on fire" tree affects only its immediate neighbors with a spread radius of one. However, with the introduction of the Wind class, this influence can extend up to a radius of 30, depending on the wind's generation and intensity(influence radius). The winds are generated randomly at the different location in each step, with its probability and radius of influence. Higher generation probabilities and larger radii increase the likelihood of wind activation, which interacting with on fire trees and spreading fire, and also, we are more likely to observe higher spreading speed and the irregular shape of fire spreading edge. This enhancement brings a new layer of realism to the simulation, demonstrating how natural elements like wind can alter the behavior of forest fires.

Details:
At the beginning of the simulation, the model populates a grid based on a specified density, randomly placing trees. Each tree receives a combustibility attribute—either "Flammable" or "Resistant"—based on the Flammable_ratio. This attribute dictates how susceptible a tree is to catching fire from neighboring burning trees.

Integration of Wind Dynamics:
To add depth to the simulation, I implemented a MultiGrid to accommodate both trees and wind agents in the same grid cells. The WindPackage class represents wind as a dynamic element affecting fire spread. Wind agents have the potential to be generated each model step, with their probability of generation controlled by the wind_chance parameter. When generated, a wind agent checks for any nearby "On Fire" trees within its radius to decide if it should activate. If activated, the wind extends the fire spread radius from the standard 1 to the larger wind_radius defined by the user, altering the usual fire spread patterns. Once a wind agent has influenced fire spread in a step, it is deactivated.

Visualization Enhancements:
Distinct colors differentiate between wind statuses and various tree states to enhance visibility. To maintain visual consistency and track wind influence accurately, wind agents feature a “visual_state_changed” attribute. This ensures that any wind activation is visually represented, preventing its color been overrided in subsequent simulation steps.

Interactive Controls:
I added sliders allow users to modify the probability of wind generation (wind_chance) and the influence radius of active winds (wind_radius). These tools enable users to explore how varying wind conditions impact fire spread dynamics, providing a hands-on approach to understanding forest fire behavior.

Data Collection:
The model collects data on the count of trees in each state ("On Fire", "Burned Out", "Fine Flammable", and "Fine Resistant") throughout the simulation. This data is vital for assessing the impact of parameters such as tree density, combustibility, and wind effects on the progression and management of forest fires.

Conclusions:
Enhancements and Capabilities:
My enhanced version of the forest fire model introduces the WindPackage class, which adds a significant layer of complexity and realism to the simulation. By incorporating wind as a dynamic element, the model not only reflects more realistic fire behavior but also offers a platform to explore the interactions within environmental factors(wind generation and intensity, tree density), tree agent innate characteristic (combustibility), and fire spreading pattern. The ability to adjust wind generation probability and influence radius through interactive sliders allows users to experiment with various scenarios and observe how changes in wind dynamics affect fire propagation.


Learning Outcomes:
Through this model, I gained insights into the significant role wind plays in influencing the spread of forest fires. The simulation reveals how wind can cause fires to spreading across unburned areas, resulting in irregular burn patterns that would be difficult to foresee without incorporating dynamic environmental factors. Additionally, allowing wind agents to coexist with trees on the same grid cells emphasizes the need to account for multiple environmental elements simultaneously when analyzing ecological events. 
