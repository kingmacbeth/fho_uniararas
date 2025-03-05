use aula_regex::TEXTO_BASE;
use regex::Regex;

fn main() {
    let re = Regex::new(
        r"\b[A-Z][[:alnum:]\u0080-\u024F.]+(?:\s[A-Z0-9][[:alnum:]\u0080-\u024F.]+),\s(\d{1,4})\b",
    )
    .unwrap();
    let result: Vec<&str> = re.find_iter(TEXTO_BASE).map(|m| m.as_str()).collect();
    println!("{:?}", result);
}
