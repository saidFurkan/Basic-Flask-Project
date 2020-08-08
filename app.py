from flask import Flask, render_template, request, redirect, url_for
import getProductInfo

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', pageTitle = "Anasayfa")

@app.route('/search', methods=["POST"])
def search():
    keyword = request.form.get("title")
    sites = request.form.getlist("options")
    size = request.form.get("size")

    result = getProductInfo.search(searchKey=keyword, productSize = size, sites = sites)

    # for i in result:
    #     for p in i:
    #         print("\nName:\t{}\nPrice:\t{}\nLink:\t{}\n".format(p.name, p.price, p.link))

    if result != []:
        return render_template('showResult.html', result=result, sites=sites, resultSize=int(size), count=len(sites), pageTitle="Show Result")

    else:
        print("Error")
        return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True) #, host='192.168.x.x')
