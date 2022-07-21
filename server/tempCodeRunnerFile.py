@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form(['location'])
    bhk = int(request.form['bhk'])
    bath= int(request.form['bath'])
    
    response= jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    return response