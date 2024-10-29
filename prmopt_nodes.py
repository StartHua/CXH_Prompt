
import os
import torch
from PIL import Image
import folder_paths
import random
import string

current_folder = os.path.dirname(os.path.abspath(__file__))


# 表情字典
expressions = {
    "自然中性表情": "A relaxed and neutral expression with calm eyes and brows.",
    "淡淡的微笑": "A subtle smile with slightly upturned lips, exuding gentle warmth.",
    "温和的微笑": "A gentle smile with curved eyes and softly upturned lips, like a warm breeze.",
    "明亮的笑容": "A bright smile with sparkling eyes and slightly flushed cheeks.",
    "露齿灿烂笑容": "A broad, toothy smile with eyes crinkling at the corners, radiating pure joy.",
    "闭眼大笑": "A hearty laugh with eyes joyfully closed and mouth wide open.",
    "职业性微笑": "A professional smile with steady, courteous eyes and a perfectly curved mouth.",
    "眼睛闪烁的开心表情": "A joyful expression with eyes sparkling like stars and an undeniable sense of happiness.",
    "欢快表情": "A lively expression with eyebrows raised and eyes full of joy.",
    "兴奋表情": "An excited expression with shining eyes and an exuberant smile.",
    "满足的表情": "A content expression with relaxed brows and a satisfied smile.",
    "平和的表情": "A serene expression with calm features and a sense of inner peace.",
    "宁静的表情": "A tranquil expression with gentle eyes and a peaceful demeanor.",
    "梦幻的表情": "A dreamy expression with slightly unfocused eyes and a faint smile.",
    "严肃表情": "A serious expression with slightly furrowed brows and a focused gaze.",
    "专注表情": "An attentive expression with intense eyes and a slight furrow of concentration.",
    "坚定的表情": "A determined expression with steady eyes and a resolute chin.",
    "自信的表情": "A confident expression with firm eyes and an assured smile.",
    "思考的表情": "A thoughtful expression with furrowed brows and a contemplative gaze.",
    "沉思的表情": "A pensive expression with deep eyes and a hint of distraction.",
    "惊讶表情": "A surprised expression with raised brows and wide, open eyes.",
    "震惊表情": "A shocked expression with dilated pupils and a look of astonishment.",
    "好奇表情": "A curious expression with wide eyes and slightly raised brows.",
    "困惑表情": "A puzzled expression with furrowed brows and a hint of confusion.",
    "害羞表情": "A shy expression with blushing cheeks and a bashful smile.",
    "调皮表情": "A playful expression with mischievous eyes and a cheeky smile.",
    "顽皮表情": "A playful expression with lively eyes and a mischievous grin.",
    "悲伤表情": "A sad expression with downcast eyes and a somber mouth.",
    "忧郁表情": "A melancholic expression with slightly downturned lips and a hint of sorrow.",
    "担忧表情": "A worried expression with furrowed brows and anxious eyes."
}




class CXH_Prompt_Expressions:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        chinese_angles = [exp for exp in expressions.keys()]
        return {
            "required": {
               "exp": (chinese_angles,{"default":"自然中性表情"})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("out",)
    FUNCTION = "gen"
    OUTPUT_NODE = False
    CATEGORY = "CXH/LLM"

    def gen(self, exp):

        return (expressions[exp],)
    