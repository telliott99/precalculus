#! /bin/bash

user="$HOME"
path=$HOME/Github/$1
pdf_path="$1.pdf"

echo $path
echo $pdf_path

# current directory should be Desktop but OK
cd "$user/Desktop"

python3 $user/bin/combine.py $1 > IF.tex

# once to generate .sty, twice for TOC, 3x for ref nums
pdflatex IF.tex >/dev/null
pdflatex IF.tex >/dev/null
pdflatex IF.tex >/dev/null

cp IF.pdf "$user/Dropbox/- stuff/$pdf_path"
mv IF.pdf "$path/$pdf_path"
rm IF.*
sleep 1

osascript -e 'quit app "TeXShop"'

# cleanup random stuff
rm $path/files/*.aux $path/files/*.log 2>/dev/null
rm $path/files/*.out $path/files/*.gz 2>/dev/null
rm $path/files/*.pdf 2>/dev/null
rm stdclsdv.sty 2>/dev/null

open -a Preview "$path/$pdf_path"


