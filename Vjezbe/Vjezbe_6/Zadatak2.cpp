#include <iostream>
#include <math.h>


void tocka_i_kruznica(double x1, double y1, double x0, double y0, double radijus){
    
    double udaljenost_dvije_tocke = sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0));
    
    if (udaljenost_dvije_tocke < radijus) {
        std::cout << "Tocka se nalazi u kruznici. " << std::endl;
    }
    
    if (udaljenost_dvije_tocke == radijus) {
        std::cout << "Tocka se nalazi na kruznici. " << std::endl;
    }
    
    if (udaljenost_dvije_tocke > radijus) {
        std::cout <<"Tocka se nalazi izvan kruznice." << std::endl;
        
    }
}

int main() {
    tocka_i_kruznica(3,2,0,0,6);
    return 0;
}