#/bin/sh

echo 'Creating IDF files...'
# python ./../combinations/combinatorics.py
echo 'DONE'

echo 'Running energy models. This may take a while...'
idfs=(./idfs/*)

for ((i=0; i<${#idfs[@]}; i++))
do
	echo "energyplus ${idfs[$i]} weatherfile"
done

echo 'DONE'
