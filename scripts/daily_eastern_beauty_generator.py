#!/usr/bin/env python3
"""Generate a daily Eastern Beauty prompt batch.

The daily task should be exploratory, not a tiny fixed menu. This generator keeps
the stable skill routes available, then forces at least one original exploration
route in every batch.
"""

from __future__ import annotations

import argparse
import datetime as dt
import random
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Route:
    family: str
    skill: str
    style: str
    temperament: str
    scene: str
    outfit: str
    action: str
    composition: str
    visual_hook: str
    prop_lock: str
    slug: str


@dataclass(frozen=True)
class ExplorationIdea:
    title: str
    brief: str
    constraint: str
    slug: str


ROUTES: list[Route] = [
    # Eastern fantasy / gu feng routes.
    Route("东方幻想古风", "东方幻想古风", "天象神朝", "年轻，神性，高贵，清冷", "云海观星台，青铜浑仪，夜空星轨", "月白与深青层叠礼袍，青铜星纹腰饰", "一手扶青铜浑仪，一手指向星图，回头看向镜头", "9比16，低机位，三分之四全身", "巨大的青铜星环在身后形成唯一主视觉", "青铜浑仪必须保持为完整天文仪器，不变成首饰、链条或背景纹样", "celestial-observatory"),
    Route("东方幻想古风", "东方幻想古风", "昆仑雪剑", "年轻，清冷，英气，孤高", "雪山悬桥，冰雾，远处昆仑山门，月光", "月白披风，银线长袍，玉甲护肩", "她握住冰玉长剑，剑光切开风雪后回头", "9比16，全身，低机位", "冰玉剑把暴雪切成一道弯月形光隙", "冰玉长剑必须保持为剑，不变成冰柱、链条或背景光纹", "kunlun-snow-sword"),
    Route("东方幻想古风", "东方幻想古风", "敦煌壁画神女", "年轻，神秘，柔美，庄严", "敦煌石窟，矿物色壁画，沙尘微光，残缺佛龛", "赭石、石青与淡金层叠飞天服饰，覆身内衬", "她展开一段壁画飘带，回望时壁画光线从墙面苏醒", "9比16，大腿以上，壁画侧光", "背后圆形壁画像日轮一样微亮", "壁画飘带必须保持为丝带，不变成手臂、头发或脸部纹样", "dunhuang-mural-oracle"),
    Route("东方幻想古风", "东方幻想古风", "沧海龙庭", "年轻，高贵，危险，神秘", "风暴海崖观象台，远海浪潮，云层裂隙，仪式平台", "深青与古金层叠礼袍，青铜海浪纹饰，玉质星盘", "一手稳住玉制星盘，一手伸向悬浮明珠", "9比16，低机位，三分之四全身", "海雾与青火组成的环形龙灯在身后升起", "玉制星盘和明珠必须保持为清晰道具，不变成链条、眼睛或水花", "tide-dragon-observatory"),
    Route("东方幻想古风", "东方幻想古风", "莲梦镇邪", "年轻，温柔，灵异，安静坚定", "夜色镜湖，莲灯，纸符，水面倒影里的倒置古城", "浅玉色长袍，水墨裙摆，莲粉色系带", "她点亮莲灯，湖面倒影中浮出倒置城门", "9比16，上半身到大腿，平视", "一盏莲灯照出水下倒置古城", "莲灯必须保持为灯，不变成花团、脸部光斑或手指", "lotus-dream-exorcist"),
    Route("东方幻想古风", "东方幻想古风", "凤阙宫火", "年轻，高贵，强势，华丽克制", "黑红宫廷火庭，漆屏，铜灯，凤凰纹影", "朱砂红礼袍，黑漆腰封，金线凤凰刺绣", "她提起凤凰宫灯，火光在身后形成单翼轮廓", "9比16，全身，低机位", "一只巨大的凤凰火翼只在画面一侧展开", "凤凰宫灯必须保持为灯笼，不变成首饰、火球或头冠", "phoenix-palace-fire"),
    Route("东方幻想古风", "东方幻想古风", "绮罗金帐", "年轻，妩媚，高贵，克制", "红金宫廷秘仪空间，纱幔，珠链，烛火，雕花屏风", "朱砂红与古金色层叠礼服，覆身内衬，珠饰冠冕", "一手扶纱幔，一手提宫灯，回眸看向镜头", "9比16，全身，三分之四视角", "红金屏风像宫廷梦境入口一样打开", "宫灯必须保持为宫灯，珠链只作背景点缀，不变成脸部或手部结构", "red-gold-luo-curtain"),
    Route("东方幻想古风", "东方幻想古风", "月宫炼华", "年轻，清冷，神性，静谧", "月宫炼丹殿，桂树，银炉，玉阶，冷月光", "月白与淡银层叠汉服，桂花暗纹，珍珠发簪", "她俯身看向银炉，手中月镜映出第二个月宫", "9比16，大腿以上，冷月侧光", "月镜里出现倒映的第二个月宫", "月镜必须保持为镜子，不变成圆月、脸或首饰", "moon-palace-alchemy"),
    Route("东方幻想古风", "东方幻想古风", "青铜神谕城", "年轻，英气，神秘，锋利", "青铜古城祭坛，甲骨纹光影，远处城墙剪影", "黑金短披甲外搭深茶色长裙，玉扣束腰", "她抬手触碰悬浮甲骨片，另一手握住短杖", "9比16，中近全身，轻微仰拍", "甲骨片在空中组成一只巨大的神谕眼", "甲骨片必须保持为骨片符号，不变成飞虫、碎脸或随机饰品", "oracle-bronze-city"),
    Route("东方幻想古风", "东方幻想古风", "雾浴私语", "年轻，柔美，私密，克制", "月光私房香雾空间，雕花屏风，铜盆，莲花水汽", "覆身交领丝绸浴袍，轻薄但不透明，披帛收拢", "她整理被水汽润湿的袖口，隔着屏风看向镜头", "9比16，大腿以上，柔和月光", "月窗格影在水汽里形成圆形光晕", "铜盆和屏风必须保持为环境道具，不变成链条、身体纹样或脸部纹理", "mist-bath-boudoir"),

    # Classical Eastern beauty routes.
    Route("古典东方美人", "古典东方美人", "洛神水镜", "年轻，柔美，神性，轻盈", "浅水河湾，月下水镜，荷叶，珍珠光", "珠白层叠丝裙，淡青披帛，珍珠发饰", "她提起袖口触碰水面，水中倒影先看向镜头", "9比16，全身，水面低角度", "水面倒影与真人产生轻微错位", "水面倒影必须保持为倒影，不变成第二个人或脸部污渍", "luoshen-water-mirror"),
    Route("古典东方美人", "古典东方美人", "宋韵茶影", "年轻，温婉，清润，书卷气", "雨后茶室，竹帘，青瓷茶盏，窗外湿润庭院", "月白宋风长衫，淡青披帛，白玉簪", "她端起青瓷茶盏，听到脚步声后微微抬眼", "9比16，大腿以上，平视近景", "茶汽在窗光里形成一条柔和银线", "青瓷茶盏必须保持为杯盏，不变成链条、手镯、花朵或灯具", "song-tea-rain"),
    Route("古典东方美人", "古典东方美人", "唐宫夜宴", "年轻，华贵，妩媚，盛唐气", "唐代宫廷夜宴，雕花屏风，烛台，琵琶，漆盘", "浅绛红唐风襦裙，金线披帛，花冠发饰", "她停下拨弦动作，隔着烛光回眸", "9比16，三分之四全身", "琵琶弦在烛光中形成一道金色斜线", "琵琶必须保持为乐器，不变成盾牌、身体纹样或背景装饰", "tang-palace-night-banquet"),
    Route("古典东方美人", "古典东方美人", "唐宫花泉仪式", "年轻，高贵大气，柔美", "唐代宫廷花泉池畔，花瓣倒影池，纱幔，烛台，香雾", "浅金与暖玉白层叠唐风礼服，覆身不透明丝绸", "一手扶纱幔，一手持金碗，将牡丹花瓣轻轻洒向水面", "9比16，全身", "花瓣落入水面形成一圈金色涟漪", "金碗必须保持为碗，花瓣必须保持为花瓣，不变成链条、火焰或皮肤纹样", "tang-flower-spring-ritual"),
    Route("古典东方美人", "古典东方美人", "江南烟雨", "年轻，柔美，含蓄，诗意", "江南廊桥，白墙黑瓦，细雨，油纸伞倒影", "浅藕色交领长裙，米白短披肩，发间素簪", "她收起油纸伞时回头，雨水从伞骨滴落", "9比16，全身，长焦压缩空间", "湿润青石板上的伞影成为唯一主视觉图形", "油纸伞必须保持完整伞形，不变成披帛、花环或背景纹样", "jiangnan-rain-bridge"),
    Route("古典东方美人", "古典东方美人", "青瓷月影", "年轻，清冷，高贵，玉感", "青瓷月室，圆窗，瓷瓶，冷月光，单枝白梅", "青瓷色长裙，月白披帛，玉簪", "她轻扶青瓷瓶，眼神越过镜头看向窗外", "9比16，上半身到大腿", "圆窗月光像青瓷釉面一样包住人物轮廓", "青瓷瓶必须保持为瓷瓶，不变成身体、脸部纹样或灯", "celadon-moon-shadow"),
    Route("古典东方美人", "古典东方美人", "昆曲花影", "年轻，优雅，含蓄妩媚", "花窗，折屏，暖烛，园林暗影", "昆曲袖形启发的浅粉绣花长裙，不是舞台戏服", "她以兰花手半遮浅笑，眼神先于身体回望", "9比16，上半身特写", "花窗影落在袖面形成第二层图案", "兰花手必须保持自然手势，不变成多指、花枝或装饰纹", "kunqu-flower-shadow"),
    Route("古典东方美人", "古典东方美人", "竹林清谈", "年轻，知性，温婉，书卷气", "竹林书斋，棋盘，茶器，纸窗斜光", "象牙白麻质长衫，竹青腰带，小玉簪", "她落下一枚棋子，抬眼像刚听懂一句话", "9比16，大腿以上，静物前景", "棋盘纵横线延伸到竹影里", "棋子必须保持为棋子，不变成眼睛、珠链或纽扣", "bamboo-literati-beauty"),
    Route("古典东方美人", "古典东方美人", "胭脂雪", "年轻，冷艳，危险，克制", "雪夜宫墙，红灯笼，黑瓦，冷石阶", "深胭脂红斗篷，月白内裙，黑发素簪", "她提灯穿过雪阶，回头时灯光照亮侧脸", "9比16，全身，高反差夜景", "红灯笼在雪地上投出唯一暖色光斑", "红灯笼必须保持为灯笼，不变成火球、头冠或链条", "rouge-snow-lantern"),
    Route("古典东方美人", "古典东方美人", "玉楼春睡", "年轻，慵懒，柔美，诗意", "春日下午内室，纱帘，花枝，书卷，暖光", "暖玉白丝绸长衫，浅粉披帛，层叠但覆身", "她从书卷上抬头，袖口自然垂落", "9比16，大腿以上，柔和近景", "花枝影子落在书页和袖面之间", "书卷必须保持为书，不变成布料、链条或皮肤纹理", "jade-chamber-spring"),

    # Modern Eastern beauty routes.
    Route("现代东方美人", "现代东方美人", "新中式杂志", "年轻知性，冷静，高级", "漆红展厅，折屏，玻璃展柜，清晨侧光", "象牙白真丝衬衫，墨绿色新中式马甲，高腰长裙", "她戴上白色手套，侧身整理展柜中的玉器", "9比16，四分之三全身，低机位", "漆红折屏反射成一道弧形晨光", "白色手套和玉器必须保持清晰，不变成链条、花瓣或皮肤纹理", "lacquer-gallery"),
    Route("现代东方美人", "现代东方美人", "东方静奢", "年轻，优雅，松弛，高级", "暖木酒店廊厅，黑石墙，一只陶瓷花器", "黑色真丝上衣，米白阔腿裤，玉扣耳饰", "她一手扶住玉杯，侧身从暖木阴影里看向镜头", "9比16，大腿以上，中景", "玉杯的小小绿色高光成为画面唯一亮点", "玉杯必须保持为杯子，不变成链条、花、戒指或背景光斑", "oriental-quiet-luxury"),
    Route("现代东方美人", "现代东方美人", "旗袍电影感", "年轻，含蓄，妩媚，电影感", "雨夜旧影院走廊，木门，钨丝灯，玻璃雨痕", "墨绿色改良旗袍，黑色短披肩，珍珠耳钉", "她在门口半转身，手指碰到耳钉，像准备离开", "9比16，全身，长焦", "走廊灯在雨玻璃上拉出一条琥珀色竖线", "珍珠耳钉必须保持为耳饰，不变成水滴、链条或眼睛", "qipao-cinema-noir"),
    Route("现代东方美人", "现代东方美人", "东方珠宝大片", "年轻，高贵，克制妩媚", "黑色丝绒摄影棚，单束柔光，翡翠耳坠特写氛围", "黑色新中式高领丝质上衣，暗纹盘扣", "她用指尖轻触翡翠耳坠，眼神看向镜头", "9比16，上半身特写", "翡翠耳坠作为唯一高光点", "翡翠耳坠必须保持为耳饰，不变成水杯、链条、眼睛或背景光斑", "jade-editorial"),
    Route("现代东方美人", "现代东方美人", "现代茶室光影", "年轻，温婉，聪慧，自然", "现代茶室，木格栅，雨窗，陶瓷杯，暖木桌", "米白交领衬衫，亚麻半裙，珍珠耳钉", "她正要喝茶时被叫住，杯盖停在半空", "9比16，上半身到大腿", "木格栅影子切在桌面和袖口上", "陶瓷杯和杯盖必须保持为茶具，不变成链条、花或手指", "modern-tea-room-light"),
    Route("现代东方美人", "现代东方美人", "都市晚宴东方", "年轻，高贵，冷静，都市感", "高层酒店窗边，城市夜景，黑金反射地面", "黑金新中式晚装，丝缎长裙，玉石戒指", "她站在落地窗前，手持小杯，从城市灯光中转身", "9比16，全身，城市夜景背景", "窗外城市灯光形成一条书法般的金色反射", "小杯必须保持为杯子，不变成戒指、链条或灯泡", "urban-evening-oriental"),
    Route("现代东方美人", "现代东方美人", "江南现代诗意", "年轻，清润，文艺，东方感", "雨后江南白墙黑瓦街口，现代长廊，水面倒影", "浅灰新中式风衣，白色真丝内搭，低马尾", "她撑伞走过水面倒影，听见你喊她后回头", "9比16，全身，35mm环境人像", "白墙黑瓦在水中形成一条墨线", "伞必须保持为伞，不变成披帛、背景纹或头饰", "jiangnan-modern-poetic"),

    # Gu feng girlfriends / private-room companionship photography routes.
    Route("古风闺蜜", "古风闺蜜", "闺阁夜话", "温暖，安心，陪伴，生活化，非暧昧", "古代闺阁夜晚，雕花木榻，纱帐，暖黄灯笼，烛火，软枕，丝被", "姐姐月白丝棉家居常服，妹妹藕荷色轻纱外衫，内层丝棉，披帛独立，布料轻薄柔软但覆身", "姐姐替妹妹把滑落的披帛拢好，两人靠近低声说睡前话", "9比16，双人半身，85mm，中近景，人物占75%-85%", "暖黄灯笼光落在两人之间，形成安静的陪伴焦点", "灯笼、软枕、丝被、披帛必须保持独立结构；两人身体边界清晰，不能融合，不能复制粘贴脸", "gufeng-bedtime-talk"),
    Route("古风闺蜜", "古风闺蜜", "灯下梳发", "照顾，守护，温柔，信任", "闺阁铜镜前，木梳，妆台，灯笼，低垂纱帐，少量月光", "姐姐烟灰蓝宋制家居长衫，妹妹浅樱粉丝棉内衫与薄纱披帛，材质分层清楚", "姐姐一手握木梳为妹妹梳发，妹妹从铜镜里看向姐姐，神态安心", "9比16，双人中近景，50mm，人物优先", "铜镜边缘反射出灯火，让两人的视线关系成为画面中心", "木梳必须保持为木梳，铜镜必须保持为镜子；头发、手指和披帛不能穿模，脸部骨相必须不同", "gufeng-lantern-hair-combing"),
    Route("古风闺蜜", "古风闺蜜", "同榻共读", "亲近，安静，书卷气，成长感", "雕花木榻，同榻读书，诗集，话本，纸窗暖光，软枕与丝被分层", "姐姐浅青丝绸家居常服，妹妹米白夏季轻衫，外层轻纱有自然垂坠", "两人共捧一本诗集，妹妹指着一行字，姐姐低头轻笑", "9比16，双人半身，85mm，生活抓拍", "书页的暖光把两张不同气质的脸连接在同一条视线里", "诗集必须保持为书，不变成布料、链条或脸部纹理；枕头和身体必须边界清楚，不能融成一团", "gufeng-shared-reading"),
    Route("古风闺蜜", "古风闺蜜", "夏夜纳凉", "松弛，陪伴，清凉，古代生活感", "湖亭夏夜，荷叶，灯笼，茶具，木栏杆，远处少量月光", "姐姐月白薄纱外衫，妹妹浅青丝棉夏季轻衫，披帛与衣袖独立飘落", "姐姐递茶给妹妹，妹妹扶着团扇回头，两人像刚听见湖面风声", "9比16，双人中景，50mm，人物占75%-85%", "荷叶间的灯笼倒影成为唯一暖色视觉钩子", "茶杯、团扇、灯笼必须保持原物体语义；团扇不能变成花或脸，茶杯不能变成链条", "gufeng-summer-pavilion"),
    Route("古风闺蜜", "古风闺蜜", "守夜温灯", "守护，安静，依赖，温柔克制", "深夜闺阁，低灯，纱帐，软枕，丝被，少量月光从窗格进入", "姐姐烟灰蓝丝棉常服，妹妹月白寝衣，外层轻纱覆身，丝被与身体边界清晰", "妹妹靠着软枕浅睡，姐姐未睡，轻轻替她整理发丝并温柔注视", "9比16，双人近景，85mm，半身到大腿", "低灯只照亮姐姐的手和妹妹安睡的侧脸", "发丝、手指、枕头、丝被必须保持独立；禁止合脸、重复脸、人物身体融合或枕头穿模", "gufeng-night-watch"),
    Route("古风闺蜜", "古风闺蜜", "江南湖亭共伞", "依赖，温暖，含蓄，雨中陪伴", "江南湖亭，夏季小雨，荷叶，石桥，水面夕照，细雨倒影", "姐姐雾蓝色棉麻长衫，妹妹月白丝棉轻衫，披帛收拢，雨中衣料有真实重量", "姐姐悄悄把油纸伞偏向妹妹，自己的肩头被雨打湿，妹妹发现后轻轻拉住她的袖口", "9比16，双人中景，85mm，人物占75%-85%", "偏斜的油纸伞和水面夕照共同说明她们的保护关系", "油纸伞必须保持为伞，雨滴和水面必须保持自然；袖口不能变成链条，人物肩膀不能融合", "gufeng-jiangnan-umbrella"),
    Route("古风闺蜜", "古风闺蜜", "山寺晨行", "成长，信任，清冷温柔，同行感", "山寺清晨，竹林山路，薄雾，石阶，远处钟楼", "姐姐深青棉麻外袍，妹妹浅杏色宋制轻衫，布料朴素有纹理层次", "两人沿石阶同行，姐姐回身伸手扶住妹妹跨过湿滑青苔", "9比16，双人环境人像，50mm，人物主体清晰", "晨雾里的伸手搀扶动作成为第一故事点", "石阶、青苔、手部动作必须清晰；不能变成仙侠飞升、悬浮粒子或神女壁纸", "gufeng-mountain-temple-companions"),
    Route("古风闺蜜", "古风闺蜜", "灯会重逢", "久别重逢，喜悦，怀旧，节庆温暖", "古代灯会夜市，纸灯笼，古街，人群虚化，摊位暖光", "姐姐茶金色宋锦短披，妹妹浅桃色丝棉长衫，节庆配色克制", "两人在灯会人群中重逢，妹妹刚要开口，姐姐已经认出她并笑着靠近", "9比16，双人近景，135mm，人群背景软焦", "一排纸灯笼在两人之间形成重逢路径", "纸灯笼必须保持为灯笼，人群必须虚化为背景；不能出现重复脸、第三主体抢戏或灯笼变首饰", "gufeng-lantern-reunion"),
    Route("古风闺蜜", "古风闺蜜", "书肆听雨", "知己，安静，书卷气，雨天陪伴", "古代书肆，雨窗，木书架，竹帘，矮桌，茶盏", "姐姐墨蓝色棉麻长衫，妹妹浅绿丝棉内衫，衣料干净朴素", "两人共读同一本话本，窗外雨声变大时一起抬头听雨", "9比16，双人半身，85mm，室内自然窗光", "雨窗反光把两人的视线连接到同一处", "书必须保持为书，茶盏必须保持为杯盏；雨窗反光不能进入脸部或眼睛", "gufeng-bookstore-listening-rain"),

    # SweetHomeGirl / lifestyle routes.
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "人民广场迎面走来", "甜系，自然，恋爱感，真实", "人民广场，夏日城市街头，斑马线，树影", "浅蓝露肩短袖，白色轻盈短裙，手提小包，耳机", "她迎面走来，发现你在看她后不经意浅笑", "9比16，大腿以上", "人流里只有她的眼神和浅笑最清晰", "耳机和小包必须保持为配饰，不变成链条、手指或背景线", "people-square-sweet"),
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "雨后街角花店", "甜系，亲近，自然，轻微恋爱感", "蓝调时刻街角花店，雨后路面，暖色灯泡", "水洗牛仔外套，奶油色吊带长裙，白色球鞋", "她抱着刚包好的花束，发现你在街对面等她后浅笑", "9比16，大腿以上，街边近距离", "雨滴里的暖色灯泡倒影像一排小灯笼", "花束必须保持为鲜花和包装纸，不变成链条、头发、手指或背景装饰", "flower-shop-bluehour"),
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "夜晚自助洗衣房", "邻家女孩，真实，松弛", "夜晚自助洗衣房，暖白灯，滚筒烘干机，玻璃门反光", "宽松白T，牛仔短裙，帆布鞋", "她把衣服从烘干机里抱出来，发现你在门口等她，忍不住笑了一下", "9比16，上半身，女友视角", "烘干机圆形玻璃门形成柔和光环", "衣服必须保持为柔软布料，不变成链条、绳索、触手或背景纹样", "laundromat-smile"),
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "便利店半夜买饮料", "兔系甜妹，生活感，亲近", "深夜便利店冷柜前，冷白灯，玻璃门反光", "宽松短袖，浅色牛仔短裤，薄针织开衫", "她拿着冰饮回头问你要不要同款", "9比16，上半身，近距离抓拍", "冷柜玻璃上的蓝白光照亮她的侧脸", "饮料瓶必须保持为饮料瓶，不变成链条、灯管或手指", "convenience-store-drink"),
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "书店翻书抬头", "氧气少女，安静，恋爱感", "独立书店，木书架，午后窗光，纸页气息", "白色棉麻衬衫，浅色短裙，帆布包", "她翻书时听见你走近，抬头停顿了一秒", "9比16，大腿以上，平视", "一束窗光落在书页和眼睛之间", "书必须保持为书，不变成花、链条或脸部纹理", "bookstore-look-up"),
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "夏夜自动贩卖机", "甜系，都市，轻微俏皮", "夏夜自动贩卖机前，冷色灯箱，街边树影", "工字背心，浅色牛仔短裤，薄衬衫外搭", "她刚拿到冰饮，转头发现你在拍她", "9比16，大腿以上，街拍抓拍", "贩卖机冷光在她发丝边缘形成蓝色轮廓", "冰饮罐必须保持为饮料罐，不变成手镯、链条或灯", "vending-machine-summer-night"),

    # Eastern aesthetic atlas routes.
    Route("东方美学图鉴", "东方美学图鉴", "四大才女人物页", "年轻，书卷气，图录感", "米白宣纸背景，浅墨晕染，香槟金圆弧，书案与古籍", "淡青宋风褙子，白色内衫，玉簪", "她翻阅古籍，低头沉思，右侧人物区清晰", "9比16，竖版图鉴海报，人物页变体", "左侧竖排姓名区与右侧人物形成博物馆图录版式", "古籍必须保持为书，不变成脸部纹样、链条或多余装饰", "atlas-talented-woman"),
    Route("东方美学图鉴", "东方美学图鉴", "四大美人封面", "年轻，典雅，收藏感", "浅色宣纸封面，竖排标题区，香槟金圆弧，淡胭脂粉", "浅粉古典长裙，花枝发簪，覆身丝绸", "代表人物侧身回眸，人物位于右侧主视觉区", "9比16，竖版图鉴封面变体", "竖排主标题与右侧人物形成第一视觉", "花枝必须保持为单一装饰，不变成脸部纹样、链条或多余人物", "atlas-four-beauties-cover"),
    Route("东方美学图鉴", "东方美学图鉴", "十二花神人物页", "年轻，典雅，图录感", "米白宣纸背景，浅墨晕染，香槟金圆弧，单枝玉兰", "月白宋风长裙，淡金腰封，玉兰簪", "她手持玉兰花枝，微侧身站在右侧人物区", "9比16，竖版图鉴海报，人物页变体", "左侧竖排姓名区与右侧人物形成博物馆图录版式", "玉兰花枝必须保持为单枝花，不变成脸部纹样、链条或多余装饰", "atlas-magnolia-goddess"),
    Route("东方美学图鉴", "东方美学图鉴", "二十四节气人物页", "年轻，清新，文化感", "9比16竖版宣纸图鉴海报，左上预留清晰标题框写“二十四节气”，标题框下方预留当前节气名位置，淡墨节气纹样，细金线，单枝柳叶", "浅绿色宋风长裙，米白披帛", "她手持柳枝，像正在记录春日第一阵风", "9比16，竖版图鉴海报，人物页变体，左侧文字区+右侧人物区", "左上标题框写二十四节气，节气名位置清晰可后期叠字，人物与柳枝保持第一视觉", "柳枝必须保持为植物枝条，不变成头发、链条或脸部纹理；标题区必须保持干净，不要伪文字乱码", "atlas-solar-term"),
    Route("东方美学图鉴", "东方美学图鉴", "敦煌飞天图鉴", "年轻，神性，壁画感，收藏感", "浅米宣纸，赭石矿物色，抽象飞天飘带，香槟金细线", "赭石与淡金飞天服饰，覆身层叠丝绸", "她手持琵琶，飘带围绕但不遮脸", "9比16，竖版图鉴封面或人物页变体", "赭石色飘带与竖排标题形成图录感", "琵琶必须保持为乐器，飘带不得穿过脸或变成手臂", "atlas-dunhuang-feitian"),

]

FIXED_FAMILY_ORDER = [
    "东方幻想古风",
    "古典东方美人",
    "现代东方美人",
    "古风闺蜜",
    "甜系纯欲生活写真",
    "东方美学图鉴",
]


EXPLORATION_IDEAS: list[ExplorationIdea] = [
    ExplorationIdea(
        "非传统空间",
        "把东方美人放入一个非传统、非古装、非普通城市的空间，让空间本身带有诗性或奇观，但不要提前限定具体风格名。",
        "必须由GPT自行命名风格，并自主推导场景、服装、动作和唯一主视觉钩子。",
        "open-unusual-space",
    ),
    ExplorationIdea(
        "未来器物",
        "从一个带东方审美的未来器物出发，围绕器物和人物关系创造画面，而不是套用已有古风或赛博模板。",
        "器物必须语义清晰，不能变成随机链条、首饰或背景噪声。",
        "open-future-object",
    ),
    ExplorationIdea(
        "日常魔幻",
        "让普通生活场景发生一个轻微不可能的东方诗意瞬间，保持真实女生感和电影感，不走夸张玄幻。",
        "魔幻只允许一个核心异常，不堆粒子、不堆光效。",
        "open-daily-magic",
    ),
    ExplorationIdea(
        "东方材料实验",
        "围绕宣纸、青瓷、漆器、竹、玉、铜、丝、墨等材料重新发明一个现代或幻想视觉空间。",
        "材料质感必须服务人物，不能抢脸，不能变成满屏纹样。",
        "open-material-study",
    ),
    ExplorationIdea(
        "跨时代相遇",
        "让古典东方审美与一个完全不同的时代或媒介相遇，但不直接指定朝代、城市或职业。",
        "保持东方美人主体和20-26岁年轻感，由GPT自行决定时代碰撞方式。",
        "open-time-crossing",
    ),
    ExplorationIdea(
        "梦境地理",
        "发明一个不存在但有东方文化气息的地理空间，让人物像正在经过某个梦境边界。",
        "需要一个清晰故事瞬间、一个主视觉形状和一个明确道具。",
        "open-dream-geography",
    ),
]


EXPLORATION_DETAIL_AXES = {
    "style_name": [
        "纸月车站",
        "青瓷雨廊",
        "竹影玻璃城",
        "漆光候鸟馆",
        "玉雾电梯井",
        "墨色潮汐室",
        "桂影天桥",
        "铜镜冷光",
        "宣纸风场",
        "莲灯地下街",
    ],
    "aesthetic": [
        "现代生活空间里出现极克制的东方诗性异常，真实摄影优先",
        "传统材料被放入当代空间，人物像刚刚发现空间发生变化",
        "轻微未来感与东方器物共存，但不走赛博朋克和游戏海报",
        "普通场景被一种东方材料气质重新染色，保持安静、年轻、电影感",
        "一个不存在的东方地理边界出现在日常路径上，人物正在经过它",
    ],
    "scene": [
        "雨后城市连廊，玻璃墙外有青瓷色水光，远处行人虚化",
        "深夜便利店冷柜前，货架尽头出现一面铜镜般的柔光反射",
        "旧书店后门小巷，宣纸一样的白色雾气从门缝里飘出",
        "现代地铁出口的长楼梯，灯箱光被竹影切成细长斑纹",
        "海边公交站，候车亭玻璃上映出不存在的月门和莲灯",
        "安静美术馆侧厅，漆黑展墙前只有一件发光的玉质器物",
        "清晨天桥，浅雾和城市高楼之间出现一条水墨般的风带",
        "老式电梯厅，金属门反射出一座很远的东方庭院",
    ],
    "outfit": [
        "米白棉麻短衫，浅青长裙，低马尾，少量玉色配饰",
        "象牙白衬衫，墨绿色马甲，宽松半裙，黑发半挽",
        "浅灰针织短上衣，青瓷色伞裙，薄纱披肩但不透明",
        "月白真丝衬衫，深茶色阔腿裤，细玉扣耳饰",
        "淡杏色轻外套，白色内搭，浅色长裙，帆布鞋",
        "雾蓝棉麻上衣，米白半裙，简单发簪，生活化",
    ],
    "story": [
        "她正伸手触碰一件异常发光的东方器物，听见你叫她后回头",
        "她走到空间边界前停下，手里的小物件和远处光影产生呼应",
        "她刚推开门，风把发丝和衣角轻轻带起，像看见了不可思议的一幕",
        "她低头确认手中道具，又抬眼看向镜头，表情介于惊讶和温柔之间",
        "她从人群旁经过，忽然被一束不合常理但很安静的东方光线吸引",
        "她将手中道具递到一半，环境里的异象刚刚出现",
    ],
    "hook": [
        "一圈像月门一样的柔光，只在人物身后半边出现",
        "青瓷色水光沿地面延伸，像一条很窄的河",
        "铜镜反射出另一个不存在的东方庭院",
        "竹影在玻璃上形成书法般的斜线",
        "一盏莲灯出现在现代空间的远处尽头",
        "宣纸雾气从门缝或窗边轻轻展开",
        "玉质器物发出低亮度冷光，成为唯一奇观点",
        "城市灯箱被墨色风带切开，形成安静的留白",
    ],
    "prop": [
        "白瓷杯",
        "小开本旧书",
        "青瓷色雨伞",
        "单枝白花",
        "玉质小盒",
        "纸质车票",
        "竹柄团扇",
        "透明玻璃水瓶",
    ],
}


def _exploration_pick(options: list[str], idea: ExplorationIdea, day: dt.date, salt: int) -> str:
    seed = day.toordinal() + sum(ord(char) for char in idea.slug) + salt
    return options[seed % len(options)]


def exploration_summary(idea: ExplorationIdea, day: dt.date) -> dict[str, str]:
    prop = _exploration_pick(EXPLORATION_DETAIL_AXES["prop"], idea, day, 23)
    return {
        "style_name": _exploration_pick(EXPLORATION_DETAIL_AXES["style_name"], idea, day, 3),
        "aesthetic": _exploration_pick(EXPLORATION_DETAIL_AXES["aesthetic"], idea, day, 5),
        "scene": _exploration_pick(EXPLORATION_DETAIL_AXES["scene"], idea, day, 7),
        "outfit": _exploration_pick(EXPLORATION_DETAIL_AXES["outfit"], idea, day, 11),
        "story": _exploration_pick(EXPLORATION_DETAIL_AXES["story"], idea, day, 13),
        "hook": _exploration_pick(EXPLORATION_DETAIL_AXES["hook"], idea, day, 17),
        "prop": prop,
        "prop_lock": f"{prop}必须保持为清晰可识别的原物体，不得变成链条、首饰、脸部纹理、背景噪声或随机装饰。",
    }


COMMON_NEGATIVE = (
    "low quality, low resolution, blurry, jpeg artifacts, watermark, text, logo, "
    "bad anatomy, bad hands, extra fingers, missing fingers, fused fingers, "
    "distorted face, asymmetrical eyes, plastic skin, over-smoothed skin, "
    "old-looking face, matronly styling, age drift, underage, childish, "
    "scenery inside face, landscape on face, object fused with face, cup turning into chain, "
    "prop morphing, object mutation, jewelry replacing prop, random chain objects, "
    "deformed prop, melted object, broken cup, lantern becoming jewelry, "
    "flowers fused into skin, fabric fused into hands, duplicate person, background stealing focus"
)


VARIANT_AXES = {
    "face": [
        "鹅蛋脸，清冷眉眼，淡妆",
        "圆润鹅蛋脸，柔和杏眼，低饱和唇色",
        "偏长鹅蛋脸，沉静眼神，自然眉形",
        "方圆脸，端正骨相，温柔但有主见",
        "小圆脸，明亮眼睛，干净亲和",
        "窄鹅蛋脸，细长眼尾，气质更疏离",
        "柔和方圆脸，眉眼舒展，成熟温婉",
        "饱满鹅蛋脸，眼神明亮，少女感但成年",
        "高颧骨轻熟脸，眼神克制，轮廓清晰",
        "圆中带长的脸型，眉眼柔软，安静亲近",
    ],
    "hair": [
        "低盘发，少量碎发贴近脸侧",
        "半挽发，发尾自然垂落",
        "高髻但发饰克制",
        "低马尾或松散发髻，生活化",
        "黑发顺直，发丝被风轻轻带起",
        "侧分长发，耳侧一缕碎发",
        "松散双环髻，发饰极少",
        "湿润空气里的微乱发丝",
        "低髻配一支素簪",
        "长发半披，发尾压在肩前",
    ],
    "time": [
        "清晨薄光",
        "午后斜光",
        "雨后蓝调时刻",
        "黄昏暖光",
        "夜晚灯火",
        "月光与低灯混合",
    ],
    "weather": [
        "晴天微风",
        "阴天柔光",
        "细雨",
        "薄雾",
        "雪后反光",
        "潮湿空气",
    ],
    "camera": [
        "平视中近景，眼神优先",
        "轻微低机位，保留人物气场",
        "肩后视角，强调正在发生的瞬间",
        "长焦压缩背景，主体更突出",
        "近距离抓拍，保留生活感",
        "侧前方三分之四角度，保留动作关系",
        "门框或窗框前景遮挡，制造窥见瞬间但不偷窥",
        "人物略偏画面一侧，留出故事方向",
        "手部和道具在前景，脸部仍最清晰",
        "半身近景，背景只保留柔和形状",
    ],
    "gesture": [
        "手指停在动作中途，不要摆拍完成态",
        "听见脚步声后微微回头",
        "整理袖口或衣摆，动作自然",
        "视线先看向道具，再看向镜头",
        "被叫住的一瞬间，表情刚刚变化",
    ],
    "palette": [
        "月白、淡青、少量香槟金",
        "雾蓝、米白、温润木色",
        "浅杏、茶金、低饱和朱砂",
        "墨蓝、暖灰、烛火金",
        "浅绿、宣纸白、淡墨灰",
        "藕荷、烟灰蓝、旧木色",
        "雪白、深青、冷银灰",
        "淡粉、米白、雨后青石灰",
        "暖玉白、浅绛红、低亮金",
        "青瓷绿、象牙白、浅茶色",
    ],
    "prop": [
        "单一主道具，背景道具只做软焦",
        "增加一个小型生活道具，但不得抢脸",
        "道具靠近手部，语义必须清晰",
        "道具放在前景边缘，形成空间层次",
        "道具只保留一件高光物，避免堆叠",
    ],
    "scene": [
        "把主场景切到入口、窗边、廊下或转角，不总在正中央",
        "加入一个可感知的远处次空间，如院门、街口、屏风后或水面尽头",
        "使用前景遮挡建立空间层次，但不得遮住脸和眼睛",
        "让人物处在移动路径上，如经过门槛、桥边、窗前或桌边",
        "把环境压缩为少量关键形状，避免背景铺满细节",
        "使用一个局部生活角落，而不是完整大场景展示",
        "让场景中存在明确方向感：她正在走来、离开、回头或停下",
        "把背景主符号放在侧后方，人物仍是第一视觉焦点",
    ],
    "outfit": [
        "改变上装轮廓：短衫、薄外衫、披帛、衬衫或家居常服中择一",
        "改变下装轮廓：长裙、短裙、阔腿裤、曲裾下摆或轻便短裤中择一",
        "强调一种真实材质：丝、棉麻、绡纱、针织、牛仔、宋锦或宣纸感纹理",
        "服装层次保持两层以内，避免堆满珠宝、披帛和复杂纹样",
        "让衣料有真实重量和垂坠，不能像塑料片或游戏皮肤",
        "用一处小面积主题色改变气质，主体服装仍保持克制",
        "穿搭必须服务故事动作，比如便于行走、递茶、翻书、撑伞或回眸",
        "避免沿用上一张的固定白裙、红金礼服或黑金晚装套路",
    ],
    "story": [
        "故事触发点来自外部声音：有人叫她、风吹动门帘、雨声突然变大",
        "故事触发点来自手中物：书页停住、茶杯递到一半、花束刚被接过",
        "故事触发点来自关系互动：等待、照顾、回应、重逢或同行",
        "故事触发点来自环境变化：灯火亮起、云影移动、雨停、月光落下",
        "人物不是展示服装，而是在完成一个生活动作的中途",
        "画面必须能用一句话说清正在发生什么",
        "优先保留未完成瞬间：将要开口、刚刚回头、手还停在半空",
        "叙事不能只写美貌，要写事件、动作和视线目标",
    ],
    "composition": [
        "大腿以上，脸、手、主道具同时清楚",
        "半身近景，眼神和手部动作优先",
        "全身竖构图，但人物高度必须占画面70%以上",
        "双人关系图时两人形成斜线，不要并排证件照",
        "人物偏左或偏右三分之一，给动作方向留空间",
        "前景道具只占边缘，不能压住脸",
        "低机位或平视二选一，不使用夸张超广角",
        "画面第一眼看脸，第二眼看动作，第三眼看场景",
    ],
    "visual_hook": [
        "一个清晰主视觉钩子：光、伞、团扇、书页、花影、帘幕或水面倒影只能选一个",
        "主视觉钩子必须和人物动作发生关系，不做纯背景装饰",
        "如果有金色、珠宝或灯火，只保留一处高光",
        "如果有花、云纹或壁画，只做低透明背景气氛",
        "钩子要帮助叙事：说明她为什么停下、回头、抬眼或伸手",
        "不要让钩子变成满屏粒子、满屏纹样或随机发光物",
    ],
    "environment_motion": [
        "微风带动发丝和衣摆，幅度克制",
        "雨滴、雾气或水面反光只做空气感",
        "帘幕、树影或灯火轻微移动，制造被抓拍感",
        "背景人群或远景保持软焦，不形成第二主体",
        "环境运动必须解释故事瞬间，而不是制造视觉噪声",
    ],
}


FAMILY_VARIANTS = {
    "东方幻想古风": [
        "减少珠宝和粒子，只保留一个奇观装置",
        "把奇观放到远景，脸部保持干净",
        "强化动作链，让神性来自事件而不是装饰",
        "使用更冷静的矿物色调，避免红金过载",
    ],
    "古典东方美人": [
        "强化古典生活瞬间，减少舞台感",
        "用器物和手势讲故事，避免只站着看镜头",
        "服装更日常、更有真实布料重量",
        "背景只保留一处文化符号，避免满屏装饰",
    ],
    "现代东方美人": [
        "偏写实杂志抓拍，避免商业大片摆拍",
        "增加城市或室内生活细节，弱化棚拍感",
        "换成更自然的动作，不要固定珠宝特写套路",
        "使用真实环境光，减少高反差广告光",
    ],
    "古风闺蜜": [
        "关系动作必须变化，不能总是坐着聊天",
        "两人一动一静，形成照顾或回应关系",
        "脸型、发型和服装色相必须明显区分",
        "背景服务两人关系，不做仙侠奇观",
    ],
    "甜系纯欲生活写真": [
        "强化真实生活抓拍，避免固定女友视角模板",
        "改变人脸风格、发型和小动作",
        "穿搭只保留生活化，不做网红封面",
        "用环境小事件制造故事，而不是单纯站姿",
    ],
    "东方美学图鉴": [
        "保持图鉴版式，但更换纸张肌理和主元素",
        "标题区只留干净区域，文字后期叠加",
        "人物动作和道具每次变化，避免同构图套壳",
        "主色跟随主题变化，避免固定米白金色模板",
    ],
}


def _variant_pick(options: list[str], day: dt.date, route: Route, position: int, salt: int) -> str:
    slug_score = sum(ord(char) for char in route.slug)
    family_score = sum(ord(char) for char in route.family)
    step = 1
    for candidate in (3, 5, 7, 2):
        if len(options) % candidate != 0:
            step = candidate
            break
    index = (day.toordinal() + slug_score + family_score + position * step + salt) % len(options)
    return options[index]


def daily_variant(route: Route, day: dt.date | None, position: int = 0) -> str:
    if day is None:
        return ""
    family_notes = FAMILY_VARIANTS.get(route.family, [])
    family_note = (
        _variant_pick(family_notes, day, route, position, 3)
        if family_notes
        else "在不改变核心路线的前提下制造新的日常瞬间"
    )
    parts = [
        f"当日变体锁定：{family_note}",
        f"脸部差异：{_variant_pick(VARIANT_AXES['face'], day, route, position, 5)}",
        f"发型变化：{_variant_pick(VARIANT_AXES['hair'], day, route, position, 11)}",
        f"时间光线：{_variant_pick(VARIANT_AXES['time'], day, route, position, 17)}",
        f"天气空气：{_variant_pick(VARIANT_AXES['weather'], day, route, position, 23)}",
        f"镜头变化：{_variant_pick(VARIANT_AXES['camera'], day, route, position, 29)}",
        f"动作微差：{_variant_pick(VARIANT_AXES['gesture'], day, route, position, 31)}",
        f"当日色彩：{_variant_pick(VARIANT_AXES['palette'], day, route, position, 37)}",
        f"道具策略：{_variant_pick(VARIANT_AXES['prop'], day, route, position, 41)}",
        f"场景变体：{_variant_pick(VARIANT_AXES['scene'], day, route, position, 43)}",
        f"穿搭变体：{_variant_pick(VARIANT_AXES['outfit'], day, route, position, 47)}",
        f"叙事变体：{_variant_pick(VARIANT_AXES['story'], day, route, position, 53)}",
        f"构图变体：{_variant_pick(VARIANT_AXES['composition'], day, route, position, 59)}",
        f"主视觉钩子：{_variant_pick(VARIANT_AXES['visual_hook'], day, route, position, 61)}",
        f"环境运动：{_variant_pick(VARIANT_AXES['environment_motion'], day, route, position, 67)}",
        "变体约束：保留原路线的核心身份，但人物、场景子空间、穿搭轮廓、叙事触发点、动作、镜头、光线、色调、主视觉钩子和副道具必须与上次明显不同。",
    ]
    return "；".join(parts)


def exploration_route(idea: ExplorationIdea, day: dt.date) -> Route:
    detail = exploration_summary(idea, day)
    return Route(
        family="探索路线",
        skill="东方美人",
        style=f"原创探索：{detail['style_name']}（探索种子：{idea.title}）",
        temperament=f"20-26岁年轻成年东亚女性，{detail['aesthetic']}，人物真实、脸和眼睛优先",
        scene=f"{detail['scene']}。探索来源：{idea.brief}",
        outfit=f"{detail['outfit']}。穿搭要求东方审美、生活可信、不过度暴露、不套用固定古风模板",
        action=f"{detail['story']}。手中道具：{detail['prop']}",
        composition="9比16，人物主体占画面60%以上；按故事在全身、大腿以上、上半身或特写中选择最合适景别",
        visual_hook=detail["hook"],
        prop_lock=f"开放探索约束：{idea.constraint} {detail['prop_lock']}",
        slug=idea.slug,
    )


def choose_routes(day: dt.date, count: int) -> list[Route]:
    rng = random.Random(day.isoformat())

    selected: list[Route] = []
    if count > 0:
        selected.append(exploration_route(rng.choice(EXPLORATION_IDEAS), day))

    by_family: dict[str, list[Route]] = {}
    for route in ROUTES:
        by_family.setdefault(route.family, []).append(route)

    # Use a deterministic rotation instead of ad hoc random sampling. A five-day
    # window covers every fixed family, and each family walks through its full
    # route list before repeating, so daily automation does not collapse back to
    # the same familiar four styles.
    fixed_slots = max(count - len(selected), 0)
    ordered_families = [family for family in FIXED_FAMILY_ORDER if family in by_family]
    if ordered_families:
        start_index = day.toordinal() % len(ordered_families)
        rotated_families = ordered_families[start_index:] + ordered_families[:start_index]
        families = rotated_families[:fixed_slots]
    else:
        families = list(by_family)
        rng.shuffle(families)

    family_order_index = {family: index for index, family in enumerate(FIXED_FAMILY_ORDER)}
    for family in families:
        if len(selected) >= count:
            break
        family_routes = by_family[family]
        route_seed = family_order_index.get(family, 0) * 3
        route_index = (day.toordinal() + route_seed) % len(family_routes)
        selected.append(family_routes[route_index])

    if len(selected) < count:
        remaining = [route for route in ROUTES if route not in selected]
        rng.shuffle(remaining)
        selected.extend(remaining[: count - len(selected)])

    return selected[:count]


def prompt_for(route: Route, day: dt.date | None = None, position: int = 0) -> str:
    variant = daily_variant(route, day, position)
    if route.family == "探索路线":
        return (
            "开放原创探索任务。请不要复用现有固定风格名，不要直接套用唐宫、宋韵、敦煌、赛博等既有模板。"
            f"{route.scene}。{route.temperament}。"
            f"{route.outfit}。{route.action}。{route.composition}。"
            f"{route.visual_hook}。"
            "最终画面必须仍然是东方美人主题：年轻成年东亚女性，年龄20-26岁，脸和眼睛第一优先，"
            "人物占画面60%以上，皮肤真实自然，主体清晰，背景服务人物，装饰密度受控。"
            f"物体语义锁定：{route.prop_lock}。"
            f"{variant}。"
        )
    if route.family == "古风闺蜜":
        return (
            "AncientFemaleCompanionship，古代中国女性陪伴真人摄影，两个成年东亚女性，年龄20-28岁，"
            "关系可以是姐妹、闺蜜、青梅旧友、同行旅伴、同门师姐妹、知己、书友或茶友。"
            "重点是陪伴、守护、依赖、信任、成长、重逢或离别，不是百合恋爱海报，不是挑逗，不是仙侠海报。"
            f"技能路线为{route.skill}，风格为{route.style}。"
            f"气质：{route.temperament}。场景：{route.scene}。服装：{route.outfit}。"
            f"互动瞬间：{route.action}。构图：{route.composition}。"
            f"主视觉钩子：{route.visual_hook}。"
            "必须真实摄影质感，35mm、50mm、85mm或135mm，镜头服务关系和故事，光线柔和自然，有情绪层次，"
            "两位人物脸部骨相不同，不能复制粘贴脸；肩膀有厚度，手臂有肉感，腰胯自然过渡，整体健康丰润。"
            "布料必须是桑蚕丝、丝棉、轻纱、软烟罗或缎面丝绸的分层结构，内层、外层、披帛、床品、枕头彼此独立。"
            "人物占画面75%-85%，人物边界清晰，背景服务人物，禁止魔法光效、HDR、影楼写真和游戏宣传图。"
            f"物体语义锁定：{route.prop_lock}。"
            f"{variant}。"
        )
    return (
        f"年轻成年东亚女性，年龄20-26岁，{route.temperament}。"
        f"技能路线为{route.skill}，风格为{route.style}。"
        f"场景：{route.scene}。服装：{route.outfit}。"
        f"故事瞬间：{route.action}。构图：{route.composition}。"
        f"主视觉钩子：{route.visual_hook}。"
        "脸和眼睛是第一视觉重点，人物占画面60%以上，皮肤真实自然，"
        "主体清晰，背景服务人物，装饰密度受控。"
        f"物体语义锁定：{route.prop_lock}。"
        f"{variant}。"
    )


def structured_block(route: Route, day: dt.date | None = None, position: int = 0) -> str:
    variant = daily_variant(route, day, position)
    if route.family == "探索路线":
        return (
            "技能: 东方美人\n"
            f"风格: {route.style}\n"
            f"审美方向: {route.temperament}\n"
            "人群: 20-26岁年轻成年东亚女性\n"
            f"场景: {route.scene}\n"
            f"穿搭: {route.outfit}\n"
            f"故事瞬间: {route.action}\n"
            f"构图: {route.composition}\n"
            f"主视觉钩子: {route.visual_hook}\n"
            f"道具语义锁定: {route.prop_lock}\n"
            f"当日变体: {variant}\n"
            "生成: 是"
        )
    if route.skill == "东方美学图鉴":
        return (
            "技能: 东方美学图鉴\n"
            "页面类型: 日更竖版图鉴海报\n"
            f"风格: {route.style}\n"
            "年龄: 20-26\n"
            f"气质: {route.temperament}\n"
            f"场景: {route.scene}\n"
            f"服装: {route.outfit}\n"
            f"动作: {route.action}\n"
            f"构图: {route.composition}\n"
            "比例: 9比16\n"
            "文字规则: 生图阶段只保留干净文字区；如果需要准确中文标题，发布前后期叠字，不依赖模型生成文字\n"
            f"当日变体: {variant}\n"
            "生成: 是"
        )
    if route.skill == "甜系纯欲生活写真":
        return (
            "技能: 甜系纯欲生活写真\n"
            "人脸风格: 由Skill自动选择，保持20-26岁年轻自然\n"
            f"场景: {route.scene}\n"
            f"穿搭: {route.outfit}\n"
            f"故事瞬间: {route.action}\n"
            f"构图: {route.composition}\n"
            f"当日变体: {variant}\n"
            "生成: 是"
        )
    if route.skill == "古风闺蜜":
        return (
            "技能: 古风闺蜜\n"
            f"场景: {route.style}\n"
            "关系: 姐姐 + 妹妹\n"
            f"气质: {route.temperament}\n"
            f"服装: {route.outfit}\n"
            f"动作: {route.action}\n"
            f"构图: {route.composition}\n"
            "比例: 9比16\n"
            f"当日变体: {variant}\n"
            "生成: 是"
        )
    return (
        f"技能: {route.skill}\n"
        f"风格: {route.style}\n"
        f"气质: {route.temperament}\n"
        f"场景: {route.scene}\n"
        f"服装: {route.outfit}\n"
        f"动作: {route.action}\n"
        f"构图: {route.composition}\n"
        "年龄: 20-26\n"
        f"当日变体: {variant}\n"
        "生成: 是"
    )


def build_markdown(day: dt.date, routes: list[Route]) -> str:
    title = f"每日东方美人探索 {day.isoformat()}"
    cover = f"/assets/ai/eastern-beauty/{day.isoformat()}/{routes[0].slug}.png"
    description = "记录每日东方美人自动探索：覆盖不同风格、穿搭、人物、场景和角度，并加入年龄与质量锁定。"

    lines = [
        "---",
        f"title: {title}",
        f"subtitle: daily-eastern-beauty-{day.isoformat()}",
        f"top_img: {cover}",
        f"cover: {cover}",
        "tags: [AI, GPT Image, 东方美人, AI绘画, Prompt]",
        f"date: {day.isoformat()} 00:10:00",
        "categories: gpt-image2",
        f"description: {description}",
        "---",
        "",
        "这是一组由「东方美人导演」自动生成的每日探索参数。每天固定五张，但风格、穿搭、人物、场景、角度都会轮转；默认锁定年轻成年女性 20-26 岁，并且五张中固定包含一张脱离既有模板的原创探索思路种子。",
        "",
        "<!-- more -->",
        "",
        "## 今日质量锁定",
        "",
        "- 年龄统一：20-26岁年轻成年东亚女性。",
        "- 风格分散：同一天不重复同一风格家族，且五张中固定包含一张原创探索思路种子。",
        "- 变体分散：即使抽到同一路线，也必须改变人物脸型、发型、场景子空间、穿搭轮廓、叙事触发点、镜头、光线、天气、动作微差、色彩、主视觉钩子和副道具。",
        "- 比例统一：五张图全部使用9:16；图鉴路线也转换为9:16竖版海报变体。",
        "- 主体优先：脸和眼睛第一优先级，人物占画面60%以上。",
        "- 道具锁定：杯子、花束、灯笼、团扇、书籍等必须保持原物体语义。",
        "- 双人检查：古风闺蜜路线必须两张脸不同骨相、人物边界清晰、布料枕头床品互相独立。",
        "- 崩坏规避：禁止景物长进脸里、道具变链条、饰品替代杯子、人物和背景融合。",
        "",
    ]

    for index, route in enumerate(routes, 1):
        image = f"/assets/ai/eastern-beauty/{day.isoformat()}/{route.slug}.png"
        lines.extend(
            [
                f"## {index}. {route.style}",
                "",
                f"![{route.style}]({image})",
                "",
                f"路线：{route.family}。{route.visual_hook}",
                "",
                "结构化参数：",
                "",
                "```text",
                structured_block(route, day, index),
                "```",
                "",
                "Prompt 摘要：",
                "",
                "```text",
                prompt_for(route, day, index),
                "```",
                "",
                "负面提示补充：",
                "",
                "```text",
                COMMON_NEGATIVE,
                "```",
                "",
            ]
        )

    lines.extend(
        [
            "## 今日复盘模板",
            "",
            "发布前检查五张图是否真正拉开：古典 / 幻想 / 现代 / 生活 / 图鉴 / 探索路线至少覆盖四类；如果出现脸部崩坏、物体变形或年龄老成，直接丢弃并用同一结构化参数重跑。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None, help="YYYY-MM-DD, defaults to today")
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--output-dir", default="examples/daily")
    parser.add_argument("--force", action="store_true", help="overwrite an existing daily post")
    args = parser.parse_args()

    day = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    routes = choose_routes(day, args.count)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{day.isoformat()}-daily-eastern-beauty.md"
    if output_file.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing daily post: {output_file}")
    output_file.write_text(build_markdown(day, routes), encoding="utf-8")
    print(output_file)


if __name__ == "__main__":
    main()
