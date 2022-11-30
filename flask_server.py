from re import L
from flask import Flask,render_template,redirect,url_for,session,request
import mariadb
app = Flask(__name__)
app.secret_key = "secret"
conn = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         user='root',
         password='toor',
         database='nfl',
         autocommit=True)

cur = conn.cursor()

@app.route('/',methods = ['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    if(session['loggedin']):
        return render_template('home.html')
    else: 
        redirect(url_for('index'))
    
@app.route('/login',methods = ['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST':
        user = request.form['user']
        pw = request.form['pw']
        cur.execute('SELECT * FROM user WHERE username = %s AND password = %s;',(user,pw))
        record = cur.fetchone()
        if record:
            session['loggedin'] = True
            session['user'] = record[0]
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password. Try Again'
        return render_template('index.html',msg = msg)

@app.route('/insert',methods = ['GET','POST'])
def insert_mainp():
    return render_template("insert.html")

@app.route('/find',methods = ['GET','POST'])
def find_mainp():
    return render_template("find.html")

@app.route('/show',methods = ['GET','POST'])
def show_mainp():
    return render_template("show.html")

@app.route('/delete',methods = ['GET','POST'])
def delete_mainp():
    return render_template("delete.html")

@app.route('/update',methods = ['GET','POST'])
def update_mainp():
    return render_template("update.html")

@app.route('/show/coach',methods = ['GET','POST'])
def show_coach():
    query = """SELECT * FROM coach"""
    cur.execute(query)
    res = cur.fetchall()
    head = cur.description
    return render_template("show_coach.html",res=res,head=head)

@app.route('/show/employee',methods = ['GET','POST'])
def show_employee():
    query = """SELECT * FROM employee"""
    cur.execute(query)
    res = cur.fetchall()
    head = cur.description
    return render_template("show_employee.html",res=res,head=head)

@app.route('/show/game',methods = ['GET','POST'])
def show_game():
    query = """SELECT * FROM game"""
    cur.execute(query)
    res = cur.fetchall()
    head = cur.description
    return render_template("show_game.html",res=res,head=head)

@app.route('/show/league',methods = ['GET','POST'])
def show_league():
    query = """SELECT * FROM league"""
    cur.execute(query)
    res = cur.fetchall()
    head = cur.description
    return render_template("show_league.html",res=res,head=head)

@app.route('/show/owner',methods = ['GET','POST'])
def show_owner():
    query = """SELECT * FROM owner"""
    cur.execute(query)
    res = cur.fetchall()
    head = cur.description
    return render_template("show_owner.html",res=res,head=head)

@app.route('/show/player',methods = ['GET','POST'])
def show_player():
    query = """SELECT * FROM player"""
    cur.execute(query)
    res = cur.fetchall()
    head = cur.description
    return render_template("show_player.html",res=res,head=head)

@app.route('/show/schedule',methods = ['GET','POST'])
def show_schedule():
    query = """SELECT * FROM schedule"""
    cur.execute(query)
    res = cur.fetchall()
    head = cur.description
    return render_template("show_schedule.html",res=res,head=head)

@app.route('/show/season',methods = ['GET','POST'])
def show_season():
    query = """SELECT * FROM season"""
    cur.execute(query)
    res = cur.fetchall()
    head = cur.description
    return render_template("show_season.html",res=res,head=head)

@app.route('/show/team',methods = ['GET','POST'])
def show_team():
    query = """SELECT * FROM team"""
    cur.execute(query)
    res = cur.fetchall()
    head = cur.description
    return render_template("show_team.html",res=res,head=head)

@app.route('/insert/league',methods = ['GET','POST'])
def insert_league():
    return render_template('insert_league.html')

@app.route('/insert/league/server',methods = ['GET','POST'])
def insert_league_server():
    if request.method == 'POST':
        league_name = request.form['league_name']
        c_fname = request.form['c_fname']
        c_lname = request.form['c_lname']
        query = """INSERT INTO league VALUES('%s','%s','%s');"""%(league_name,c_fname,c_lname)
        cur.execute(query)
        return render_template("insert_league.html")

@app.route('/insert/team',methods = ['GET','POST'])
def insert_team():
    return render_template('insert_team.html')

@app.route('/insert/team/server',methods = ['GET','POST'])
def insert_team_server():
    if request.method == 'POST':
        t_name = request.form['t_name']
        t_loc = request.form['t_loc']
        league_name = request.form['league_name']
        owner_id = request.form['owner_id']
        query = """INSERT INTO league VALUES('%s','%s','%s',%s);"""%(t_name,t_loc,league_name,owner_id)
        cur.execute(query)
        return render_template("insert_league.html")

@app.route('/insert/owner',methods = ['GET','POST'])
def insert_owner():
    return render_template('insert_owner.html')

@app.route('/insert/owner/server',methods = ['GET','POST'])
def insert_owner_server():
    if request.method == 'POST':
        league_name = request.form['league_name']
        o_fname = request.form['o_fname']
        o_lname = request.form['o_lname']
        owner_id = request.form['owner_id']
        query = """INSERT INTO owner VALUES(%s,'%s','%s','%s');"""%(owner_id,o_fname,o_lname,league_name)
        cur.execute(query)
        return render_template("insert_owner.html")
    
@app.route('/insert/employee',methods = ['GET','POST'])
def insert_employee():
    return render_template('insert_employee.html')

@app.route('/insert/employee/server',methods = ['GET','POST'])
def insert_employee_server():
    if request.method == 'POST':
        e_num = request.form['e_num']
        e_fn = request.form['e_fn']
        e_ln = request.form['e_ln']
        e_dob = request.form['e_dob']
        e_type = request.form['e_type']
        e_sal = request.form['e_sal']
        team_name = request.form['t_name']
        query = """INSERT INTO employee VALUES('%s','%s','%s','%s','%s',%s,'%s');"""%(e_num,e_fn,e_ln,e_dob,e_type,e_sal,team_name)
        cur.execute(query)
        return render_template("insert_employee.html")

@app.route('/insert/coach',methods = ['GET','POST'])
def insert_coach():
    return render_template('insert_coach.html')

@app.route('/insert/coach/server',methods = ['GET','POST'])
def insert_coach_server():
    if request.method == 'POST':
        e_num = request.form['e_num']
        c_pos = request.form['c_pos']
        t_name = request.form['t_name']
        query = """INSERT INTO coach VALUES('%s','%s','%s');"""%(e_num,c_pos,t_name)
        cur.execute(query)
        return render_template("insert_coach.html")

@app.route('/insert/player',methods = ['GET','POST'])
def insert_player():
    return render_template('insert_player.html')

# @app.route('/insert/player/server',methods = ['GET','POST'])
# def insert_player_server():
#     if request.method == 'POST':
#         e_num = request.form['e_num']
#         p_pos = request.form['p_pos']
#         t_name = request.form['t_name']
#         query = """INSERT INTO player VALUES('%s','%s','%s');"""%(e_num,p_pos,t_name)
#         cur.execute(query)
#         return render_template("insert_player.html")

@app.route('/insert/season',methods = ['GET','POST'])
def insert_season():
    return render_template('insert_season.html')

@app.route('/insert/season/server',methods = ['GET','POST'])
def insert_season_server():
    if request.method == 'POST':
        s_year = request.form['s_year']
        s_sw = request.form['s_sw']
        s_ew = request.form['s_ew']
        query = """INSERT INTO season VALUES(%s,'%s','%s');"""%(s_year,s_sw,s_ew)
        cur.execute(query)
        return render_template("insert_season.html")

@app.route('/insert/game',methods = ['GET','POST'])
def insert_game():
    return render_template('insert_game.html')

@app.route('/insert/game/server',methods = ['GET','POST'])
def insert_game_server():
    if request.method == 'POST':
        s_year = request.form['s_year']
        g_num = request.form['g_num']
        ht = request.form['ht']
        vt = request.form['vt']
        query = """INSERT INTO game VALUES(%s,'%s','%s',%s);"""%(g_num,ht,vt,s_year)
        cur.execute(query)
        return render_template("insert_game.html")

@app.route('/insert/schedule',methods = ['GET','POST'])
def insert_schedule():
    return render_template('insert_schedule.html')

@app.route('/insert/schedule/server',methods = ['GET','POST'])
def insert_schedule_server():
    if request.method == 'POST':
        g_num = request.form['g_num']
        t_name = request.form['t_name']
        sched_name = request.form['sched_name']
        query = """INSERT INTO schedule VALUES(%s,'%s','%s');"""%(g_num,t_name,sched_name)
        cur.execute(query)
        return render_template("insert_schedule.html")

@app.route('/delete/league',methods = ['GET','POST'])
def delete_league():
    return render_template('delete_league.html')

@app.route('/delete/league/server',methods = ['GET','POST'])
def delete_league_server():
    if request.method == 'POST':
        l_name = request.form['l_name']
        query = """DELETE FROM league WHERE League_name = '%s'"""%(l_name)
        cur.execute(query)
        return render_template('delete_league.html')

@app.route('/delete/owner',methods = ['GET','POST'])
def delete_owner():
    return render_template('delete_owner.html')

@app.route('/delete/owner/server',methods = ['GET','POST'])
def delete_owner_server():
    if request.method == 'POST':
        o_id = request.form['o_id']
        query = """DELETE FROM owner WHERE owner_id = %s"""%(o_id)
        cur.execute(query)
        return render_template('delete_owner.html')

@app.route('/delete/team',methods = ['GET','POST'])
def delete_team():
    return render_template('delete_team.html')

@app.route('/delete/team/server',methods = ['GET','POST'])
def delete_team_server():
    if request.method == 'POST':
        t_name = request.form['t_name']
        query = """DELETE FROM team WHERE team_name = '%s'"""%(t_name)
        cur.execute(query)
        return render_template('delete_team.html')

@app.route('/delete/employee',methods = ['GET','POST'])
def delete_employee():
    return render_template('delete_employee.html')

@app.route('/delete/employee/server',methods = ['GET','POST'])
def delete_employee_server():
    if request.method == 'POST':
        e_num = request.form['e_num']
        query = """DELETE FROM employee WHERE emp_num = '%s'"""%(e_num)
        cur.execute(query)
        return render_template('delete_employee.html')

@app.route('/delete/coach',methods = ['GET','POST'])
def delete_coach():
    return render_template('delete_coach.html')

@app.route('/delete/coach/server',methods = ['GET','POST'])
def delete_coach_server():
    if request.method == 'POST':
        e_num = request.form['e_num']
        query = """DELETE FROM coach WHERE emp_num = '%s'"""%(e_num)
        cur.execute(query)
        return render_template('delete_coach.html')

@app.route('/delete/player',methods = ['GET','POST'])
def delete_player():
    return render_template('delete_player.html')

@app.route('/delete/player/server',methods = ['GET','POST'])
def delete_player_server():
    if request.method == 'POST':
        e_num = request.form['e_num']
        query = """DELETE FROM player WHERE emp_num = '%s'"""%(e_num)
        cur.execute(query)
        return render_template('delete_player.html')

@app.route('/delete/season',methods = ['GET','POST'])
def delete_season():
    return render_template('delete_season.html')

@app.route('/delete/season/server',methods = ['GET','POST'])
def delete_season_server():
    if request.method == 'POST':
        s_y = request.form['s_y']
        query = """DELETE FROM season WHERE season_year = %s"""%(s_y)
        cur.execute(query)
        return render_template('delete_season.html')

@app.route('/delete/game',methods = ['GET','POST'])
def delete_game():
    return render_template('delete_game.html')

@app.route('/delete/game/server',methods = ['GET','POST'])
def delete_game_server():
    if request.method == 'POST':
        g_num = request.form['g_num']
        query = """DELETE FROM game WHERE game_num = %s"""%(g_num)
        cur.execute(query)
        return render_template('delete_game.html')

@app.route('/find/employee',methods = ['GET','POST'])
def find_employee():
    return render_template('find_employee.html')

@app.route('/find/employee/server',methods = ['GET','POST'])
def find_employee_server():
    if request.method == 'POST':
        e_num = request.form['e_num']
        query = """SELECT * FROM employee WHERE emp_num = '%s'"""%(e_num)
        cur.execute(query)
        res = cur.fetchall()
        head = cur.description
        return render_template('find_employee.html',res = res,head = head)

@app.route('/find/owner',methods = ['GET','POST'])
def find_owner():
    return render_template('find_owner.html')

@app.route('/find/owner/server',methods = ['GET','POST'])
def find_owner_server():
    if request.method == 'POST':
        o_id = request.form['o_id']
        query = """SELECT * FROM owner WHERE owner_id = %s"""%(o_id)
        cur.execute(query)
        res = cur.fetchall()
        return render_template('find_owner.html',res = res)

@app.route('/update/coach',methods = ['GET','POST'])
def update_coach():
    return render_template('update_coach.html')

@app.route('/update/coach/server',methods = ['GET','POST'])
def update_coach_server():
    if request.method == 'POST':
        e_num = request.form['e_num']
        c_pos = request.form['c_pos']
        t_name = request.form['t_name']
        query = """UPDATE coach SET coach_position = '%s',team_name = '%s' WHERE emp_num = '%s'"""%(c_pos,t_name,e_num)
        cur.execute(query)
        new_query = """SELECT * FROM coach WHERE emp_num = '%s'"""%(e_num)
        cur.execute(new_query)
        res = cur.fetchall()
        head = cur.description
        return render_template("update_coach.html",res = res,head = head)

@app.route('/update/employee',methods = ['GET','POST'])
def update_employee():
    return render_template('update_eployee.html')

@app.route('/update/employee/server',methods = ['GET','POST'])
def update_employee_server():
    if request.method == 'POST':
        e_num = request.form['e_num']
        e_fn = request.form['e_fn']
        e_ln = request.form['e_ln']
        e_dob = request.form['e_dob']
        e_type = request.form['e_type']
        e_sal = request.form['e_sal']
        team_name = request.form['t_name']
        query = """UPDATE employee SET emp_fname = '%s',emp_lname = '%s',emp_dob = '%s',emp_type = '%s',emp_salary = %s,team_name = '%s' WHERE emp_num = '%s'"""%(e_fn,e_ln,e_dob,e_type,e_sal,team_name,e_num)
        cur.execute(query)
        new_query = """SELECT * FROM employee WHERE emp_num = '%s'"""%(e_num)
        cur.execute(new_query)
        res = cur.fetchall()
        head = cur.description
        return render_template("update_employee.html",res = res,head = head)

@app.route('/update/game',methods = ['GET','POST'])
def update_game():
    return render_template('update_game.html')

@app.route('/update/game/server',methods = ['GET','POST'])
def update_game_server():
    if request.method == 'POST':
        s_year = request.form['s_year']
        g_num = request.form['g_num']
        ht = request.form['ht']
        vt = request.form['vt']
        query = """UPDATE game SET season_year = %s,visiting_team = '%s',home_team = '%s' WHERE game_num = %s"""%(s_year,vt,ht,g_num)
        cur.execute(query)
        new_query = """SELECT * FROM game WHERE game_num = %s"""%(g_num)
        cur.execute(new_query)
        res = cur.fetchall()
        head = cur.description
        return render_template("update_game.html",res = res,head = head)

@app.route('/update/league',methods = ['GET','POST'])
def update_league():
    return render_template('update_league.html')

@app.route('/update/league/server',methods = ['GET','POST'])
def update_league_server():
    if request.method == 'POST':
        league_name = request.form['league_name']
        c_fname = request.form['c_fname']
        c_lname = request.form['c_lname']
        query = """UPDATE league SET commissioner_fname = '%s',commissioner_lname = '%s' WHERE league_name = '%s'"""%(c_fname,c_lname,league_name)
        cur.execute(query)
        new_query = """SELECT * FROM league WHERE league_name = '%s'"""%(league_name)
        cur.execute(new_query)
        res = cur.fetchall()
        head = cur.description
        return render_template("update_league.html",res = res,head = head)

@app.route('/update/player',methods = ['GET','POST'])
def update_player():
    return render_template('update_player.html')

@app.route('/update/player/server',methods = ['GET','POST'])
def update_player_server():
    if request.method == 'POST':
        e_num = request.form['e_num']
        p_pos = request.form['p_pos']
        t_name = request.form['t_name']
        query = """UPDATE player SET player_position = '%s',team_name = '%s' WHERE emp_num = '%s'"""%(p_pos,t_name,e_num)
        cur.execute(query)
        new_query = """SELECT * FROM player WHERE emp_num = '%s'"""%(e_num)
        cur.execute(new_query)
        res = cur.fetchall()
        head = cur.description
        return render_template("update_player.html",res = res,head = head)

@app.route('/update/team',methods = ['GET','POST'])
def update_team():
    return render_template('update_team.html')

@app.route('/update/team/server',methods = ['GET','POST'])
def update_team_server():
    if request.method == 'POST':
        t_name = request.form['t_name']
        t_loc = request.form['t_loc']
        league_name = request.form['league_name']
        owner_id = request.form['owner_id']
        query = """UPDATE team SET team_location = '%s',league_name = '%s',owner_id = %s WHERE team_name = '%s'"""%(t_loc,league_name,owner_id,t_name)
        cur.execute(query)
        new_query = """SELECT * FROM team WHERE team_name = '%s'"""%(t_name)
        cur.execute(new_query)
        res = cur.fetchall()
        head = cur.description
        return render_template("update_team.html",res = res,head = head)

@app.route("/query",methods = ['GET','POST'])
def query():
    return render_template("query.html")

@app.route("/query/server",methods = ['GET','POST'])
def query_server():
    if request.method == 'POST':
        query = request.form['query']
        cur.execute(query)
        res = cur.fetchall()
        head = cur.description
        return render_template("query.html",res = res,head = head)


if __name__ == '__main__':
    app.run(debug=True)