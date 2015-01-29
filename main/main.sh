#/bin/sh

echo 'Creating IDF files...'
python ./../combinations/combinatorics.py
echo 'DONE'

echo 'Running energy models. This may take a while...'

idfs=(./idfs/[0-9]*.idf)

for ((i=0; i<${#idfs[@]}; i++))
do
	runenergyplus ${idfs[$i]} USA_NY_New.York-J.F.Kennedy.Intl.AP.744860_TMY3.epw &
done

echo 'DONE'
