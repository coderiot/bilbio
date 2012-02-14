args <- commandArgs(TRUE)

library(ggplot2)

scaling <- function(data) {
	agg = aggregate(data$Frequency, by=list(Year=data$Year), FUN=sum)
	for(i in unique(data$Year)) {
		data[which(data$Year == i),]$Frequency = subset(data, data$Year == i)$Frequency /subset(agg, agg$Year == i)$x
	}
	return(data)
}

if (args[1] == "csmath") {
	mydata <- read.table('csmath', header=T)
	data <- scaling(mydata)
	levs <- levels(data$Subject)
	data$Subject <- factor(data$Subject, levels = c(levs[3], levs[1], levs[2]))
} else if (args[1] == "csph") {
	mydata <- read.table('csph', header=T)
	data <- scaling(mydata)
	levs <- levels(data$Subject)
	data$Subject <- factor(data$Subject, levels = c(levs[3], levs[1], levs[2]))
} else if (args[1] == "combcs") {
	mydata <- read.table('combcs', header=T)
	data <- scaling(mydata)
	levs <- levels(data$Subject)
	data$Subject <- factor(data$Subject, levels = c(levs[1], levs[2], levs[3]))
}
png(paste(args[1],"scaled.png", sep=""), 1280, 800, res=110)
ggplot(data, aes(Year,Frequency,colour = Subject)) +  geom_area(aes(colour = Subject, fill= Subject), alpha=1, position = 'identity') + opts(panel.background = theme_rect(fill = 'white'))+ opts(legend.position = "bottom") +  scale_x_continuous(breaks=unique(data$Year))

dev.off()
