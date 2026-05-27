print(" Loan Eligibility Checker 25")

age = int(input("Enter your age: "))
salary = int(input("Enter your monthly salary: "))
employment = input("Enter employment type (salaried/self-employed): ")

if age < 21 or age > 60:
    print("Rejected: Age should be between 21 and 60.")

elif salary < 25000:
    print("Rejected: Salary should be at least ₹25,000.")

elif employment not in ["salaried", "self-employed"]:
    print("Rejected: Employment type must be salaried or self-employed.")

elif age >= 21 and age <= 30 and salary < 30000:
    print("Needs guarantor.")

elif age > 55 and employment == "self-employed":
    print("High risk, senior review needed.")

else:
    print("Approved.")