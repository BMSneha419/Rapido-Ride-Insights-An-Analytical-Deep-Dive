import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the cleaned dataset
df = pd.read_csv('cleaned_rapido_data.csv')

sns.set_style("whitegrid")

# --- Are there clear rush hours for different services? ---
print("Plotting hourly demand for different services...")
plt.figure(figsize=(12, 7))
sns.countplot(x='hour_of_day', hue='trip_type', data=df)
plt.title('Ride Demand by Hour of Day and Trip Type')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Rides')
plt.legend(title='Trip Type')
plt.show()

# --- How does the average fare change by service and distance? ---
print("\nPlotting fare-per-km distribution...")
plt.figure(figsize=(12, 7))
sns.boxplot(x='trip_type', y='fare_per_km', data=df)
plt.title('Fare-per-km Distribution by Trip Type')
plt.xlabel('Trip Type')
plt.ylabel('Fare per Kilometer (INR)')
plt.show()

# --- Are cancellations more frequent on specific days or times? ---
print("\nPlotting cancellation rates by day of the week...")
# Calculating cancellation counts for each day of the week
cancellation_by_day = df[df['ride_status'] == 'cancelled'].groupby('day_of_week').size().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], fill_value=0)
cancellation_by_day = cancellation_by_day.reset_index(name='count')

plt.figure(figsize=(12, 7))
sns.barplot(x='day_of_week', y='count', data=cancellation_by_day)
plt.title('Total Ride Cancellations by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Cancellations')
plt.show()

# --- How does ride duration relate to distance? ---
print("\nPlotting relationship between duration and distance...")
plt.figure(figsize=(12, 7))
sns.scatterplot(x='distance', y='duration', hue='trip_type', data=df)
plt.title('Trip Duration vs. Distance by Trip Type')
plt.xlabel('Distance (km)')
plt.ylabel('Duration (minutes)')
plt.show()

# --- How do the total rides and cancellations change by day of the week? ---
print("\nPlotting total rides and cancellations by day of the week...")
df_daily_counts = df.groupby('day_of_week')['ride_status'].value_counts().unstack().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], fill_value=0)
df_daily_counts.plot(kind='bar', figsize=(12, 7), rot=0)
plt.title('Total Rides vs. Cancellations by Day of Week', fontsize=16)
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Number of Rides/Cancellations', fontsize=12)
plt.legend(title='Ride Status')
plt.tight_layout()
plt.show()

# --- Do ride duration and distance increase during rush hour? ---
print("\nPlotting average trip duration during rush hour vs. non-rush hour...")
plt.figure(figsize=(10, 6))
sns.barplot(x='is_rush_hour', y='duration', data=df, palette="coolwarm", estimator=sum)
plt.title('Total Duration of Rides: Rush Hour vs. Non-Rush Hour', fontsize=16)
plt.xlabel('Is Rush Hour?', fontsize=12)
plt.ylabel('Total Duration (minutes)', fontsize=12)
plt.xticks([0, 1], ['Non-Rush Hour', 'Rush Hour'])
plt.tight_layout()
plt.show()

# --- What is the distribution of total fare? ---
print("\nPlotting the distribution of total fare...")
plt.figure(figsize=(10, 6))
sns.histplot(df['total_fare'], bins=50, kde=True)
plt.title('Distribution of Total Fare', fontsize=16)
plt.xlabel('Total Fare (INR)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.show()

# --- What are the most popular payment methods? ---
print("\nPlotting the most popular payment methods...")
plt.figure(figsize=(10, 6))
payment_counts = df['payment_method'].value_counts()
sns.barplot(x=payment_counts.index, y=payment_counts.values, palette="rocket")
plt.title('Most Popular Payment Methods', fontsize=16)
plt.xlabel('Payment Method', fontsize=12)
plt.ylabel('Number of Rides', fontsize=12)
plt.tight_layout()
plt.show()