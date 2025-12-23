import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import plotly.express as px

from class_names import CLASS_NAMES
from nutrition_data import NUTRITION_INFO

st.set_page_config(page_title="Fruit & Veg Classifier", page_icon="🥦", layout="centered")

st.title("🍎 Fruit & Vegetable Classification System")
st.write("Upload image → Predict → View Nutrition")


@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "hibrid.keras",
        compile=False,
    )


model = load_model()

def preprocess_image(img):
    img = img.resize((224,224))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)
    return img

def extract_number(value):
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        return float(value.split()[0])  # "50 kcal" -> 50
    return 0.0


def show_nutrition_graphs(info, name):
    labels = ["Calories","Carbohydrates","Protein","Fiber"]
    values = [extract_number(info[k]) for k in labels]


    bar = px.bar(
        x=labels, y=values, text=values,
        title=f"Nutritional Values of {name}",
        template="plotly_white"
    )
    bar.update_layout(title_x=0.5)
    st.plotly_chart(bar, use_container_width=True)

    donut = px.pie(
        names=labels[1:], values=values[1:], hole=0.5,
        title="Macronutrient Distribution"
    )
    donut.update_layout(title_x=0.5)
    st.plotly_chart(donut, use_container_width=True)

file = st.file_uploader("📤 Upload Image", type=["jpg","png","jpeg"])

if file:
    image = Image.open(file).convert("RGB")
    st.image(image, use_column_width=True)

    if st.button("🔍 Predict"):
        img = preprocess_image(image)
        pred = model.predict(img)
        idx = np.argmax(pred)
        confidence = np.max(pred)*100
        name = CLASS_NAMES[idx]

        st.success(f"Prediction: **{name}**")
        st.info(f"Confidence: **{confidence:.2f}%**")

        info = NUTRITION_INFO[name]
        col1, col2 = st.columns(2)
        col1.metric("🔥 Calories", info["Calories"])
        col1.metric("🍞 Carbs", info["Carbohydrates"])
        col2.metric("🥩 Protein", info["Protein"])
        col2.metric("🌾 Fiber", info["Fiber"])

        st.info(f"💡 Benefits: {info['Benefits']}")
        show_nutrition_graphs(info, name)
