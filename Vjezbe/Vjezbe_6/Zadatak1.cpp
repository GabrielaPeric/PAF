#include <iostream>

void jednadzba_pravca(double x1, double y1, double x2, double y2) {
    
    double k = (y2-y1)/(x2-x1);
    double l = k*(-x1) + y1;
 
    if (l == 0) {
        std::cout << "Jednadzba pravca glasi "<< k << "x" << std::endl;
    }
    else {
        std::cout << "Jednadzba pravca glasi " << k << "x + " << l  << std::endl;
    }
} 

int main() {
    jednadzba_pravca(4,2,2,3);
    return 0;
}