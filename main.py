import pandas as pd
import matplotlib.pyplot as plt

# Read charts.csv file
main_data_frame = pd.read_csv('charts.csv')


def bye():
    print("Goodbye!")


def top_ranked_song_for_a_particular_day():
    particular_day = input("Enter the date you wish to see results for in yyyy-mm-dd format:\n")

    top_10_songs_in_date = (main_data_frame['rank'] <= 10) & (main_data_frame['date'] == particular_day)
    top_10_songs_in_date = main_data_frame[top_10_songs_in_date]
    top_10_songs_in_date = top_10_songs_in_date[['rank', 'song', 'artist']]

    print("----------------------------------------------------------------------------------")
    print(f"\nTop ranked songs for the date {particular_day}\n")
    print(top_10_songs_in_date.to_string(index=False))
    print("----------------------------------------------------------------------------------\n")

    c = input("M - Main menu\tQ - Quit\n")
    if c == "Q" or c == "q":
        bye()
    else:
        main()


def songs_of_an_artist():
    artist = input("Enter the name of the artist:\n")

    artist_songs = main_data_frame['artist'].str.contains(artist.title(), regex=True, na=True)
    artist_songs = main_data_frame[artist_songs][['song']]

    print("----------------------------------------------------------------------------------")
    print(f"Songs of {artist} are:\n")
    print(artist_songs.drop_duplicates().head(10).to_string(index=False))
    print("----------------------------------------------------------------------------------")

    c = input("M - Main menu\tQ - Quit\n")
    if c == "Q" or c == "q":
        bye()
    else:
        main()


def find_artist_of_a_song():
    song = input("Enter the name of the song:\n")

    song_data = main_data_frame['song'] == song.title()
    artist = main_data_frame[song_data][['artist']].drop_duplicates().to_string(index=False, header=False)

    print("----------------------------------------------------------------------------------")
    print(f"The song: {song} \nThe artist(s): {artist}")
    print("----------------------------------------------------------------------------------")
    c = input("M - Main menu\tQ - Quit\n")
    if c == "Q" or c == "q":
        bye()
    else:
        main()


def history_of_the_song():
    song = input("Enter the name of the song:\n")

    song_data = main_data_frame['song'] == song.title()
    history_song = main_data_frame[song_data][['date', 'rank', 'last-week', 'peak-rank', 'weeks-on-board']]

    print("----------------------------------------------------------------------------------")
    print(f"Details for the song '{song}'")
    print(history_song.to_string(index=False))
    print("----------------------------------------------------------------------------------")
    c = input("M - Main menu\tQ - Quit\n")
    if c == "Q" or c == "q":
        bye()
    else:
        main()


def visualise_songs_rank_changing():
    song = input("Enter the name of the song:\n")

    song_data = main_data_frame['song'] == song.title()
    song_rank_change = main_data_frame[song_data][['date', 'rank']][::-1]

    plt.plot(song_rank_change["date"], song_rank_change["rank"])
    plt.xticks(rotation=90)
    plt.title(f"Song: '{song}', rank changing.")
    plt.xlabel('Date')
    plt.ylabel('rank')
    plt.show()

    c = input("M - Main menu\tQ - Quit\n")
    if c == "Q" or c == "q":
        bye()
    else:
        main()


def main():
    print("----------------------------------------------------------------------------------")
    print("\nHello there! Please choose an option from the following:\n")
    print("1 - Retrieve the details for the top ranked song for a particular day\n")
    print("2 - Retrieve the songs of an artist by the name\n")
    print("3 - Retrieve the name of the artist of a song\n")
    print("4 - Retrieve the history of a song by the name of the song\n")
    print("5 - Visualise the song rank changing.\n")
    print("M - Main menu\n")
    print("Q - Quit")
    print("----------------------------------------------------------------------------------")

    while True:
        choice = input("Please enter your choice: \n")
        if choice == "Q" or choice == "q":
            bye()
            break
        elif choice == "M" or choice == "m":
            main()
        elif choice == "1":
            top_ranked_song_for_a_particular_day()
        elif choice == "2":
            songs_of_an_artist()
        elif choice == "3":
            find_artist_of_a_song()
        elif choice == "4":
            history_of_the_song()
        elif choice == "5":
            visualise_songs_rank_changing()

        else:
            print("Please enter a valid choice!")
            main()
        break


main()
