import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # The most common month
    most_common_month = df["month"].mode()[0]
    print(f"The most common month is: {most_common_month}")

    # The most common day of week
    most_common_day = df["day_week"].mode()[0]
    print(f"The most common day of week is: {most_common_day}")

    # The most common start hour
    most_common_hour = df["hour"].mode()[0]
    print(f"The most common start hour is: {most_common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Most commonly used start station
    most_used_start_station = df["Start Station"].mode()[0]
    print(f"The most commonly used start station is: {most_used_start_station}")

    # Most commonly used end station
    most_used_end_station = df["End Station"].mode()[0]
    print(f"The most commonly used end station is: {most_used_end_station}")

    # Most frequent combination of start station and end station trip
    df["combo"] = "From " + df["Start Station"] + " to " + df["End Station"]
    most_frequent_combo = df["combo"].mode()[0]
    print(f"Most frequent combination of start station and end station trip: {most_frequent_combo}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Total travel time
    total_travel = df["Trip Duration"].sum().round(1)
    print(f"Total travel time: {total_travel} seconds")

    # Mean travel time
    mean_travel = df["Trip Duration"].mean().round(1)
    print(f"Mean travel time: {mean_travel} seconds")
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Counts of user types
    user_types_count = df["User Type"].value_counts()
    print(f"Count of user types: {user_types_count}")

    # Specify city since washington does not have gender and birth year data
    if city != "washington":
        # Counts of gender
        gender_count = df["Gender"].value_counts()
        print(f"Count of users' gender: {gender_count}")

        # Earliest, most recent, and most common year of birth
        earliest = int(df["Birth Year"].min())
        print(f"Earliest year of birth is: {earliest}")
    
        most_recent = int(df["Birth Year"].max())
        print(f"Most recent year of birth is: {most_recent}")
    
        most_common_year = int(df["Birth Year"].mode()[0])
        print(f"Most common year of birth is: {most_common_year}")

    else:
        print("Washington's gender and birth year data is not available.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
