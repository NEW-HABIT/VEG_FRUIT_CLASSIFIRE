

# 🍎 Fruit & Vegetable Classification & Nutrition Analysis System

A **deep learning–based web application** that identifies **36 different fruits and vegetables** from images and displays their **nutritional information with modern interactive graphs**, deployed locally using **Streamlit**.

---

## 📌 Project Overview

This project uses a **Hybrid Deep Learning Model (CNN + Dense Architecture)** to classify fruits and vegetables from images.

Once an image is uploaded, the system:

- ✅ Predicts the fruit or vegetable name  
- ✅ Shows confidence score  
- ✅ Displays nutritional values  
- ✅ Visualizes nutrition using modern interactive charts  

### 🎯 Suitable For
- 🎓 Final Year / Capstone Project  
- 📊 Machine Learning Demonstration  
- 🌐 Health & Nutrition Applications  
- 🧪 Computer Vision Research  

---

## 🚀 Key Features

- ✅ Image-based classification (36 classes)  
- ✅ Hybrid CNN deep learning model  
- ✅ Streamlit-based modern web UI  
- ✅ Interactive nutrition graphs (Plotly)  
- ✅ Local hosting (no cloud dependency)  
- ✅ Expandable nutrition database  
- ✅ Resume & viva-ready project structure  

---

## 🧠 Hybrid Model Architecture

### 🔹 What is a Hybrid Model?

A **Hybrid Model** combines:

- **Convolutional Neural Networks (CNNs)** for feature extraction  
- **Fully Connected Dense Layers** for high-level classification  

### 🔹 Benefits of Hybrid Architecture
- Improved feature learning  
- Better generalization  
- Higher accuracy on complex image datasets  

---

### 🔹 Model Structure (High Level)

```
Input Image (224×224×3)
        ↓
Convolution Layers
        ↓
Feature Maps Extraction
        ↓
Flatten Layer
        ↓
Dense Layers
        ↓
Softmax Output (36 Classes)
```

📌 The model is saved in **`.keras` format**, making it:

- Deployment-friendly  
- Framework-consistent  
- Easy to reuse  

---

## 🖼 Model Architecture Diagram


```
!(model_structure.png)
```

---

## 🥦 Classes Covered (36 Categories)

Apple, Banana, Beetroot, Bell Pepper, Cabbage, Capsicum, Carrot,  
Cauliflower, Chilli Pepper, Corn, Cucumber, Eggplant, Garlic,  
Ginger, Grapes, Jalepeno, Kiwi, Lemon, Lettuce, Mango, Onion,  
Orange, Paprika, Pear, Peas, Pineapple, Pomegranate, Potato,  
Raddish, Soy Beans, Spinach, Sweetcorn, Sweet Potato, Tomato,  
Turnip, Watermelon  

---

## 🥗 Nutrition Analysis Module

For each predicted fruit or vegetable, the system displays:

- 🔥 Calories  
- 🍞 Carbohydrates  
- 🥩 Protein  
- 🌾 Fiber  
- 💡 Health Benefits  

### 📊 Modern Graphs Used
- **Bar Chart** – Nutritional values comparison  
- **Donut Chart** – Macronutrient distribution  

Powered by **Plotly** for:
- Interactive hover  
- Clean UI  
- Professional visualization  

---

## 🖥 Web Application UI

Built using **Streamlit**, offering:

- Image upload interface  
- Real-time prediction  
- Responsive design  
- Modern chart visualizations  

---

## 📁 Project Structure

```
fruit_veg_app/
│
├── app.py                # Streamlit web app
├── hibrid.keras          # Trained hybrid model
├── class_names.py        # Class labels
├── nutrition_data.py    # Nutrition database
├── requirements.txt     # Dependencies
├── assets/
│   └── model_structure.png
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/fruit-veg-classifier.git
cd fruit-veg-classifier
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application (Local Hosting)
```bash
streamlit run app.py
```

📍 The app will open at:
```
http://localhost:8501
```

---

## 🧪 Technologies Used

- Python  
- TensorFlow / Keras  
- CNN (Hybrid Architecture)  
- Streamlit  
- Plotly  
- NumPy  
- Pillow  

---

## 🌟 Benefits of This System

- 📸 Automated fruit & vegetable recognition  
- 🥗 Instant nutrition awareness  
- 🧠 AI-powered decision support  
- 🏥 Useful for health & diet planning  
- 🎓 Excellent academic & demo project  
- 📈 Easy to scale to more categories  

---

## 🔮 Future Enhancements

- 🧠 Grad-CAM visualization  
- 🌙 Dark mode UI  
- 📄 Nutrition PDF report download  
- 🔐 Admin panel for nutrition editing  
- ☁️ Cloud deployment (Render / Hugging Face)  
- 📱 Mobile-friendly optimization  

---

## 👤 Author

**Barshan Adhikari**

- GitHub: https://github.com/NEW-HABIT  
- LinkedIn: https://www.linkedin.com/in/barshan-adhikari  

---

## 📜 License

This project is developed for **educational and research purposes**.  
You are free to use, modify, and enhance it.

