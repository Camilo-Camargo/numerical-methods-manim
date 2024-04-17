from  manim import *
from  newton_raphson import NewtonRaphsonRoots
from  sympy.abc import x
from sympy import latex, sympify

H1 = 32
H2 = 28 


class NewtonRaphsonMethod(MovingCameraScene):
    _mobjects = []
    _slide_factor = 1

    def next_slide(self):
        width = self.camera.frame_width 
        objout = []
        for obj in self.mobjects:
            objout.append(obj.animate.shift(self._slide_factor * width * LEFT))
        self._slide_factor += 1

        self.play(*objout)

        for obj in self.mobjects:
            self._mobjects.append(obj)
            self.remove(obj)



    def construct(self):
        ## Introduction 
        width = self.camera.frame_width
        title = Text(r"Multiples Roots", font_size=H1, weight=BOLD)
        by = Text("Camilo Andres Camargo Castaneda", font_size=H2)
        VGroup(title, by).arrange(DOWN)
        self.play(Write(title),Write(by)) 
 
        self.next_slide()

        newton_raphon_title_definition = Text("Isaac Newton + Joseph Raphson")
        newton_raphon_title_definition.to_corner(UP+LEFT)

        newton_raphon_title = Text("Newton Raphson", font_size=H1, weight=BOLD)
        newton_raphon_title.to_corner(UP+LEFT)
        #self.play(Write(newton_raphon_title_definition))

        self.play(
            Transform(newton_raphon_title_definition, newton_raphon_title)
        ) 

 

        ## Newton Raphon Proof 
        f = (x-3)*(x-1)*(x-1)
        method = NewtonRaphsonRoots(f)

        fx = lambda k: float(sympify(f.subs(x, k)).evalf())
        f_tex = MathTex(r"f(x) = " + latex(f))

        df  = method.df
        dfx = lambda k: float(sympify(df.subs(x, k)).evalf())
        df_tex = MathTex(r"f\prime(x) = " + latex(df))

        df2 = method.df2
        df2x = lambda k: float(sympify(df2.subs(x, k)).evalf())
        df2_tex = MathTex(r"f\prime\prime(x) = " + latex(df2))

        fns = VGroup(f_tex, df_tex, df2_tex).arrange(DOWN)

        fun = (fx, dfx, df2x)

        self.camera.frame.save_state() 

        for fn in fns:
            self.play(Write(fn))

        self.next_slide()
        self.wait()

        self.play(self.camera.frame.animate.set(width=width*8))
        self.wait()

        axes = Axes(
            x_range=[0,4, 0.1],
            y_range=[0,4, 0.1],
            x_length = 50,
            y_length = 50,
            axis_config = {
                "include_numbers": True,
                "include_tip": False
            }
        )
        axes.add_coordinates()
        self.play(Create(axes))
        f_chart = axes.plot(fx)
        self.play(Write(f_chart))

        left = method.compute(0)
        right = method.compute(4)


        #self.proof(left, fun, axes)
        #self.proof(right, fun, axes)


        self.next_slide()

        self.wait()
        #Taylor Proof
        taylor_title = Title("Taylor Proof")
        taylor_1 = MathTex(r"f(x_{i+1}) = \sum_{n=1}^{\infty} \frac{f^n(x_i)(x_{i+1}-x_i)^n}{n!}")
        taylor_2 = MathTex(r"f(x_{i+1})= f(x_i) + f\prime(x_i)(x_{i+1} - x_i)")
        taylor_3 = MathTex(r"0 = f(x_i) + f\prime(x_i)(x_{i+1} - x_i)")
        taylor_4 = MathTex(r" \frac{-f(x_i)}{f\prime(x_i)} = (x_{i+1} - x_i)")
        taylor_5 = MathTex(r" x_i -\frac{f(x_i)}{f\prime(x_i)} = (x_{i+1})")
        taylor_6 = MathTex(r"(x_{i+1}) = x_i -\frac{f(x_i)}{f\prime(x_i)}")
        taylor_proof = VGroup(
            taylor_title,
            taylor_1,
            taylor_2,
            taylor_3,
            taylor_4,
            taylor_5,
            taylor_6,
        ).arrange(DOWN)

        self.play(Restore(self.camera.frame))

        self.play(self.camera.frame.animate.set(width=width*1.5))

        for taylor in taylor_proof:
            self.play(Write(taylor))

        #self.play([FadeOut(i) for i in taylor])



    def proof(self, vars, fun,axes):
        fx, dfx, df2x = fun

        for i,xl in enumerate(vars.keys()):

            x_ = vars[xl]
            y_ = fx(x_) 
            dy_ = df2x(x_)
            f_dot = axes.coords_to_point(x_, y_, 0)
            f_dot = Dot(f_dot).set_color(RED) 
            f_dot_lines = axes.get_lines_to_point(f_dot.get_center())
            line_offset = float(100)
            x_dot = axes.coords_to_point(x_, 0, 0)

            self.camera.frame.save_state()
            self.play(self.camera.frame.animate.scale(0.5).move_to(f_dot))

            x_dot = Dot(x_dot) 
            x_line= Line(x_dot.get_center()-[0,line_offset,0], x_dot.get_center()+[0,line_offset,0]) 

            x_f_line = Line(x_dot.get_center(), f_dot.get_center())
            self.play(Create(x_line))
            self.play(Create(f_dot))
            self.play(
                Create(f_dot_lines[1]),
                FadeOut(x_line)
            )


            # tangente 
            tan = lambda _x: y_ + dy_*(_x - x_)
            x_a_p = x_*line_offset
            x_b_p = x_*(-line_offset)
            print(type(x_a_p))
            x_tan_a = axes.coords_to_point(x_a_p,tan(x_a_p), 0)
            x_tan_a = Dot(x_tan_a)
            x_tan_b = axes.coords_to_point(x_b_p, tan(x_b_p), 0)
            x_tan_b = Dot(x_tan_b)
            x_tan = Line(x_tan_a.get_center(), x_tan_b.get_center()).set_color(ORANGE) 

            x_axis_line = None
            x_1 = None

            if(i < len(vars.keys())-1):
                x_1 = vars[list(vars.keys())[i+1]]
                x_axis_a_dot = axes.coords_to_point(x_1, 0, 0)
                x_axis_a_dot = Dot(x_axis_a_dot)

                x_axis_b_dot = axes.coords_to_point(x_, 0,0)
                x_axis_b_dot = Dot(x_axis_b_dot)

                x_axis_line = Line(x_axis_a_dot.get_center(), x_axis_b_dot.get_center())


            self.play(Create(x_tan), Create(x_axis_a_dot))
            self.play(Create(x_f_line))

            y_brace = Brace(x_axis_line)
            y_brace_tex = y_brace.get_tex(r"\Delta f(x)-0")
            self.play(Create(x_tan))
            self.wait()

            self.play(Create(y_brace), Write(y_brace_tex))

            if(x_axis_line):
                self.play(Create(x_axis_line))
                x_brace = Brace(x_axis_line)
                x_brace_tex = x_brace.get_tex(r"\Delta x_{i+1} - x_i")
                self.play(Create(x_brace), Write(x_brace_tex))
                self.wait()


            self.wait(2)

            self.play(FadeOut(y_brace), FadeOut(y_brace_tex), FadeOut(x_axis_a_dot))

            if(x_axis_line):
                self.play(FadeOut(x_brace), FadeOut(x_brace_tex))
            self.play(
                FadeOut(f_dot),
                FadeOut(x_tan),
                FadeOut(f_dot_lines)
            )

            self.play(Restore(self.camera.frame))


