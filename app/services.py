import os
from flask import json
import requests
from fuzzywuzzy import fuzz, process


class Services:

    def __init__(self, app):
        self.app = app
    
    def process_message(self, message):
        try:
            
            message = json.loads(message)
            replyToken = message["events"][0]["replyToken"]
            typeMessage = message["events"][0]["message"]["type"]
            textMessage = message["events"][0]["message"]["text"]

            replyTextError = [
                {
                    "type": "text",
                    "text": "I don't know what you mean. Please try again."
                }
            ]

            textReply = []

            if (typeMessage == "text"):
                internal = self.checkerInternal(textMessage)
                if internal == "จำนวนเห็นชอบ" :
                    count = self.app.mongo.data_vote.count_documents({"vote": "เห็นชอบ"})
                    textReply = [
                        {
                            "type": "text",
                            "text": f"เห็นชอบ จำนวน {count} คน"
                        },
                    ]
                elif internal == "จำนวนไม่เห็นชอบ":
                    count = self.app.mongo.data_vote.count_documents({"vote": "ไม่เห็นชอบ"})
                    textReply = [
                        {
                            "type": "text",
                            "text": f"ไม่เห็นชอบ จำนวน {count} คน"
                        },
                    ]
                elif internal == "จำนวนที่ออกเสียง":
                    vote_criteria = {"$in": ["เห็นชอบ", "ไม่เห็นชอบ"]}
                    count = self.app.mongo.data_vote.count_documents({"vote": vote_criteria})
                    textReply = [
                        {
                            "type": "text",
                            "text": f"คนที่ออกเสียง จำนวน {count} คน"
                        },
                    ]
                elif internal == "จำนวนงดออกเสียง":
                    count = self.app.mongo.data_vote.count_documents({"vote": "งดออกเสียง"})
                    textReply = [
                        {
                            "type": "text",
                            "text": f"งดออกเสียง จำนวน {count} คน"
                        },
                    ]
                elif not internal:
                    return self.reply_message_error(replyToken, replyTextError)
                
                return self.reply_message_success(replyToken, textReply)
                    

        except Exception as e:
            print(e)
            return self.reply_message_error(replyToken, replyTextError)


    def checkerInternal(self, message):
        dataTrain = []
        file_path = os.path.join(os.path.dirname(__file__), 'train_data.json')
        with open(file_path, 'r', encoding='utf-8') as file:
                dataTrain = json.loads(file.read())

        texts = [data["label"] for data in dataTrain]

        best_match, score = process.extractOne(message, texts)
        threshold = 80

        if score >= threshold:
            for data in dataTrain:
                if data["label"] == best_match:
                    return data["value"]
        else:
            return


    def reply_message_error(self, replyToken, replyMessage):
        url = self.app.config['API_LINE']

        payload = json.dumps({
            "replyToken": replyToken,
            "messages": replyMessage
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.app.config['LINE_ACCESS_TOKEN']
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return


    def reply_message_success(self, replyToken, replyMessage):
        url = self.app.config['API_LINE']

        payload = json.dumps({
            "replyToken": replyToken,
            "messages": replyMessage
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.app.config['LINE_ACCESS_TOKEN']
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return