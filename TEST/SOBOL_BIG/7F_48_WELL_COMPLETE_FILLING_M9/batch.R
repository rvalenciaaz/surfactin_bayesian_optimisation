# Load necessary libraries
library(data.table)
library(pmp)
library(tidyr)



# Load your metabolomic data
# Replace 'path_to_your_data.csv' with the path to your data file
iteration <- "0"
data <- fread(paste("baseline_corrected/",iteration,"_baseline_corrected.csv",sep=""))

original_order <- fread(paste("ms_run_tables/",iteration,"_ms_table.csv",sep=""))


matrix_df <- pivot_wider(data, names_from = compound, values_from = integral)

df_filtered <- matrix_df[!grepl("Blank|Solvent", matrix_df$file), ]

#sample_order <- 
batch <- substr(df_filtered$file, 1, 1)
class <- ifelse(grepl("QC", df_filtered$file), "QC", "Sample")


corrected_data <- QCRSC(df=data, order=sample_order, batch=batch, 
                        classes=class, spar=0, minQC=4)

plots <- sbc_plot (df=data, corrected_df=corrected_data, classes=class, 
                   batch=batch, output=NULL, indexes=c(1, 5, 30))

data_normalised <- pqn_normalisation(df=corrected_data,classes=classes, qc_label="QC")
# Preprocessing
# Implement any preprocessing steps here (e.g., filtering, missing value imputation)

# Batch Correction
# Apply batch correction methods here. 
# Example: data_corrected <- removeBatchEffect(data, batch = data$batch)

# Quality Control
# Implement quality control steps here (e.g., QC-RSC)

# Normalization
# Apply normalization methods here.
# Example: data_normalized <- normalize(data_corrected, method = 'quantile')

# Post-processing and Analysis
# Perform further analysis as needed (e.g., statistical testing, clustering, PCA)

# Save or output the processed data
write.csv(data_normalised, paste("batch_correction/",iteration,"_batch_corrected.csv",sep=""))
