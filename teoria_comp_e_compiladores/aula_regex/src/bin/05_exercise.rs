use aula_regex::TEXTO_BASE;
use regex::Regex;

fn main() {
    let re = Regex::new(
        r"\b(?:análise|integração)+(?:\s+de|\s+com|\s+para)?(?:\s+[a-z\u0080-\u024F]+)*\b",
    )
    .unwrap();
    let result: Vec<&str> = re.find_iter(TEXTO_BASE).map(|m| m.as_str()).collect();
    println!("{:?}", result);
}
