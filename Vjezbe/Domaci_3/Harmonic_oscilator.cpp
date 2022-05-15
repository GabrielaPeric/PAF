#include <iostream>
#include <Harmonic_oscillator.h>
#include <math.h>

HarmonicOscillator::HarmonicOscillator(double x0, double v0, double a0, double k0, double m0, double step = 0.1)
    {
        x = x0;
        v = v0;
        a = a0;
        k = k0;
        m = m0;
        t = 0;
        dt = step;
        x_list.push_back(x);
        v_list.push_back(v);
        a_list.push_back(a);
        t_list.push_back(t);

    }

void HarmonicOscillator::evolve()
{
    
     t += dt;
    x = x +v*dt;
    v = v + a*dt;
    a = (-k/m)*x;
    x_list.push_back(x);
    v_list.push_back(v);
    a_list.push_back(a);
    t_list.push_back(t);        

    

};