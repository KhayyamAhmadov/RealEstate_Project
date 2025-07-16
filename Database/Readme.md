# Real Estate Database System (OLTP + DWH)

## 📦 Archive Information
This repository contains a complete Real Estate database system including:
- **OLTP Database**: Operational transaction processing
- **DWH Database**: Data warehouse for analytics

Both databases are archived in RAR parts (25MB each) for GitHub compatibility.

## 🚀 Quick Setup

### Step 1: Clone Repository
```
git clone https://github.com/YOUR_USERNAME/RealEstate_Project.git
cd RealEstate_Project
```

### Step 2: Choose Database Type

#### Option A: Extract OLTP Database (Transactional)
```
cd Database/OLTP
```

#### Option B: Extract DWH Database (Analytics) 
```
cd Database/DWH
```

#### Option C: Extract Both Databases
```
cd Database/OLTP
```
*Extract OLTP first (follow steps below), then:*
```
cd ../DWH
```
*Extract DWH (follow same steps)*

### Step 3: Extract Database Archive

#### For Windows (Recommended):
**For OLTP:**
1. Navigate to: `RealEstate_Project\Database\OLTP\`
2. Double-click on: `RealEstateDB_OLTP.part01.rar`

**For DWH:**
1. Navigate to: `RealEstate_Project\Database\DWH\`
2. Double-click on: `RealEstate_DWH.part1.rar`

*WinRAR will automatically detect and extract all parts*

#### For Linux/Mac:
**Install unrar first:**
```
sudo apt install unrar
```
**Or for Mac:**
```
brew install unrar
```

**Extract OLTP database:**
```
unrar x RealEstateDB_OLTP.part01.rar
```

**Extract DWH database:**
```
unrar x RealEstate_DWH.part1.rar
```

#### Alternative method (7zip):
**Install 7zip:**
```
sudo apt install p7zip-full
```

**Extract OLTP:**
```
7z x RealEstateDB_OLTP.part01.rar
```

**Extract DWH:**
```
7z x RealEstate_DWH.part1.rar
```

### Step 4: Databases Ready
After extraction, your Real Estate database system will be available:
- **OLTP**: Transaction processing data in `Database/OLTP/` directory
- **DWH**: Analytics and reporting data in `Database/DWH/` directory

## 📋 Archive Contents

### OLTP Database
- **Type**: Operational transaction processing
- **Location**: `Database/OLTP/` directory
- **Size**: ~250MB (split into RAR parts)
- **Parts**: RealEstateDB_OLTP.part01.rar → part10.rar

### DWH Database  
- **Type**: Data warehouse for analytics
- **Location**: `Database/DWH/` directory
- **Size**: ~50MB (split into RAR parts)
- **Parts**: RealEstate_DWH.part1.rar, RealEstate_DWH.part2.rar

## 🔧 Troubleshooting

### If extraction fails:

**For OLTP database:**
```
cd Database/OLTP
ls -la RealEstateDB_OLTP.part*.rar
7z x RealEstateDB_OLTP.part01.rar
```

**For DWH database:**
```
cd Database/DWH
ls -la RealEstate_DWH.part*.rar
7z x RealEstate_DWH.part1.rar
```

### For Windows users:
**OLTP:**
1. Navigate to: `RealEstate_Project\Database\OLTP\`
2. Right-click on: `RealEstateDB_OLTP.part01.rar`
3. Select: "Extract Here"

**DWH:**
1. Navigate to: `RealEstate_Project\Database\DWH\`
2. Right-click on: `RealEstate_DWH.part1.rar`
3. Select: "Extract Here"

## 🏢 Database Types Explained

### OLTP (Online Transaction Processing)
- **Purpose**: Daily operations, transactions, real-time data entry
- **Use Cases**: Property listings, customer management, sales transactions
- **Characteristics**: Normalized, fast inserts/updates, concurrent users

### DWH (Data Warehouse)
- **Purpose**: Analytics, reporting, business intelligence
- **Use Cases**: Sales reports, market trends, performance dashboards  
- **Characteristics**: Denormalized, optimized for queries, historical data

## 📊 Database Schema Overview

### OLTP Schema Structure

#### Dynamic Tables (Transactional Data)
- **EstateListing** - Main property listings (price, location, dates)
- **Apartment** - Apartment-specific details (floor, rooms, area)
- **House** - House properties (area, sot, rooms)
- **Office** - Office spaces (area, building type, rooms)
- **CommercialProperty** - Commercial real estate details
- **Garage** - Garage properties
- **Land** - Land plots
- **SellerInfo** - Seller contact and agency information
- **Description** - Property descriptions
- **ListingImages** - Property photos
- **Labels** - Property tags and labels
- **URL** - Listing URLs and sources

#### Static Tables (Reference Data)
- **City** - Cities with coordinates
- **MetroStations** - Metro stations and locations
- **EstateCategory** - Property categories
- **SalesType** - Sale/rent types
- **SellerType** - Individual/agency seller types
- **Settlements** - Neighborhoods and settlements

### DWH Schema Structure

#### STG Layer (Staging)
Raw data ingestion from source systems with minimal transformation

#### CORE Layer (Data Warehouse Core)
- **Dimension Tables** (`dim_*`)
  - `dim_date` - Date dimension with calendar attributes
  - `dim_city` - Geographic locations and regions
  - `dim_category` - Property categories and types
  - `dim_metro_station` - Metro stations with coordinates
  - `dim_price_category` - Price ranges and categories
  - `dim_area_category` - Area size categories
  - `dim_room_category` - Room count categories
  - `dim_sales_type` - Sales and rental types
  - `dim_seller_type` - Seller classifications

- **Fact Tables** (`fact_*`)
  - `fact_estate_listing_basic` - Core listing metrics
  - `fact_property_details` - Property characteristics
  - `fact_listing_content` - Descriptions and seller info
  - `fact_listing_images` - Image metadata
  - `fact_listing_labels` - Property tags
  - `fact_listing_urls` - Source URLs and platforms

#### DM Layer (Data Marts)
Pre-aggregated analytics tables for business reporting:
- `dm_basic_metrics` - General property statistics
- `dm_price_analysis` - Price trends and analysis
- `dm_location_analysis` - Geographic insights
- `dm_baku_metro_analysis` - Metro accessibility analysis
- `dm_seller_analysis` - Seller performance metrics
- `dm_property_features` - Property characteristics analysis
- `dm_content_analysis` - Listing content quality metrics

## 📝 Notes
- Professional enterprise database architecture (OLTP + DWH)
- Industry standard used by major real estate companies
- Each part is under GitHub's 100MB file limit
- RAR format ensures data integrity and compression

## 🆘 Support
If you encounter issues with archive extraction, please open an issue.
