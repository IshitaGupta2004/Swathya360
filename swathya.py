# Ayurveda Health App - Single File Version
# Author: Your Team Name
# Description: Finds BMI, Ayurvedic body type, and gives health tips

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# Function to determine body type
def get_body_type(answers, bmi):
    vata = answers[0] + answers[3]
    pitta = answers[1] + answers[4]
    kapha = answers[2] + answers[5]

    # Adjust score based on BMI
    if bmi > 25:
        kapha += 2
    elif bmi < 18.5:
        vata += 2

    if max(vata, pitta, kapha) == vata:
        return "Vata"
    elif max(vata, pitta, kapha) == pitta:
        return "Pitta"
    else:
        return "Kapha"

# Diet & Exercise Plan
def diet_exercise(body_type):
    print("\n=== Diet & Exercise Plan ===")
    if body_type == "Kapha":
        print("Diet: Light, warm, spicy foods. Avoid dairy and fried items.")
        print("Exercise: Brisk walk/jog 45 min, HIIT, yoga stretches.")
    elif body_type == "Pitta":
        print("Diet: Cooling foods like cucumber, melons, coconut water.")
        print("Exercise: Swimming, cycling, moderate cardio.")
    else:
        print("Diet: Warm, soft foods like soups, khichdi, milk with spices.")
        print("Exercise: Yoga, light weights, slow cycling.")

# Hair & Skin Care
def hair_skin(body_type):
    print("\n=== Hair & Skin Care ===")
    if body_type == "Kapha":
        print("Hair: Neem or tea tree oil, avoid heavy conditioners.")
        print("Skin: Exfoliate with besan + turmeric, use aloe vera gel.")
    elif body_type == "Pitta":
        print("Hair: Coconut oil massage, hibiscus or amla hair packs.")
        print("Skin: Sandalwood paste, rose water, avoid excess sun.")
    else:
        print("Hair: Warm sesame/almond oil, fenugreek paste.")
        print("Skin: Milk + honey mask, use coconut/olive oil for dryness.")

# Seasonal Routine
def seasonal(body_type):
    print("\n=== Seasonal Routine ===")
    if body_type == "Kapha":
        print("Spring: Wake early, exercise hard, avoid naps.")
        print("Summer: Stay hydrated, avoid heavy foods.")
    elif body_type == "Pitta":
        print("Spring: Avoid overheating, gentle exercise.")
        print("Summer: Stay cool, avoid midday sun.")
    else:
        print("Spring: Gentle yoga, avoid cold exposure.")
        print("Summer: Cooling drinks, light activity.")

# ---------------------- App Flow ----------------------

print("=== Ayurveda Health App ===")

# Level 1
print("\n--- Level 1: Basic Details ---")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
problem = input("Any health problem? (none if no): ")

bmi = calculate_bmi(weight, height)
print(f"\nYour BMI is: {bmi}")

# Level 2
print("\n--- Level 2: Questionnaire ---")
print("Answer: 1 = Rarely, 2 = Sometimes, 3 = Often")
q1 = int(input("Do you feel cold & have dry skin? "))
q2 = int(input("Do you feel warm & get irritated? "))
q3 = int(input("Do you gain weight easily & feel sluggish? "))
q4 = int(input("Are you thin & find it hard to gain weight? "))
q5 = int(input("Do you have strong digestion but acidity? "))
q6 = int(input("Do you have slow digestion & feel heavy after meals? "))
answers = [q1, q2, q3, q4, q5, q6]

# Level 3
print("\n--- Level 3: Result ---")
body_type = get_body_type(answers, bmi)
print(f"{name}, your Ayurvedic Body Type is: {body_type}")

# Level 4
input("\nPress Enter to see Diet & Exercise Plan...")
diet_exercise(body_type)

# Level 5
input("\nPress Enter to see Hair & Skin Care Tips...")
hair_skin(body_type)

# Level 6
input("\nPress Enter to see Seasonal Routine...")
seasonal(body_type)

print("\n--- End of Program ---")
