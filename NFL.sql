CREATE TABLE League (
    League_name varchar(3), 
    commissioner_fname varchar(20), 
    commissioner_lname varchar(20),
    PRIMARY KEY (League_name)
);
CREATE TABLE Owner (
    owner_id bigint,
    owner_fname varchar(20),
    owner_lname varchar(20),
    league_name varchar(3),
    PRIMARY KEY (owner_id),
    FOREIGN KEY (league_name) REFERENCES League(League_name)
);
CREATE TABLE Team (
    team_name varchar(35),
    team_location varchar(35),
    league_name varchar(3),
    owner_id bigint,
    PRIMARY KEY (team_name),
    FOREIGN KEY (league_name) REFERENCES League(League_name),
    FOREIGN KEY (owner_id) REFERENCES Owner(owner_id)
);
CREATE TABLE Employee (
    emp_num char(5),
    emp_fname varchar(20),
    emp_lname varchar(20),
    emp_dob date,
    emp_type varchar(20),
    emp_salary numeric(10,2),
    team_name varchar(35),
    PRIMARY KEY (emp_num),
    FOREIGN KEY (team_name) REFERENCES Team(team_name)
);
CREATE TABLE Coach (
    emp_num char(5),
    coach_position varchar(20),
    team_name varchar(35),
    PRIMARY KEY (emp_num),
    FOREIGN KEY (team_name) REFERENCES Team(team_name)
);
CREATE TABLE Player (
    emp_num char(5),
    player_position varchar(20),
    team_name varchar(35),
    PRIMARY KEY (emp_num),
    FOREIGN KEY (team_name) REFERENCES Team(team_name)
);
CREATE TABLE Season (
    season_year bigint,
    season_start_week date,
    season_end_week date,
    PRIMARY KEY (season_year)
);
CREATE TABLE Game (
    game_num int,
    visiting_team varchar(35),
    home_team varchar(35),
    season_year bigint,
    PRIMARY KEY (game_num),
    FOREIGN KEY (season_year) REFERENCES season(season_year)
);
CREATE TABLE Schedule (
    team_name varchar(35),
    game_num int,
    sched_opponent varchar(35),
    FOREIGN KEY (game_num) REFERENCES Game(game_num)
);
