# Convert GEBCO bathymetry data (NetCDF file) in to XYZ data (ASCII Text)
# Python Module required  - netCDF4
# Input - Give your GEBCO NetCDF file (.nc) location in user input section
# Output - This script return/generate a ASCII text file contains XYZ format (Longitude,Latitude,Elevation)
# Note - Verify the variable names in the NetCDF file using any other tools like Panoply (windows),ncdump(Ubuntu) 
# Here giving 'lat' for Latitude 'lon' for longitude 'elevation' for depth/elevation 
# Variable names are case-sensitive 

from netCDF4 import Dataset
import csv

#----User Input
fn = r"C:\Users\name\Downloads\GEBCO_03_Jun_2022_75746fdc53f3\gebco_2021_n10.0_s8.0_w75.0_e77.0.nc" #Location of GEBCO bathymetry .nc file
opfn='GEBCO_xyz.txt' #Output file name
#----End of user input

ds = Dataset(fn, mode='r')
lat = ds['lat'][:] # variable name for Latitude (Case sensitive)
lon = ds['lon'][:] # variable name for Longitude (Case sensitive)
ele = ds['elevation'][:] # variable name for Elevation (Case sensitive)

with open(opfn, 'w', newline='') as file:
    writer = csv.writer(file,delimiter ='\t')
    writer.writerow(["Lat", "Lon","Elevation"])
    for i in range(len(lat)):
        for j in range(len(lon)):
            writer.writerow([lat[i], lon[j],ele[i][j]])
