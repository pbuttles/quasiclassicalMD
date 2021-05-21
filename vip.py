# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 03:24:09 2021

@author: pbuttles
"""

from manimlib import *

class quasiclassical_derivation(Scene):
    def construct(self):
        classicaln = Tex(r"\mathcal Z_{CM} = \frac{1}{N!\lambda^{3N}}\int d{\bf r}_1 d{\bf r}_2\dots d{\bf r}_N e^{-\beta V({\bf r}_1, {\bf r}_2, \dots, {\bf r}_N)}")
        classical = Tex(r"\mathcal Z_{CM} = \frac{1}{N!\lambda^{3N}}\int d{\bf r}_1 d{\bf r}_2 e^{-\beta V({\bf r}_1, {\bf r}_2)}")
        quantum = Tex(r"\mathcal Z_{QM} = \Tr \left[ e^{-\beta \hat H} \right]")
        ZCM = Tex(r"\mathcal Z_{CM}")
        #ZQM = Tex(r"\mathcal Z_{QM}")
        Zs = Tex("\mathcal Z_{QM}"," = ","\mathcal Z_{CM}")
        Zs[0:3].set_color(BLUE)
        Zs[4:].set_color(RED)
        
        cnm = VGroup(classical,quantum)
        delet = VGroup(classical,Zs)
        #Zgroup = VGroup(ZCM,ZQM)
        
        classicaln.set_color(RED)
        classical.set_color(RED)
        quantum.set_color(BLUE)
        ZCM.set_color(RED)
        #ZQM.set_color(BLUE)

        classicaln.shift(UP*0.5)
        classical.shift(UP*0.5)
        ZCM.next_to(classical)
        quantum.next_to(classical,direction=DOWN,buff=0.1)
        #ZQM.move_to((classical.get_corner(LEFT+DOWN)-np.array([quantum.get_corner(LEFT+UP)])))
        

        self.wait(1)
        self.play(Write(classicaln))
        self.play(TransformMatchingShapes(classicaln,classical,path_arc = 0))
        self.wait(1)
        self.play(Write(quantum))
        self.wait(0.5)
        self.remove(classical)
        self.play(cnm.animate.to_edge(UP,buff=1))
        empty = Tex(r"_")
        empty.next_to(quantum,direction=RIGHT,buff=0.1)
        quantumexpr = Tex(r" \Tr \left[ e^{-\beta \hat H} \right]")
        quantumexpr.next_to(empty,direction=LEFT,buff=0.1)
        quantumexpr.set_color(BLUE)
        quantumZ = Tex(r"\mathcal Z_{QM} = ")
        quantumZ.next_to(quantumexpr,direction=LEFT,buff=0.2)
        quantumZ.set_color(BLUE)
        editablequantum = VGroup(quantumexpr,quantumZ)
        self.play(Write(Zs))
        self.play(WiggleOutThenIn(Zs[0:3]),run_time=1)
        self.play(WiggleOutThenIn(Zs[4:]),run_time=1)
        self.add(editablequantum)
        self.remove(quantum)
        self.play(FadeOut(Zs),FadeOut(classical),editablequantum.animate.to_edge(UP,buff=1))
        
        #self.add(ZCM)
        #self.add(ZQM)
        #self.play(ZCM.animate.shift(DOWN))
        #self.play(ZQM.animate.shift(DOWN))
        #self.play(Transform(Zgroup,Zs))
        
        ###############################################################
        
        H = Tex(r"\hat H")
        equals = Tex(r" = ")
        Hmatrix = Tex(r"\begin{pmatrix} E_1 & 0 & \dots & 0 \\ 0 & E_2 & \dots & 0\\ \vdots & \vdots & \ddots & \vdots\\ 0 & 0 & \dots& E_\alpha \end{pmatrix}")
        H.shift(LEFT*3)
        equals.next_to(H,direction=RIGHT,buff=0.5)
        Tr = Tex(r"\Tr ")
        Tr.next_to(equals,direction=RIGHT,buff=0.3)
        Hmatrix.next_to(Tr,direction=RIGHT,buff=0.3)
        Trleft = Tex(r"\Tr\left[")
        Trright = Tex(r"\right]")
        Trleft.next_to(H,direction=LEFT,buff=0.1)
        Trright.next_to(H,direction=RIGHT,buff=0.1)
        Trmatrix = Tex(r"\Tr \begin{pmatrix} E_1 & 0 & \dots & 0 \\ 0 & E_2 & \dots & 0\\ \vdots & \vdots & \ddots & \vdots\\ 0 & 0 & \dots& E_n \end{pmatrix}")
        H.shift(UP*0.1)
        
        Hexpr = VGroup(H,equals,Hmatrix,Tr,Trright,Trleft)
        
        sumt = Tex(r"=\sum_\alpha E_\alpha")
        sumt.shift(RIGHT*3.7)
        
        empty.next_to(quantumexpr,direction=RIGHT,buff=0.1)
        qsum = Tex(r"\sum_\alpha e^{-\beta E_\alpha}")
        qsum.set_color(BLUE)
        qsum.next_to(empty,direction=LEFT*1)
        qsum.shift(DOWN*0.1)
        
        self.wait(1)
        self.play(Write(H),Write(equals),Write(Hmatrix))
        self.play(Write(Trleft),Write(Trright),Write(Tr))
        self.play(Hexpr.animate.shift(LEFT))
        #self.wait(0.5)
        self.play(TransformFromCopy(Hmatrix,sumt))
        #self.wait(0.5)
        self.play(TransformMatchingShapes(sumt,qsum),FadeOut(quantumexpr),FadeOut(H),FadeOut(equals),FadeOut(Hmatrix),FadeOut(Trleft),FadeOut(Trright),FadeOut(Tr))
        self.wait(0.5)
        
        normalizationcondition = TexText("Normalization Condition:")
        normalizationcondition.set_color(YELLOW)
        normalizationcondition2 = TexText("If you look everywhere, a particle will be somewhere (Prob. = 1)")
        normalizationcondition.shift(DOWN*2)
        normalizationcondition2.next_to(normalizationcondition,direction=DOWN,buff=0.3)
        condition = VGroup(normalizationcondition,normalizationcondition2)
        norm = Tex(r"\int d{\bf r}_1 d{\bf r}_2 \dots d{\bf r}_N | \psi_\alpha ({\bf r}_1, {\bf r}_2,\dots, {\bf r}_N)|^2")
        norm2 = Tex(r"\int d{\bf r}_1 d{\bf r}_2 | \psi_\alpha ({\bf r}_1, {\bf r}_2)|^2")
        one = Tex(r" = 1")
        one.next_to(norm2,direction=RIGHT,buff=0.1)
        normone = VGroup(norm2,one)
        
        quantumnormone = Tex(r"\mathcal{Z}_{QM}=\sum_\alpha",r"(1)",r"e^{-\beta E_\alpha}")
        quantumnormone[0:6].set_color(BLUE)
        quantumnormone[7:8].set_color(WHITE)
        quantumnormone[9:].set_color(BLUE)
        #quantumnormone.set_color_by_tex(r"\mathcal{Z}_{QM}=\sum_\alpha",color=BLUE,substring=False)
        #quantumnormone.set_color_by_tex(r"e^{-\beta E_\alpha}",color=BLUE,substring=False)
        quantumnorm = Tex(r"\mathcal{Z}_{QM}=\sum_\alpha \int d{\bf r}_1 d{\bf r}_2 | \psi_\alpha ({\bf r}_1, {\bf r}_2)|^2 e^{-\beta E_\alpha}")
        quantumnorm.set_color(BLUE)
        quantumnorm[6:25].set_color(WHITE)
        quantumnorm2 = Tex(r"\mathcal{Z}_{QM}=\int d{\bf r}_1 d{\bf r}_2 \sum_\alpha | \psi_\alpha ({\bf r}_1, {\bf r}_2)|^2 e^{-\beta E_\alpha}")
        quantumnorm2.set_color(BLUE)
        
        self.play(Write(normalizationcondition))
        self.play(Write(normalizationcondition2))
        self.wait(1.5)
        self.play(Write(norm))
        self.play(TransformMatchingShapes(norm,norm2))
        self.play(Write(one))
        self.wait(1)
        editable2 = VGroup(quantumZ,qsum)
        self.remove(qsum)
        self.play(FadeOut(normalizationcondition),FadeOut(normalizationcondition2),normone.animate.shift(DOWN*1.5),TransformMatchingShapes(editable2,quantumnormone))
        self.wait()
        self.play(TransformMatchingShapes(quantumnormone,quantumnorm),FadeOut(norm2),FadeOut(one),)
        #self.wait(1)
        self.play(TransformMatchingShapes(quantumnorm,quantumnorm2))
        lookfamiliar = TexText("Look familiar?")
        lookfamiliar.set_color(RED)
        lookfamiliar.next_to(quantumnorm2,direction=UP)
        classical.next_to(quantumnorm2,direction=DOWN,buff=0.2,aligned_edge=LEFT)
        classical.shift(LEFT*0.5)
        self.wait(1)
        self.play(FadeIn(lookfamiliar),quantumnorm2.animate.shift(RIGHT*1.2),TransformFromCopy(quantumnorm2,classical))
        
        multiplyby = TexText(r"Multiply by")
        cleverone = Tex(r"1 = \frac{N!\lambda^{3N}}{N!\lambda^{3N}}")
        cleverone.next_to(quantumnorm2,direction=UP)
        cleverone[2:7].set_color(color=GREEN)
        cleverone[8:].set_color(color=GREEN)
        multiplyby.next_to(cleverone,direction=LEFT)
        cleverone.shift(UP*0.7)
        multiplyby.shift(UP*0.6)
        
        self.wait(1.5)
        self.play(Write(multiplyby),Write(cleverone),FadeOut(lookfamiliar))
        
        quantumclever = Tex(r"\mathcal{Z}_{QM}=\frac{N!\lambda^{3N}}{N!\lambda^{3N}} \int d{\bf r}_1 d{\bf r}_2 \sum_\alpha | \psi_\alpha ({\bf r}_1, {\bf r}_2)|^2 e^{-\beta E_\alpha}")
        quantumclever.set_color(BLUE)
        quantumclever[4:9].set_color(GREEN)
        quantumclever[9].set_color(WHITE)
        quantumclever[10:15].set_color(GREEN)
        quantumclever2 = Tex(r"\mathcal{Z}_{QM}=\frac{1}{N!\lambda^{3N}} \int d{\bf r}_1 d{\bf r}_2 N!\lambda^{3N} \sum_\alpha | \psi_\alpha ({\bf r}_1, {\bf r}_2)|^2 e^{-\beta E_\alpha}")
        quantumclever2.set_color(BLUE)
        quantumclever2[6:11].set_color(GREEN)
        quantumclever2[18:23].set_color(GREEN)
        
        self.play(TransformMatchingShapes(quantumnorm2,quantumclever),classical.animate.next_to(quantumclever,direction=DOWN,aligned_edge=LEFT))
        self.play(TransformMatchingShapes(quantumclever,quantumclever2),classical.animate.next_to(quantumclever2,direction=DOWN,aligned_edge=LEFT),FadeOut(cleverone),FadeOut(multiplyby))
        
        W = Tex(r"W^{(2)}({\bf r}_1, {\bf r}_2) = N!\lambda^{3N} \sum_\alpha | \psi_\alpha ({\bf r}_1, {\bf r}_2)|^2 e^{-\beta E_\alpha}")
        W.next_to(quantumclever2,direction=UP)
        W[:11].set_color(PURPLE)
        W[12:17].set_color(GREEN)
        W[17:].set_color(BLUE)
        
        slatersums = TexText("Slater Sums")
        slatersums.set_color(PURPLE)
        slatersums.next_to(W,direction=UP,buff=0.2,aligned_edge=ORIGIN)
        
        quantumW = Tex(r"\mathcal{Z}_{QM}=\frac{1}{N!\lambda^{3N}} \int d{\bf r}_1 d{\bf r}_2 W^{(2)}({\bf r}_1, {\bf r}_2)")
        quantumW.next_to(classical,direction=UP,buff=0.2,aligned_edge=LEFT)
        quantumW.set_color(BLUE)
        quantumW[18:].set_color(PURPLE)
        
        self.wait(3.5)
        self.play(Write(W),Write(slatersums))
        self.wait(1)
        self.play(TransformMatchingShapes(quantumclever2,quantumW),FadeOut(W),FadeOut(slatersums))
        self.play(quantumW.animate.set_color(BLUE))
        self.wait(1)
        
        equality = Tex(r"e^{-\beta V({\bf r}_1, {\bf r}_2)} = W^{(2)}({\bf r}_1, {\bf r}_2)")
        equality[:11].set_color(RED)
        equality[12:].set_color(BLUE)
        
        final = VGroup(quantumW,classical)
        
        self.play(TransformMatchingShapes(final,equality))
        self.wait(0.5)
        self.play(equality[0:3].animate.set_color(WHITE),equality[3:11].animate.set_color(YELLOW),equality[12:].animate.set_color(PURPLE))
        
        Potential = Tex(r"-\frac{\ln{\left(W^{(2)}({\bf r}_1, {\bf r}_2)\right)}}{\beta}")
        PotentialV = Tex(r"V({\bf r}_1, {\bf r}_2)")
        PotentialV.set_color(YELLOW)
        Potential.shift(RIGHT*1.5)
        equals.next_to(Potential,direction=LEFT)
        Potential.set_color(WHITE)
        Potential[4:15].set_color(PURPLE)
        PotentialV.next_to(equals,direction=LEFT)
        
        Pot = VGroup(Potential,PotentialV,equals)
        
        self.wait(0.5)
        self.play(TransformMatchingShapes(equality,Pot))
        self.play(ApplyWave(PotentialV))
        self.wait(0.5)
        self.play(Pot.animate.to_edge(UP,buff=1))
        
        bigarrow = Tex(r"\Downarrow").scale(3)
        bigarrow.shift(LEFT*0.8)
        bigarrow.shift(UP)
        solve = TexText("Solve ")
        Wexpr = Tex(r"W^{(2)}({\bf r}_1, {\bf r}_2)")
        Wexpr.set_color(PURPLE)
        fromQM = TexText("\, from QM")
        fromQM[4:].set_color(PURPLE)
        solve.next_to(bigarrow,direction=RIGHT,buff=0.5)
        Wexpr.next_to(solve,direction=RIGHT,buff=0.35)
        fromQM.next_to(Wexpr,direction=RIGHT,buff=0.35)
        skipsteps = VGroup(solve,Wexpr,fromQM)
        
        self.play(FadeIn(bigarrow),Write(skipsteps))
        
        potential0 = Tex(r"u_{\uparrow \downarrow} = u_{\downarrow \uparrow} = k_BT \ln{\left( 1 + \frac{\lambda ^2}{\pi r^2} e^{-2\pi r^2/\lambda ^2}\right)}")
        potential1 = Tex(r"u_{\uparrow \uparrow} = u_{\downarrow \downarrow} = k_BT \ln{\left( 1 - e^{-2\pi r^2/\lambda ^2}\right)}")
        potential0.set_color(BLUE_B)
        potential1.set_color(BLUE_B)
        potential0.shift(DOWN*1)
        potential1.shift(DOWN*2.5)
        
        self.wait(1)
        self.play(Write(potential0),Write(potential1),run_time=1)
        self.play(FadeOut(skipsteps),FadeOut(PotentialV),FadeOut(Pot),FadeOut(bigarrow),potential0.animate.shift(UP*1.75),potential1.animate.shift(UP*1.75))
        self.play(ApplyWave(potential0),ApplyWave(potential1))
        self.wait(3)
        
        
        
        
        
        