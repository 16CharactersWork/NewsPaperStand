#!/bin/bash

version="0.0.1"
old_ifs="${IFS}"
cache_dir="${HOME}/.cache/news-cli"
dependencies=("ls" "cat" "curl" "sed" "awk" "tr" "du" "rm" "mkdir" "git" "diff" "patch" "zathura" "pup")
github_source="https://raw.githubusercontent.com/16CharactersWork/master/newsp-cli"



    echo What newspaper are you looking for?
    read newspaper_input



#Replace spaces with pluses
newspaper_input="$(printf "%s" "${newspaper}" | tr " " "+")"

echo "Please select a news paper"  

#The one command I can get to find everything 
scapemg=$(curl -s "https://mgreader.com/?cat=231&s=${newspaper}" | 
pup "header h2 a" | 
cut -d '"' -f2 | 
pup 'text{}'
)




found_link=$(curl -s 'https://mgreader.com/the-new-york-times-25-august-2022.html' | 
pup 'a[target="_blank"]' | 
cut -d '"' -f4 |
grep 'https:*'
)





