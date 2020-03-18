# Louis Burns
# GISC 6317 GIS Programming
# Fall 2014 Final Project
# Program to find custom walkability

import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

env.workspace = r"C:\usr\Burns\FinalProject\DFWAmenities.gdb"
env.scratchWorkspace = r"C:\usr\Burns\FinalProject\DFWAmenities.gdb"

# Instructions to user
print "Please rank the following amenities on a scale 1-10 with 10 being most important.\r"
print "The 12 amenities are bars and pubs, coffee shops, delis and bakeries, gas stations, grocery stores, ice cream shops, parks, pharmacies, restaurants, schools, shopping malls, and water features (lakes, streams or rivers).\r\r"

# Begin ranking loop
happy = "N"
while happy != "Y":
    # Ask user to rank amenities
    rBar = int(raw_input("1. Bars and pubs? "))
    rCoffee = int(raw_input("2. Coffee shops? "))
    rDeli = int(raw_input("3. Delis and bakeries? "))
    rGas = int(raw_input("4. Gas stations? "))
    rGStore = int(raw_input("5. Grocery stores? "))
    rIceCream = int(raw_input("6. Ice cream shops? "))
    rPark = int(raw_input("7. Parks? "))
    rPharm = int(raw_input("8. Pharmacies? "))
    rRestaurant = int(raw_input("9. Restaurants? "))
    rSchool = int(raw_input("10. Schools? "))
    rShopping = int(raw_input("11. Shopping malls? "))
    rWater = int(raw_input("12. Water features (lakes, streams or rivers)? "))

    # Review selection
    print "You ranked the amenities as follows:"
    print "1. Bars and pubs " + str(rBar)
    print "2. Coffee shops " + str(rCoffee)
    print "3. Delis and bakeries " + str(rDeli)
    print "4. Gas stations " + str(rGas)
    print "5. Grocery stores " + str(rGStore)
    print "6. Ice cream shops " + str(rIceCream)
    print "7. Parks " + str(rPark)
    print "8. Pharmacies " + str(rPharm)
    print "9. Restaurants " + str(rRestaurant)
    print "10. Schools " + str(rSchool)
    print "11. Shopping malls " + str(rShopping)
    print "12. Water features " + str(rWater)

    # Confirm choices
    happy = raw_input("Are you happy with your selections? (Y/N) ")
    while happy != "Y":
        redo = raw_input("Which amenity would you like to edit? (1-12)")
        if redo == "1":
            rBar = int(raw_input("1. Bars and pubs? "))
        elif redo == "2":
            rCoffee = int(raw_input("2. Coffee shops? "))
        elif redo == "3":
            rDeli = int(raw_input("3. Delis and bakeries? "))
        elif redo == "4":
            rGas = int(raw_input("4. Gas stations? "))
        elif redo == "5":
            rGStore = int(raw_input("5. Grocery stores? "))
        elif redo == "6":
            rIceCream = int(raw_input("6. Ice cream shops? "))
        elif redo == "7":
            rPark = int(raw_input("7. Parks? "))
        elif redo == "8":
            rPharm = int(raw_input("8. Pharmacies? "))
        elif redo == "9":
            rRestaurant = int(raw_input("9. Restaurants? "))
        elif redo == "10":
            rSchool = int(raw_input("10. Schools? "))
        elif redo == "11":
            rShopping = int(raw_input("11. Shopping malls? "))
        elif redo == "12":
            rWater = int(raw_input("12. Water features (lakes, streams or rivers)? "))
        print
        print "You ranked the amenities as follows:"
        print "1. Bars and pubs " + str(rBar)
        print "2. Coffee shops " + str(rCoffee)
        print "3. Delis and bakeries " + str(rDeli)
        print "4. Gas stations " + str(rGas)
        print "5. Grocery stores " + str(rGStore)
        print "6. Ice cream shops " + str(rIceCream)
        print "7. Parks " + str(rPark)
        print "8. Pharmacies " + str(rPharm)
        print "9. Restaurants " + str(rRestaurant)
        print "10. Schools " + str(rSchool)
        print "11. Shopping malls " + str(rShopping)
        print "12. Water features " + str(rWater)
        happy = raw_input("Are you happy with your selections? (Y/N) ")

print
print "Please wait while I update your custom walkability index."

# Update "Index" column in "AllAmenities" layer based on NAICS code
fc = r"C:\usr\Burns\FinalProject\DFWAmenities.gdb\AllAmenities"
cursor = arcpy.UpdateCursor(fc)
row = cursor.next()
while row:
    if row.getValue("NAICS_EXT") in ("72241001", "72241003", "72241004", "72241005", "72241006", "72241007", "72241008"):
        row.setValue("Index", rBar)
    elif row.getValue("NAICS_EXT") == "72251505":
        row.setValue("Index", rCoffee)
    elif row.getValue("NAICS_EXT") in ("72251302", "72251303"):
        row.setValue("Index", rDeli)
    elif row.getValue("NAICS_EXT") in ("44719005", "44719007"):
        row.setValue("Index", rGas)
    elif row.getValue("NAICS_EXT") in ("44511001", "44511002"):
        row.setValue("Index", rGStore)
    elif row.getValue("NAICS_EXT") == "72251512":
        row.setValue("Index", rIceCream)
    elif row.getValue("NAICS_EXT") == "1":
        row.setValue("Index", rPark)
    elif row.getValue("NAICS_EXT") in ("44511003", "44611009"):
        row.setValue("Index", rPharm)
    elif row.getValue("NAICS_EXT") in ("72251110", "72251115", "72251117", "72251118", "72251401", "72251402"):
        row.setValue("Index", rRestaurant)
    elif row.getValue("NAICS_EXT") in ("61111007", "61131009", "62441006"):
        row.setValue("Index", rSchool)
    elif row.getValue("NAICS_EXT") == "2":
        row.setValue("Index", rShopping)
    elif row.getValue("NAICS_EXT") == "3":
        row.setValue("Index", rWater)
    cursor.updateRow(row)
    row = cursor.next()
del row
del cursor

print
print "Please wait while I generate your custom walkability heat map."

# Generate IDW heat map
walkability_heatmap = Idw("AllAmenities.shp", "Index")
##walkability_heatmap.save(r"C:\usr\Burns\FinalProject\walkability_heatmap")
