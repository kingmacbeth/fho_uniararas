use aula_regex::TEXTO_BASE;
use regex::Regex;

fn main() {
    // Engloba intervalo UNICODE 128 a 591 \u0080-\u024F, incluindo os caracteres latinos
    let re = Regex::new(r"\b(?:[A-Z][a-z\u0080-\u024F][a-z]+)(?:[\s][A-Z][a-z\u0080-\u024F]+)*\b")
        .unwrap();
    let result: Vec<&str> = re.find_iter(TEXTO_BASE).map(|m| m.as_str()).collect();
    println!("{:?}", result);
}
