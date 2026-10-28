from manim import *

FONT = 'Noto Sans CJK SC'

class AssociativeLaw(Scene):
    def construct(self):
        title = Text('乘法结合律', font_size=48, font=FONT)
        title.to_edge(UP)
        self.play(Write(title), run_time=2.0)

        formula = MathTex(
            '(', 'a', r'\\times', 'b', ')', r'\\times', 'c',
            '=', 'a', r'\\times', '(', 'b', r'\\times', 'c', ')',
            font_size=56
        )
        formula.next_to(title, DOWN, buff=0.6)
        formula[1].set_color(YELLOW)
        formula[3].set_color(BLUE)
        formula[6].set_color(GREEN)
        formula[8].set_color(YELLOW)
        formula[11].set_color(BLUE)
        formula[13].set_color(GREEN)
        self.play(Write(formula), run_time=2.5)
        self.wait(0.8)

        left_group = VGroup(formula[0], formula[1], formula[2], formula[3], formula[4])
        right_group = VGroup(formula[10], formula[11], formula[12], formula[13], formula[14])
        left_box = SurroundingRectangle(left_group, color=YELLOW, buff=0.08)
        right_box = SurroundingRectangle(right_group, color=GREEN, buff=0.08)
        left_label = Text('先算 a×b', font_size=24, font=FONT, color=YELLOW)
        right_label = Text('先算 b×c', font_size=24, font=FONT, color=GREEN)
        left_label.next_to(left_box, DOWN, buff=0.15)
        right_label.next_to(right_box, DOWN, buff=0.15)
        self.play(Create(left_box), Create(right_box), run_time=1.5)
        self.play(Write(left_label), Write(right_label), run_time=1.5)
        self.wait(1.5)
        self.play(
            FadeOut(left_box), FadeOut(right_box),
            FadeOut(left_label), FadeOut(right_label),
            run_time=1.0
        )

        concrete = MathTex(
            '(', '2', r'\\times', '3', ')', r'\\times', '4',
            '=', '2', r'\\times', '(', '3', r'\\times', '4', ')',
            font_size=52
        )
        concrete.next_to(formula, DOWN, buff=0.9)
        concrete[1].set_color(YELLOW)
        concrete[3].set_color(BLUE)
        concrete[6].set_color(GREEN)
        concrete[8].set_color(YELLOW)
        concrete[11].set_color(BLUE)
        concrete[13].set_color(GREEN)
        self.play(Write(concrete), run_time=2.0)
        self.wait(1.0)

        calc1 = MathTex(r'(2 \\times 3) \\times 4', '=', r'6 \\times 4', '=', '24', font_size=44)
        calc2 = MathTex(r'2 \\times (3 \\times 4)', '=', r'2 \\times 12', '=', '24', font_size=44)
        calc1.next_to(concrete, DOWN, buff=0.6).shift(LEFT * 3.2)
        calc2.next_to(concrete, DOWN, buff=0.6).shift(RIGHT * 3.2)
        calc1[2].set_color(BLUE)
        calc1[4].set_color(GREEN)
        calc2[2].set_color(GREEN)
        calc2[4].set_color(YELLOW)
        self.play(Write(calc1), Write(calc2), run_time=2.5)
        self.wait(1.5)

        box1 = SurroundingRectangle(calc1[0], color=YELLOW, buff=0.08)
        box2 = SurroundingRectangle(calc2[0], color=GREEN, buff=0.08)
        self.play(Create(box1), Create(box2), run_time=1.5)
        self.wait(1.0)

        conclusion = Text('两种分组方式结果相同', font_size=32, font=FONT)
        conclusion.next_to(VGroup(calc1, calc2), DOWN, buff=0.8)
        self.play(Write(conclusion), run_time=2.0)
        self.wait(1.5)

        self.play(
            FadeOut(formula), FadeOut(concrete),
            FadeOut(calc1), FadeOut(calc2),
            FadeOut(box1), FadeOut(box2),
            FadeOut(conclusion),
            run_time=1.5
        )

        visual_title = Text('用 24 个点看分组', font_size=36, font=FONT)
        visual_title.next_to(title, DOWN, buff=0.6)
        self.play(Write(visual_title), run_time=1.5)

        def dot_block(rows, cols, color, spacing=0.26):
            block = VGroup()
            for i in range(rows):
                for j in range(cols):
                    dot = Dot(radius=0.06, color=color)
                    dot.move_to([j * spacing, i * spacing, 0])
                    block.add(dot)
            return block

        left_blocks = VGroup(
            dot_block(2, 3, YELLOW),
            dot_block(2, 3, BLUE),
            dot_block(2, 3, GREEN),
            dot_block(2, 3, RED),
        )
        left_blocks.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        left_blocks.move_to(LEFT * 3.2 + DOWN * 0.4)

        right_blocks = VGroup(
            dot_block(3, 4, ORANGE),
            dot_block(3, 4, PURPLE),
        )
        right_blocks.arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        right_blocks.move_to(RIGHT * 2.8 + DOWN * 0.4)

        left_label = Text('(2×3)×4：4 组，每组 6 个', font_size=24, font=FONT)
        right_label = Text('2×(3×4)：2 组，每组 12 个', font_size=24, font=FONT)
        left_label.next_to(left_blocks, DOWN, buff=0.35)
        right_label.next_to(right_blocks, DOWN, buff=0.35)

        self.play(
            LaggedStart(*[FadeIn(b) for b in left_blocks], lag_ratio=0.15),
            run_time=2.0
        )
        self.play(Write(left_label), run_time=1.5)
        self.play(
            LaggedStart(*[FadeIn(b) for b in right_blocks], lag_ratio=0.2),
            run_time=2.0
        )
        self.play(Write(right_label), run_time=1.5)
        self.wait(1.5)

        final = MathTex(r'(2 \\times 3) \\times 4', '=', r'2 \\times (3 \\times 4)', '=', '24', font_size=40)
        final.next_to(VGroup(left_label, right_label), DOWN, buff=0.5)
        self.play(Write(final), run_time=2.0)
        self.wait(3.0)
