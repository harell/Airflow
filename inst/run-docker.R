# Setup -------------------------------------------------------------------
pkgload::load_all(export_all = FALSE, helpers = FALSE)

# Run Docker --------------------------------------------------------------
docker$kill_all_containers()
docker$remove_dangling_images()
withr::with_dir(usethis::proj_path("inst"),{
    DockerCompose$new()$stop()
    DockerCompose$new()$start()
})

# Open UI -----------------------------------------------------------------
cat('Opening browser in ')
for(i in 10:1) {cat(i, '...', sep=''); Sys.sleep(1)}
withr::with_dir(
    usethis::proj_path("inst"),
    DockerCompose$new()$browse_url("airflow")
)
