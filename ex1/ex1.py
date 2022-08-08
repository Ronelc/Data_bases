import csv
from io import TextIOWrapper
from zipfile import ZipFile

# opens file for oscars table.
# CHANGE!

oscar_file = open("oscar_t.csv", 'w', encoding="utf-8")
out_oscar = csv.writer(oscar_file, delimiter=",", quoting=csv.QUOTE_NONE)

film_file = open("film_t.csv", 'w', encoding="utf-8")
out_film = csv.writer(film_file, delimiter=",", quoting=csv.QUOTE_NONE)

studio_file = open("studio_t.csv", 'w', encoding="utf-8")
out_studio = csv.writer(studio_file, delimiter=",", quoting=csv.QUOTE_NONE)

directors_file = open("directors_t.csv", 'w', encoding="utf-8")
out_directors = csv.writer(directors_file, delimiter=",",
                           quoting=csv.QUOTE_NONE)

authors_file = open("authors_t.csv", 'w', encoding="utf-8")
out_authors = csv.writer(authors_file, delimiter=",", quoting=csv.QUOTE_NONE)

actors_file = open("actors_t.csv", 'w', encoding="utf-8")
out_actors = csv.writer(actors_file, delimiter=",", quoting=csv.QUOTE_NONE)


# process_file goes over all rows in original csv file, and sends each row to process_row()
# DO NOT CHANGE!!!
def process_file():
    with ZipFile('archive.zip') as zf:
        with zf.open('oscars_df.csv', 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            for row in reader:
                # remove some of the columns
                chosen_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16,
                                  29]
                row = [row[index] for index in chosen_indices]

                # change "," into && in list values
                lists_values_indices = [7, 11, 12, 13]
                for list_value_index in lists_values_indices:
                    row[list_value_index] = row[list_value_index].replace(',',
                                                                          '&&')

                # pre-process : remove all quotation marks from input and turns NA into null value ''.
                row = [v.replace(',', '') for v in row]
                row = [v.replace("'", '') for v in row]
                row = [v.replace('"', '') for v in row]
                row = [v if v != 'NA' else "" for v in row]

                # In the first years of oscars in the database they used "/" for example 1927/28, so we will change these.
                row[2] = row[2].split("/")[0]

                # In 1962 two movies were written as winners, then we change one of them to nominee.
                if row[4] == "Winner" and row[2] == "1962" and row[
                    14] == "8d5317bd-df12-4f24-b34d-e5047ef4665e":
                    row[4] = "Nominee"

                # In 2020 Nomadland won and marked as nominee by mistake.
                if row[2] == "2020" and row[1] == "Nomadland":
                    row[4] = "Winner"

                process_row(row)

    oscar_file.close()
    film_file.close()
    studio_file.close()
    directors_file.close()
    authors_file.close()
    actors_file.close()


# return a list of all the inner values in the given list_value.
# you should use this to handle value in the original table which
# contains an inner list of values.
# DO NOT CHANGE!!!
def split_list_value(list_value):
    return list_value.split("&&")


film_lst = []
oscar_lst = []
studio_lst = []
actors_lst = []
directors_lst = []
authors_lst = []

def helper(row, file, keys_lst):
    for i in row[0]:
        if i != " " and i != "":
            if [i, row[1]] not in keys_lst:
                keys_lst.append([i, row[1]])
                file.writerow([i, row[1]])


# process_row should splits row into the different csv table files
# CHANGE!!!

def process_row(row):

    # 1 film name: 'The Irishman',
    # 2 oscar year: '2019',
    # 3 studio: 'Martin Scorsese Robert De Niro Jane Rosenthal and Emma Tillinger Koskoff',
    # 4 award:'Nominee',
    # 5 relase year: '2019',
    # 6 time: '209',
    # 7 gener: 'Biography&&Crime&&Drama',
    # 8 imdb rating:'7.8',
    # 9 imdb votes: '349303',
    # 10 content rating: 'R',
    # 11 directors: 'Martin Scorsese',
    # 12 authors: 'Steven Zaillian',
    # 13 actors: 'Robert De Niro&& Al Pacino&& Joe Pesci&& Jesse Plemons&& Bobby Cannavale&& Anna Paquin&& Harvey Keitel&& Ray Romano&& Stephen Graham&& Aleksa Palladino&& Stephanie Kurtzuba&& Jack Huston&& Kathrine Narducci&& Domenick Lombardozzi&& Paul Herman&& Gary Basaraba&& Marin Ireland',
    # 14 film ID: 'cf8fb1fa-1a2b-48bd-a241-c7e9d487c09d']

    studio_split = split_list_value(row[3])
    directors_split = split_list_value(row[11])
    authors_split = split_list_value(row[12])
    actors_split = split_list_value(row[13])


    film_row = [row[1], row[2], row[3], row[5], row[6], row[7], row[8], row[9],
                row[10], row[11], row[12], row[13], row[14]]

    oscar_row = [row[2], row[14]]
    studio_row = [studio_split, row[14]]
    directors_row = [directors_split, row[14]]
    authors_row = [authors_split, row[14]]
    actors_row = [actors_split, row[14]]

    if film_row not in film_lst:
        film_lst.append(film_row)
        out_film.writerow(film_row)


    if row[4] == 'Winner' or row[2] == "Oscar Year":
        if oscar_row not in oscar_lst:
            oscar_lst.append(oscar_row)
            out_oscar.writerow(oscar_row)
    helper(studio_row, out_studio, studio_lst)
    helper(directors_row, out_directors, directors_lst)
    helper(authors_row, out_authors, authors_lst)
    helper(actors_row, out_actors, actors_lst)


# return the list of all tables
# CHANGE!!!
def get_names():
    return ["film_t", "oscar_t", "studio_t", "actors_t", "directors_t",
            "authors_t"]


if __name__ == "__main__":
    process_file()
