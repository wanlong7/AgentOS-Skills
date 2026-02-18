import requests

def get_weather(city):
    """
    通过外部接口获取天气原始数据
    """
    try:
        # 针对中文城市名，这个接口支持拼音或直接输入
        url = f"https://wttr.in/{city}?format=%C+%t"
        # 加上 headers 模拟浏览器，防止被屏蔽
        headers = {'User-Agent': 'curl/7.64.1'}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            return response.text
        else:
            return "无法获取天气数据"
    except Exception as e:
        return f"查询出错: {str(e)}"

# 测试代码（可选）
if __name__ == "__main__":
    print(get_weather("Beijing"))