INSERT INTO league VALUES("AFL","Roger","Goodbell");

INSERT INTO owner VALUES
(1,"Rob","Walton","AFL"),
(2,"David","Tepper","AFL"),
(3,"Kim","Pegula","AFL"), 
(4,"Jimmy","Haslam","AFL"), 
(5,"Steve","Tisch","AFL");

INSERT INTO team VALUES
("Carolina Panthers","Carolina","AFL",2),
("Denver Broncos","Denver","AFL",1),
("Buffalo Bills","New York","AFL",3),
("Cleveland Browns","Cleveland","AFL",4),
("New York Giants","New York","AFL",5);

INSERT INTO employee VALUES
("CP0C","Steve","Wilkes","1969-08-08","coach",50000,"Carolina Panthers"),
("CP01","Baker","Mayfield","1995-04-14","player",100000,"Carolina Panthers"),
("CP02","Samuel","Darnold","1997-06-05","player",110000,"Carolina Panthers"),
("CPO3","Laviska","Shenault","1998-10-05","player",105000,"Carolina Panthers"),
("CPO4","Jaycee","Horn","1999-11-26","player",125000,"Carolina Panthers"),
("DB0C","Nathaniel","Hackett","1979-12-19","coach",75000,"Denver Broncos"),
("DB01","Russell","Wilson","1988-11-29","player",150000,"Denver Broncos"),
("DB02","Jerry","Jeudy","1999-04-24","player",175000,"Denver Broncos"),
("DB03","Courtland","Sutton","1995-10-10","player",167000,"Denver Broncos"),
("DB04","Patric","Surtain","2000-04-14","player",102000,"Denver Broncos");

INSERT INTO player VALUES
("CP01","quarterback","Carolina Panthers"),
("CP02","quarterback","Carolina Panthers"),
("CP03","wide receiver","Carolina Panthers"),
("CP04","cornerback","Carolina Panthers"),
("DB01","quarterback","Denver Broncos"),
("DB02","wide receiver","Denver Broncos"),
("DB03","wide receiver","Denver Broncos"),
("DB04","cornerback","Denver Broncos");

INSERT INTO coach VALUES
("CP0C","main","Carolina Panthers"),
("DB0C","main","Denver Broncos");

INSERT INTO season VALUES
(2018,"2018-04-08","2018-07-08"),
(2019,"2019-06-08","2019-09-08"),
(2020,"2020-02-08","2020-05-08"),
(2021,"2020-05-08","2020-08-08");

INSERT INTO game VALUES
(1,"Carolina Panthers","Denver Broncos",2019),
(2,"Clevelands Browns","Buffalo Bills",2020),
(3,"New York Giants","Denver Broncos",2018),
(4,"Carolina Panthers","Buffalo Bills",2021),
(5,"New York Giants","Cleveland Browns",2019),
(6,"Buffalo Bills","Denver Broncos",2021);

INSERT INTO schedule VALUES
("Denver Broncos",1,"Carolina Panthers"),
("Buffalo Bills",2,"Clevelands Browns"),
("Denver Broncos",3,"New York Giants"),
("Buffalo Bills",4,"Carolina Panthers"),
("Cleveland Browns",5,"New York Giants"),
("Denver Broncos",6,"Buffalo Bills");

--show all quarterbacks

select employee.emp_fname,employee.emp_lname FROM employee 
join player on employee.emp_num = player.emp_num
where player.player_position = "quarterback";

select employee.emp_fname,employee.emp_lname,owner.owner_fname,owner.owner_lname
from employee join team on employee.team_name = team.team_name
join owner on team.owner_id = owner.owner_id;

select distinct employee.emp_fname,employee.emp_lname from
player join employee on employee.emp_num = player.emp_num 
join team on employee.team_name = team.team_name
join game on game.home_team = team.team_name
where player.player_position = "cornerback";

select game.game_num,season.season_start_week,season.season_end_week from
game join season on game.season_year = season.season_year
where season.season_year > 2019;

aggregate

select employee.team_name,count(*)"Number of employees"
from employee
group by employee.team_name
order by count(*) desc;

DELIMITER $$ 
CREATE TRIGGER insert_emp 
AFTER INSERT ON employee for EACH ROW 
BEGIN DECLARE msg varchar(50); 
DECLARE val int; 
SET msg = ('no. of employees in team exceeds 5');
SET val = (SELECT count(*) from employee WHERE team_name=new.team_name GROUP BY team_name); 
if val > 5 
THEN SIGNAL SQLSTATE '45000' 
SET MESSAGE_TEXT = msg; 
END IF; 
END $$

select employee.team_name,SUM(employee.emp_salary)"Sum of salary" 
from employee group by employee.team_name;

select player.player_position,AVG(employee.emp_salary)"AVG salary per position"
from player join employee on player.emp_num = employee.emp_num 
group by player_position;

select * from employee
group by emp_salary
order by emp_salary desc limit 1,1;

select team_name from team
union
select visiting_team from game;

select team_name from team
union all
select home_team from game where season_year > 2019;

select owner.owner_fname,owner.owner_lname from 
owner join team on owner.owner_id = team.owner_id
where team.team_name not in (select team_name from employee);

select * from team 
where team.team_name not in (select home_team from game);

DELIMITER $$ 
CREATE PROCEDURE backup() 
BEGIN 
DECLARE done INT DEFAULT 0; 
DECLARE emp_num CHAR(5); 
DECLARE emp_fname VARCHAR(20); 
DECLARE emp_lname VARCHAR(20); 
DECLARE emp_dob date; 
DECLARE emp_type VARCHAR(20); 
DECLARE emp_salary DECIMAL(10,2);
DECLARE team_name VARCHAR(35);  
DECLARE emp_cursor CURSOR FOR SELECT * FROM employee; 
DECLARE CONTINUE HANDLER FOR NOT FOUND 
SET done = 1; OPEN emp_cursor; 
label: LOOP FETCH emp_cursor INTO emp_num,emp_fname,emp_lname,emp_dob,emp_type,emp_salary,team_name; 
INSERT INTO backup_table VALUES(emp_num,emp_fname,emp_lname,emp_dob,emp_type,emp_salary,team_name); IF done = 1 THEN LEAVE label; 
END IF; 
END LOOP; 
CLOSE emp_cursor; 
END $$
DELIMITER ; 

CREATE TABLE backup_table (
    emp_num char(5),
    emp_fname varchar(20),
    emp_lname varchar(20),
    emp_dob date,
    emp_type varchar(20),
    emp_salary numeric(10,2),
    team_name varchar(35),
    PRIMARY KEY (emp_num)
);

DELIMITER $$ 
CREATE FUNCTION avgSal(teamName varchar(35)) 
RETURNS decimal(10,2)
DETERMINISTIC 
BEGIN 
DECLARE av_sal decimal(10,2);
SET av_sal = (SELECT AVG(emp_sal) from employee where team_name=teamName GROUP BY team_name);
RETURN av_sal;
END $$
DELIMITER ;