create table film_t
(
    film_name      varchar(100),
    oscar_year     int                      not null,
    studio         varchar,
    release_year   int                      not null,
    duration       int,
    genres         varchar(100),
    imdb_rating    float,
    imdb_votes     int,
    content_rating varchar(100),
    directors      varchar,
    authors        varchar,
    actors         varchar,
    filmId         varchar(100) primary key not null

);

create table oscar_t
(
    oscar_year int primary key not null,
    filmId     varchar(100)    not null
);

create table studio_t
(
    studio varchar(100) not null,
    filmId varchar(100) not null,
    primary key (studio, filmId)
);


create table directors_t
(
    directors varchar(100) not null,
    filmId    varchar(100) not null,
    primary key (directors, filmId)
);

create table authors_t
(
    authors varchar(100) not null,
    filmId  varchar(100) not null,
    primary key (authors, filmId)
);

create table actors_t
(
    actors varchar(100) not null,
    filmId varchar(100) not null,
    primary key (actors, filmId)
);





