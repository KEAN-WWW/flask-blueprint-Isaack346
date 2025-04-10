from flask import Flask, render_template
from application.bp.homepage.homepage import homepage

# initialize Flask service and set global template folder
app = Flask(__name__, template_folder="templates")

# register blueprint
app.register_blueprint(homepage)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
