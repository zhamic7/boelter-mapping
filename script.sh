x="$(cat nodes.txt | tail -18)"
printf "$x"
for i in $(seq 6 -1 1)
do
	y="$(echo -e "$x" | tr 76 $((i))$((i-1)))"
	echo -e "$y" >> nodes.txt
	echo -e "$y"
	echo $i
done
