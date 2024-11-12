using namespace std;

struct produto{
    int codigo;
    char nome[50];
    float valor;
};

void imprime(produto p){
        cout <<  "Codigo" << p.codigo << endl;
        cout <<  "Nome" <<  p.nome << endl;
        cout <<  "Valor" << p.valor << endl;
}

/*
produto estoque[5];
for (int i = 0; i < 5; i++)
{
    imprime(estoque[i]);
}
*/

int main(){
    produto estoque[5];

    // leitura do vetor de structs 
    for (int i = 0; i <  5;  i++){
        cout <<  "Codigo" << endl;
        cin >> estoque[i].codigo;
        cout <<  "Nome" << endl;
        cin >> estoque[i].nome;
        cout <<  "Valor" << endl;
        cin >> estoque[i].valor;
    }

    // Imprimir valores superior a 2000
    for (int i = 0; i < 2; i++)
    {
        if (estoque[i].valor > 2000){
                    cout << endl << "Codigo" << estoque[i].codigo;
                    cout << endl << "Nome" << estoque[i].nome;
                    cout << endl << "Valor" << estoque[i].valor;
                }

        // Imprime valor com 10% de desconto
        else if (estoque[i].valor < 1000)
        {
            cout << "Valor com desconto" << estoque[i].valor * 0.9;
        }        
    }

    return 0;
}