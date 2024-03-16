import pandas as pd

def match_func(df, gender='Female', age_lb=20, age_ub=65, interests=['Literature']):
    filtered = df[(df['Gender'] == gender)
        & (df['Age'] >= age_lb)
        & (df['Age'] <= age_ub)
        & (df['Shared Interests'].isin(interests))]
    return filtered
    
df = pd.read_csv("./patient-database.csv", delimiter=',')
df.columns = [i.strip() for i in df.columns]
df = df[['Gender','Age','Level of Severity','Shared Interests','Support Needs']]
for col in df.columns:
    if (col != 'Age'):
        df[col] = df[col].apply(lambda x: str(x).strip())

def main():
    print("This is a demonstration to show how an app user can input preferences to optimise peer-to-peer matching: ")
    print("Gender:") 
    gender = input().strip()
    print("Age Range:")
    print("lower bound:")
    age_lb = int(input().strip())
    print("upper bound:")
    age_ub = int(input().strip())
    print("Interests (use ,to separate): ")
    interests = input().strip()
    interests = interests.split(",")
    filtered = match_func(df, gender, age_lb, age_ub, interests)
    print(filtered)

if __name__ == '__main__':
    main()



