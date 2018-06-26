# coding=UTF-8
from gensim import models
from textrank4zh import TextRank4Keyword
import config as config,random
import text_similarity as ts
from summa import keywords
from firebase import firebase
fb = firebase.FirebaseApplication(config.CUSTOM_ACCESS_URL, None)

testing = {
        "system_id":12312,
        "agents":[{
                "agent_ID": 1290378912,
                "agent_name": "firstaid",
                 "intents": [
                    {
                      "intent_name": "first_aaid",
                      "training_phrases": [
                        "Nosebleeds","what should i do when nosebleeds"
                      ],
                      "response_text": ["首先,坐著，但別躺下,讓頭部高過心臟可以減少血流.之後,以拇指、食指一起由鼻翼往中間按壓至少5分鐘，張嘴呼吸,按壓約5分鐘後，如仍未止血，再繼續壓10分鐘."]
                    }
                  ]}]
}


def get_result(system_id,threshold,text):
    intent_response = "No any match value"
    intent_name = ""
    result = get_user_db()
    intent_cost = 0
    entities_cost = 0
    num_count = 0

    return_result = {
        "Success": True,
        "ResolvedQuery":text,
        "Agent": "",
        "Intent": "",
        "Responses": [],
        "Result":[],
        "Score": 0,
        "Threshold": threshold,
        "Speech": ""
}

    for firebase_id in result:
        item = result[firebase_id]
    if item["system_id"] == system_id:
        d = item["agents"]
        print(item["agents"])
        return_result["Agent"] = d[0]["agent_name"]

    try:
        # the default word_min_len is 1
        print("checking similar...")
        for word in keywords.keywords(text):
            num_count += 1
        print("num_count:",num_count)

        for intent in d[0]["intents"]:
            intent_cost = 0
            for phrase in intent["training_phrases"]:
                print("check phrase:" + phrase)
                print(text,":",phrase)
                entities_cost = ts.sentence_similarity(text,phrase)
                print(entities_cost)
                if entities_cost >= intent_cost:
                    intent_cost = entities_cost
                    intent_name = intent["intent_name"]
                    intent_response = intent["response_text"]
                return_result["Result"].append({"Intent":intent["intent_name"],"phrase":phrase,"Source":entities_cost})
        if intent_cost < threshold:
            return_result["Success"] = False
        else:
            return_result["Intent"] = intent_name
            return_result["Responses"] = intent_response
            return_result["Score"] = intent_cost
            return_result["Speech"] = random.choice(intent_response)

            return return_result

    except Exception as e:
        return str(repr(e))


def get_result_inget(system_id,text,model,d):
    # get the result by enter the system_id and text (now default as hard code)

    # after select the data by the api
    RESULT_INTENT = ""
    INTENT_COST = 0
    NUM_COUNT = 0
    USER_INPUT_KEYWORDS=[]
    CHECKING_PERCENTAGE = 0.6
    # testing = {
    #     "Agent": {
    #         "Agent_name": "急救",
    #         "Intent": [
    #             {
    #                 "Intent_name": "急救_流鼻血",
    #                 "training_phrases": [{
    #                     "text": "流鼻血點算呀",
    #                     "phase": ["流鼻血", "點算"]
    #                 },{
    #                     "text":"流鼻血點做好",
    #                     "phase":["流鼻血","做好"]
    #                 }],
    #                 "Response_text": [
    #                     "首先,坐著，但別躺下,讓頭部高過心臟可以減少血流.之後,以拇指、食指一起由鼻翼往中間按壓至少5分鐘，張嘴呼吸,按壓約5分鐘後，如仍未止血，再繼續壓10分鐘."
    #                 ]
    #             },
    #             {
    #                 "Intent_name": "急救_皮膚過敏",
    #                 "training_phrases": [{
    #                     "text":"皮膚敏感點算",
    #                     "phase":["皮膚","點算"]
    #                 },{
    #                     "text":"皮膚過敏點算",
    #                     "phase":["過敏","皮膚","點算"]
    #                 }],
    #                 "Response_text": [
    #                     "皮膚過敏回應1of2",
    #                     "皮膚過敏回應2of2"
    #                 ]
    #             },
    #             {
    #                 "Intent_name": "SmallTalk_空姐抽",
    #                 "training_phrases": [{
    #                     "text": "空姐會抽菸嗎",
    #                     "phase": ["空姐","抽菸"]
    #                 }],
    #                 "Response_text": [
    #                     "血清中的膽固醇偏高"
    #                 ]
    #             }
    #         ]
    #     }
    # }

    try:
        user_input = TextRank4Keyword()
        agent_entities = TextRank4Keyword()
        user_input.analyze(text=text, lower=True, window=2)
        for word in user_input.get_keywords(10, word_min_len=2):
            NUM_COUNT += 1
            USER_INPUT_KEYWORDS.append(word.word)

        for intent in d['Agent']['Intent']:
            for entities in intent["Entities"]:
                agent_entities.analyze(text=entities, lower=True, window=2)
                ENTITIES_COST = 0
                for word in USER_INPUT_KEYWORDS:
                    cost = 0
                    for entities_item in agent_entities.get_keywords(10, word_min_len=2):
                        res = model.similarity(str(word), str(entities_item.word))
                        if res > cost:
                            cost = res
                    ENTITIES_COST += cost
                    if ENTITIES_COST / NUM_COUNT >= INTENT_COST:
                        INTENT_COST = ENTITIES_COST / NUM_COUNT
                        RESULT_INTENT = intent

        # for intent in testing['Agent']['Intent']:
        #     for training_pharses in intent['training_phrases']:
        #         ENTITIES_COST = 0
        #         for word in USER_INPUT_KEYWORDS:
        #             cost = 0
        #             for phase in training_pharses['phase']:
        #                 print("checking similarity", datetime.datetime.now())
        #                 res = model.similarity(str(word), str(phase))
        #                 if res > cost:
        #                     cost = res
        #                 ENTITIES_COST += cost
        #             if ENTITIES_COST / NUM_COUNT >= INTENT_COST:
        #                 INTENT_COST = ENTITIES_COST / NUM_COUNT
        #                 RESULT_INTENT = intent

        if INTENT_COST < CHECKING_PERCENTAGE:
            result = {
                "Success": False,
                "Error_message": "No match result"
            }
            return result
        else:
            result = {
                "Success": True,
                "Agent": d['Agent']['Agent_name'],
                "Intent": RESULT_INTENT['Intent_name'],
                "Responses": RESULT_INTENT['Response_text'],
                "Speech": RESULT_INTENT['Response_text'][0]
            }
            return result

    except Exception as e:
        result = {
            "Success": False,
            "Error_message": str(repr(e))
        }
        return result


def create_new_kits(system_id):
    try:
        result = {
            'system_id' : system_id
        }
        result = fb.post('/sub_agent_eng', result)
        return {"status":"success"}
    except Exception as ex:
        return {"status":"fail","exception":ex}


def create_agent(system_id,agent):
    # create a new agent by enter the system_id and agent
    # INSERT INTO custom_agent (agent_ID,system_ID,agent_name,response_text) VALUES (agent[],.....)
    # post connection on api
    try:
        result = get_user_db()
        ret_result = {
            "system_id": system_id,
            "agents": agent
        }
        print(ret_result)
        result = create_agent_db(ret_result)
        return result
    except Exception as ex:
        print(ex)
        return {"status":"fail","exception":ex}


def update_agent(system_id,agent):
    # update the exist agent by enter the system_id and agent
    # UPDATE custom_agent SET agent_ID = .... , .... WHERE agent_ID = ...
    try:
        result = get_user_db()
        for firebase_id in result:
            item = result[firebase_id]
            if item["system_id"] == system_id:
                result = {
                    "system_id":item["system_id"],
                    "agents":agent
                }
                update_db(result,firebase_id)
                return {"status":"success"}
    except Exception as ex:
        return {"status":"fail","exception":ex}


def delete_agent(system_id,agent_id):
    # delete the exist agent by search the system_id and agent_name
    # DELETE FROM custom_agent WHERE agent_name = ... && system_ID = ...
    try:
        result = get_user_db()
        for firebase_id in result:
            item = result[firebase_id]
            if item["system_id"] == system_id:
                result = {
                    "system_id":item["system_id"],
                    "agents": {}
                }
                for agent in item["system_id"]:
                    if agent["agent_id"] != agent_id:
                        result["agents"].append(agent)
    except Exception as ex:
        return {"status":"fail","exception":ex}


def update_db(result,firebase_id):
    try:
        print(firebase_id )
        result = fb.put('/sub_agent_eng', firebase_id,result)
        return {"status":"success"}
    except Exception as ex:
        print(ex)
        return {"status":"fail"}

def create_agent_db(result):
    try:
        result = fb.post('/sub_agent_eng',result)
        return {"status":"success"}
    except Exception as ex:
        print(ex)
        return {"status":"fail"}


def get_user_db():
    result = fb.get('/sub_agent_eng', None)
    return result
