use error_chain::error_chain;
extern crate reqwest;
extern crate select;

use scraper::{Html, Selector};
use select::document::Document;
use select::predicate::{Attr, Class, Name, Predicate};


error_chain! 
{
    foreign_links
    {
        Io(std::io::Error);
        HttpRequest(reqwest::Error);
    }
}

fn main() {
    covid("https://www.worldometers.info/coronavirus/#countries");
}

fn covid(url: &str) {
    let mut resp = reqwest::get(url).await?.text().await?;
    assert!(resp.status().is_success());

    let ducument = Document::from_read(resp).unwrap();

    println!("# Top 10 countries");
    for row in document.find(Class("total_row_world")).take(10) {
        let nation = row.find(Class("mt_a")).map(|tag| tag.text()).collect::<Vec<_>>();
        println!("{}", nation.join("-"))
    }
   
}        