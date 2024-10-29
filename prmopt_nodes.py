
import os
import torch
from PIL import Image
import folder_paths
import random
import string

current_folder = os.path.dirname(os.path.abspath(__file__))


# 表情字典
expressions = {
    "自然中性表情": "neutral expression",
    "淡淡的微笑": "subtle smile",
    "温和的微笑": "gentle smile",
    "明亮的笑容": "bright smile",
    "露齿灿烂笑容": "big smile showing teeth",
    "闭眼大笑": "laugh with closed eyes",
    "职业性微笑": "professional smile",
    "眼睛闪烁的开心表情": "happy expression with sparkling eyes",
    "欢快表情": "joyful expression",
    "兴奋表情": "excited expression",
    "满足的表情": "content expression",
    "平和的表情": "peaceful expression",
    "宁静的表情": "serene expression",
    "梦幻的表情": "dreamy expression",
    "严肃表情": "serious expression",
    "专注表情": "focused expression",
    "坚定的表情": "determined expression",
    "自信的表情": "confident expression",
    "思考的表情": "thoughtful expression",
    "沉思的表情": "contemplative expression",
    "惊讶表情": "surprised expression",
    "震惊表情": "shocked expression",
    "好奇表情": "curious expression",
    "困惑表情": "confused expression",
    "害羞表情": "shy expression",
    "调皮表情": "playful expression",
    "顽皮表情": "mischievous expression",
    "悲伤表情": "sad expression",
    "忧郁表情": "melancholic expression",
    "担忧表情": "worried expression"
}

# 眼神变化字典
eye_expressions = {
    "直视前方": "looking straight ahead",
    "向上看": "looking up",
    "向下看": "looking down",
    "侧目": "looking to the side",
    "望向远方": "looking into distance",
    "闭眼": "eyes closed",
    "半闭眼": "half-closed eyes"
}


class CXH_Prompt_Expressions:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        chinese_angles = [exp for exp in expressions.keys()]
        eye_exp = [eye for eye in eye_expressions.keys()]
        return {
            "required": {
               "exp": (chinese_angles,{"default":"自然中性表情"}),
               "eye": (eye_exp,{"default":"直视前方"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("out",)
    FUNCTION = "gen"
    OUTPUT_NODE = False
    CATEGORY = "CXH/LLM"

    def gen(self, exp,eye):

        return (expressions[exp]+","+ eye_expressions[eye],)
    
