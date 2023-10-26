# data descriptions

```Python
# load in each of the dataframes
data_path = "/home/jeffx/ACME/WearableHealthPredictor/data"
activity_environment_df = pd.read_csv(f"{data_path}/activity_environment_data.csv")  
personal_health_df = pd.read_csv(f"{data_path}/personal_health_data.csv")
digital_interaction_df = pd.read_csv(f"{data_path}/digital_interaction_data.csv")

# merge all of the above dataframes on User_ID
merged_df = activity_environment_df.merge(personal_health_df, on='User_ID')
health_df = merged_df.merge(digital_interaction_df, on='User_ID')

# drop irrelevant columns
cols_to_drop = ['User_ID', 'Timestamp_x', 'Battery_Level', 'Timestamp_y', 'Timestamp', 'Anomaly_Flag', 'Screen_Time', 'Notifications_Received', 'Day_of_Week']
health_df = health_df.drop(cols_to_drop, axis=1)

# fill columns with NaN values to have a value of 'None'
nan_columns = ['Exercise_Type', 'Exercise_Intensity', 'Medical_Conditions', 'Alcohol_Consumption', 'Stress_Level', 'Mood']
for col in nan_columns:
    health_df[col] = health_df[col].fillna('None')
    
print("Exercise_Type unique:", health_df['Exercise_Type'].unique())
print("Exercise_Intensity unique:", health_df['Exercise_Intensity'].unique())
print("Gender unique:", health_df['Gender'].unique())
print("Medical_Conditions unique:", health_df['Medical_Conditions'].unique())
print("Alcohol_Consumption unique:", health_df['Alcohol_Consumption'].unique())
print("Stress_Level unique:", health_df['Stress_Level'].unique())
print("Mood unique:", health_df['Mood'].unique())
```

```
Exercise_Type unique: ['Running' 'Yoga' 'Strength Training' 'None']
Exercise_Intensity unique: ['Low' 'Moderate' 'None' 'High']
Gender unique: ['Other' 'Male' 'Female']
Medical_Conditions unique: ['Diabetes' 'None' 'Hypertension']
Alcohol_Consumption unique: ['Moderate' 'Heavy' 'None']
Stress_Level unique: ['Moderate' 'High' 'Low']
Mood unique: ['Neutral' 'Anxious' 'Sad' 'Happy']
```