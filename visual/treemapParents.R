library(treemap)
data <- read.table('../results/SetSpecFreqParents.dat')
data <- data.frame(data)

png(filename = "treeParent.png", width = 800, height = 600)

tmPlot(data, index="V1", vSize="V2", title="Verteilung der Themen im arxiv.org Datensatz")

dev.off()
