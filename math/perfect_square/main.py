from manim import *
import numpy as np

FONT = 'Noto Sans CJK SC'

class PerfectSquareFormula(Scene):
    def construct(self):
        self.show_sum_square()
        self.show_difference_square()

    def show_sum_square(self):
        title = Text('完全平方和公式：面积拼图', font_size=42, font=FONT)
        title.to_edge(UP)
        self.play(Write(title), run_time=1.2)

        formula = MathTex('(a+b)^2', '=', 'a^2', '+', '2ab', '+', 'b^2', font_size=40)
        formula.next_to(title, DOWN, buff=0.25)
        formula[0].set_color(YELLOW)
        formula[2].set_color(YELLOW)
        formula[4].set_color(BLUE)
        formula[6].set_color(RED)
        self.play(Write(formula), run_time=1.0)
        self.wait(0.4)

        a = 2.6
        b = 1.4
        s = a + b
        origin = np.array([-5.1, -1.8, 0])

        outer = Square(side_length=s, color=WHITE, stroke_width=3)
        outer.move_to(origin + np.array([s / 2, s / 2, 0]))

        rect_a2 = Rectangle(width=a, height=a, color=YELLOW, fill_opacity=0.45, stroke_width=2)
        rect_a2.move_to(origin + np.array([a / 2, a / 2, 0]))
        rect_ab1 = Rectangle(width=b, height=a, color=BLUE, fill_opacity=0.45, stroke_width=2)
        rect_ab1.move_to(origin + np.array([a + b / 2, a / 2, 0]))
        rect_ab2 = Rectangle(width=a, height=b, color=GREEN, fill_opacity=0.45, stroke_width=2)
        rect_ab2.move_to(origin + np.array([a / 2, a + b / 2, 0]))
        rect_b2 = Rectangle(width=b, height=b, color=RED, fill_opacity=0.6, stroke_width=2)
        rect_b2.move_to(origin + np.array([a + b / 2, a + b / 2, 0]))

        self.play(Create(outer), run_time=1.0)

        label_a_bottom = MathTex('a', font_size=34, color=YELLOW)
        label_a_bottom.move_to(origin + np.array([a / 2, -0.28, 0]))
        label_b_bottom = MathTex('b', font_size=34, color=BLUE)
        label_b_bottom.move_to(origin + np.array([a + b / 2, -0.28, 0]))
        label_a_left = MathTex('a', font_size=34, color=YELLOW)
        label_a_left.move_to(origin + np.array([-0.28, a / 2, 0]))
        label_b_left = MathTex('b', font_size=34, color=BLUE)
        label_b_left.move_to(origin + np.array([-0.28, a + b / 2, 0]))
        self.play(Write(label_a_bottom), Write(label_b_bottom), Write(label_a_left), Write(label_b_left), run_time=1.2)
        self.wait(0.3)

        label_a2 = MathTex('a^2', font_size=36).move_to(rect_a2.get_center())
        label_ab1 = MathTex('ab', font_size=34).move_to(rect_ab1.get_center())
        label_ab2 = MathTex('ab', font_size=34).move_to(rect_ab2.get_center())
        label_b2 = MathTex('b^2', font_size=36).move_to(rect_b2.get_center())

        self.play(FadeIn(rect_a2), run_time=0.5)
        self.play(Write(label_a2), run_time=0.6)
        self.play(FadeIn(rect_ab1), run_time=0.5)
        self.play(Write(label_ab1), run_time=0.6)
        self.play(FadeIn(rect_ab2), run_time=0.5)
        self.play(Write(label_ab2), run_time=0.6)
        self.play(FadeIn(rect_b2), run_time=0.5)
        self.play(Write(label_b2), run_time=0.6)
        self.wait(0.8)

        eq1 = MathTex('(a+b)^2', '=', 'a^2', '+', 'ab', '+', 'ab', '+', 'b^2', font_size=34)
        eq1.move_to(np.array([2.6, 1.0, 0]))
        eq1[0].set_color(YELLOW)
        eq1[2].set_color(YELLOW)
        eq1[4].set_color(BLUE)
        eq1[6].set_color(GREEN)
        eq1[8].set_color(RED)

        eq2 = MathTex('=', 'a^2', '+', '2ab', '+', 'b^2', font_size=38)
        eq2.next_to(eq1, DOWN, buff=0.3, aligned_edge=LEFT)
        eq2[1].set_color(YELLOW)
        eq2[3].set_color(BLUE)
        eq2[5].set_color(RED)

        note = Text('四个面积块拼成大正方形', font_size=26, font=FONT)
        note.next_to(eq2, DOWN, buff=0.5)

        self.play(Write(eq1), run_time=1.0)
        self.play(Write(eq2), run_time=1.0)
        self.play(Write(note), run_time=0.8)
        self.wait(2.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)

    def show_difference_square(self):
        title = Text('完全平方差公式：面积割补', font_size=42, font=FONT)
        title.to_edge(UP)
        self.play(Write(title), run_time=1.2)

        formula = MathTex('(a-b)^2', '=', 'a^2', '-', '2ab', '+', 'b^2', font_size=40)
        formula.next_to(title, DOWN, buff=0.25)
        formula[0].set_color(YELLOW)
        formula[2].set_color(YELLOW)
        formula[4].set_color(BLUE)
        formula[6].set_color(RED)
        self.play(Write(formula), run_time=1.0)
        self.wait(0.4)

        a = 4.0
        b = 1.4
        origin = np.array([-5.0, -1.8, 0])

        big_square = Square(side_length=a, color=WHITE, fill_opacity=0.1, stroke_width=3)
        big_square.move_to(origin + np.array([a / 2, a / 2, 0]))

        label_a_bottom = MathTex('a', font_size=34, color=YELLOW)
        label_a_bottom.move_to(origin + np.array([a / 2, -0.28, 0]))
        label_a_left = MathTex('a', font_size=34, color=YELLOW)
        label_a_left.move_to(origin + np.array([-0.28, a / 2, 0]))
        label_b_bottom = MathTex('b', font_size=34, color=RED)
        label_b_bottom.move_to(origin + np.array([a - b / 2, -0.28, 0]))
        label_b_left = MathTex('b', font_size=34, color=RED)
        label_b_left.move_to(origin + np.array([-0.28, a - b / 2, 0]))

        self.play(
            Create(big_square),
            Write(label_a_bottom),
            Write(label_a_left),
            Write(label_b_bottom),
            Write(label_b_left),
            run_time=1.2
        )
        self.wait(0.4)

        right_strip = Rectangle(width=b, height=a, color=BLUE, fill_opacity=0.55, stroke_width=2)
        right_strip.move_to(origin + np.array([a - b / 2, a / 2, 0]))
        label_ab_right = MathTex('ab', font_size=34).move_to(right_strip.get_center())

        self.play(FadeIn(right_strip), Write(label_ab_right), run_time=1.0)
        self.wait(0.4)

        top_strip = Rectangle(width=a, height=b, color=GREEN, fill_opacity=0.35, stroke_width=2)
        top_strip.move_to(origin + np.array([a / 2, a - b / 2, 0]))
        label_ab_top = MathTex('ab', font_size=34).move_to(origin + np.array([(a - b) / 2, a - b / 2, 0]))

        overlap = Rectangle(width=b, height=b, color=RED, fill_opacity=0.75, stroke_width=2)
        overlap.move_to(origin + np.array([a - b / 2, a - b / 2, 0]))
        label_b2 = MathTex('b^2', font_size=32).move_to(overlap.get_center())

        self.play(FadeIn(top_strip), Write(label_ab_top), run_time=1.0)
        self.play(FadeIn(overlap), Write(label_b2), run_time=0.8)
        self.wait(0.8)

        eq1 = MathTex('a^2', '-', 'ab', '-', 'ab', '+', 'b^2', font_size=36)
        eq1.move_to(np.array([2.8, 1.2, 0]))
        eq1[0].set_color(YELLOW)
        eq1[2].set_color(BLUE)
        eq1[4].set_color(GREEN)
        eq1[6].set_color(RED)

        eq2 = MathTex('=', 'a^2', '-', '2ab', '+', 'b^2', font_size=38)
        eq2.next_to(eq1, DOWN, buff=0.3, aligned_edge=LEFT)
        eq2[1].set_color(YELLOW)
        eq2[3].set_color(BLUE)
        eq2[5].set_color(RED)

        eq3 = MathTex('=', '(a-b)^2', font_size=40)
        eq3.next_to(eq2, DOWN, buff=0.3, aligned_edge=LEFT)
        eq3[1].set_color(YELLOW)

        note = Text('减去两块 ab，补回重叠的 b^2', font_size=26, font=FONT)
        note.next_to(eq3, DOWN, buff=0.5)

        self.play(Write(eq1), run_time=1.0)
        self.play(Write(eq2), run_time=1.0)
        self.play(Write(eq3), run_time=1.0)
        self.play(Write(note), run_time=0.8)
        self.wait(1.5)

        remain = Square(side_length=a - b, color=YELLOW, fill_opacity=0.45, stroke_width=3)
        remain.move_to(origin + np.array([(a - b) / 2, (a - b) / 2, 0]))
        remain_label_w = MathTex('a-b', font_size=34, color=YELLOW)
        remain_label_w.next_to(remain, DOWN, buff=0.12)
        remain_label_h = MathTex('a-b', font_size=34, color=YELLOW)
        remain_label_h.next_to(remain, LEFT, buff=0.12)

        self.play(
            FadeOut(right_strip),
            FadeOut(top_strip),
            FadeOut(overlap),
            FadeOut(label_ab_right),
            FadeOut(label_ab_top),
            FadeOut(label_b2),
            FadeOut(big_square),
            FadeOut(label_a_bottom),
            FadeOut(label_a_left),
            FadeOut(label_b_bottom),
            FadeOut(label_b_left),
            run_time=1.2
        )
        self.play(FadeIn(remain), Write(remain_label_w), Write(remain_label_h), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
