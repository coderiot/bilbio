set terminal png enhanced font  "Helvitica, 14" size 600,400
set output 'pieSubplot.png'
set style data histogram
set title 'Verteilung der Themenanzahl bei den restlichen 1.8%'
set xlabel 'Anzahl Themen'
set ylabel 'Häufigkeit'
set style fill solid 0.75 border -1
# set xtics rotate by -45
set noborder
unset key
set ytics out nomirror
set xtics out nomirror
set xtics font "Helvitica, 10"
plot '../results/freqSubjectRules.dat' using 2:xticlabels(1) lc rgb '#1161d9' notitle with boxes
