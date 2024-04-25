MACS 40550 1 Agent-Based Modeling
Assignment 1: Parameters & Agents
Janet Cao
Git link: https://github.com/JanetYing/MACSS40550_Assignment1_Parameters-Agents.git

Background:
The forest fire model selected from the Mesa examples library serves to simulate the spread of fire across a forested grid, offering insights into the dynamics of fire behavior. The model's initial design aimed to visualize how fire spread through various densities of forested landscapes. My enhancement introduces a categorization of tree combustibility, differentiating trees as either "Highly Combustible" (Flammable) or "Less Combustible" (Resistant), adding a layer of complexity and realism to the simulation. This categorization is inspired by real-world attributes such as texture, moisture content, and the presence of volatile compounds, which influence a tree's likelihood to ignite and sustain combustion.

Design Concepts: 
In the enhanced model, tree agents possess a new attribute, “combustibility”, influencing their interaction with fire. This addition allows the simulation to more accurately portray forest fire dynamics, as different tree types react differently to fire. The model’s agent-based structure simulate each tree's firing behavior and state can influence and be influenced by its surroundings.

Details:
Key aspects like the grid-based environment, tree density control, discrete step simulation, and the core visualization approach remain unchanged, preserving the model's original framework while integrating new features.
Initialization: In the model, trees are initialized on a grid where the density parameter determines the overall tree population in the fixed size area. The Flammable_ratio then influences the proportion of these trees that are inherently more prone to burning. I set the condition of all trees in the first column to "On Fire" to initiate the simulation. This setup creates a diverse forest composition, integral to studying how varying propensities to burn affect fire spread.
Input Data: The model primarily relies on internal parameters (“density” and “Flammable_ratio”) to generate the simulation. 


Changes from the Original Model:
I introduced the “combustibility” parameter, allowing the model to differentiate between flammable and resistant trees. I've refined the logic of fire spread to account for this attribute: Flammable trees have a higher probability of catching and transmitting fire to their neighbors, reflecting a natural propensity to burn more easily. Conversely, Resistant trees are less likely to ignite, simulating a natural fire retardant characteristic. The fire spread logic was also updated to consider this attribute, making the spread of fire contingent not only on proximity but also on the inherent combustibility of each tree. 
To display these changes, I refined the model's visualization capabilities. Now, as shown in Fig 1, users can clearly see the interactions between individual trees and their neighbors, observing how fire spreads over time. The speed and extent of the spread are influenced by the density (which affects proximity) and the combustibility of the trees, providing an intuitive grasp of how different types of trees influence fire behavior. The visualization also offers numerical counts and percentages of the various types of trees in different states over time, as shown in Fig 2 and 3.

Conclusions:
The enhanced model provides a more detailed and dynamic simulation of forest fires, reflecting the variability found in natural forests. It allows users to explore how different compositions and density of tree combustibility affect fire spread, offering insights useful for forest management and fire prevention strategies. By maintaining the original model's core elements while integrating new features, the enhanced model serves as a tool for education, planning, and research in forest fire behavior and management.
