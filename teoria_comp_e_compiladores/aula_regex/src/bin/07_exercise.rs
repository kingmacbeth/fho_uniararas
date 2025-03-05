use aula_regex::TEXTO_BASE;
use regex::Regex;

fn main() {
    let re =
        Regex::new(r"\d{2}(?:[\s]+de)(?:[\s][a-z\u0080-\u024F]+\b)(?:[\s]+de)\s\d{4}*").unwrap();
    let result: Vec<&str> = re.find_iter(TEXTO_BASE).map(|m| m.as_str()).collect();
    println!("{:?}", result);
}
