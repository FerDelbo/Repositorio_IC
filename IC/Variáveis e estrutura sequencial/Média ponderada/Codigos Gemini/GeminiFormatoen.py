echo "Enter the first note:"
read note1
echo "Enter the second note:"
read note2
echo "Enter the third note:"
read note3
echo "Enter the fourth note:"
read note4
weighted_avg=`echo "scale=1; ($note1 * 1 + $note2 * 2 + $note3 * 3 + $note4 * 4) / 10" | bc`
echo "Weighted average: $weighted_avg"
