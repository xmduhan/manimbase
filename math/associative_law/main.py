from manim import *
import numpy as np

FONT = 'Noto Sans CJK SC'

class AssociativeLaw(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=68 * DEGREES, theta=-48 * DEGREES)
        title = Text('乘法结合律：体积模型', font_size=44, font=FONT)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=1.5)

        formula = MathTex(r'(a\times b)\times c', '=', r'a\times (b\times c)', font_size=42)
        formula.next_to(title, DOWN, buff=0.15)
        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula), run_time=1.5)

        s = 0.45

        def make_cubes(nx, ny, nz, center, colors):
            group = VGroup()
            info = []
            x0 = center[0] - (nx - 1) * s / 2
            y0 = center[1] - (ny - 1) * s / 2
            z0 = center[2]
            for k in range(nz):
                for i in range(nx):
                    for j in range(ny):
                        cube = Cube(
                            side_length=s * 0.93,
                            fill_opacity=0.75,
                            fill_color=colors[k % len(colors)],
                            stroke_width=0.8,
                            stroke_color=WHITE,
                        )
                        cube.move_to(np.array([x0 + i * s, y0 + j * s, z0 + k * s]))
                        group.add(cube)
                        info.append((cube, i, j, k))
            return group, info

        g1, info1_3d = make_cubes(2, 3, 4, np.array([-1.1, 0, -0.8]), [YELLOW, BLUE, GREEN, RED])
        self.play(
            LaggedStart(*[FadeIn(cube, scale=0.8) for cube in g1], lag_ratio=0.02),
            run_time=2.5
        )

        label1 = Text('第1组：底 2×3，高 4', font_size=26, font=FONT)
        eq1 = MathTex(r'(2\times 3)\times 4 = 6\times 4 = 24', font_size=34)
        info1 = VGroup(label1, eq1).arrange(DOWN, aligned_edge=LEFT)
        info1.to_corner(DL, buff=0.25)
        self.add_fixed_in_frame_mobjects(info1)
        self.play(Write(info1), run_time=1.2)
        self.wait(1.0)

        g2, info2_3d = make_cubes(3, 4, 2, np.array([1.3, 0, -0.8]), [ORANGE, PURPLE])
        self.play(
            LaggedStart(*[FadeIn(cube, scale=0.8) for cube in g2], lag_ratio=0.02),
            run_time=2.5
        )

        label2 = Text('第2组：底 3×4，高 2', font_size=26, font=FONT)
        eq2 = MathTex(r'2\times (3\times 4) = 2\times 12 = 24', font_size=34)
        info2 = VGroup(label2, eq2).arrange(DOWN, aligned_edge=LEFT)
        info2.to_corner(DR, buff=0.25)
        self.add_fixed_in_frame_mobjects(info2)
        self.play(Write(info2), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(info1), FadeOut(info2), run_time=0.8)

        final_text = Text('两种分组，方块总数相同', font_size=30, font=FONT)
        final_eq = MathTex(r'(2\times 3)\times 4', '=', r'2\times (3\times 4)', '=', '24', font_size=44)
        final_group = VGroup(final_text, final_eq).arrange(DOWN, buff=0.15)
        final_group.to_edge(DOWN, buff=0.35)
        self.add_fixed_in_frame_mobjects(final_group)
        self.play(Write(final_group), run_time=1.5)
        self.wait(1.5)

        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(4.0)
        self.stop_ambient_camera_rotation()
