from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Innovartus SaaS Application</h1>
    <p>Cloud Computing Case Study 3</p>
    """

if __name__ == "__main__":
    app.run(debug=True)