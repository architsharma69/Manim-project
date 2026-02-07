from manim import *
from intro import IntroductionScene

class MainScene(Scene):
    def construct(self):
        intro = IntroductionScene(self.play, self.add, self.wait)

        anim1 = intro.get_animation()
        self.wait(2)
