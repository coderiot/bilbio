set terminal png enhanced font  "Helvitica, 14" size 600,400 
set output 'setSpecFreq.png'
set style data histogram
set title 'Häufigkeit der Physikthemen im arxiv.org Datensatz'
set xlabel 'Themen' 
set ylabel 'Häufigkeit'
set style fill solid 0.75 border -1  
set xtics rotate by -45
set noborder
unset key
set ytics out nomirror 
set xtics out nomirror 
set xtics font "Helvitica, 10"
plot '../results/SetSpecFreqPhysics.dat' using 2:xticlabels(1) lc rgb '#1161d9' notitle with boxes
