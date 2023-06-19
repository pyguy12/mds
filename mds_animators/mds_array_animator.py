from mds_animators.mds_animator import MDSAnimator
from manim import *


class MDSArrayAnimator(MDSAnimator):
    def __init__(self, scene):
        self.scene = scene
        self.array_objects = []  # Store the visuals for each value in the array

    def animate_init(self, values: list):
        for index, value in enumerate(values):
            # Create a visual representation of the value
            value_repr = self._create_value_representation(value)

            # Position it according to its index in the array
            value_repr.move_to(self._get_position_for_index(index))

            # Add it to the array_objects list
            self.array_objects.append(value_repr)

            # Add it to the scene with an animation
            self.scene.play(Write(value_repr))
    
    def _create_value_representation(self, value):
        # Create a text object for the value
        text = Text(str(value))

        # Create a box to surround the text
        box = SurroundingRectangle(text)

        # Group the text and the box together so they can be moved as one
        value_repr = VGroup(text, box)

        return value_repr

    def _get_position_for_index(self, index):
        # This method positions each value 2 units to the right of the previous one
        return index * RIGHT

    def animate_insertion(self, value, index=None):
        # Implement animation for insertion in an array
        pass

    def animate_deletion(self, index):
        # Implement animation for deletion from an array
        pass

    def animate_access(self, index):
        # Implement animation for accessing an element in an array
        pass

    def animate_reversal(self): 
        # Implement animation for reversing an array
        pass

    # ...other operations...
