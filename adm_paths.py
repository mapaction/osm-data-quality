import geopandas as gpd
from pathlib import Path
import os

BASE_PATH = Path("G:/Shared drives/prepared-country-data/")
ADM_PATH = Path("GIS/2_Active_Data/202_admn/")
ADM = "ad1"
COUNTRIES = [
    "bangladesh",
    "cameroon",
    "dominica",
    "dominican-republic",
    "fiji",
    "guatemala",
    "honduras",
    "indonesia",
    "iraq",
    "kenya",
]

if __name__ == "__main__":

    # Transform all country shapefiles from the CMF to geojson
    # TODO: In some cases having invalid geometry problems with the output geojsons...
    for country in COUNTRIES:
        path = BASE_PATH / country / ADM_PATH
        for f in os.listdir(path):
            if ADM in f and "py" in f and f.endswith(".shp"):
                shp_file = gpd.read_file(path / f)
                shp_file.to_file(
                    f"adm_geojson/{country}_{ADM}.geojson", driver="GeoJSON"
                )

