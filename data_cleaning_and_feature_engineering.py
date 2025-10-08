import pandas as pd

df = pd.read_csv('rides_data.csv')

# --- Combining Date and Time into a Single Datetime Column ---
print("Combining 'date' and 'time' columns...")
df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
# Droping the original date and time columns as they are no longer needed
df.drop(['date', 'time'], axis=1, inplace=True)
print("Datetime column created successfully.")

# --- Handling Missing Values ---
# Filling NaN fare values for cancelled rides with 0
print("Handling missing fare values...")
df.loc[df['ride_status'] == 'cancelled', ['ride_charge', 'misc_charge', 'total_fare', 'payment_method']] = 0
# Checking for any remaining missing values
print("Missing values after filling:")
print(df[['ride_charge', 'misc_charge', 'total_fare', 'payment_method']].isnull().sum())
print("Missing values handled successfully.")

# --- Feature Engineering ---
# Creating Time-Based Features
print("\nCreating new time-based features...")
df['day_of_week'] = df['datetime'].dt.day_name()
df['hour_of_day'] = df['datetime'].dt.hour
df['month'] = df['datetime'].dt.month
df['year'] = df['datetime'].dt.year
# Creating a 'daypart' feature to categorize rides into time of day
def get_daypart(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'
df['daypart'] = df['hour_of_day'].apply(get_daypart)
# Creating a boolean feature for weekends
df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])
print("New time-based features created.")

# Creating 'trip_type' and 'fare_per_km' features
print("\nCreating trip type and fare features...")
df['trip_type'] = df['services'].apply(lambda x: 'Bike' if 'bike' in x else ('Auto' if 'auto' in x else ('Cab' if 'cab' in x else 'Parcel')))
df['fare_per_km'] = df['total_fare'] / df['distance']
# Handling cases where distance is 0 to avoid division by zero
df['fare_per_km'].replace([float('inf'), -float('inf')], 0, inplace=True)
print("New trip type and fare features created.")

# Creating Rush Hour Indicator ---
print("Creating 'is_rush_hour' indicator...")

# Defining a function to check for rush hour
def is_rush_hour(hour):
    # Morning rush hour is from 7 to 10  
    # Evening rush hour is from 17 to 20
    return (7 <= hour < 10) or (17 <= hour < 20)

# Applying the function to the 'hour_of_day' column
df['is_rush_hour'] = df['hour_of_day'].apply(is_rush_hour)

print("'is_rush_hour' column added successfully.")

# --- Saving the Cleaned Data ---
# Saving the cleaned DataFrame to a new CSV file
print("\nSaving cleaned data to 'cleaned_rapido_data.csv'...")
df.to_csv('cleaned_rapido_data.csv', index=False)
print("Cleaned data successfully saved!")