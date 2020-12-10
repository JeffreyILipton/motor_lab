from flask import Flask, jsonify, request, abort, make_response
import stepper_commands

app = Flask(__name__)

motor_loc={'loc':5}
light={'power':False}


@app.route('/',methods=['GET', 'POST','PUT','DELETE'])
def index():
    return "You have made it to the motor control machine!"




#show the location of the motor
@app.route('/motor', methods=['GET'])
def get_motor():
    return jsonify({"motor_loc":motor_loc})

#update the location of the motor
@app.route('/motor', methods = ['PUT'])
def updateMotor():
    if (not request.json) or (not ('loc' in request.json)):
        abort(400)
    motor_loc['loc']=request.json.get('loc',motor_loc['loc'])
    stepper_commands.move_to(motor_loc['loc'])
    return jsonify({'motor_loc':motor_loc}), 200
    abort(404)
 
 
 
#show the status of the laser 
@app.route('/laser', methods=['GET'])
def get_laser():
    return jsonify({"light":light})

#update the status of the laser
@app.route('/laser', methods = ['PUT'])
def updateLaser():
    if (not request.json) or (not ('power' in request.json)):
        abort(400)
    light['power']=request.json.get('power',light['power'])
    stepper_commands.toggle_LED(light['power'])
    return jsonify({'light':light}), 200
    abort(404)
    
    
    
    

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'That ID is invalid'}),404)

if __name__ == '__main__':
    app.run(debug=True)