DDoS Attack Simulation using NS2
This repository contains a script to simulate a Distributed Denial-of-Service (DDoS) attack using the NS2 (Network Simulator 2) simulator. NS2 is a popular simulation tool for networking research, which provides substantial support for simulation of TCP, routing, and multicast protocols over wired and wireless networks.

Prerequisites
Before running the simulation, ensure that you have the following installed:

NS2 (Network Simulator 2)
NAM (Network Animator) for visualizing the network
Explanation
Simulator Setup: The script initializes the NS2 simulator and sets up the NAM trace file.
Node Creation: Nodes are created for the victim, routers, and attackers.
Link Creation: Duplex links are established between the nodes with specified bandwidth and delay.
Traffic Setup: UDP agents and CBR (Constant Bit Rate) traffic are configured to simulate the attack from the attackers to the victim.
Simulation Execution: The simulation is set to run for 10 seconds, after which it calls the finish procedure to stop the simulation and open the NAM visualizer.
