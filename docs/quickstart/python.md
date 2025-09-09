---
title: Streaming Data in the Cloud with GDAL, VSI, and STAC
tags: [cloud, streaming, GDAL, VSI, STAC, collaboration]
---

# Streaming Data in the Cloud with GDAL, VSI, and STAC

Today’s theme is **Creative Data Exploration in the Cloud**. We’ll learn how to stream data into our CyVerse instance, define key concepts (GDAL, VSI, STAC), and practice opening cloud-hosted datasets directly without downloading them.

---

## 1. Startup Procedure: Opening the Lab

We’ll use the [OASIS QuickStart: Cloud Triangle](https://cu-esiil.github.io/home/quickstart/cloud/) to start our **CyVerse instance**.

- Log in to JupyterHub through CyVerse.  
- Confirm the **triangle environment** is running.  
- Open a terminal and check that `gocmd` is ready:

```bash
gocmd --help
```

If this works, your persistent storage connection is set up.

**Checkpoint:** You now have a shared cloud lab ready to use.

---

## 2. Collaboration: GitHub Workflow

We’ll use GitHub to work collaboratively. As last week:

### Preferred Method: GitHub Widget
- Open the **GitHub tab** in JupyterLab (left sidebar).  
- Log in with your GitHub account if prompted.  
- Navigate to your repository.  
- Edit a `.md` file, save, and use the widget buttons to **Pull → Commit → Push**.  
- Confirm the edit appears on GitHub in your browser.

### Alternative Method: Command Line
```bash
git pull origin main
# edit your file in JupyterLab, then save
git add file.md
git commit -m "edit example"
git push origin main
```

**Checkpoint:** Everyone has successfully pushed an edit to GitHub.

---

## 3. Key Concepts: GDAL, VSI, and STAC

### GDAL
- **Geospatial Data Abstraction Library**.  
- Reads/writes geospatial data (raster and vector).  
- Used widely in Python (`from osgeo import gdal`).

### VSI (Virtual File System)
- A GDAL feature that lets you open remote files as if they were local.  
- Examples:  
  - `/vsicurl/` → stream from HTTP/HTTPS  
  - `/vsis3/` → stream from Amazon S3 buckets  
  - `/vsizip/` → read inside zipped archives without extracting  

### STAC (SpatioTemporal Asset Catalog)
- A standard API for discovering and describing geospatial data.  
- Used by catalogs like [Planetary Computer](https://planetarycomputer.microsoft.com/).  
- Metadata describes spatial extent, time, and available assets.  
- Tools: `pystac-client`, `planetary_computer`.

---

## 4. Example: Streaming with GDAL + VSI

```python
from osgeo import gdal

# Example: Landsat band 4 hosted on AWS
url = "/vsicurl/https://landsat-pds.s3.amazonaws.com/c1/L8/001/002/LC08_L1TP_001002_20200810_20200823_01_T1/LC08_L1TP_001002_20200810_20200823_01_T1_B4.TIF"

# Open remote raster
ds = gdal.Open(url)
print("Raster size:", ds.RasterXSize, ds.RasterYSize, "Bands:", ds.RasterCount)

# Read first band
band = ds.GetRasterBand(1).ReadAsArray()
print("Array shape:", band.shape)
```

---

## 5. Example: Discovering Data with STAC

```python
# pip install pystac-client planetary-computer

from pystac_client import Client
import planetary_computer as pc

# Open Planetary Computer STAC
catalog = Client.open("https://planetarycomputer.microsoft.com/api/stac/v1")

# Search Sentinel-2 over Boulder, CO in July 2021
search = catalog.search(
    collections=["sentinel-2-l2a"],
    bbox=[-105.3, 39.9, -105.1, 40.1],
    datetime="2021-07-01/2021-07-31",
    limit=1,
)

items = list(search.items())
item = items[0]
print("Item ID:", item.id)

# Get signed URL for red band (B04)
asset = item.assets["B04"]
signed_href = pc.sign(asset.href)
print("Signed URL:", signed_href)
```

---

## 6. Example: Combining STAC + VSI

Use the signed STAC URL with GDAL’s `/vsicurl/` to stream directly:

```python
from osgeo import gdal

vsi_url = "/vsicurl/" + signed_href
ds = gdal.Open(vsi_url)

print("Size:", ds.RasterXSize, ds.RasterYSize, "Bands:", ds.RasterCount)
```

---

## 7. Saving Results to the CyVerse Data Store

Use the **CyVerse Data Store** for persistence beyond your session. This mirrors last week’s steps (install → init → transfer).

### 7.1 Install and Initialize `gocmd`

```bash
# Fetch latest release version and install locally
GOCMD_VER=$(curl -L -s https://raw.githubusercontent.com/cyverse/gocommands/main/VERSION.txt); \
curl -L -s https://github.com/cyverse/gocommands/releases/download/${GOCMD_VER}/gocmd-${GOCMD_VER}-linux-amd64.tar.gz | tar zxvf -

# Initialize with your CyVerse credentials
./gocmd init

# Confirm login/profile
./gocmd whoami
```

### 7.2 Transfer files to the Data Store (upload) Initialize `gocmd` for the CyVerse Data Store

```bash
# Initialize and follow prompts (use your CyVerse username/password)
# Common defaults:
#   Host: data.cyverse.org
#   Port: 1247
#   Zone: iplant
# Accept defaults if pre-filled by the image.

gocmd init

# Confirm login/profile
gocmd whoami

# Optional: list your home in the Data Store
gocmd ls i:/
```

### 7.3 Transfer files to the Data Store (upload)

```bash
# Create a folder (first time only)
gocmd mkdir -p i:my_folder

# Upload a file from the current working directory → Data Store
# Example: result from your analysis
gocmd transfer prism_tipping_point.png i:my_folder/prism_tipping_point.png

# Upload multiple files (globs are expanded by the shell)
gocmd transfer *.png i:my_folder/
```

### 7.4 Transfer files from the Data Store (download)

```bash
# Download from Data Store → current directory
gocmd transfer i:my_folder/prism_tipping_point.png .

# Download a whole folder recursively (to a local folder)
mkdir -p downloads
gocmd transfer -r i:my_folder/ downloads/
```

This ensures your results are safe and can be accessed later by you or collaborators.

---

## Key Learning Goals

- Start a CyVerse instance and confirm `gocmd` works.  
- Use the GitHub widget for collaborative editing (CLI as backup).  
- Understand GDAL, VSI, and STAC.  
- Stream remote datasets with GDAL + VSI.  
- Discover and sign assets with STAC.  
- Save outputs to the CyVerse Data Store with `gocmd transfer`.  

---

### Theme Recap

Today we explored **streaming data in the cloud**. By combining GDAL, VSI, and STAC, we can work collaboratively in our CyVerse instance, pull in new data without downloads, and persist our creative explorations in GitHub and the CyVerse Data Store.
