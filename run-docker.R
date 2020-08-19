# Setup -------------------------------------------------------------------
pkgload::load_all(export_all = FALSE, helpers = FALSE)
with_dir <- withr::with_dir
app <- c("apache", "airflowdocker", "Shawe82", "puckel", "udemy")[5]
source_path <- file.path(getwd(), app)

# Run Docker --------------------------------------------------------------
docker$kill_all_containers()
docker$remove_dangling_images()
with_dir(source_path, DockerCompose$new()$stop())
with_dir(source_path, DockerCompose$new()$start())

# Open UI -----------------------------------------------------------------
cat('Opening browser in ')
for(i in 7:1) {cat(i, '...', sep=''); Sys.sleep(1)}
with_dir(source_path, DockerCompose$new()$browse_url("webserver"))
