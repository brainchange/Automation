INPUT=Acc_Info1.csv
OLDIFS=$IFS
IFS=","
nm=""
eml=""
pswd=""
cno=""
cmo=""
cy=""
cv="" 
echo "---name---|------email------|---password---|-------ccno-------|--ccmo--|--ccy--|-cvv-|"
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
i=1
while read name email password ccno ccmo ccy cvv
do
	echo "[$i]|$name|$email|$password|$ccno|$ccmo|$ccy|$cvv|"
	i=$((i+1))
done < $INPUT
IFS=$OLDIFS
read -p "Choose Account: " x
i=1
INPUT=Acc_Info1.csv
OLDIFS=$IFS
IFS=","
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read name email password ccno ccmo ccy cvv
do
	if [ "$i" = "$x" ]; then
		nm=$name
		eml=$email
		pswd=$password
		cno=$ccno
		cmo=$ccmo
		cy=$ccy
		cv=$cvv
		break
	fi
	i=$((i+1))
done < $INPUT
IFS=$OLDIFS
read -p "How many courses to choose from main link, main2 and extra links? (example: 2 1 3) " a b c
IFS=";" read -a ADDR < main_links.csv
IFS=";" read -a ADDR1 < main_links2.csv
IFS=";" read -a ADDR2 < extra_links.csv
count=1
A=()
while [ "$count" -le $a ]      # Generate 10 ($MAXCOUNT) random integers.
do
  number=$RANDOM
  let "number %= ${#ADDR[@]}"
  A+=(${ADDR[$number]})
  let "count += 1"  # Increment count.
done
count=1
B=()
while [ "$count" -le $b ]      # Generate 10 ($MAXCOUNT) random integers.
do
  number=$RANDOM
  let "number %= ${#ADDR1[@]}"
  B+=(${ADDR1[$number]})
  let "count += 1"  # Increment count.
done
count=1
C=()
while [ "$count" -le $c ]      # Generate 10 ($MAXCOUNT) random integers.
do
  number=$RANDOM
  let "number %= ${#ADDR2[@]}"
  C+=(${ADDR2[$number]})
  let "count += 1"  # Increment count.
done
echo "<!DOCTYPE html>" >> output_bash.html
echo "<html>\n" >> output_bash.html
echo "   <body>" >> output_bash.html
echo "      <h1>Name: $nm Email: $eml Password: $pswd<br>CC No. : $cno CC Expiry date: $cmo/$cy CVV: $cv</h1>" >> output_bash.html
echo "      <h1><br> MAIN LINKS <br></h1>" >> output_bash.html
x=${#A[@]}
no=$((x-1))
for i in `seq 0 $no`;
        do
                echo "     <a href=${A[$i]}>${A[$i]}<br></a> " >> output_bash.html
        done
x=${#B[@]}
no=$((x-1))
for i in `seq 0 $no`;
        do
                echo "     <a href=${B[$i]}>${B[$i]}<br></a> " >> output_bash.html
        done
x=${#C[@]}
no=$((x-1))
for i in `seq 0 $no`;
        do
                echo "     <a href=${C[$i]}>${C[$i]}<br></a> " >> output_bash.html
        done
echo "   </body>" >> output_bash.html
echo "</html>" >> output_bash.html
