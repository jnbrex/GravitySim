from body import Body
import math

class GravitySim:
    max_combination_distance = 0.5

    def __init__(self, step_size: float, bodies: set[Body]):
        self.step_size = step_size
        self.bodies = bodies
    
    def simulate_step(self) -> list[list[float]]:
        self.reset_force_and_acceleration()
        self.calculate_force_vectors()
        self.calculate_acceleration_vectors()
        self.update_velocities()
        self.combine_bodies()
        self.update_coordinates()
        
        positions = []
        masses = []
        for body in self.bodies:
            positions.append([body.x, body.y])
            masses.append(body.mass)

        return positions, masses

    def reset_force_and_acceleration(self) -> None:
        for body in self.bodies:
            body.x_force = 0
            body.y_force = 0
            body.x_acceleration = 0
            body.y_acceleration = 0

    def calculate_force_vectors(self) -> None:
        for i, body in enumerate(self.bodies):
            for j, other in enumerate(self.bodies):
                if i == j:
                    continue
                
                x_force, y_force = body.calculate_force_vector(
                    other, self.max_combination_distance)
                body.x_force += x_force
                body.y_force += y_force
    
    def calculate_acceleration_vectors(self) -> None:
        for body in self.bodies:
            body.x_acceleration = body.x_force / body.mass
            body.y_acceleration = body.y_force / body.mass

    def update_velocities(self) -> None:
        for body in self.bodies:
            body.x_velocity += body.x_acceleration * self.step_size
            body.y_velocity += body.y_acceleration * self.step_size

    def update_coordinates(self) -> None:
        for body in self.bodies:
            body.x += body.x_velocity * self.step_size
            body.y += body.y_velocity * self.step_size

    def combine_bodies(self) -> None:
        bodies = set()
        removed_bodies_indices = set()
        for i, body in enumerate(self.bodies):
            if i in removed_bodies_indices:
                continue

            for j, other in enumerate(self.bodies):
                if i == j or j in removed_bodies_indices:
                    continue
                
                distance = math.sqrt(
                    (other.x - body.x)**2 + (other.y - body.y)**2)
                
                if distance < self.max_combination_distance:
                    removed_bodies_indices.add(j)
                    body.x_velocity = (
                        (body.x_velocity * body.mass +
                        other.x_velocity * other.mass) /
                        (body.mass + other.mass))
                    body.y_velocity = (
                        (body.y_velocity * body.mass +
                        other.y_velocity * other.mass) /
                        (body.mass + other.mass))
                    body.mass += other.mass
                
            bodies.add(body)
        self.bodies = bodies
