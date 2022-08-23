import streamlit as st
import pickle
import numpy as np
from PIL import Image

@st.cache()
def load_homepage_image(img):
    image = Image.open(img)

    return image

@st.cache(allow_output_mutation=True)
def load_model(file_name):

    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    
    return model    

def predict(model,x):
    return model.predict(x)

model = load_model("model.p")
homepage_img = load_homepage_image("homepage_img.jpg")

st.title("Guitar Price Prediction")

st.image(homepage_img)

brand_options = ('Charvel', 'Cort', 'Dean', 'ESP LTD', 'Epiphone', 'Fender',
       'Fender Squier', 'Gibson', 'Gretsch', 'Harley Benton', 'Ibanez',
       'Jackson', 'Kramer', 'Music Man', 'PRS', 'Reverend', 'Schecter', 'Sire',
       'Solar', 'Sterling', 'Washburn', 'Yamaha')
brand = st.sidebar.selectbox("Brand",brand_options)

year_options = ('1990s', '2000s', '2010', '2011', '2012', '2013', '2014','2015', '2016', '2017', '2018', '2019', '2020', '2021','2022')
year = st.sidebar.selectbox("Year",year_options)

made_in_options = ('China', 'India', 'Indonesia', 'Japan', 'Mexico', 'South Korea',
       'United States', 'Vietnam')
made_in = st.sidebar.selectbox("Made In",made_in_options)

number_of_strings_options = ('6', '7', '8','9', '12')
number_of_strings = st.sidebar.selectbox("Number of Strings",number_of_strings_options)

body_type_options = ('Hollowbody', 'Semi-Hollow', 'Solid Body')
body_type = st.sidebar.selectbox("Body Type",body_type_options)

body_shape_options = ('Double Cut', 'ES', 'Explorer', 'Firebird', 'Iceman', 'Jaguar',
       'Jazzmaster', 'Les Paul', 'Mustang', 'Offset', 'PRS', 'SG',
       'Single Cut', 'Stratocaster', 'Super Strat', 'Telecaster', 'V')
body_shape = st.sidebar.selectbox("Body Shape",body_shape_options)

body_material_options = ('Agathis', 'Alder', 'Ash', 'Basswood', 'Jabon', 'Limba', 'Mahogany',
       'Maple', 'Meranti', 'Nato', 'Nyatoh', 'Okoume', 'Paulownia', 'Pine',
       'Poplar', 'Sapele', 'Sassafras', 'Spruce', 'Sungkai', 'Terentang')
body_material = st.sidebar.selectbox("Body Material",body_material_options)

neck_joint_options = ('Bolt-On', 'Neck-Through', 'Set')
neck_joint = st.sidebar.selectbox("Neck Joint", neck_joint_options)

neck_material_options = ('Limba', 'Mahogany', 'Maple', 'Nato', 'Nyatoh', 'Okoume', 'Panga Panga','Wenge')
neck_material = st.sidebar.selectbox("Neck Material", neck_material_options)

neck_profile_options = ('Asymmetrical', 'C', 'D', 'GRGR', 'Nitro Baritone', 'SA', 'Soft V to C',
       'Super Wizard', 'U', 'V', 'Vintage', 'Wizard')
neck_profile = st.sidebar.selectbox("Neck Profile",neck_profile_options)

scale_size_options = ('21.5"', '24"', '24.5"', '24.6"', '24.75"', '25"', '25.5"',
       '26.25" to 25.5"', '26.5"', '26.5" to 25.5"', '26.75"', '27"',
       '27" to 25.5"', '27.7"', '28"', '28" to 26"', '28.625"', '29.75"',
       '30"')
scale_size = st.sidebar.selectbox("Scale Size",scale_size_options)

frets_options = ('Jumbo', 'Jumbo Evo Gold', 'Medium', 'Medium Jumbo', 'Narrow Tall',
       'Vintage', 'Vintage Tall', 'XL Jumbo', 'XL Jumbo Evo Gold')
frets = st.sidebar.selectbox("Frets",frets_options)

fretboard_material_options = ('Blackwood', 'Ebony', 'Engineered', 'Granadillo', 'Jatoba', 'Laurel',
       'Maple', 'Pau Ferro', 'Purpleheart', 'Richlite', 'Roseacer', 'Rosewood',
       'Sungkai', 'Terentang', 'Walnut', 'Wenge') 
fretboard_material = st.sidebar.selectbox("Fretboard Material",fretboard_material_options)

number_of_frets_options = ('20', '21', '22', '24')
number_of_frets = st.sidebar.selectbox("Number of Frest",number_of_frets_options)

fretboard_radius_options = ('10"', '10" to 14"', '11.5"', '12"', '12" to 16"', '12.6"', '13.78"',
       '14"', '15"', '15.748"', '15.75"', '16"', '17"', '20"', '7.25"', '8.5"',
       '9"', '9.5"', '9.5" to 14"', '9.843"')
fretboard_radius = st.sidebar.selectbox("Fretboard Radius",fretboard_radius_options)

stainless_steel_frets_options = ("No","Yes")
stainless_steel_frets = st.sidebar.selectbox("Stainless Steel Frets",stainless_steel_frets_options)

nut_options = ('Black Tusq XL', 'Bone', 'Boneite', 'Bonoid', 'Compensated', 'Graphite',
       'Ivory Tusq', 'Locking', 'NuBone', 'PRS Propietary', 'Plastic','Synthetic Bone')
nut = st.sidebar.selectbox("Nut",nut_options)

nut_width_options = ('40.5mm (1.594'')', '40mm (1.575'')', '41.3mm (1.625'')',
       '41.7mm (1.643'')', '41.9mm (1.65'')', '41mm (1.614'')',
       '42.1mm (1.656'')', '42.5mm (1.675'')', '42.7mm (1.68'')',
       '42.8mm (1.685'')', '42.9mm (1.688'')', '42mm (1.654'')',
       '43mm (1.693'')', '44.5mm (1.75'')', '45mm (1.77'')',
       '47.6mm (1.875'')', '47mm (1.85'')', '48mm (1.89'')', '49.5mm (1.95'')',
        '52.4mm (2.062'')', '54mm (2.126'')', '55mm (2.165'')','63.5mm (2.5'')')
nut_width = st.sidebar.selectbox("Nut Width",nut_width_options)

switch_options = ('0 Way', '3 Way', '4 Way', '5 Way')
switch = st.sidebar.selectbox("Switch",switch_options)

knobs_options = ('Bell', 'Dome', 'Speed')
knobs = st.sidebar.selectbox("Knobs",knobs_options)

volume_controls = st.sidebar.slider("Volume Controls",1,3)
tone_controls = st.sidebar.slider("Tone Controls",0,2)

pickup_configurations_options = ('H', 'HH', 'HHH', 'HHS', 'HHX', 'HP90', 'HP90P90', 'HS', 'HSH', 'HSS',
       'P90', 'P90P90', 'P90P90P90', 'SH', 'SP90', 'SS', 'SSS', 'XXH')
pickup_configurations = st.sidebar.selectbox("Pickup Configurations",pickup_configurations_options)

top_pickup_brand_options = ("No","Yes")
top_pickup_brand = st.sidebar.selectbox("Top Pickup Brand",top_pickup_brand_options,help="Pickup brands like Seymour Duncan, EMG, DiMarzio, Ibanez etc. are considered to be one of the top pickup brands")

pickups_power_options = ('Active', 'Active-Active', 'Active-Active-Active', 'Active-Passive',
       'Passive', 'Passive-Active-Passive', 'Passive-Passive','Passive-Passive-Active', 'Passive-Passive-Passive')
pickups_power = st.sidebar.selectbox("Pickups Power",pickups_power_options)

locking_tuners_options = ("No","Yes")
locking_tuners = st.sidebar.selectbox("Locking Tuners",locking_tuners_options)

tremolo_options = ("No","Yes")
tremolo = st.sidebar.selectbox("Tremolo",tremolo_options)

bridge_type_options = ('Bigsby Tremolo', 'Edge', 'Edge Zero', 'Edge Zero II', 'Evertune',
       'Fixed', 'Floyd Rose', 'Kahler', 'Lo-Pro Edge', 'Tremolo')
bridge_type = st.sidebar.selectbox("Bridge Type",bridge_type_options)

make_prediction = st.sidebar.button("Predict")

if make_prediction:
    
    brand_value = brand_options.index(brand)
    year_value = year_options.index(year)
    configuration_value = pickup_configurations_options.index(pickup_configurations)
    strings_value = number_of_strings_options.index(number_of_strings)
    made_in_value = made_in_options.index(made_in)
    body_type_value = body_type_options.index(body_type)
    body_shape_value = body_shape_options.index(body_shape)
    body_material_value = body_material_options.index(body_material)
    neck_joint_value = neck_joint_options.index(neck_joint)
    neck_material_value = neck_material_options.index(neck_material)
    neck_profile_value = neck_profile_options.index(neck_profile)
    scale_size_value = scale_size_options.index(scale_size)
    frets_value = frets_options.index(frets)
    fretboard_material_value = fretboard_material_options.index(fretboard_material)
    number_of_frets_value = number_of_frets_options.index(number_of_frets)
    fretboard_radius_value = fretboard_radius_options.index(fretboard_radius)
    stainless_steel_frets_value = stainless_steel_frets_options.index(stainless_steel_frets)
    nut_value = nut_options.index(nut)
    nut_width_value = nut_width_options.index(nut_width)
    switch_value = switch_options.index(switch)
    knobs_value = knobs_options.index(knobs)
    volume_controls_value = volume_controls
    tone_controls_value = tone_controls
    top_pickup_brand_value = top_pickup_brand_options.index(top_pickup_brand)
    pickups_power_value = pickups_power_options.index(pickups_power)
    locking_tuners_value = locking_tuners_options.index(locking_tuners)
    bridge_type_value = bridge_type_options.index(bridge_type)
    tremolo_value = tremolo_options.index(tremolo)

    predicators = [brand_value,year_value,configuration_value,strings_value,made_in_value,body_type_value,body_shape_value,body_material_value,
    neck_joint_value,neck_material_value,neck_profile_value,scale_size_value,frets_value,fretboard_material_value,number_of_frets_value,
    fretboard_radius_value,stainless_steel_frets_value,nut_value,nut_width_value,switch_value,knobs_value,volume_controls,
    tone_controls,top_pickup_brand_value,pickups_power_value,locking_tuners_value,bridge_type_value,tremolo_value]

    predicators = np.array(predicators).reshape(1,-1)
    predicted_price = predict(model,predicators)

    st.write(f"Guitar price is predicted as {predicted_price}$")



