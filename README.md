# sub_agent_apt
The webservice api to handle the backend process of mark1 and sub agent 

# setting
Flask 0.12.1 <br >
textrank4zh 0.3 <br >
gensim 3.4.0 <br >

## create new agent
Input json format:
```json
{
	"system_id":12312,
	"agent":[
		{
		"agent_ID": 1290378912,
		"agent_name": "急救",
         "intents": [
            {
              "intent_name": "急救_流鼻血",
              "training_phrases": [
                "流鼻血點算呀","流鼻血點做好"
              ],
              "response_text": "首先,坐著，但別躺下,讓頭部高過心臟可以減少血流.之後,以拇指、食指一起由鼻翼往中間按壓至少5分鐘，張嘴呼吸,按壓約5分鐘後，如仍未止血，再繼續壓10分鐘."
            }
          ]}]
}
```

## update exist agent
Input json format:
```json
{
	"system_id":12312,
	"agent":[
		{
		"agent_ID": 1290378912,
		"agent_name": "急救",
         "intents": [
            {
              "intent_name": "急救_流鼻血",
              "training_phrases": [
                "流鼻血點算呀","流鼻血點做好"
              ],
              "response_text": "首先,坐著，但別躺下,讓頭部高過心臟可以減少血流.之後,以拇指、食指一起由鼻翼往中間按壓至少5分鐘，張嘴呼吸,按壓約5分鐘後，如仍未止血，再繼續壓10分鐘."
            }
          ]}]
}
```

## get_result
Url link:/sub_agent
Input json format:
```json
{
	"system_id":12312,
	"text":"如果眼睛發炎應該要點做"
}
```

Output json format:
```json
{
    "Agent": "急救",
    "Intent": "急救_眼睛發炎",
    "ResolvedQuery": "如果眼睛發炎應該要點做",
    "Responses": [
        "輕眨眼睛,輕輕擦掉入侵物,用冰敷,清洗眼睛"
    ],
    "Result": [
        {
            "Intent": "急救_流鼻血",
            "Source": 0.4999446227483934,
            "phrase": "流鼻血點算呀"
        },
        {
            "Intent": "急救_流鼻血",
            "Source": 0.5428879865355242,
            "phrase": "流鼻血點做好"
        },
        {
            "Intent": "急救_皮膚過敏",
            "Source": 0.5865590228505326,
            "phrase": "皮膚敏感點算"
        },
        {
            "Intent": "急救_皮膚過敏",
            "Source": 0.5865590228505326,
            "phrase": "皮膚過敏點算"
        },
        {
            "Intent": "急救_心臟病發",
            "Source": 0.45033203980891506,
            "phrase": "心臟病發需要做啲咩嘢"
        },
        {
            "Intent": "急救_心臟病發",
            "Source": 0.29113979681357305,
            "phrase": "心臟病發"
        },
        {
            "Intent": "急救_骨折",
            "Source": 0.6122415042219606,
            "phrase": "骨折需要做啲咩嘢"
        },
        {
            "Intent": "急救_骨折",
            "Source": 0.5296278035066421,
            "phrase": "骨折點算"
        },
        {
            "Intent": "急救_骨折",
            "Source": 0.5725711672937729,
            "phrase": "骨折點做好"
        },
        {
            "Intent": "急救_中暑",
            "Source": 0.6026603484852697,
            "phrase": "中暑需要做啲咩嘢"
        },
        {
            "Intent": "急救_中暑",
            "Source": 0.5200466477699512,
            "phrase": "中暑點算"
        },
        {
            "Intent": "急救_中暑",
            "Source": 0.5629900115570821,
            "phrase": "中暑點做好"
        },
        {
            "Intent": "急救_中暑",
            "Source": 0.4688230189991392,
            "phrase": "中暑"
        },
        {
            "Intent": "急救_溺水",
            "Source": 0.4584990306606323,
            "phrase": "溺水需要做啲咩嘢"
        },
        {
            "Intent": "急救_溺水",
            "Source": 0.37588532994531376,
            "phrase": "溺水點算"
        },
        {
            "Intent": "急救_溺水",
            "Source": 0.4188286937324446,
            "phrase": "溺水點做好"
        },
        {
            "Intent": "急救_溺水",
            "Source": 0.28496050177325793,
            "phrase": "溺水"
        },
        {
            "Intent": "急救_眼睛發炎",
            "Source": 0.8402051955540414,
            "phrase": "眼睛發炎需要做啲咩嘢"
        },
        {
            "Intent": "急救_眼睛發炎",
            "Source": 0.7575914948387229,
            "phrase": "眼睛發炎點算"
        },
        {
            "Intent": "急救_眼睛發炎",
            "Source": 0.8005348586258535,
            "phrase": "眼睛發炎點做好"
        },
        {
            "Intent": "急救_眼睛發炎",
            "Source": 0.7493013316187563,
            "phrase": "眼睛發炎"
        }
    ],
    "Score": 0.8402051955540414,
    "Speech": "輕眨眼睛,輕輕擦掉入侵物,用冰敷,清洗眼睛",
    "Success": true,
    "Threshold": 0.6
}
```
## delete_agent
Url link:/delete_agent
```json
{
    "system_id":12312,
    "agent_id":12312
}
```