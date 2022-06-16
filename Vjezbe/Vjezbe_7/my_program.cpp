#include <iostream>
#include <Particle.h>

int main()
{
    Particle p1(100,45,0,0);
    std::cout << "Domet iznosi: " << p1.range() << std::endl;
    std::cout << "Trajanje je: " << p1.time() << std::endl;

    Particle p2(10,60,0,0);
    std::cout <<"Domet iznosi: " << p2.range() << std::endl;
    std::cout <<"Trajanje iznosi: " << p2.time() << std::endl;

}