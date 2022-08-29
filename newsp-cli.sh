#!/bin/bash

version="0.0.1"
old_ifs="${IFS}"
cache_dir="${HOME}/.cache/news-cli"
dependencies=("ls" "cat" "curl" "sed" "awk" "tr" "du" "rm" "mkdir" "git" "diff" "patch" "img2pdf" "zathura" "html2text")
github_source="https://raw.githubusercontent.com/16CharactersWork/master/newsp-cli"

#Scraping
re

curl --silent "https://mgreader.com/?cat=231&s=New+York"
