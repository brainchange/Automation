nm=""
eml=""
pswd=""
plink=""
cno=""
cmo=""
cy=""
cv=""
current=""
f=$(mktemp XXXXXXXXXX.html)
echo "---name---|------email------|---password---|----profile--link-----|-------ccno-------|--ccmo--|--ccy--|-cvv-|----------current--courses-------|"
INPUT=udemy_acc2.csv
OLDIFS=$IFS
IFS=";"
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
i=1
while read name email password profile ccno ccmo ccy cvv courses
do
	echo "[$i]|$name|$email|$password|$profile|$ccno|$ccmo|$ccy|$cvv|$courses|"
	i=$((i+1))
done < $INPUT
IFS=$OLDIFS
read -p "Choose Account: " x
i=1
INPUT=udemy_acc2.csv
OLDIFS=$IFS
IFS=";"
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read name email password profile ccno ccmo ccy cvv courses
do
	if [ "$i" = "$x" ]; then
		nm=$name
		eml=$email
		pswd=$password
		plink=$profile
		cno=$ccno
		cmo=$ccmo
		cy=$ccy
		cv=$cvv
		current=$courses
		break
	fi
	i=$((i+1))
done < $INPUT
IFS=$OLDIFS
read -p "How many courses to choose from main links and extra links? (example: 2 1) " a b
IFS=";" read -a ADDR < udemy_main.csv
IFS=";" read -a ADDR1 < udemy_extra.csv
IFS=',' read -ra ADDR2 <<< "$current"
curno=${#ADDR2[@]}
curno=$((curno-1))
count=1
A=()
while [ "$count" -le $a ]      # Generate 10 ($MAXCOUNT = $a) random integers.
do
  number=$RANDOM
  let "number %= ${#ADDR[@]}"
  initial=0
  final=0
  for i in `seq 0 $curno`;
        do
                if [[ "${ADDR[$number]}" = "${ADDR2[$i]}" ]]; then
			echo "$nm is already enrolled in ${ADDR[$number]} trying other course!! "
			initial=1
			break
		fi
        done
  if [ "$initial" = "$final" ]; then
  	A+=(${ADDR[$number]})
  	let "count += 1"  # Increment count.
  fi
done
count=1
B=()
while [ "$count" -le $b ]      # Generate 10 ($MAXCOUNT =$b) random integers.
do
  number=$RANDOM
  let "number %= ${#ADDR1[@]}"
  initial=0
  final=0
  for i in `seq 0 $curno`;
        do
                if [[ "${ADDR1[$number]}" = "${ADDR2[$i]}" ]]; then
			echo "$nm is already enrolled in ${ADDR1[$number]} trying other course!! "
			initial=1
			break
		fi
        done
  if [ "$initial" = "$final" ]; then
  	B+=(${ADDR1[$number]})
  	let "count += 1"  # Increment count.
  fi
done
echo "<!DOCTYPE html>" >> $f
echo "<html>" >> $f
echo "   <body>" >> $f
echo "      <h1>Name: $nm <br>Email: $eml <br>Password: $pswd<br>Profile Link: href=$plink>$plink <br>CC No. : $cno <br>CC Expiry date: $cmo/$cy <br>CVV: $cv</h1>" >> $f
echo "      <h1><br> MAIN LINKS <br></h1>" >> $f
x=${#A[@]}
no=$((x-1))
for i in `seq 0 $no`;
        do
                echo "     <a href=${A[$i]}>${A[$i]}<br></a> " >> $f
        done
x=${#B[@]}
no=$((x-1))
echo "      <h1><br> EXTRA LINKS<br></h1>" >> $f
for i in `seq 0 $no`;
        do
                echo "     <a href=${B[$i]}>${B[$i]}<br></a> " >> $f
        done
echo "   </body>" >> $f
echo "</html>" >> $f
google-chrome --no-sandbox /home/Automation/$f
