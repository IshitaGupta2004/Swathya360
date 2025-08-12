# Swathya360
# Ayurveda Health Assistant (Tkinter) 🚩

Simple level-based Ayurveda Health Assistant desktop app built with Python and Tkinter.
It detects your dominant dosha (Vata / Pitta / Kapha) using a short questionnaire + BMI,
and then shows diet, exercise, hair & skin care, seasonal tips and allows saving the plan.

## Features
- Level-based UI (Basic info → Questionnaire → Result → Recommendations → Save plan)
- BMI calculation (height in cm, weight in kg)
- Dosha detection using 6 quick questions
- Diet, exercise, hair & skin tips for each dosha
- Season-based tips and ability to save the plan as a text file

## Requirements
- Python 3.8+
- (Optional) Pillow for better image handling in Tkinter:
  ```bash
  pip install pillow

  python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python gui.py


