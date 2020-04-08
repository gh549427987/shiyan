import datetime
import flask
import redis

app = flask.Flask('shiyanlou-sse-chat')
app.secret_key = 'shiyanlou'
app.config['DEBUG'] = True
r = redis.StrictRedis()

@app.route('/')
def home():
    if 'user' not in flask.session:
        return flask.redirect('/login')
    user = flask.session['user']
    return flask.render_template('home.html', user=user)

def event_stream():
    pubsub = r.pubsub()
    pubsub.subscribe('chat')
    for message in pubsub.listen():
        data = message['data']
        if type(data) == bytes:
            yield 'data: {}\n\n'.format(data.decode())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        flask.session['user'] = flask.request.form['user']
        return flask.redirect('/')
    return ('<form action="" method="post">User Name: <input name="user">'
            '<input type="submit" value="login" /></form>')

@app.route('/post', methods=['POST'])
def post():
    message = flask.request.form['message']
    user = flask.session.get('user', 'anonymous')
    now = datetime.datetime.now().replace(microsecond=0).time()
    r.publish('chat', '[{}] {}: {}\n'.format(now.isoformat(), user, message))
    return flask.Response(status=204)

@app.route('/stream')
def stream():
    return flask.Response(event_stream(), mimetype='text/event-stream')

