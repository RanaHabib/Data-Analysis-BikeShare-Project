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
    city = ''
    while(True):
        if(city == 'Chicago' or city == 'New york city' or city == 'Washington'):
            break
        else:
            city = input('Would you like to see data for Chicago, New york city, Washington')
            
    
    choice = ''
    while(True):
        if(choice == 'month' or choice == 'day' or choice == 'both' or choice == 'none'):
            break
        else:
            choice = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.')
    
    month = 'none'
    day = 0
    
    # get user input for month (all, january, february, ... , june)
    if(choice == 'both' or choice == 'month'):
        while(True):
            if(month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June'):
                break
            else:
                month = input('Which month? January, February, March, April, May or June?')
                
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if(choice == 'both' or choice == 'day'):
        while(True):
            if(day >= 1 and day <= 7):
                break
            else:
                day = int(input('Which day? Please type your response as an integer e.g: 1 = sunday.'))
    
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
    #Reading the csv file.
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    #converting start time and end time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #Making a new hour column.
    df['Hour'] = df['Start Time'].dt.hour
    
    #Making a new month column.
    df['Month'] = df['Start Time'].dt.month
    
    #Making a new day column.
    df['Day of week'] = df['Start Time'].dt.weekday_name    
    
    #Filtering month.
    if(month != 'none'):
        months_of_year = ['January','February','March','April','May','June']
        index_of_month = months_of_year.index(month) + 1
        df = df[df['Month'] == index_of_month]
    
    #Filtering day.
    if(day != 0):
        day_of_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        index_of_day = day_of_week[day - 1]
        df = df[df['Day of week'] == index_of_day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month: ', df['Month'].value_counts().index[0])

    # display the most common day of week
    print('Most common day of week: ', df['Day of week'].value_counts().index[0])

    # display the most common start hour
    print('Most common start hour: ',df['Hour'].value_counts().index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common start station: ', df['Start Station'].value_counts().index[0])

    # display most commonly used end station
    print('Most common end station: ', df['End Station'].value_counts().index[0])

    # display most frequent combination of start station and end station trip
    print(pd.DataFrame(df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)).iloc[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: ', df['Trip Duration'].sum())
    
    # display mean travel time
    print('Mean travel time: ', df['Trip Duration'].mean())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types: ', df['User Type'].value_counts())

    if(city == 'Chicago' or city == 'New york city'):
            # Display counts of gender
            print('Counts of gender: ', df['Gender'].value_counts())
            
            # Display earliest, most recent, and most common year of birth
            print('Most earliest year of birth: ', df['Birth Year'].sort_values().iloc[0])
            print('Most recent year of birth: ', df['Birth Year'].sort_values(ascending = False).iloc[0])
            print('Most common year of birth', df['Birth Year'].value_counts().index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


