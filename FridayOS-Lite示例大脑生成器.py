# -*- coding: utf-8 -*-
"""云栈科技 模拟公司数据生成器 v2 —— 物料标准化版（固定种子，可复现）
v2 变化：结构化 frontmatter（全库可查询）、画像、信息来源脚注、MOC总览页、里程碑/时间线"""
import random, os, csv
random.seed(2026)
BASE = '/sessions/friendly-upbeat-wozniak/mnt/Friday/FridayOS-Lite/示例大脑-云栈科技'

SURN = "王李张刘陈杨黄赵吴周徐孙马朱胡郭何林罗高郑梁谢宋唐许韩冯邓曹彭曾肖田董潘袁蒋蔡余杜".strip()
M_GIVEN = ["伟","磊","强","俊杰","浩","宇航","子轩","志远","建国","晨","昊然","泽宇","凯","文博","睿","明轩","嘉豪","劲松","云飞","柏涛","一鸣","承宇","景行","卓",
"鹏飞","世杰","骁","润东","梓豪","彦祖","启航","思远","彬","岩","乐天","少卿","哲","卫东","海川","牧之"]
F_GIVEN = ["芳","娜","敏","静怡","丽","婷婷","雪","晓彤","梦琪","欣怡","雨桐","诗涵","佳音","若彤","蕊","紫萱","可欣","海燕","慧","俪","映雪","语嫣","安琪","品如",
"舒窈","清漪","南絮","知夏","书瑶","沁","以柔","星辰","乐瑶","菁","若云"]
used = set()
def mkname(gender):
    while True:
        n = random.choice(SURN) + random.choice(M_GIVEN if gender=='男' else F_GIVEN)
        if n not in used:
            used.add(n); return n

EDU = [("浙江大学","硕士"),("浙江大学","本科"),("杭州电子科技大学","本科"),("浙江工业大学","本科"),("华中科技大学","本科"),("武汉大学","硕士"),
("电子科技大学","本科"),("南京大学","硕士"),("合肥工业大学","本科"),("宁波大学","本科"),("浙江理工大学","本科"),("西安电子科技大学","本科"),
("中南大学","本科"),("浙江财经大学","本科"),("上海大学","硕士"),("安徽大学","本科"),("杭州师范大学","本科"),("重庆邮电大学","本科")]
PREV = ["鲸帆科技","星澜数据","蜂语网络","青冥软件","曜石信息","南屏智能","杭州某头部电商","上海某金融科技公司","深圳某物流SaaS厂商","本地某外包公司","纸鸢互动","云岭信息","某运营商省公司"]

PROJECTS = {
 "智仓WMS":      dict(cust="（自有产品）", status="进行中 · 核心产品", period="2019-03 至今", amount="（产品线）", desc="公司核心 SaaS 产品：智能仓储管理系统，60+ 付费客户，年续费率 87%。", risk="4.0 重构期间双线作战，核心后端人力极度紧张。", ms=[]),
 "云栈BI平台":   dict(cust="（自有产品）", status="进行中", period="2024-06 至今", amount="（产品线）", desc="第二产品线：面向制造和物流客户的轻量 BI 报表平台，已签 9 家。", risk="数据团队人手不足，需求排队超过 6 周。", ms=[]),
 "宁波东海港供应链协同系统": dict(cust="宁波东海港集团", status="交付冲刺 ⚠️", period="2025-09 ~ 2026-07", amount="¥680 万", desc="港口供应链协同定制项目，公司今年最大单。", risk="客户要求 7 月底前上线（原计划 8 月中），后端进度落后约 2 周，急需增援。",
   ms=[("2025-12","需求冻结","✅ 完成"),("2026-04","核心模块联调","✅ 完成（延期 2 周）"),("2026-06-30","UAT 进入","⚠️ 有风险"),("2026-07-31","上线验收","🔴 客户底线，不可移动")]),
 "银杏医疗HIS集成项目": dict(cust="银杏医疗", status="进行中", period="2026-02 ~ 2026-11", amount="¥210 万", desc="连锁医院 HIS 系统与智仓WMS 的耗材管理集成。", risk="医疗行业接口规范多，测试工作量超预期。", ms=[]),
 "长风物流TMS项目": dict(cust="长风物流", status="收尾 ✅", period="2025-04 ~ 2026-06", amount="¥350 万", desc="运输管理系统定制开发，6 月底验收。", risk="已进入验收阶段，团队 7 月起可释放。", ms=[]),
 "杭州城投智慧园区项目": dict(cust="杭州城投", status="维保中 ✅", period="2024-08 ~ 2025-12", amount="¥520 万", desc="智慧园区一体化平台，已交付，处于一年维保期。", risk="维保只需 1-2 人轮值，团队大部分已可释放。", ms=[]),
 "智仓WMS 4.0重构": dict(cust="（自有产品）", status="进行中 · 技术专项", period="2025-11 至今", amount="（内部投入）", desc="核心产品微服务化重构，决定未来三年技术竞争力。", risk="只许成功：重构期间不能影响线上 60+ 客户。", ms=[]),
 "慧眼质检AI试点": dict(cust="三禾制造", status="POC 试点", period="2026-04 ~ 2026-08", amount="¥45 万（POC）", desc="基于视觉大模型的产线质检试点，探索第三增长曲线。", risk="试点性质，投入控制在 3 人以内。", ms=[]),
 "移动端App一体化": dict(cust="（自有产品）", status="收尾 ✅", period="2025-08 ~ 2026-06", amount="（内部投入）", desc="智仓WMS 移动端重写，iOS/Android 双端合一。", risk="6 月发版后转入维护，团队可释放。", ms=[]),
 "内部效能平台": dict(cust="（内部）", status="半搁置 ⏸️", period="2025-06 至今", amount="（内部投入）", desc="内部 DevOps 效能平台，优先级让位于商业项目。", risk="长期 1 人维护，其余成员可随时抽调。", ms=[]),
}
CUSTOMERS = {
 "宁波东海港集团": dict(industry="港口/供应链", status="交付中 · 战略客户", contact="周总（信息化部总经理）", note="今年最大单 ¥680 万；按时交付则有二期智慧口岸项目（预估 ¥1200 万）。",
   tl=[("2025-06","展会接触，唐婷婷跟进"),("2025-08","POC 演示通过"),("2025-09","签约 ¥680 万"),("2026-06","交付冲刺，周总对进度不满（见 inbox）")]),
 "银杏医疗":   dict(industry="连锁医疗", status="交付中", contact="梅主任（信息科）", note="医疗行业标杆客户，验收后可做行业案例复制。",
   tl=[("2025-11","行业展会线索"),("2026-02","签约 ¥210 万")]),
 "长风物流":   dict(industry="物流运输", status="验收中", contact="戴总监（运营）", note="验收顺利，有续签维保+TMS二期意向。",
   tl=[("2025-03","老客户转介绍"),("2025-04","签约 ¥350 万"),("2026-06","验收会顺利（见 exec/本周计划）")]),
 "杭州城投":   dict(industry="政企/园区", status="维保中", contact="章处（信息办）", note="政企标杆，回款周期长但信用好。",
   tl=[("2024-05","招投标中标"),("2025-12","终验通过，转维保")]),
 "三禾制造":   dict(industry="离散制造", status="POC 试点", contact="冯厂长", note="AI 质检试点客户，决定第三曲线方向。",
   tl=[("2026-03","行业论坛认识"),("2026-04","POC 签约 ¥45 万")]),
 "微澜零售":   dict(industry="连锁零售", status="售前阶段 🔥", contact="贺总（COO）", note="200+ 门店仓配一体化需求，预估合同 ¥400 万，Q3 关键赢单目标。",
   tl=[("2026-05","贺总主动询单（看了东海港案例）"),("2026-07-15","方案提交截止 🔴"),("2026-08","预计招标")]),
}

SPEC = [
 ("技术研发中心","CTO","P9/M4",1,0.9,(65,75),"tech_lead"),
 ("技术研发中心","架构师","P8",2,0.9,(45,55),"tech_core"),
 ("技术研发中心","后端工程师","P7",4,0.85,(32,40),"backend"),
 ("技术研发中心","后端工程师","P6",7,0.85,(23,30),"backend"),
 ("技术研发中心","后端工程师","P5",5,0.85,(15,21),"backend"),
 ("技术研发中心","前端工程师","P6",4,0.7,(21,28),"frontend"),
 ("技术研发中心","前端工程师","P5",5,0.7,(14,20),"frontend"),
 ("技术研发中心","移动端工程师","P6",3,0.8,(21,27),"mobile"),
 ("技术研发中心","测试工程师","P6",2,0.4,(18,24),"qa"),
 ("技术研发中心","测试工程师","P5",5,0.4,(11,16),"qa"),
 ("技术研发中心","运维工程师","P6",3,0.9,(18,26),"ops"),
 ("技术研发中心","数据工程师","P6",3,0.75,(22,30),"data"),
 ("技术研发中心","研发项目经理","P7",3,0.5,(25,33),"pm"),
 ("产品设计部","产品总监","P8/M3",1,0.5,(42,50),"product"),
 ("产品设计部","产品经理","P6",5,0.5,(20,28),"product"),
 ("产品设计部","UI/UX设计师","P5",4,0.25,(13,19),"design"),
 ("交付实施部","交付总监","P8/M3",1,0.7,(40,48),"delivery"),
 ("交付实施部","实施工程师","P5",5,0.7,(11,16),"delivery"),
 ("交付实施部","客户成功经理","P5",2,0.3,(12,17),"delivery"),
 ("销售部","销售VP","P9/M4",1,0.7,(55,65),"sales"),
 ("销售部","大客户销售","P6",7,0.6,(13,18),"sales"),
 ("销售部","渠道销售","P5",4,0.6,(10,14),"sales"),
 ("销售部","售前工程师","P6",4,0.8,(18,25),"presales"),
 ("市场部","市场总监","P7/M2",1,0.4,(28,35),"mkt"),
 ("市场部","内容运营","P4",2,0.3,(9,13),"mkt"),
 ("市场部","活动策划","P4",1,0.3,(9,12),"mkt"),
 ("人力行政部","HRD","P8/M3",1,0.3,(35,42),"func"),
 ("人力行政部","HRBP","P5",2,0.2,(13,18),"func"),
 ("人力行政部","招聘专员","P4",1,0.2,(9,12),"func"),
 ("人力行政部","行政专员","P4",2,0.15,(7,10),"func"),
 ("人力行政部","前台","P3",1,0.05,(6,8),"func"),
 ("人力行政部","IT支持","P4",1,0.9,(9,12),"func"),
 ("财务法务部","财务总监","P8/M3",1,0.3,(35,42),"func"),
 ("财务法务部","会计","P5",2,0.2,(10,14),"func"),
 ("财务法务部","出纳","P4",1,0.15,(8,10),"func"),
 ("财务法务部","法务专员","P5",1,0.4,(13,17),"func"),
 ("财务法务部","内审专员","P5",1,0.4,(12,16),"func"),
]
assert sum(s[3] for s in SPEC) == 99

POOL = {
 "backend": [("智仓WMS","后端开发"),("智仓WMS 4.0重构","重构开发"),("宁波东海港供应链协同系统","后端开发"),("银杏医疗HIS集成项目","后端开发"),("长风物流TMS项目","后端开发"),("杭州城投智慧园区项目","后端开发"),("内部效能平台","平台开发")],
 "frontend":[("智仓WMS","前端开发"),("云栈BI平台","前端开发"),("宁波东海港供应链协同系统","前端开发"),("长风物流TMS项目","前端开发"),("杭州城投智慧园区项目","前端开发")],
 "mobile":  [("移动端App一体化","移动端开发"),("智仓WMS","移动端支持")],
 "qa":      [("智仓WMS","测试"),("宁波东海港供应链协同系统","测试"),("银杏医疗HIS集成项目","测试"),("长风物流TMS项目","测试"),("移动端App一体化","测试")],
 "ops":     [("智仓WMS","SRE/运维"),("智仓WMS 4.0重构","基础设施"),("内部效能平台","平台运维")],
 "data":    [("云栈BI平台","数据开发"),("慧眼质检AI试点","算法工程"),("智仓WMS","数据支持")],
 "pm":      [("宁波东海港供应链协同系统","项目经理"),("银杏医疗HIS集成项目","项目经理"),("长风物流TMS项目","项目经理")],
 "product": [("智仓WMS","产品规划"),("云栈BI平台","产品规划"),("移动端App一体化","产品规划"),("慧眼质检AI试点","产品规划")],
 "design":  [("智仓WMS","UI设计"),("云栈BI平台","UI设计"),("移动端App一体化","UI设计")],
 "delivery":[("宁波东海港供应链协同系统","实施交付"),("银杏医疗HIS集成项目","实施交付"),("长风物流TMS项目","实施交付"),("杭州城投智慧园区项目","实施/维保")],
 "presales":[("微澜零售（售前）","售前方案"),("宁波东海港供应链协同系统","售前方案"),("慧眼质检AI试点","售前方案")],
 "tech_lead":[("智仓WMS 4.0重构","技术负责人"),("智仓WMS","技术决策")],
 "tech_core":[("智仓WMS 4.0重构","架构设计"),("智仓WMS","架构把关")],
 "sales": [], "mkt": [], "func": [],
}
GRADE_W = [("S",10),("A",25),("B+",30),("B",30),("C",5)]
G_COMMENT = {"S":["全年最佳之一，超额完成","关键战役的核心功臣"],"A":["稳定输出，超出预期","独当一面，值得加码"],
"B+":["符合预期，偶有亮点","靠谱，有上升空间"],"B":["完成本职","中规中矩"],"C":["低于预期，已面谈","状态下滑，需观察"]}
def grade():
    r = random.uniform(0,100); acc=0
    for g,w in GRADE_W:
        acc+=w
        if r<=acc: return g
    return "B"

emps = []
no = 1
def add(name,gender,age,dept,title,level,sal,join,edu,prev,projs,p24,p25,note=""):
    global no
    emps.append(dict(no=no,name=name,gender=gender,age=age,dept=dept,title=title,level=level,sal=sal,join=join,edu=edu,prev=prev,projs=projs,p24=p24,p25=p25,note=note)); no+=1

add("（你）创始人 & CEO","—",38,"CEO办公室","创始人 & CEO","—",30,"2019-03",("浙江大学","硕士"),"连续创业者",[("智仓WMS","创始人"),("微澜零售（售前）","关键决策")],"—","—","这就是你。工资条上最低的高管。")
add("韩磊","男",31,"技术研发中心","后端工程师","P7",34,"2020-07",("杭州电子科技大学","本科"),"鲸帆科技（后端开发）",
    [("智仓WMS","核心模块Owner（库存引擎）"),("智仓WMS 4.0重构","重构主力")],"S","S",
    "智仓WMS 库存引擎唯一精通者。2024、2025 连续两年 S。⚠️ 月薪低于 2025 年新进的同级 P7（见沈劲松）。")
add("沈劲松","男",33,"技术研发中心","后端工程师","P7",38,"2025-09",("华中科技大学","硕士"),"上海某金融科技公司（高级后端）",
    [("宁波东海港供应链协同系统","后端负责人")],"—","B+","2025 年高薪引进，能力扎实，但入职薪资高于司龄 5 年的同级老员工。")
add("陆云飞","男",29,"技术研发中心","后端工程师","P6",27,"2021-03",("浙江工业大学","本科"),"星澜数据（后端开发）",
    [("长风物流TMS项目","后端主力"),("智仓WMS","早期模块开发")],"A","A","长风TMS 6月底验收，7月起可释放。Java/Spring 体系，懂仓储业务。")
add("赵承宇","男",27,"技术研发中心","后端工程师","P6",25,"2022-06",("电子科技大学","本科"),"蜂语网络（后端开发）",
    [("长风物流TMS项目","后端开发"),("内部效能平台","早期成员")],"B+","A","长风TMS 收尾中，7月起可释放。性格稳，加班扛得住。")
add("郭一鸣","男",30,"技术研发中心","后端工程师","P6",24,"2021-11",("合肥工业大学","本科"),"青冥软件（Java开发）",
    [("内部效能平台","主力（半搁置项目）"),("杭州城投智慧园区项目","后端开发（已交付）")],"B+","B+","效能平台半搁置，随时可抽调；做过城投项目，熟悉政企交付节奏。")
add("唐婷婷","女",32,"销售部","大客户销售","P6",16,"2020-05",("浙江财经大学","本科"),"深圳某物流SaaS厂商（销售）",
    [],"S","S","连续两年销冠，宁波东海港单子的签单人。微澜零售也是她在跟。⚠️ 据说被竞对接触过。")
add("方知夏","女",26,"产品设计部","产品经理","P6",22,"2023-04",("南京大学","硕士"),"杭州某头部电商（产品）",
    [("云栈BI平台","产品Owner")],"A","S","BI 平台从 0 到 1 的产品 Owner，晋升 P7 第一候选。")

used.update(["韩磊","沈劲松","陆云飞","赵承宇","郭一鸣","唐婷婷","方知夏"])
TAKEN = {("技术研发中心","后端工程师","P7"):2, ("技术研发中心","后端工程师","P6"):3,
         ("销售部","大客户销售","P6"):1, ("产品设计部","产品经理","P6"):1}

for dept,title,level,cnt,mratio,band,tag in SPEC:
    cnt -= TAKEN.get((dept,title,level),0)
    for _ in range(cnt):
        gender = '男' if random.random()<mratio else '女'
        name = mkname(gender)
        base_age = {"P3":24,"P4":26,"P5":28,"P6":30,"P7":33,"P8":37,"P9":41}
        lvl_key = level.split('/')[0]
        age = base_age.get(lvl_key,30) + random.randint(-2,3)
        sal = random.randint(*band)
        yr = max(2019, 2026 - random.choice([0,1,1,2,2,3,3,4,5,6,7]))
        join = f"{yr}-{random.randint(1,12):02d}"
        projs = []
        pool = POOL[tag]
        if pool:
            k = 1 if lvl_key in ("P3","P4") else random.choice([1,2,2,3])
            projs = random.sample(pool, min(k,len(pool)))
        p24 = grade() if yr<=2024 else "—"
        p25 = grade() if yr<=2025 else "—"
        add(name,gender,age,dept,title,level,sal,join,EDU[random.randrange(len(EDU))][0:2] if False else random.choice(EDU),random.choice(PREV),projs,p24,p25)

assert len(emps)==100

def W(path, content):
    p = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p,'w',encoding='utf-8') as f: f.write(content)

FOOT_EMP = "\n---\n*数据口径：薪酬/绩效以 `raw/员工花名册2026-06.csv` 原件为准，本页为派生视图。修改本页须同步更新 frontmatter 的 `updated`。建档请用 `system/模板/员工档案模板.md`。*\n"

# ===== 员工页（v2 模板：结构化 frontmatter + 画像 + 口径脚注）=====
for e in emps:
    yrs = 2026 - int(e['join'][:4])
    pj = "\n".join(f"- [[{p}]] — {r}" for p,r in e['projs']) or "- （职能岗位，不直接挂项目）"
    first_proj = e['projs'][0][0] if e['projs'] else None
    portrait = f"{e['title']}（{e['level']}），{e['join'][:4]} 年加入" + (f"，当前主要投入 [[{first_proj}]]。" if first_proj else "，支撑全公司日常运转。")
    note = f"\n## 老板备注\n\n> ⚠️ {e['note']}\n" if e['note'] else ""
    c24 = random.choice(G_COMMENT.get(e['p24'],["—"])) if e['p24']!="—" else "（未入职/不适用）"
    c25 = random.choice(G_COMMENT.get(e['p25'],["—"])) if e['p25']!="—" else "（未参与考核）"
    risk = "\n风险标记: 关注" if "⚠️" in e['note'] else ""
    body = f"""---
type: 员工
工号: YZ{e['no']:03d}
姓名: {e['name']}
性别: {e['gender']}
年龄: {e['age']}
部门: {e['dept']}
岗位: {e['title']}
职级: {e['level']}
状态: 在职
入职: {e['join']}
月薪k: {e['sal']}
绩效2024: {e['p24']}
绩效2025: {e['p25']}{risk}
created: {e['join']}-15
updated: 2026-06-10
tags: [员工, {e['dept']}]
---

# {e['name']}

> [[{e['dept']}]] · {e['title']} {e['level']} · 在职 {yrs} 年 · 月薪 ¥{e['sal']},000

## 画像

{portrait}

## 履历

| 阶段 | 内容 |
|---|---|
| 教育 | {e['edu'][0]} · {e['edu'][1]} |
| 上一站 | {e['prev']} |
| 加入云栈 | {e['join']} |

## 项目经历

{pj}

## 绩效

| 年度 | 等级 | 评语 |
|---|---|---|
| 2024 | {e['p24']} | {c24} |
| 2025 | {e['p25']} | {c25} |
{note}{FOOT_EMP}"""
    W(f"wiki/团队/{e['name']}.md", body)

# ===== 部门页 =====
from collections import defaultdict
by_dept = defaultdict(list)
for e in emps: by_dept[e['dept']].append(e)
for dept, members in by_dept.items():
    rows = "\n".join(f"| [[{m['name']}]] | {m['title']} | {m['level']} | {m['p25']} |" for m in sorted(members,key=lambda x:x['no']))
    avg = sum(m['sal'] for m in members)/len(members)
    titles = defaultdict(int)
    for m in members: titles[m['title']]+=1
    comp = "、".join(f"{t}×{c}" for t,c in titles.items())
    W(f"wiki/部门/{dept}.md", f"""---
type: 部门
部门: {dept}
人数: {len(members)}
平均月薪k: {avg:.1f}
created: 2026-01-05
updated: 2026-06-10
tags: [部门]
---

# {dept}

> {len(members)} 人 · 平均月薪 ¥{avg:.1f}k · 构成：{comp}

| 姓名 | 岗位 | 职级 | 2025绩效 |
|---|---|---|---|
{rows}

---
*人数/薪酬口径以 `raw/员工花名册2026-06.csv` 为准。本页随人员异动更新。*
""")

# ===== 项目页 =====
proj_members = defaultdict(list)
for e in emps:
    for p,r in e['projs']: proj_members[p].append((e['name'],r))
for pname, meta in PROJECTS.items():
    mem = proj_members.get(pname,[])
    rows = "\n".join(f"| [[{n}]] | {r} |" for n,r in mem)
    cust = meta['cust'] if meta['cust'].startswith('（') else f"[[{meta['cust']}]]"
    ms = ""
    if meta['ms']:
        ms = "\n## 里程碑\n\n| 时间 | 节点 | 状态 |\n|---|---|---|\n" + "\n".join(f"| {a} | {b} | {c} |" for a,b,c in meta['ms']) + "\n"
    W(f"wiki/项目/{pname}.md", f"""---
type: 项目
项目: {pname}
客户: {meta['cust'].strip('（）') if meta['cust'].startswith('（') else meta['cust']}
状态: {meta['status']}
周期: {meta['period']}
合同额: {meta['amount']}
人数: {len(mem)}
created: 2025-01-10
updated: 2026-06-10
tags: [项目]
---

# {pname}

> 客户：{cust} · {meta['status']} · {meta['period']} · 合同额：{meta['amount']}

{meta['desc']}
{ms}
## 成员（{len(mem)}人）

| 姓名 | 角色 |
|---|---|
{rows}

## 当前风险 / 备注

{meta['risk']}

---
*成员名单与员工档案双向链接；状态变更须同步 frontmatter 的 `状态` 与 `updated`。建档请用 `system/模板/项目档案模板.md`。*
""")
mem = proj_members.get("微澜零售（售前）",[])
rows = "\n".join(f"| [[{n}]] | {r} |" for n,r in mem)
W("wiki/项目/微澜零售（售前）.md", f"""---
type: 项目
项目: 微澜零售（售前）
客户: 微澜零售
状态: 售前阶段 🔥
周期: 2026-05 ~
合同额: 预估 ¥400 万
人数: {len(mem)+1}
created: 2026-05-06
updated: 2026-06-10
tags: [项目, 售前]
---

# 微澜零售（售前）

> 客户：[[微澜零售]] · 售前阶段 🔥 Q3 关键赢单目标 · 预估合同 ¥400 万（200+ 门店仓配一体化）

## 里程碑

| 时间 | 节点 | 状态 |
|---|---|---|
| 2026-07-15 | 方案提交截止 | 🔴 倒计时 |
| 2026-08 | 预计招标 | 待定 |

## 跟进人

| 姓名 | 角色 |
|---|---|
| [[唐婷婷]] | 商务主谈 |
{rows}

## 当前风险 / 备注

竞对（星澜数据）也在投标；7 月中旬要交方案，售前需要技术侧出架构师支持。

---
*建档请用 `system/模板/项目档案模板.md`。*
""")

# ===== 客户页 =====
for cname, m in CUSTOMERS.items():
    related = [p for p,meta in PROJECTS.items() if meta['cust']==cname]
    if cname=="微澜零售": related=["微澜零售（售前）"]
    rel = "\n".join(f"- [[{p}]]" for p in related) or "-（暂无）"
    tl = "\n".join(f"| {d} | {ev} |" for d,ev in m['tl'])
    W(f"wiki/客户/{cname}.md", f"""---
type: 客户
客户: {cname}
行业: {m['industry']}
状态: {m['status']}
关键联系人: {m['contact']}
created: 2025-06-01
updated: 2026-06-10
tags: [客户]
---

# {cname}

> {m['industry']} · {m['status']} · 关键联系人：{m['contact']}

## 商务时间线

| 时间 | 事件 |
|---|---|
{tl}

## 合作项目

{rel}

## 备注

{m['note']}

---
*商务动态随时间线追加，不删旧行。建档请用 `system/模板/客户档案模板.md`。*
""")

# ===== CSV 花名册 =====
os.makedirs(os.path.join(BASE,'raw'),exist_ok=True)
with open(os.path.join(BASE,'raw/员工花名册2026-06.csv'),'w',encoding='utf-8-sig',newline='') as f:
    w = csv.writer(f)
    w.writerow(["工号","姓名","性别","年龄","部门","岗位","职级","入职时间","月薪(千元)","2024绩效","2025绩效"])
    for e in emps:
        w.writerow([f"YZ{e['no']:03d}",e['name'],e['gender'],e['age'],e['dept'],e['title'],e['level'],e['join'],e['sal'],e['p24'],e['p25']])

# ===== 组织架构 =====
lines=[]
for dept in ["CEO办公室","技术研发中心","产品设计部","交付实施部","销售部","市场部","人力行政部","财务法务部"]:
    ms = by_dept[dept]
    titles = defaultdict(int)
    for m in ms: titles[f"{m['title']}({m['level']})"]+=1
    tl = "、".join(f"{t}×{c}" for t,c in titles.items())
    lines.append(f"- **[[{dept}]]**（{len(ms)}人）：{tl}")
W("wiki/公司/组织架构.md", f"""---
type: 公司
created: 2026-01-05
updated: 2026-06-10
tags: [公司]
---

# 组织架构（2026-06，全员 100 人）

{chr(10).join(lines)}

> 配比：技术研发 47%｜销售+市场 20%｜产品设计 10%｜交付实施 8%｜职能 14%｜CEO 1%
""")

# ===== MOC 总览页（v2 新增）=====
# 团队总览
star = [e for e in emps if e['p24'] in("S",) and e['p25'] in ("S",)]
double_a = [e for e in emps if e['p24'] in("S","A") and e['p25'] in ("S","A") and e not in star and e['p24']!="—"]
lvl = defaultdict(int)
for e in emps: lvl[e['level'].split('/')[0]] += 1
lvl_row = " · ".join(f"{k}×{lvl[k]}" for k in ["P3","P4","P5","P6","P7","P8","P9"] if k in lvl)
dept_rows = "\n".join(f"| [[{d}]] | {len(ms)} | ¥{sum(m['sal'] for m in ms)/len(ms):.1f}k |" for d,ms in by_dept.items())
avg_age = sum(e['age'] for e in emps)/len(emps)
W("wiki/团队/团队总览.md", f"""---
type: 总览
created: 2026-06-10
updated: 2026-06-10
tags: [总览, 团队]
---

# 团队总览（MOC）

> 全员 100 人 · 平均年龄 {avg_age:.1f} 岁 · 职级分布：{lvl_row}

## 各部门

| 部门 | 人数 | 平均月薪 |
|---|---|---|
{dept_rows}

## 连续两年 S（明星名单）

{chr(10).join(f"- [[{e['name']}]]（{e['dept']} · {e['title']}）" for e in star)}

## 连续两年 S/A（潜力池）

{chr(10).join(f"- [[{e['name']}]]（{e['dept']} · {e['title']}）" for e in double_a[:12])}

---
*本页是团队域的入口（Map of Content）。个体信息点姓名进档案；数据口径以 raw/ 花名册为准。*
""")

# 项目总览
order = ["交付冲刺 ⚠️","售前阶段 🔥","进行中 · 核心产品","进行中 · 技术专项","进行中","POC 试点","收尾 ✅","维保中 ✅","半搁置 ⏸️"]
allp = dict(PROJECTS); allp["微澜零售（售前）"]=dict(cust="微澜零售",status="售前阶段 🔥",period="2026-05 ~",amount="预估 ¥400 万",desc="",risk="7/15 方案截止",ms=[])
rows = "\n".join(f"| [[{n}]] | {m['status']} | {m['cust'] if m['cust'].startswith('（') else '[['+m['cust']+']]'} | {m['amount']} | {m['risk'][:28]}… |"
    for n,m in sorted(allp.items(), key=lambda kv: order.index(kv[1]['status']) if kv[1]['status'] in order else 99))
W("wiki/项目/项目总览.md", f"""---
type: 总览
created: 2026-06-10
updated: 2026-06-10
tags: [总览, 项目]
---

# 项目总览（MOC）

> {len(allp)} 个项目 · 排序：越靠上越需要老板关注

| 项目 | 状态 | 客户 | 合同额 | 风险一瞥 |
|---|---|---|---|---|
{rows}

---
*状态图例：⚠️ 冲刺 · 🔥 售前关键 · ✅ 收尾/维保（人力可释放）· ⏸️ 搁置（人力可抽调）。详情进项目页。*
""")

# 客户总览
rows = "\n".join(f"| [[{c}]] | {m['industry']} | {m['status']} | {m['contact']} |" for c,m in CUSTOMERS.items())
W("wiki/客户/客户总览.md", f"""---
type: 总览
created: 2026-06-10
updated: 2026-06-10
tags: [总览, 客户]
---

# 客户总览（MOC）

| 客户 | 行业 | 状态 | 关键联系人 |
|---|---|---|---|
{rows}

---
*新客户建档用 `system/模板/客户档案模板.md`，并在本表加一行。*
""")

print("v2 完成。员工:",len(emps)," 韩磊薪酬核对:",[(e['name'],e['sal']) for e in emps if e['name'] in('韩磊','沈劲松')])
print("明星名单:",[e['name'] for e in star])
