"""GitHub专业技能（本地可用版，修复content未定义错误）"""
def run(content, memory):
    """
    处理GitHub相关问题的核心函数
    :param content: 用户输入的完整内容（必传，修复变量未定义的关键）
    :param memory: 对话记忆（可选，暂未使用）
    :return: 格式化的回答
    """
    # 第一步：兜底验证，确保content变量一定存在（修复核心）
    if not content or content is None:
        return "❌ 未获取到你的问题，请重新输入（如：GitHub怎么创建仓库）"
    
    # 第二步：提取用户的核心问题（去掉提示词优化的冗余内容）
    # 兼容原始输入和优化后的提示词两种格式
    if "核心需求：" in content:
        core_question = content.split("核心需求：")[-1].split("\n")[0].strip()
    else:
        core_question = content.strip()
    
    # 第三步：针对"创建仓库"问题返回具体答案
    if "创建仓库" in core_question or "新建仓库" in core_question:
        answer = """
✅ GitHub创建仓库（新手一步一步来）：
1. 登录GitHub官网：https://github.com/（没有账号先注册）；
2. 点击右上角的「+」号 → 选择「New repository」（新建仓库）；
3. 填写关键信息：
   - Repository name：仓库名（必填，比如：my-first-repo）；
   - Description：仓库描述（可选，比如：我的第一个GitHub仓库）；
   - Visibility：仓库可见性（Public=公开，Private=私有，新手选Public）；
4. 可选优化：勾选「Add a README file」（自动创建README，方便别人了解仓库）；
5. 点击最下方的「Create repository」→ 仓库创建完成！

💡 新手注意：
- 仓库名不能有空格，可用下划线/短横线代替（如：my_first_repo）；
- 首次创建建议勾选README，避免仓库为空；
"""
    # 可扩展：添加其他GitHub问题的回答（比如"上传代码"）
    elif "上传代码" in core_question or "推送代码" in core_question:
        answer = """
✅ GitHub上传代码（新手版）：
1. 先在本地初始化Git（需安装Git）：
   - 打开终端，进入代码文件夹 → 执行：git init
   - 关联远程仓库：git remote add origin https://github.com/你的用户名/仓库名.git
2. 提交代码：
   - git add .（添加所有文件）
   - git commit -m "第一次提交"（备注提交信息）
3. 推送到GitHub：
   - git push -u origin main（推送到main分支）
💡 注意：首次推送需要登录GitHub账号验证。
"""
    # 兜底回答：未匹配到具体问题时返回通用指引
    else:
        answer = f"""
✅ 已收到你的GitHub问题：「{core_question}」
目前支持的问题：创建仓库、上传代码
如果是其他问题（如：删除仓库、分支管理），可补充说明，我会为你解答！
"""
    return answer

# 技能元信息（程序识别用，不用改）
SKILL_META = {
    "name": "github_skill",
    "version": "1.0.0",
    "description": "处理GitHub基础操作问题（修复content未定义错误）"
}
