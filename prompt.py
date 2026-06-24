def build_prompt(data):
    return f"""你是一个专业旅行规划师。请根据用户信息生成旅行行程，严格按照下方 JSON 格式输出，不要输出任何其他内容，不要加解释，不要加 markdown 代码块。

输出格式（严格遵守，字段名不可更改）：
{{
  "destination": "目的地",
  "days": 天数,
  "people": 人数,
  "budget": "预算",
  "style": "风格",
  "schedule": [
    {{
      "day": 1,
      "morning":   {{ "activity": "上午活动", "transport": "交通方式", "food": "餐饮推荐" }},
      "afternoon": {{ "activity": "下午活动", "transport": "交通方式", "food": "餐饮推荐" }},
      "evening":   {{ "activity": "晚上活动", "transport": "交通方式", "food": "餐饮推荐" }}
    }}
  ]
}}

用户信息：
目的地：{data['destination']}
天数：{data['days']}
人数：{data['people']}
预算：{data['budget']}
风格：{data['style']}
必去地点：{data.get('must_go', '无')}

注意：
- schedule 数组必须有 {data['days']} 个元素，对应每一天
- 每天必须包含 morning / afternoon / evening 三个字段
- 每个时段必须包含 activity / transport / food 三个字段
- 只输出 JSON，第一个字符必须是 {{，最后一个字符必须是 }}
"""