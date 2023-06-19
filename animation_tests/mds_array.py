from mds_animators.mds_array_animator import MDSArrayAnimator
from mds_data_structures.mds_array import MDSArray
from manim import Scene

class ArrayScene(Scene):
    def construct(self):
        # create animator with the current scene
        animator = MDSArrayAnimator(self)
        
        # create array with initial values and animator
        arr = MDSArray([1, 2, 3, 4], animator)
