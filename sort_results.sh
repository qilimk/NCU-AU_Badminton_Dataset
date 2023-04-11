#mkdir badminton_dataset_tw
 
#for f in `ls -d *results`;
#do 
#	echo $f;
#	mv ${f}/* badminton_dataset_tw; 
#done

idx=00;
for f in `cat action_labels.txt`;
do 
	t=`printf "%02d\n" $idx`;
	echo $t $f;
	((idx++));
	mkdir ${t}_${f}; 
	mv badminton_dataset_tw/*_${t}.mp4 ${t}_${f}/;
done

