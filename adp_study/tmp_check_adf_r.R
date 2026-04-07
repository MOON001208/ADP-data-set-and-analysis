library(tseries)
d <- read.csv("adp_study/data/timeseries_stationarity_daily.csv")
d$date <- as.Date(d$date)
d <- d[order(d$date), ]
x <- ts(d$value, frequency = 7)
cat("R raw ADF\n")
print(adf.test(x))
cat("R diff ADF\n")
print(adf.test(diff(x)))
