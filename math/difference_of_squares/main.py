from manim import *
import numpy as np

FONT = 'Noto Sans CJK SC'

class DifferenceOfSquares(Scene):
    def construct(self):
        title = Text('平方差公式：面积演示', font_size=44, font=FONT)
        title.to_edge(UP)
        self.play(Write(title), run_time=1.5)

        formula = MathTex('a^2', '-', 'b^2', '=', '(a+b)(a-b)', font_size=44)
        formula.next_to(title, DOWN, buff=0.2)
        formula[0].set_color(YELLOW)
        formula[2].set_color(RED)
        self.play(Write(formula), run_time=1.5)
        self.wait(0.5)

        a = 5
        b = 2
        scale = 0.55
        A = a * scale
        B = b * scale
        H = (a - b) * scale
        W = (a - b) * scale

        origin = np.array([-4.0, -1.5, 0])

        big_square = Square(side_length=A, color=YELLOW, fill_opacity=0.15, stroke_width=3)
        big_square.move_to(origin + np.array([A / 2, A / 2, 0]))

        small_square = Square(side_length=B, color=RED, fill_opacity=0.55, stroke_width=3)
        small_square.move_to(origin + np.array([A - B / 2, A - B / 2, 0]))

        label_a_left = MathTex('a', font_size=36, color=YELLOW).next_to(big_square, LEFT, buff=0.1)
        label_a_bottom = MathTex('a', font_size=36, color=YELLOW).next_to(big_square, DOWN, buff=0.1)
        label_b_top = MathTex('b', font_size=36, color=RED).next_to(small_square, UP, buff=0.1)
        label_b_right = MathTex('b', font_size=36, color=RED).next_to(small_square, RIGHT, buff=0.1)

        self.play(Create(big_square), run_time=1.5)
        self.play(Write(label_a_left), Write(label_a_bottom), run_time=1.0)
        self.play(FadeIn(small_square), Write(label_b_top), Write(label_b_right), run_time=1.5)
        self.wait(0.8)

        area_text1 = MathTex('a^2', font_size=42, color=YELLOW)
        area_text1.move_to(big_square.get_center() + LEFT * 0.8 + UP * 0.5)
        area_text2 = MathTex('-b^2', font_size=42, color=RED)
        area_text2.move_to(small_square.get_center())
        self.play(Write(area_text1), Write(area_text2), run_time=1.2)
        self.wait(0.8)

        l_shape_text = Text('剩下 L 形面积 = a² - b²', font_size=30, font=FONT)
        l_shape_text.next_to(formula, DOWN, buff=0.25)
        self.play(
            FadeOut(small_square),
            FadeOut(label_b_top),
            FadeOut(label_b_right),
            FadeOut(area_text2),
            run_time=1.2
        )
        self.play(Write(l_shape_text), run_time=1.2)
        self.wait(0.5)

        bottom = Rectangle(width=A, height=H, color=BLUE, fill_opacity=0.45, stroke_width=2)
        bottom.move_to(origin + np.array([A / 2, H / 2, 0]))
        left_top = Rectangle(width=W, height=B, color=GREEN, fill_opacity=0.45, stroke_width=2)
        left_top.move_to(origin + np.array([W / 2, H + B / 2, 0]))

        self.play(
            FadeOut(big_square),
            FadeOut(area_text1),
            FadeOut(label_a_left),
            FadeOut(label_a_bottom),
            run_time=1.0
        )
        self.play(Create(bottom), Create(left_top), run_time=1.5)

        label_a_bottom2 = MathTex('a', font_size=32, color=BLUE).next_to(bottom, DOWN, buff=0.1)
        label_h_left = MathTex('a-b', font_size=32, color=BLUE).next_to(bottom, LEFT, buff=0.1)
        label_w_top = MathTex('a-b', font_size=32, color=GREEN).next_to(left_top, UP, buff=0.1)
        label_b_left = MathTex('b', font_size=32, color=GREEN).next_to(left_top, LEFT, buff=0.1)
        self.play(
            Write(label_a_bottom2),
            Write(label_h_left),
            Write(label_w_top),
            Write(label_b_left),
            run_time=1.5
        )
        self.wait(0.8)

        rearrange_text = Text('把左上部分旋转后移到右侧', font_size=28, font=FONT)
        rearrange_text.next_to(l_shape_text, DOWN, buff=0.12)
        self.play(Write(rearrange_text), run_time=1.0)
        self.wait(0.5)

        target_center = np.array([origin[0] + A + B / 2, origin[1] + H / 2, 0])
        left_top_target = left_top.copy()
        left_top_target.rotate(-PI / 2, about_point=left_top_target.get_center())
        left_top_target.move_to(target_center)

        self.play(FadeOut(label_w_top), FadeOut(label_b_left), run_time=0.4)
        self.play(Transform(left_top, left_top_target), run_time=2.5, rate_func=smooth)
        self.wait(0.5)

        final_outline = SurroundingRectangle(VGroup(bottom, left_top), color=WHITE, buff=0.03, stroke_width=3)
        final_label_w = MathTex('a+b', font_size=34, color=WHITE).next_to(final_outline, DOWN, buff=0.12)
        final_label_h = MathTex('a-b', font_size=34, color=WHITE).next_to(final_outline, LEFT, buff=0.12)
        self.play(Create(final_outline), Write(final_label_w), Write(final_label_h), run_time=1.8)
        self.wait(0.8)

        final_area_text = MathTex('(a+b)(a-b)', font_size=42, color=WHITE)
        final_area_text.next_to(final_label_w, DOWN, buff=0.35)
        self.play(Write(final_area_text), run_time=1.5)
        self.wait(0.8)

        box = SurroundingRectangle(formula, color=YELLOW, buff=0.1)
        self.play(Create(box), run_time=1.0)

        conclusion = Text('面积相同，因此 a² - b² = (a+b)(a-b)', font_size=30, font=FONT)
        conclusion.to_edge(DOWN, buff=0.3)
        self.play(Write(conclusion), run_time=1.5)
        self.wait(3.0)
