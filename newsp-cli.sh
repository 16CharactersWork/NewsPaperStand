#!/bin/bash

version="0.0.1"
old_ifs="${IFS}"
cache_dir="${HOME}/.cache/news-cli"
dependencies=("ls" "cat" "curl" "sed" "awk" "tr" "du" "rm" "mkdir" "git" "diff" "patch" "img2pdf" "zathura" "html2text")
github_source="https://raw.githubusercontent.com/16CharactersWork/master/newsp-cli"

#The one command I can get to find everything 
curl "https://mgreader.com/?cat=231&s=New+York+Times" | 
pup "header h2 a" | 
cut -d '"' -f2 | 
pup 'text{}'


#Command to display download  link
curl -s 'https://mgreader.com/the-new-york-times-25-august-2022.html' | 
pup 'a[target="_blank"]' | 
cut -d '"' -f4 |
grep 'https:*'

