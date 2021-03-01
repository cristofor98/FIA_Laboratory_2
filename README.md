# Flocking behaviour
> This is a library for game that implements flocking behaviour

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to run](#setup)
* [Code Examples](#features)
* [Contact](#contact)

## General info
This is a library that implements 3 different behaviours. First is flocking behaviour, the secomnd is attack mode this is mode when rocks attack player and other mode is defence mode when rocks avoid player attack so in this way they save

## Technologies
* Python 3.8.2

## How to run
apply function update_rock_behaviour in update sprite

## Code Examples
function update_rock_behaviour

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




## Contact
Created by @cristofor98

