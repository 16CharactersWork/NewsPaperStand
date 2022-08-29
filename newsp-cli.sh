#!/bin/bash

version="0.0.1"
old_ifs="${IFS}"
cache_dir="${HOME}/.cache/news-cli"
dependencies=("ls" "cat" "curl" "sed" "awk" "tr" "du" "rm" "mkdir" "git" "diff" "patch" "zathura" "pup")
github_source="https://raw.githubusercontent.com/16CharactersWork/master/newsp-cli"




searching() {

#Replace spaces with pluses
search_query="$(printf "%s" "${}" | tr " " "+")"
  
#The one command I can get to find everything 
scapemg=$(curl "https://mgreader.com/?cat=231&s=${search_query}" | 
pup "header h2 a" | 
cut -d '"' -f2 | 
pup 'text{}'
)
}

#Command to display download  link
found() {
found_link=$(curl -s 'https://mgreader.com/the-new-york-times-25-august-2022.html' | 
pup 'a[target="_blank"]' | 
cut -d '"' -f4 |
grep 'https:*'
)
}

#downloand newspaper to temp cache
downloaded() {

}

search_newspaper() {
    prompt "What news paper?"
    newspaper_input="$(reply)"
}
