#coding=UTF-8
from flask import Flask,jsonify,request
import sub_agent_api_chinese_version.config as config
from sub_agent_api_chinese_version.sub_agent_api import get_result,get_result_inget,create_agent,create_new_kits,update_agent,delete_agent
app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'enter api system'


@app.route('/sub_agent', methods=['POST'])
def api_article():
    system_id = request.json['system_id']
    if request.args.get("threshold") == "" or request.args.get("threshold") is None:
        threshold = 0.6
    else:
        threshold = request.args.get("threshold")

    text = request.json['text']
    result = get_result(system_id,threshold,text,config.MODLES)
    return jsonify(result)


@app.route('/sub_agent', methods  =['GET'])
def api_get_article():
    system_id = request.args.get("system_id")
    text = request.args.get("text")
    try:
        result = get_result_inget(system_id,text,config.model,config.d)

    except Exception as e:
        return jsonify(str(repr(e)))
    return result


@app.route('/create_agent', methods=['POST'])
def api_create_article():
    system_id = request.json['system_id']
    agent = request.json['agent']
    result = create_agent(system_id,agent)
    return jsonify(result)

@app.route('/create_new_kit', methods=['POST'])
def api_create_kit_article():
    system_id = request.json['system_id']
    agent = request.json['agent']
    result = create_new_kits(system_id,agent)
    return jsonify(result)

@app.route('/update_agent',methods=['POST'])
def api_insert_article():
    system_id = request.json['system_id']
    agent = request.json['agent']
    result = update_agent(system_id,agent)
    return jsonify(result)


@app.route('/delete_agent',methods=['POST'])
def api_delete_article():
    system_id = request.json['system_id']
    agent_id = request.json['agent_id']
    result = delete_agent(system_id,agent_id)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
