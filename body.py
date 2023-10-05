import math

class Body:
    gravitational_constant = 1

    def __init__(self,
                 mass: float,
                 x: float,
                 y: float,
                 x_velocity: float = 0,
                 y_velocity: float = 0) -> None:
        self.mass = mass
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.x_acceleration = 0
        self.y_acceleration = 0
        self.x_force = 0
        self.y_force = 0

    def calculate_force_vector(
            self, other, max_combination_distance: float) -> tuple[float]:
        d = max(max_combination_distance,
                math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2))
        force = ((self.gravitational_constant * self.mass * other.mass)
                /
                (d**2))
        angle = math.atan2(other.y - self.y, other.x - self.x)
        x_force = math.cos(angle) * force
        y_force = math.sin(angle) * force
        return (x_force, y_force)
