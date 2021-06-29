#!/bin/bash

help()
{
cat << EOF
usage: [-o|--outfile OUTFILENAME] [-f|--force] [-h|--help]

Build a PDF from a document written in Pandoc-flavored Markdown and a collection of YAML-formatted style and metadata files.

OPTIONS:
   -o|--outfile     Specify the OUTFILENAME.
   -h|--help        Show this message
EOF
}

while getopts 'o:h' flag; do
  case "${flag}" in
    o) OUTFILE=${OPTARG} ;;
    h) help
       exit 1 ;;
  esac
done

pandoc -s -f markdown+smart --citeproc --bibliography=$PWD/references.bib \
--csl=$PWD/files/chicago-fullnote-bibliography-short-title-subsequent.csl \
--pdf-engine=xelatex --template=$PWD/files/article.latex --highlight-style='kate' \
metadata.yaml thanks.yaml abstract.yaml $PWD/*.md -o $OUTFILE