import json
from streamlit_js_eval import streamlit_js_eval 

class storage:
    KEY = "chat_history"

    @staticmethod
    def load_history():
        saved = streamlit_js_eval(
            js_expression=f"window.localStorage.getItem('{storage.KEY}')",
            key='load_history',
        )
        try:
            return json.loads(saved) if saved else []
        except:
            return []
        
    @staticmethod
    def save_history(history):
        streamlit_js_eval(
            js_expression=f"window.localStorage.setItem('{storage.KEY}', '{json.dumps(history)}')",
            key='save_history',
        )

    @staticmethod
    def clear_history():
        streamlit_js_eval(
            js_expression=f"window.localStorage.removeItem('{storage.KEY}')",
            key='clear_history',
        )