
print("Risk Assessment Tool")
print("--------------------")

likelihood = int(input("Likelihood of the hazard (1-5): "))
severity = int(input("Severity of the hazard (1-5): "))
frequency = int(input("Exposure frequency (1-5): "))


risk_score = likelihood * severity * frequency

if risk_score <= 25:
    level = "Low Risk"
elif risk_score <= 50:
    level = "Medium Risk"
else:
    level = "High Risk"

print("\nCalculated Risk Score:", risk_score)
print("Risk Level:", level)

input("\nPress Enter to exit...")