#include <iostream>
#include <Particle.h>
#include <math.h>


Particle::Particle(double v0, double theta, double x0, double y0, double step)
    {
       x = x0;
       y = y0;
       kut = theta*M_PI/180;
       vx = v0*cos(kut);
       vy = v0*sin(kut);
       t = 0;
       dt = step;

    }

void Particle::evolve()
{
    while(y >= 0)
    {
     vx += 0.;
     vy += g*dt;
     
     x += vx*dt;
     y += vy*dt;
     
     t += dt;
    }
}

double Particle::range()
{
    evolve();
    domet = x;
    return domet;
}

double Particle::time()
{
    evolve();
    trajanje = t;
    return trajanje;
}
