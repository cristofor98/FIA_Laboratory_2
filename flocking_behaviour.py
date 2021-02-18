import numpy as np
from p5 import Vector

WIDTH = 800
HEIGHT = 600

PERCEPTION = 100
MAX_SPEED = 2
MAX_FORCE = 0.2       
        
def edges(current):
    if current.position[0] > WIDTH:
        current.position[0] = 0
    elif current.position[0] < 0:
        current.position[0] = WIDTH

    if current.position[1] > HEIGHT:
        current.position[1] = 0
    elif current.position[1] < 0:
        current.position[1] = HEIGHT

def align(current, boids):
    steering = Vector(*np.zeros(2))
    total = 0
    avg_vec = Vector(*np.zeros(2))
    for boid in boids:
        if np.linalg.norm(Vector(*boid.position) - Vector(*current.position)) < PERCEPTION:
            avg_vec += Vector(*boid.velocity)
            total += 1
    if total > 0:
        avg_vec /= total
        avg_vec = Vector(*avg_vec)
        avg_vec = avg_vec / np.linalg.norm(avg_vec) * MAX_SPEED
        steering = avg_vec - Vector(*current.velocity)
    return steering

def cohesion(current, boids):
    steering = Vector(*np.zeros(2))
    total = 0
    center_of_mass = Vector(*np.zeros(2))
    for boid in boids:
        if np.linalg.norm(np.array(boid.position) - np.array(current.position)) < PERCEPTION:
            center_of_mass += Vector(*boid.position)
            total += 1
    if total > 0:
        center_of_mass /= total
        center_of_mass = Vector(*center_of_mass)
        vec_to_com = center_of_mass - Vector(*current.position)
        if np.linalg.norm(vec_to_com) > 0:
            vec_to_com = (vec_to_com / np.linalg.norm(vec_to_com)) * MAX_SPEED
        steering = vec_to_com - Vector(*current.vel)
        if np.linalg.norm(steering) > MAX_FORCE:
            steering = (steering / np.linalg.norm(steering)) * MAX_FORCE

    return steering

def separation(current, boids):
    steering = Vector(*np.zeros(2))
    total = 0
    avg_vector = Vector(*np.zeros(2))
    for boid in boids:
        distance = np.linalg.norm(np.array(boid.position) - np.array(current.position))
        if current.position != boid.position and distance < PERCEPTION:
            diff = Vector(*current.position) - Vector(*boid.position)
            diff /= distance
            avg_vector += diff
            total +=1
    if total > 0:
        avg_vector /= total
        avg_vector = Vector(*avg_vector)
        if np.linalg.norm(steering) > 0:
            avg_vector = (avg_vector / np.linalg.norm(steering)) * MAX_SPEED
        steering = avg_vector - Vector(*current.velocity)
        if np.linalg.norm(steering) > MAX_FORCE:
            steering = (steering / np.linalg.norm(steering)) * MAX_FORCE

    return steering

def apply_behaviour(current, boids):

    acceleration = [0, 0]
    alignment = align(current, boids)
    cohesionment = cohesion(current, boids)
    separationment = separation(current, boids)


    current.acceleration += alignment
    current.acceleration += cohesionment
    current.acceleration += separationment


def defence_mode(rock_position, rock_velocity, acceleration, current, missile, my_ship):
    missile_list = list(missile)
    distance_from_ship = Vector(*current.pos) - Vector(*my_ship.pos)

    if len(missile_list) > 0:
        diff = Vector(*current.pos) - Vector(*missile_list[0].pos)
    
    update_ahead = len(distance_from_ship) / MAX_SPEED
    future_position = Vector(*current.pos) + Vector(*current.vel) * update_ahead
    future_velocity = (Vector(*current.pos) - future_position) * MAX_SPEED

    velocity = future_velocity - Vector(*current.vel)
    
    rock_position += velocity
    rock_velocity += acceleration
    
    return rock_position,rock_velocity 

def attack_mode(rock_position, rock_velocity, acceleration, current, missile, my_ship):    
    missile_list = list(missile)
    attack_direction = Vector(*my_ship.pos) - Vector(*current.pos)
    if len(missile_list)  > 0:
        attack_direction = Vector(*my_ship[0].pos) - Vector(*current.pos)
    
    update_ahead = len(attack_direction) / MAX_SPEED
    future_position = Vector(*current.pos) + Vector(*current.vel) * update_ahead
    future_velocity = (Vector(*current.pos) - future_position) * MAX_SPEED
    
    velocity = future_velocity - Vector(*current.vel)
    
    rock_position += velocity
    rock_velocity += acceleration
    
    return rock_position,rock_velocity 

def update_rock_behaviour(current, boids, ship, missile):
    acceleration = [0, 0]
    position = Vector(*(current.pos))
    velocity = Vector(*(current.vel))
    acceleration = current.acceleration
      
    position += velocity
    velocity += acceleration

    if np.linalg.norm(velocity) > MAX_SPEED:
        velocity = velocity / np.linalg.norm(velocity) * MAX_SPEED

    if len(missile)>10
        position,velocity = attack_mode(position, velocity, acceleration, current, missiles, ship)
    elif len(missile)>2
        position,velocity = defence_mode(position, velocity, acceleration, current, missiles, ship)

    current.pos = [position.x.item(), position.y.item()]
    current.vel = [velocity.x.item(), velocity.y.item()]


   