#include <iostream>

void ispisi_listu(int lista[], int n) {
    for(int i = 0; i < n; i++) {
        std::cout << lista[i] << ", ";
    }
    std::cout << std::endl;  
}

void ispisi_listu_u_intervalu(int lista[], int n, int a, int b) {
    std::cout << "Elementi u intervalu od " << a << " do " << b << " su:  ";
    for(int i = 0; i < n; i++) {
        if (lista[i] >= a && lista[i] <= b) {
            std::cout << lista[i] << ", ";
        }
    }  
    std::cout << std::endl;
} 

void zamjena(int lista[], int n, int c, int d) {
    int temp = lista[c];
    lista[c] = lista[d];
    lista[d] = temp;
    ispisi_listu(lista,n);
}


int main() {
    const int n = 8;
    int moja_lista[n] = {5,-9,7,-10,17,-11,20,-1};
    ispisi_listu(moja_lista,n);
    ispisi_listu_u_intervalu(moja_lista,n,-10,10);
    zamjena(moja_lista, n, 3,6);
    return 0;
}