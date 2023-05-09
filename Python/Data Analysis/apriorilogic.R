options(repos = c(CRAN = "https://cran.rstudio.com/"))

# # Check mlxtend package exist, then install
# if(!require(mlxtend)) install.packages('mlxtend')


# # Load data
df1 <- read.csv('C:/Users/Trieu Pham/OneDrive - BTM Global Consulting/Projects/data csv/dataM1.csv',stringsAsFactors = FALSE)

# # Data preprocessing
df1 <- df1[c('InvoiceID', 'SubCategory Name')]
df1 <- df1[ave(df1$'SubCategory Name', df1$InvoiceID, FUN=length) > 1, ]
dataset_str <- df1
dataset_str <- aggregate(dataset_str['SubCategory Name'], by=list(dataset_str$InvoiceID),FUN=function(x) { paste(x, collapse=",") })
names(dataset_str) <- c('InvoiceID', 'SubCategory Name')
