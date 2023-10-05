from animation import Animation
from body import Body
from gravity_sim import GravitySim
import random

def generate_bodies(
        num_bodies: int = 200,
        min_mass: float = 5,
        max_mass: float = 10,
        min_x: float = -30,
        max_x: float = 30,
        min_y: float = -30,
        max_y: float = 30,
        min_x_velocity: float = -12,
        max_x_velocity: float = 10,
        min_y_velocity: float = -10,
        max_y_velocity: float = 12):
    bodies = set()
    for _ in range(num_bodies):
        bodies.add(Body(
            random.uniform(min_mass, max_mass),
            random.uniform(min_x, max_x),
            random.uniform(min_y, max_y),
            random.uniform(min_x_velocity, max_x_velocity),
            random.uniform(min_y_velocity, max_y_velocity)))
    return bodies

bodies = set()
bodies = bodies.union(generate_bodies(50, 2, 15, 0, 100, 0, 100, 0, 5, -5, 0))
bodies = bodies.union(generate_bodies(50, 2, 15, 0, 100, -100, 0, -5, 0, -5, 0))
bodies = bodies.union(generate_bodies(50, 2, 15, -100, 0, -100, 0, -5, 0, 0, 5))
bodies = bodies.union(generate_bodies(50, 2, 15, -100, 0, 0, 100, 0, 5, 0, 5))
bodies.add(Body(250, 0, 0))

step_size = 0.005
max_combination_distance = 0.5
num_steps = 10000

sim = GravitySim(bodies, step_size, max_combination_distance)

positions_sequence = []
masses_sequence = []
positions_string_sequence = []

for i in range(num_steps):
    positions, masses = sim.simulate_step()
    positions_sequence.append(positions)
    masses_sequence.append(masses)
    if i % (num_steps / 100) == 0:
        print(f"Simulation {i / num_steps * 100}% complete.")

animation = Animation(positions_sequence, masses_sequence)

animation.animate_simulation()
