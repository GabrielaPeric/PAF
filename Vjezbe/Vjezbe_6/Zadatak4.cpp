#include <iostream>

void rjesi_sustav(float a1, float b1, float c1, float a2, float b2, float c2) {
    /*  x = (c1 - b1*y)/a1, 
    y(b2 - b1*a2/a1) = c2 - c1*a2/a1 */
    float v1 = b2 - b1*a2/a1;
    float v2 = c2 - c1*a2/a1;
    float y = v2/v1;
    float x = (c1 - b1*y)/a1;

    std::cout << "x = " << x << ", a y = " << y << std::endl;
}
 
int main() {
    rjesi_sustav(1,3,5,2,4,6);
    return 0;
}