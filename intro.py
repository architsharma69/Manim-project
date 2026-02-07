from manim import *

class IntroductionScene:
    def __init__(self, play, add, wait):
        self.play = play
        self.add = add
        self.wait = wait

    def get_animation(self):
        title = MarkupText('<gradient from="RED" to="YELLOW">Hello, World!</gradient>', font_size=100).to_edge(UP)
        self.play(Write(title, run_time=5))