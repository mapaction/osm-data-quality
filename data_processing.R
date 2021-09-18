library(sf)
library(yaml)
library(tmap)

sf_results <- st_read('results/cameroon_ad1_mapoc.geojson')
params <- read_yaml('country_overview/config.yml')

# Overview map ------------------------------------------------------------

map_overall <- tm_shape(sf_results) +
  tm_fill('report.result.value', 
              palette = "BuGn",
              style='pretty',
              title="Confidence Index")+
  tm_layout(frame = FALSE)
