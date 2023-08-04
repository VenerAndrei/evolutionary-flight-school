from physics.Vector2D import Vector2D

class Object:
    def __init__(self,position: Vector2D = Vector2D(0,0), mass = 1):
        self.mass = mass
        self.position = position
        self.velocity = Vector2D(0,0)
        self.acceleration = Vector2D(0,0)
        self.appliedForces = []
        self.maxVelocity = 3;
    def applyForce(self, force: Vector2D):
        self.appliedForces.append(force)

    def getNetForce(self):
        # Calculate the net force
        netForce = Vector2D(0,0)
        for force in self.appliedForces:
            netForce = netForce + force;
        return netForce
    
    def updatePhysics(self):
        netForce = self.getNetForce()
        # Get the net acceleration: F = m*a
        netAcceleration = (netForce * (1/self.mass))

        # Update the velocity 
        self.velocity = self.velocity + netAcceleration
        if self.velocity.x > self.maxVelocity:
            self.velocity.x = self.maxVelocity
        if self.velocity.x < -self.maxVelocity:
            self.velocity.x = -self.maxVelocity

        if self.velocity.y > self.maxVelocity:
            self.velocity.y = self.maxVelocity
        if self.velocity.y < -self.maxVelocity:
            self.velocity.y = -self.maxVelocity
        # Update the position
        self.position = self.position + self.velocity

        # Reset applied forces
        self.appliedForces = []

    
