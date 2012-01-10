args <- commandArgs(TRUE)

library(ggplot2)


if (args[1] == "csmath") {
	data <- read.table('csmath', header=T)
	levs <- levels(data$Subject)
	data$Subject <- factor(data$Subject, levels = c(levs[3], levs[1], levs[2]))
} else if (args[1] == "csph") {
	data <- read.table('csph', header=T)
	levs <- levels(data$Subject)
	data$Subject <- factor(data$Subject, levels = c(levs[3], levs[1], levs[2]))
} else if (args[1] == "combcs") {
	data <- read.table('combcs', header=T)
	levs <- levels(data$Subject)
	data$Subject <- factor(data$Subject, levels = c(levs[1], levs[2], levs[3]))
}
png(paste(args[1],".png", sep=""), 1280, 800, res=110)
ggplot(data, aes(Year,Frequency,colour = Subject)) +  geom_area(aes(colour = Subject, fill= Subject), alpha=1, position = 'identity') + opts(panel.background = theme_rect(fill = 'white'))
dev.off()
