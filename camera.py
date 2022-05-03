# Followed Tutorial https://www.youtube.com/watch?v=qd6muA2Z0T8

from pyrr import Vector3, vector, vector3, matrix44
from math import sin, cos, radians

class Camera:
    def __init__(self):
        self.camera_pos = Vector3([0, 4, 3])
        self.camera_front = Vector3([0, 0, -1])
        self.camera_up = Vector3([0, 1, 0])
        self.camera_right = Vector3([1, 0, 0])
        self.mouse_sensitivity = 0.25
        self.yaw = -90
        self.pitch = 0

def get_view_matrix(self):
    return matrix44.create_look_at(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)

def process_mouse_movement(self, x_offset, y_offset, constraint_pitch=True):
    x_offset *= self.mouse_sensitivity
    y_offset *= self.mouse_sensitivity

    self.yaw += x_offset
    self.pitch += y_offset

    if constraint_pitch:
        if self.pitch > 45:
            self.pitch = 45
        if self.pitch < -45:
            self.pitch = -45
    
    self.update_camera_vectors()

def update_camera_vectors(self):
    front = Vector3([0, 0, 0])
    front.x = cos(radians(self.yaw)) * cos(radians(self.pitch))
    front.y = sin(radians(self.pitch))
    front.z = sin(radians(self.yaw)) * cos(radians(self.pitch))

    self.camera_front = vector.normalise(front)
    self.camer_right = vector.normalise(vector3.cross(self.camera_front, Vector3([0, 1, 0])))
    self.camera_up = vector.normalise(vector3.cross(self.camera_right, self.camera_front))
