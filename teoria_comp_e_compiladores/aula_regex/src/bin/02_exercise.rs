use aula_regex::TEXTO_BASE;
use regex::Regex;

fn main() {
    let re =
        Regex::new(r"\b[A-Z][a-zA-Z0-9][a-zA-Z0-9]+(?:\s[A-Z][a-zA-Z0-9][a-zA-Z0-9]+)\b").unwrap();
    let result: Vec<&str> = re.find_iter(TEXTO_BASE).map(|m| m.as_str()).collect();
    println!("{:?}", result);
}
