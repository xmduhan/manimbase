from manim import *

class DistributiveLaw(Scene):
    def construct(self):
        title = Text('Distributive Law', font_size=48)
        title.to_edge(UP)
        self.play(Write(title))

        equation = MathTex('a(b+c)', '=', 'ab', '+', 'ac', font_size=48)
        equation.next_to(title, DOWN, buff=0.5)
        equation[0].set_color(YELLOW)
        equation[2].set_color(BLUE)
        equation[4].set_color(GREEN)
        self.play(Write(equation))
        self.wait(0.5)

        a = 2.0
        b = 2.5
        c = 1.5
        scale = 1.0

        rect_ab = Rectangle(width=b*scale, height=a*scale, color=BLUE, fill_opacity=0.4)
        rect_ac = Rectangle(width=c*scale, height=a*scale, color=GREEN, fill_opacity=0.4)
        rect_bc = VGroup(rect_ab, rect_ac).arrange(RIGHT, buff=0, aligned_edge=DOWN)
        rect_bc.move_to(ORIGIN).shift(DOWN*0.5)

        label_a = MathTex('a').next_to(rect_bc, LEFT, buff=0.2)
        label_b = MathTex('b').next_to(rect_ab, UP, buff=0.1)
        label_c = MathTex('c').next_to(rect_ac, UP, buff=0.1)
        label_ab = MathTex('ab').move_to(rect_ab.get_center())
        label_ac = MathTex('ac').move_to(rect_ac.get_center())
        label_bc = MathTex('b+c').next_to(rect_bc, DOWN, buff=0.2)

        self.play(Create(rect_ab), Create(rect_ac))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.play(Write(label_ab), Write(label_ac))
        self.play(Write(label_bc))
        self.wait(0.5)

        total = MathTex('a(b+c)', '=', 'ab', '+', 'ac', font_size=40)
        total.next_to(rect_bc, DOWN, buff=1.0)
        total[0].set_color(YELLOW)
        total[2].set_color(BLUE)
        total[4].set_color(GREEN)
        self.play(TransformFromCopy(equation, total))
        self.play(Indicate(rect_ab, color=BLUE), Indicate(rect_ac, color=GREEN))
        self.wait(2)
