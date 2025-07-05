from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>Python Calculator</title>
<h2>Simple Calculator</h2>
<form method="post">
  <input name="a" type="number" required> 
  <select name="op">
    <option value="+">+</option>
    <option value="-">-</option>
    <option value="*">*</option>
    <option value="/">/</option>
  </select>
  <input name="b" type="number" required>
  <button type="submit">Calculate</button>
</form>

{% if result is not none %}
  <h3>Result: {{ result }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["op"]
        try:
            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                result = a / b
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
