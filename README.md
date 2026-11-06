# 🍎 FoodNutrition — AI-Based Food Detection & Personalized Nutrition Analysis

A full-stack **Flask** web application that uses a **deep learning** model (TensorFlow/Keras) to identify food items from uploaded images and provide detailed **nutritional analysis** with personalized health recommendations.

---

## ✨ Features

- **🔍 Food Image Recognition** — Upload a photo and the AI model classifies it into one of 20 food categories using a CNN trained on a custom dataset.
- **📊 Nutritional Breakdown** — Displays calories, protein, carbs, fat, fiber, and more from a curated nutrition CSV database.
- **👤 User Authentication** — Register, login, and manage your profile with hashed passwords (Werkzeug).
- **🏥 Nutrition Profile** — Set personal health goals (weight loss, muscle gain, etc.) for tailored dietary advice.
- **📜 Nutrition History** — Track all past food analyses with timestamps and detailed logs.
- **📧 Daily Nutrition Alerts** — Optional email-based daily nutrition summary via SMTP and APScheduler.
- **📱 Responsive UI** — Clean, mobile-friendly interface with custom CSS styling.

---

## 🧠 Supported Food Classes (20)

| | | | |
|---|---|---|---|
| Bacon | Banana | Bread | Broccoli |
| Butter | Carrots | Cheese | Chicken |
| Cucumber | Eggs | Fish | Lettuce |
| Milk | Onions | Peppers | Potatoes |
| Sausages | Spinach | Tomato | Yogurt |

---

## 🗂️ Project Structure

```
FoodNutrition/
├── app.py                   # Main Flask application
├── train_model.py           # Model training script
├── test_prediction.py       # Model testing/validation
├── smtp_test.py             # Email configuration tester
├── requirements.txt         # Python dependencies
├── database.db              # SQLite database (user data & history)
├── model/
│   ├── food_model.keras     # Trained CNN model
│   └── class_names.txt      # Food class labels
├── dataset/
│   ├── train/               # Training images (20 classes)
│   ├── val/                 # Validation images
│   └── test/                # Test images
├── nutrition/
│   └── nutrition.csv        # Nutritional data for food items
├── static/
│   ├── style.css            # Application styles
│   └── images/              # Static assets
├── templates/
│   ├── home.html            # Main upload & analysis page
│   ├── login.html           # User login page
│   ├── register.html        # User registration page
│   ├── result.html          # Nutrition results display
│   ├── nutrition_profile.html   # Health profile setup
│   └── nutrition_history.html   # Past analysis history
└── uploads/                 # User-uploaded food images
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pavankumar054/FoodNutrition.git
   cd FoodNutrition
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/Mac
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your_secret_key_here
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   ```
   http://localhost:5000
   ```

---

## 🏋️ Training the Model

To retrain the food classification model on your own dataset:

```bash
python train_model.py
```

The training script uses the images in `dataset/train/`, `dataset/val/`, and `dataset/test/` directories organized by food class.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Flask, Python |
| **ML/AI** | TensorFlow, Keras, OpenCV, NumPy |
| **Database** | SQLite3 |
| **Data Processing** | Pandas |
| **Authentication** | Werkzeug (password hashing) |
| **Email Alerts** | SMTP, APScheduler |
| **Frontend** | HTML5, CSS3, Jinja2 Templates |

---

## 📋 Requirements

```
Flask>=3.0.0,<4.0.0
Werkzeug>=3.0.0,<4.0.0
tensorflow>=2.16.0,<3.0.0
keras>=3.0.0,<4.0.0
opencv-python-headless>=4.8.0
numpy>=1.26.0,<3.0.0
pandas>=2.2.0,<4.0.0
APScheduler>=3.10.0,<4.0.0
python-dotenv>=1.0.0
gunicorn>=22.0.0
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Pavan Kumar**

- GitHub: [@Pavankumar054](https://github.com/Pavankumar054)

---

> Built with ❤️ using Flask and TensorFlow
