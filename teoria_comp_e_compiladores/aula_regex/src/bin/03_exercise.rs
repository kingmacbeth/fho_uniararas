use aula_regex::TEXTO_BASE;
use regex::Regex;

fn main() {
    let re = Regex::new(r"\d{2}:\d{2}\s\w{2}").unwrap();
    let result: Vec<&str> = re.find_iter(TEXTO_BASE).map(|m| m.as_str()).collect();
    println!("{:?}", result);
}
