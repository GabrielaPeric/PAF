#include <iostream>
#include <vector>

using std::vector;

class HarmonicOscillator {
    
    private:

        double x, v, k, m, t;
        double dt;
        double a;

        void evolve();

    public:
        HarmonicOscillator(double x0, double v0, double a0, double k0, double m0, double step = 0.1);
        
        vector<double>x_list;
        vector<double>v_list;
        vector<double>a_list;
        vector<double>t_list;


};
