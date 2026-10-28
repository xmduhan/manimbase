from manim import *
import numpy as np

FONT = 'Noto Sans CJK SC'

class DistributiveLaw(Scene):
    def construct(self):
        title = Text('乘法分配律', font_size=48, font=FONT)
        title.to_edge(UP)
        self.play(Write(title), run_time=2.0)

        # 开头：展示 a(b+c) 分配到 ab+ac 的过程
        intro_expr = MathTex('a', '(', 'b', '+', 'c', ')', font_size=56)
        intro_expr.next_to(title, DOWN, buff=0.5)
        intro_expr[0].set_color(YELLOW)
        intro_expr[2].set_color(BLUE)
        intro_expr[4].set_color(GREEN)
        self.play(Write(intro_expr), run_time=2.0)
        self.wait(0.8)

        node_a = MathTex('a', font_size=60, color=YELLOW)
        node_b = MathTex('b', font_size=60, color=BLUE)
        node_c = MathTex('c', font_size=60, color=GREEN)
        node_a.move_to(LEFT * 2.2 + DOWN * 0.8)
        node_b.move_to(RIGHT * 0.2 + DOWN * 0.2)
        node_c.move_to(RIGHT * 0.2 + DOWN * 1.4)
        schematic = VGroup(node_a, node_b, node_c)
        self.play(Write(schematic), run_time=1.5)

        arrow_b = CurvedArrow(node_a.get_right(), node_b.get_left(), angle=-TAU / 4, color=BLUE)
        arrow_c = CurvedArrow(node_a.get_right(), node_c.get_left(), angle=TAU / 4, color=GREEN)
        self.play(Create(arrow_b), Create(arrow_c), run_time=2.5)
        self.wait(0.8)

        # 视角平移，显示结果
        intro_group = VGroup(intro_expr, schematic, arrow_b, arrow_c)
        self.play(intro_group.animate.shift(LEFT * 2.5), run_time=2.0, rate_func=smooth)
        result = MathTex('=', 'a', 'b', '+', 'a', 'c', font_size=56)
        result.next_to(intro_expr, RIGHT, buff=0.35)
        result[1].set_color(YELLOW)
        result[2].set_color(BLUE)
        result[4].set_color(YELLOW)
        result[5].set_color(GREEN)
        self.play(Write(result), run_time=2.0)
        self.wait(1.2)
        self.play(FadeOut(intro_group), FadeOut(result), run_time=1.0)

        equation = MathTex('a(b+c)', '=', 'ab', '+', 'ac', font_size=48)
        equation.next_to(title, DOWN, buff=0.5)
        equation[0].set_color(YELLOW)
        equation[2].set_color(BLUE)
        equation[4].set_color(GREEN)
        self.play(Write(equation), run_time=2.0)
        self.wait(1.2)

        a, b, c = 2.0, 2.5, 1.5
        scale = 0.8
        gap = 0.8

        # 第1组：两个长方形相邻，共用一条边
        rect_ab1 = Rectangle(width=b*scale, height=a*scale, color=BLUE, fill_opacity=0.4)
        rect_ac1 = Rectangle(width=c*scale, height=a*scale, color=GREEN, fill_opacity=0.4)
        group1 = VGroup(rect_ab1, rect_ac1).arrange(RIGHT, buff=0, aligned_edge=DOWN)
        group1.move_to(np.array([-3.0, -0.6, 0]))

        label_a1 = MathTex('a').next_to(group1, LEFT, buff=0.15)
        label_b1 = MathTex('b').next_to(rect_ab1, UP, buff=0.1)
        label_c1 = MathTex('c').next_to(rect_ac1, UP, buff=0.1)
        label_ab1 = MathTex('ab').move_to(rect_ab1.get_center())
        label_ac1 = MathTex('ac').move_to(rect_ac1.get_center())
        label_bc1 = MathTex('b+c').next_to(group1, DOWN, buff=0.2)

        caption1 = Text('第1组：两个长方形相邻（共边）', font_size=28, font=FONT)
        caption1.next_to(label_bc1, DOWN, buff=0.3)

        self.play(
            Create(rect_ab1), Create(rect_ac1),
            Write(label_a1), Write(label_b1), Write(label_c1),
            run_time=3.0
        )
        self.play(Write(label_ab1), Write(label_ac1), run_time=2.0)
        self.play(Write(label_bc1), Write(caption1), run_time=2.0)
        self.wait(1.5)

        # 第2组：先分开显示，再合并到与第1组相同
        rect_ab2 = Rectangle(width=b*scale, height=a*scale, color=BLUE, fill_opacity=0.4)
        rect_ac2 = Rectangle(width=c*scale, height=a*scale, color=GREEN, fill_opacity=0.4)
        group2 = VGroup(rect_ab2, rect_ac2).arrange(RIGHT, buff=gap, aligned_edge=DOWN)
        group2.move_to(np.array([2.5, -0.6, 0]))

        label_a2 = MathTex('a').next_to(rect_ab2, LEFT, buff=0.15)
        label_b2 = MathTex('b').next_to(rect_ab2, UP, buff=0.1)
        label_c2 = MathTex('c').next_to(rect_ac2, UP, buff=0.1)

        self.play(
            Create(rect_ab2), Create(rect_ac2),
            Write(label_a2), Write(label_b2), Write(label_c2),
            run_time=3.0
        )
        self.wait(1.0)

        # 先分别显示两个长方形的面积
        label_ab2 = MathTex('ab').move_to(rect_ab2.get_center())
        label_ac2 = MathTex('ac').move_to(rect_ac2.get_center())
        self.play(Write(label_ab2), Write(label_ac2), run_time=2.0)
        self.wait(1.5)

        merged_center = np.array([
            rect_ab2.get_right()[0] + rect_ac2.width / 2,
            rect_ab2.get_center()[1],
            0
        ])

        label_c2_target = label_c2.copy().next_to(
            rect_ac2.copy().move_to(merged_center), UP, buff=0.1
        )

        self.play(
            rect_ac2.animate.move_to(merged_center),
            label_ac2.animate.move_to(merged_center),
            label_c2.animate.move_to(label_c2_target),
            run_time=4.0,
            rate_func=smooth
        )
        self.wait(1.0)

        label_bc2 = MathTex('b+c').next_to(VGroup(rect_ab2, rect_ac2), DOWN, buff=0.2)
        caption3 = Text('合并后：与第1组相同', font_size=28, font=FONT)
        caption3.next_to(label_bc2, DOWN, buff=0.3)

        self.play(Write(label_bc2), run_time=2.0)
        self.play(Write(caption3), run_time=2.0)
        self.wait(3.0)

        total = MathTex('a(b+c)', '=', 'ab', '+', 'ac', font_size=40)
        total.next_to(caption3, DOWN, buff=0.4)
        total[0].set_color(YELLOW)
        total[2].set_color(BLUE)
        total[4].set_color(GREEN)
        self.play(TransformFromCopy(equation, total), run_time=2.5)
        self.wait(3.0)
