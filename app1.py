from flask import Flask, jsonify , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invites.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Invite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}


@app.route("/", methods=["GET"])
def Welcome_Anonymousy():
    return jsonify({"message" : "Hi, You're warmly invited to the fucntion"})

@app.route("/<name>", methods=["GET"])
def Welcome_member(name):
    return jsonify({"message" : f" Hi {name}, You're warmly invited to the fucntion"})

@app.route("/invite", methods=["POST"])
def invite_member():
    data = request.get_json()
    name = data.get("name")

    invite = Invite(name=name)
    db.session.add(invite)
    db.session.commit()

    return jsonify({"message" : f" Hi {name}, You're warmly invited to the fucntion"})

@app.route("/invites", methods=["GET"])
def list_invites():
    invites = Invite.query.all()
    return jsonify([invite.to_dict() for invite in invites])


@app.route("/invite2", methods=["GET"])
def invite_member2():
    name = request.args.get("name", "Guest")  # <-- read from URL

    return jsonify({
        "message": f"Hi {name}, You're warmly invited to the function"
    })


@app.route("/getme", methods=["GET", "POST"])
def get_me():
    # Try reading JSON from request body for both GET and POST
    data = request.get_json(silent=True) or {}
    

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Return the data as JSON
    return jsonify({"received_data": data})



if __name__ == "__main__":
    # Create database tables (first time only)
    with app.app_context():
        db.create_all()    # <-- 4 spaces indentation inside with
    app.run(debug=True)     # <-- 4 spaces aligned with 'with'