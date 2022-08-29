#!/bin/bash

version="0.0.1"
old_ifs="${IFS}"
cache_dir="${HOME}/.cache/news-cli"
dependencies=("ls" "cat" "curl" "sed" "awk" "tr" "du" "rm" "mkdir" "git" "diff" "patch" "zathura" "pup")
github_source="https://raw.githubusercontent.com/16CharactersWork/master/newsp-cli"

declare -i count=0

echo What newspaper are you looking for?
read newspaper_input


#Replace spaces with pluses
newspaper_input="$(printf "%s" "${newspaper}" | tr " " "+")"

#The one command I can get to find everything 
for each in $(curl -s "https://mgreader.com/?cat=231&s=${newspaper}" | 
pup "header h2 a" | 
cut -d '"' -f2 | 
pup 'text{}' 
); do
  count=$(( count + 1 ))
  select (("${count}) $each"))
done
 
if [ "$count" -eq 0 ]; then
  echo "No newspaper."
fi


#echo "select your choice, and select only the link above the date"
#select choice in printf$scapemg

#found_link=$(curl -s 'https://mgreader.com/the-new-york-times-25-august-2022.html' | 
#pup 'a[target="_blank"]' | 
#cut -d '"' -f4 |
#grep 'https:*'
#)





