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
    for i in range(num_bodies):
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
# bodies.add(Body(50, 5, -5))
# bodies.add(Body(5, 5, 5))
# bodies.add(Body(5, -5, 0))
# bodies.add(Body(5, -1.5, -0.5))
# bodies.add(Body(5, 2, -4))
# bodies.add(Body(6, 6, -5))
# bodies.add(Body(12, -5, 7))
# bodies.add(Body(3, -7, 9))
# bodies.add(Body(7, 8.5, -0.9))
# bodies.add(Body(9, 20, 4))
# bodies.add(Body(8, -13, 5.9))
# bodies.add(Body(7, 14, 0.7))
# bodies.add(Body(5, -6.5, -3.5))

step_size = 0.005

sim = GravitySim(step_size, bodies)

positions_sequence = []
masses_sequence = []
positions_string_sequence = []

num_steps = 10000
for i in range(num_steps):
    positions, masses = sim.simulate_step()
    positions_sequence.append(positions)
    masses_sequence.append(masses)
    if i % (num_steps / 100) == 0:
        print(f"Simulation {i / num_steps * 100}% complete.")

animation = Animation(positions_sequence, masses_sequence)

animation.animate_simulation()
