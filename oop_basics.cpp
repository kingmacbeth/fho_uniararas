#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Classe Editora


class Editora{
private:
    string nomeEditora;
    string endereco;
    string cnpj;

public:
    Editora();
    Editora(string nomeEditora, string endereco, string cnpj);
    
    string getNomeEditora();
    string getEnderecoEditora();
    string getCnpjEditora();
    
    void setNomeEditora(string nomeEditora);
    void setEnderecoEditora(string endereco);
    void setCnpjEditora(string cnpj);
};

Editora::Editora(){
    this->nomeEditora = " ";
    this->endereco = " ";
    this->cnpj = " ";
}

Editora::Editora(string nomeEditora, string endereco, string cnpj){
    this -> nomeEditora = nomeEditora;
    this -> endereco = endereco;
    this -> cnpj = cnpj; 
}

string Editora::getNomeEditora(){
    return this -> nomeEditora;
}

string Editora::getEnderecoEditora(){
    return this -> endereco;
}

string Editora::getCnpjEditora(){
    return this -> cnpj;
}

void Editora::setNomeEditora(string nomeEditora){
    this -> nomeEditora = nomeEditora;
}

void Editora::setEnderecoEditora(string endereco){
    this -> endereco = endereco;
}

void Editora::setCnpjEditora(string cnpj){
    this -> cnpj = cnpj;
}

// Classe Livro


class Livro : public Editora{
private:
    string titulo;
    int edicao;
    string autor ;

public:
    Livro();
    Livro(string titulo, int edicao, string autor, string nomeEditora, string endereco, string cnpj);
    
    string getTitulo();
    int getEdicao();
    string getAutor();
    
    void setTitulo(string titulo);
    void setEdicao(int edicao);
    void setAutor(string autor);
};

Livro::Livro(){
    this->titulo = " ";
    this->edicao = 0;
    this->autor = " ";
}

Livro::Livro(string titulo, int edicao, string autor, string nomeEditora, string endereco, string cnpj):Editora(nomeEditora, endereco, cnpj){
    this -> titulo = titulo;
    this -> edicao = edicao;
    this -> autor = autor;
}

string Livro::getTitulo(){
    return this -> titulo;
}

int Livro::getEdicao(){
    return this -> edicao;
}

string Livro::getAutor(){
    return this -> autor;
}

void Livro::setTitulo(string titulo){
    this -> titulo = titulo;
}

void Livro::setEdicao(int edicao){
    this -> edicao = edicao;
}

void Livro::setAutor(string autor){
    this -> autor = autor;
}

// Classe Consumidor


class Consumidor {
private:
    string nomeConsumidor;
    vector <Livro> livrosAdquiridos; //cria a composicao com livro
    string cpf;

public:
    Consumidor();
    
    string getNomeConsumidor();
    void getLivros(); //imprime os livros do consumidor
    string getCpf();
    
    void setNomeConsumidor(string nomeConsumidor);
    void setInserirLivros(Livro L1);
    void setCpf(string cpf);
    
};

Consumidor::Consumidor(){
    this->nomeConsumidor = " ";
    this->cpf = " ";
}

string Consumidor::getNomeConsumidor(){
    return this -> nomeConsumidor;
}

void Consumidor::getLivros(){
    for(int i = 0; i < livrosAdquiridos.size(); i++){
       cout << livrosAdquiridos[i].getTitulo() <<endl;
   }
}

string Consumidor::getCpf(){
    return this -> cpf;
}

void Consumidor::setNomeConsumidor(string nomeConsumidor){
    this -> nomeConsumidor = nomeConsumidor;
}

void Consumidor::setInserirLivros(Livro L1){
    this -> livrosAdquiridos.push_back(L1);
}

void Consumidor::setCpf(string cpf){
    this -> cpf = cpf;
}


int main() {
    Editora editora;
    Livro livro1, livro2;
    Consumidor consumidor;

    // Dados da Editora
    editora.setNomeEditora("Tom&Tom");
    editora.setEnderecoEditora("Rua das Aldeias, 32");
    editora.setCnpjEditora("123.456-0");
    cout << "Nome da Editora: " << editora.getNomeEditora() << endl;
    cout << "Endereço da Editora: " << editora.getEnderecoEditora() << endl;
    cout << "CNPJ da Editora: " << editora.getCnpjEditora() << endl;

    // Dados dos Livros
    livro1.setTitulo("Alice no País das Maravilhas");
    livro1.setEdicao(1);
    livro1.setAutor("Lewis Carroll");
    livro2.setTitulo("Rapunzel");
    livro2.setEdicao(2);
    livro2.setAutor("Unknown");
    cout << "Título do Livro: " << livro1.getTitulo() << endl;
    cout << "Edição do Livro: " << livro1.getEdicao() << endl;
    cout << "Autor do Livro: " << livro1.getAutor() << endl;

    // Dados do Consumidor
    consumidor.setNomeConsumidor("Renato");
    consumidor.setCpf("987.654-0");
    consumidor.setInserirLivros(livro1);
    consumidor.setInserirLivros(livro2);

    cout << "Livros adquiridos por " << consumidor.getNomeConsumidor() << ":" << endl;
    consumidor.getLivros();
    cout << "CPF do consumidor: " << consumidor.getCpf() << endl;
    
    return 0;
}