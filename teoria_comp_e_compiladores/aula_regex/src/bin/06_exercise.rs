use aula_regex::TEXTO_BASE;
use regex::Regex;

fn main() {
    // Nao entendi o enunciado deste exercicio
    let re = Regex::new(r"\d{4}|\d{5}-\d{4}*").unwrap();
    let result: Vec<&str> = re.find_iter(TEXTO_BASE).map(|m| m.as_str()).collect();
    println!("{:?}", result);
}
