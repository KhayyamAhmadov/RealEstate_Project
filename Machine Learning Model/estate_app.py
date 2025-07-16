import streamlit as st
import pandas as pd
import numpy as np
import joblib
import folium
from streamlit_folium import st_folium
from math import radians, cos, sin, asin, sqrt
import os

# Page config
st.set_page_config(
    page_title="Baku Emlak Qiymət Təxmini", 
    page_icon="🏠",
    layout="wide"
)

# Load model
@st.cache_resource
def load_model():
    try:
        return joblib.load('baku_emlak_model.pkl')

    except:
        st.error("Model faylı tapılmadı! Zəhmət olmasa baku_emlak_model.pkl faylını yükləyin.")
        return None

# @st.cache_resource
# def load_model():
#     try:
#         current_dir = os.path.dirname(os.path.abspath(__file__))
#         model_path = os.path.join(current_dir, 'baku_emlak_model.pkl')
        
#         st.write(f"Model path: {model_path}")
#         model = joblib.load(model_path)
#         return model
#     except Exception as e:
#         st.error(f"Model faylı tapılmadı! Xəta: {str(e)}")
#         return None


# Coordinates data
METRO_STATIONS = {
    '20 Yanvar': {'lat': 40.4035, 'lon': 49.8295},
    '28 May': {'lat': 40.3777, 'lon': 49.8504},
    '8 Noyabr': {'lat': 40.4048, 'lon': 49.8425},
    'Avtovağzal': {'lat': 40.4134, 'lon': 49.8020},
    'Azadlıq Prospekti': {'lat': 40.4191, 'lon': 49.8316},
    'Bakmil': {'lat': 40.4113, 'lon': 49.8827},
    'Dərnəgül': {'lat': 40.4216, 'lon': 49.8234},
    'Elmlər Akademiyası': {'lat': 40.3742, 'lon': 49.8299},
    'Əhmədli': {'lat': 40.3883, 'lon': 49.9383},
    'Gənclik': {'lat': 40.3973, 'lon': 49.8676},
    'Həzi Aslanov': {'lat': 40.3925, 'lon': 49.9530},
    'İçərişəhər': {'lat': 40.3662, 'lon': 49.8351},
    'İnşaatçılar': {'lat': 40.3786, 'lon': 49.8199},
    'Koroğlu': {'lat': 40.4114, 'lon': 49.9360},
    'Memar Əcəmi': {'lat': 40.3976, 'lon': 49.8232},
    'Nəriman Nərimanov': {'lat': 40.4009, 'lon': 49.8798},
    'Nəsimi': {'lat': 40.3856, 'lon': 49.8615},
    'Neftçilər': {'lat': 40.4071, 'lon': 49.9654},
    'Nizami': {'lat': 40.3787, 'lon': 49.8417},
    'Qara Qarayev': {'lat': 40.4031, 'lon': 49.9498},
    'Sahil': {'lat': 40.3722, 'lon': 49.8414},
    'Xətai': {'lat': 40.3847, 'lon': 49.8945},
    'Xalqlar Dostluğu': {'lat': 40.3955, 'lon': 49.9452},
    'Xocəsən': {'lat': 40.4365, 'lon': 49.7726},
    'Ulduz': {'lat': 40.4137, 'lon': 49.9070},
    'Cəfər Cabbarlı': {'lat': 40.3775, 'lon': 49.8497}
}

DISTRICTS = {
    'Yasamal': {'lat': 40.3836, 'lon': 49.8289, 'premium': 1.3},
    'Nərimanov': {'lat': 40.4076, 'lon': 49.8675, 'premium': 1.4},
    'Nəsimi': {'lat': 40.3860, 'lon': 49.8405, 'premium': 1.5},
    'Sabunçu': {'lat': 40.4489, 'lon': 49.9496, 'premium': 0.9},
    'Suraxanı': {'lat': 40.3965, 'lon': 50.0047, 'premium': 0.8},
    'Xətai': {'lat': 40.3779, 'lon': 49.9050, 'premium': 1.2},
    'Səbail': {'lat': 40.3599, 'lon': 49.8325, 'premium': 1.7},
    'Binəqədi': {'lat': 40.4255, 'lon': 49.8152, 'premium': 1.0},
    'Qaradağ': {'lat': 40.3213, 'lon': 49.7245, 'premium': 0.7},
    'Xəzər': {'lat': 40.3765, 'lon': 50.0456, 'premium': 0.8},
    'Pirallahı': {'lat': 40.5083, 'lon': 50.2923, 'premium': 0.6}
}

VIP_LOCATIONS = {
    'İçərişəhər': {'lat': 40.366499, 'lon': 49.834388},           
    'Tarqovı (Nizami küç.)': {'lat': 40.376793, 'lon': 49.841630}, 
    'Flame Towers ətrafı': {'lat': 40.359795, 'lon': 49.828002},   
    'Neftçilər prospekti': {'lat': 40.368870, 'lon': 49.846514},   
    'White City (Ağ Şəhər)': {'lat': 40.371014, 'lon': 49.876761}, 
    'Port Baku': {'lat': 40.373292, 'lon': 49.860967},            
    'Şüvəlan': {'lat': 40.481950, 'lon': 50.123390},             
    'Bilgəh': {'lat': 40.574765, 'lon': 50.006822},               
    'Nardaran': {'lat': 40.573932, 'lon': 50.035234},            
    'Buzovna': {'lat': 40.511924, 'lon': 50.136145},            
    'Badamdar (yuxarı)': {'lat': 40.351998, 'lon': 49.829225},
    'Təzə Pir': {'lat': 40.370770, 'lon': 49.836145},             
    'Elmlər Akademiyası': {'lat': 40.378536, 'lon': 49.829172},   
    'Hyatt Regency': {'lat': 40.391261, 'lon': 49.827713},
    'Botanika bağı': {'lat': 40.370050, 'lon': 49.831530}
}

CITY_CENTER = {'lat': 40.3630, 'lon': 49.8338}

# Helper functions
def calculate_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    return 6371 * c * 1000

def find_closest_metro(lat, lon):
    min_dist = float('inf')
    closest_metro = None
    for metro_name, coords in METRO_STATIONS.items():
        dist = calculate_distance(lat, lon, coords['lat'], coords['lon'])
        if dist < min_dist:
            min_dist = dist
            closest_metro = metro_name
    return min_dist, closest_metro

def find_closest_district(lat, lon):
    min_dist = float('inf')
    district_premium = 1.0
    closest_district = None
    for district_name, coords in DISTRICTS.items():
        dist = calculate_distance(lat, lon, coords['lat'], coords['lon'])
        if dist < min_dist:
            min_dist = dist
            district_premium = coords['premium']
            closest_district = district_name
    return district_premium, min_dist, closest_district

def find_closest_vip_location(lat, lon, max_distance=5000):
    min_dist = float('inf')
    for vip_name, coords in VIP_LOCATIONS.items():
        dist = calculate_distance(lat, lon, coords['lat'], coords['lon'])
        if dist < min_dist:
            min_dist = dist
    return min_dist if min_dist <= max_distance else 6000

def create_features(area, rooms, floor, lat, lon, is_new, has_title, is_repaired):
    features = {}
    features['area'] = area
    features['rooms'] = rooms
    features['floor'] = floor
    features['lat'] = lat
    features['lon'] = lon
    features['is_new'] = int(is_new)
    features['has_title'] = int(has_title)
    features['is_repaired'] = int(is_repaired)
    features['area_per_room'] = area / rooms
    features['room_area_ratio'] = rooms / area
    features['floor_area_score'] = floor * np.log1p(area)
    features['room_efficiency'] = area / (rooms + 1)

    metro_distance, closest_metro = find_closest_metro(lat, lon)
    features['metro_distance'] = metro_distance
    features['closest_metro'] = closest_metro

    district_premium, district_distance, closest_district = find_closest_district(lat, lon)
    features['district_premium'] = district_premium
    features['district_distance'] = district_distance
    features['vip_distance'] = find_closest_vip_location(lat, lon)
    features['center_distance'] = calculate_distance(lat, lon, CITY_CENTER['lat'], CITY_CENTER['lon'])
    
    # Boolean location features
    features['is_near_metro'] = int(metro_distance < 800)
    features['is_central'] = int(features['center_distance'] < 4000)
    features['is_premium_area'] = int(district_premium > 1.3)
    features['is_vip_close'] = int(features['vip_distance'] < 1500)
    features['is_vip_super'] = int(features['vip_distance'] < 500)
    
    # Floor features
    features['is_good_floor'] = int((floor >= 2) & (floor <= 10))
    features['is_middle_floor'] = int((floor >= 3) & (floor <= 7))
    features['is_high_floor'] = int(floor >= 10)
    features['is_penthouse'] = int(floor >= 15)
    features['floor_ratio'] = floor / (floor + 10)
    
    # Area features
    features['is_optimal_area'] = int((area >= 60) & (area <= 120))
    features['area_efficiency'] = area / (rooms * 15)
    features['room_size_score'] = np.clip(features['area_per_room'] / 25, 0, 2)
    
    # Categorical features
    if features['area_per_room'] <= 20:
        features['room_size_type'] = 0
    elif features['area_per_room'] <= 30:
        features['room_size_type'] = 1
    else:
        features['room_size_type'] = 2
    
    if floor <= 1:
        features['floor_group'] = 0
    elif floor <= 3:
        features['floor_group'] = 1
    elif floor <= 10:
        features['floor_group'] = 2
    else:
        features['floor_group'] = 3
    
    # Combination features
    features['gold_combo'] = features['is_new'] * features['is_premium_area'] * features['is_near_metro']
    features['platinum_combo'] = features['is_vip_super'] * features['is_new'] * features['has_title']
    features['premium_central'] = features['is_premium_area'] * features['is_central']
    
    # Scores
    features['luxury_score'] = (features['is_new'] * 3 + features['is_vip_close'] * 2 + 
                               features['is_premium_area'] * 2 + features['has_title'] * 1 + 
                               features['is_middle_floor'] * 1)
    
    features['infrastructure_score'] = (1 / (metro_distance + 100) * 0.5 + 
                                       1 / (features['vip_distance'] + 100) * 0.3 + 
                                       1 / (features['center_distance'] + 100) * 0.2)
    
    features['accessibility_score'] = (features['is_near_metro'] * 3 + features['is_central'] * 2 + 
                                      features['is_vip_close'] * 2)
    
    # Location premium
    metro_factor = max(0, 1 - metro_distance / 1500)
    vip_factor = max(0, 1 - features['vip_distance'] / 2000)
    center_factor = max(0, 1 - features['center_distance'] / 8000)
    features['location_premium'] = (metro_factor * 0.4 + vip_factor * 0.3 + 
                                   center_factor * 0.2 + (district_premium - 1) * 0.1)
    
    # Polynomial features
    features['area_squared'] = area ** 2
    
    return features

def create_map(lat=40.3630, lon=49.8338):
    m = folium.Map(location=[lat, lon], zoom_start=11)
    
    for name, coords in METRO_STATIONS.items():
        folium.Marker(
            [coords['lat'], coords['lon']],
            popup=f"Metro: {name}",
            icon=folium.Icon(color='blue', icon='train', prefix='fa')
        ).add_to(m)
    
    for name, coords in VIP_LOCATIONS.items():
        folium.Marker(
            [coords['lat'], coords['lon']],
            popup=f"VIP: {name}",
            icon=folium.Icon(color='red', icon='star', prefix='fa')
        ).add_to(m)
    
    return m

# Main app
def main():
    st.title("🏠 Baku Emlak Qiymət Təxmini")
    model_package = load_model()
    if model_package is None:
        return
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📍 Əmlakın Yeri")
        map_data = st_folium(create_map(), width=700, height=400)
        if map_data['last_clicked']:
            selected_lat = map_data['last_clicked']['lat']
            selected_lon = map_data['last_clicked']['lng']
        else:
            selected_lat = 40.3630
            selected_lon = 49.8338
        
        coord_col1, coord_col2 = st.columns(2)
        with coord_col1:
            lat = st.number_input("Enlik (Latitude)", value=selected_lat, format="%.6f")
        with coord_col2:
            lon = st.number_input("Uzunluq (Longitude)", value=selected_lon, format="%.6f")
    
    with col2:
        st.subheader("🏢 Əmlak Məlumatları")
        
        area = st.number_input("Sahə (m²)", min_value=15, max_value=350, value=80)
        rooms = st.selectbox("Otaq sayı", options=[1, 2, 3, 4, 5, 6, 7, 8], index=1)
        floor = st.number_input("Mərtəbə", min_value=1, max_value=35, value=5)
        
        st.subheader("🔧 Əlavə Məlumatlar")
        col_bool1, col_bool2, col_bool3 = st.columns(3)
        
        with col_bool1:
            is_new = st.checkbox("Yeni tikili", value=True)
        with col_bool2:
            has_title = st.checkbox("Kupçası var", value=True)
        with col_bool3:
            is_repaired = st.checkbox("Təmirli", value=True)
    
    if st.button("💰 Qiymət Təxmin Et", type="primary"):
        with st.spinner("Qiymət hesablanır..."):
            features_dict = create_features(area, rooms, floor, lat, lon, is_new, has_title, is_repaired)
            
            selected_features = model_package['selected_features']
            
            feature_vector = []
            for feature in selected_features:
                if feature in features_dict:
                    feature_vector.append(features_dict[feature])
                else:
                    feature_vector.append(0)  
            
            # Make prediction
            prediction = model_package['final_model'].predict([feature_vector])[0]
            
            st.success(f"🎯 Təxmin edilən qiymət: **{prediction:,.0f} AZN**")
            
            # Additional information
            st.subheader("📊 Məkan Məlumatları")
            
            info_col1, info_col2 = st.columns(2)
            
            with info_col1:
                st.metric("En yaxın metro", features_dict['closest_metro'], f"{features_dict['metro_distance']:.0f}m")
                st.metric("Şəhər mərkəzinə məsafə", "", f"{features_dict['center_distance']:.0f}m")

if __name__ == "__main__":
    main()