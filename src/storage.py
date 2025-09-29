import json
from streamlit_js_eval import streamlit_js_eval 

class Storage:
    KEY = "chat_history"

    @staticmethod
    def load_history():
        saved = streamlit_js_eval(
            js_expression=f"window.localStorage.getItem('{Storage.KEY}')",
            key='load_history',
        )
        try:
            return json.loads(saved) if saved else []
        except:
            return []
        
    @staticmethod
    def save_history(history):
        streamlit_js_eval(
            js_expression=f"window.localStorage.setItem('{Storage.KEY}', '{json.dumps(history)}')",
            key='save_history',
        )

    @staticmethod
    def clear_history():
        streamlit_js_eval(
            js_expression=f"window.localStorage.removeItem('{Storage.KEY}')",
            key='clear_history',
        )