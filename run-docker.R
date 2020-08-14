# Setup -------------------------------------------------------------------
pkgload::load_all(export_all = FALSE, helpers = FALSE)
with_dir <- withr::with_dir

# Prepare Files -----------------------------------------------------------
path <- file.path('inst', 'docs', 'airflow-section-4')
source_path <- file.path(getwd(), path)
target_path <- file.path("C:/Docker", basename(path))
unlink(target_path, recursive = TRUE, force = TRUE)
fs::dir_create(target_path)
fs::dir_copy(source_path, target_path, overwrite = TRUE)

# Run Docker --------------------------------------------------------------
with_dir(target_path, DockerCompose$new()$stop())
with_dir(target_path, DockerCompose$new()$start())

# Open UI -----------------------------------------------------------------
cat('Opening browser in ')
for(i in 7:1) {cat(i, '...', sep=''); Sys.sleep(1)}
browseURL("http://localhost:8080") # Airflow
