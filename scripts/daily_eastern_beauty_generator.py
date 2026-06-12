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

    # SweetHomeGirl / lifestyle routes.
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "人民广场迎面走来", "甜系，自然，恋爱感，真实", "人民广场，夏日城市街头，斑马线，树影", "浅蓝露肩短袖，白色轻盈短裙，手提小包，耳机", "她迎面走来，发现你在看她后不经意浅笑", "9比16，大腿以上", "人流里只有她的眼神和浅笑最清晰", "耳机和小包必须保持为配饰，不变成链条、手指或背景线", "people-square-sweet"),
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "雨后街角花店", "甜系，亲近，自然，轻微恋爱感", "蓝调时刻街角花店，雨后路面，暖色灯泡", "水洗牛仔外套，奶油色吊带长裙，白色球鞋", "她抱着刚包好的花束，发现你在街对面等她后浅笑", "9比16，大腿以上，街边近距离", "雨滴里的暖色灯泡倒影像一排小灯笼", "花束必须保持为鲜花和包装纸，不变成链条、头发、手指或背景装饰", "flower-shop-bluehour"),
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "夜晚自助洗衣房", "邻家女孩，真实，松弛", "夜晚自助洗衣房，暖白灯，滚筒烘干机，玻璃门反光", "宽松白T，牛仔短裙，帆布鞋", "她把衣服从烘干机里抱出来，发现你在门口等她，忍不住笑了一下", "9比16，上半身，女友视角", "烘干机圆形玻璃门形成柔和光环", "衣服必须保持为柔软布料，不变成链条、绳索、触手或背景纹样", "laundromat-smile"),
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "便利店半夜买饮料", "兔系甜妹，生活感，亲近", "深夜便利店冷柜前，冷白灯，玻璃门反光", "宽松短袖，浅色牛仔短裤，薄针织开衫", "她拿着冰饮回头问你要不要同款", "9比16，上半身，近距离抓拍", "冷柜玻璃上的蓝白光照亮她的侧脸", "饮料瓶必须保持为饮料瓶，不变成链条、灯管或手指", "convenience-store-drink"),
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "书店翻书抬头", "氧气少女，安静，恋爱感", "独立书店，木书架，午后窗光，纸页气息", "白色棉麻衬衫，浅色短裙，帆布包", "她翻书时听见你走近，抬头停顿了一秒", "9比16，大腿以上，平视", "一束窗光落在书页和眼睛之间", "书必须保持为书，不变成花、链条或脸部纹理", "bookstore-look-up"),
    Route("甜系纯欲生活写真", "甜系纯欲生活写真", "夏夜自动贩卖机", "甜系，都市，轻微俏皮", "夏夜自动贩卖机前，冷色灯箱，街边树影", "工字背心，浅色牛仔短裤，薄衬衫外搭", "她刚拿到冰饮，转头发现你在拍她", "9比16，大腿以上，街拍抓拍", "贩卖机冷光在她发丝边缘形成蓝色轮廓", "冰饮罐必须保持为饮料罐，不变成手镯、链条或灯", "vending-machine-summer-night"),

    # Eastern aesthetic atlas routes.
    Route("东方美学图鉴", "东方美学图鉴", "四大才女人物页", "年轻，书卷气，图录感", "米白宣纸背景，浅墨晕染，香槟金圆弧，书案与古籍", "淡青宋风褙子，白色内衫，玉簪", "她翻阅古籍，低头沉思，右侧人物区清晰", "3比4，1080x1440，人物页", "左侧竖排姓名区与右侧人物形成博物馆图录版式", "古籍必须保持为书，不变成脸部纹样、链条或多余装饰", "atlas-talented-woman"),
    Route("东方美学图鉴", "东方美学图鉴", "四大美人封面", "年轻，典雅，收藏感", "浅色宣纸封面，竖排标题区，香槟金圆弧，淡胭脂粉", "浅粉古典长裙，花枝发簪，覆身丝绸", "代表人物侧身回眸，人物位于右侧主视觉区", "3比4，1080x1440，封面", "竖排主标题与右侧人物形成第一视觉", "花枝必须保持为单一装饰，不变成脸部纹样、链条或多余人物", "atlas-four-beauties-cover"),
    Route("东方美学图鉴", "东方美学图鉴", "十二花神人物页", "年轻，典雅，图录感", "米白宣纸背景，浅墨晕染，香槟金圆弧，单枝玉兰", "月白宋风长裙，淡金腰封，玉兰簪", "她手持玉兰花枝，微侧身站在右侧人物区", "3比4，1080x1440，人物页", "左侧竖排姓名区与右侧人物形成博物馆图录版式", "玉兰花枝必须保持为单枝花，不变成脸部纹样、链条或多余装饰", "atlas-magnolia-goddess"),
    Route("东方美学图鉴", "东方美学图鉴", "二十四节气人物页", "年轻，清新，文化感", "宣纸背景，淡墨节气纹样，细金线，单枝柳叶", "浅绿色宋风长裙，米白披帛", "她手持柳枝，像正在记录春日第一阵风", "3比4，1080x1440，人物页", "节气文字区与人物像博物馆展签一样克制", "柳枝必须保持为植物枝条，不变成头发、链条或脸部纹理", "atlas-solar-term"),
    Route("东方美学图鉴", "东方美学图鉴", "敦煌飞天图鉴", "年轻，神性，壁画感，收藏感", "浅米宣纸，赭石矿物色，抽象飞天飘带，香槟金细线", "赭石与淡金飞天服饰，覆身层叠丝绸", "她手持琵琶，飘带围绕但不遮脸", "3比4，1080x1440，封面或人物页", "赭石色飘带与竖排标题形成图录感", "琵琶必须保持为乐器，飘带不得穿过脸或变成手臂", "atlas-dunhuang-feitian"),

]

FIXED_FAMILY_ORDER = [
    "东方幻想古风",
    "古典东方美人",
    "现代东方美人",
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


def exploration_route(idea: ExplorationIdea) -> Route:
    return Route(
        family="探索路线",
        skill="东方美人",
        style=f"原创探索思路：{idea.title}",
        temperament="由GPT根据探索思路自行推导，必须保持年轻、东方美人主体、20-26岁",
        scene=f"由GPT根据探索思路自行发明：{idea.brief}",
        outfit="由GPT自行设计，要求东方审美、人物优先、不过度暴露、不落入固定古风模板",
        action="由GPT自行设计一个正在发生的故事瞬间，必须有明确手部动作和视线目标",
        composition="默认9比16；由GPT在全身、大腿以上、上半身或特写中选择最适合的一种",
        visual_hook="由GPT自行设计一个唯一主视觉钩子；必须新鲜、清晰、可被一句话概括",
        prop_lock=f"开放探索约束：{idea.constraint} 同时所有具体道具一旦生成，必须保持原物体语义，不得变形为链条、皮肤纹样或脸部噪声",
        slug=idea.slug,
    )


def choose_routes(day: dt.date, count: int) -> list[Route]:
    rng = random.Random(day.isoformat())

    selected: list[Route] = []
    if count > 0:
        selected.append(exploration_route(rng.choice(EXPLORATION_IDEAS)))

    by_family: dict[str, list[Route]] = {}
    for route in ROUTES:
        by_family.setdefault(route.family, []).append(route)

    # Use a deterministic rotation instead of ad hoc random sampling. A five-day
    # window covers every fixed family, and each family walks through its full
    # route list before repeating, so daily automation does not collapse back to
    # the same familiar four styles.
    ordered_families = [family for family in FIXED_FAMILY_ORDER if family in by_family]
    if len(ordered_families) >= 5:
        omitted_index = day.toordinal() % len(ordered_families)
        families = ordered_families[:omitted_index] + ordered_families[omitted_index + 1 :]
    else:
        families = list(by_family)
        rng.shuffle(families)

    for family_index, family in enumerate(families):
        if len(selected) >= count:
            break
        family_routes = by_family[family]
        route_index = (day.toordinal() + family_index) % len(family_routes)
        selected.append(family_routes[route_index])

    if len(selected) < count:
        remaining = [route for route in ROUTES if route not in selected]
        rng.shuffle(remaining)
        selected.extend(remaining[: count - len(selected)])

    return selected[:count]


def prompt_for(route: Route) -> str:
    if route.family == "探索路线":
        return (
            "开放原创探索任务。请不要复用现有固定风格名，不要直接套用唐宫、宋韵、敦煌、赛博等既有模板。"
            f"{route.scene}。{route.temperament}。"
            f"{route.outfit}。{route.action}。{route.composition}。"
            f"{route.visual_hook}。"
            "最终画面必须仍然是东方美人主题：年轻成年东亚女性，年龄20-26岁，脸和眼睛第一优先，"
            "人物占画面60%以上，皮肤真实自然，主体清晰，背景服务人物，装饰密度受控。"
            f"物体语义锁定：{route.prop_lock}。"
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
    )


def structured_block(route: Route) -> str:
    if route.family == "探索路线":
        return (
            "技能: 东方美人\n"
            "风格: 原创探索，由GPT自行命名\n"
            f"探索思路: {route.scene.removeprefix('由GPT根据探索思路自行发明：')}\n"
            "人群: 20-26岁年轻成年东亚女性\n"
            "场景: 由GPT自行发明\n"
            "服装: 由GPT自行设计，保留东方审美与人物主体\n"
            "动作: 由GPT自行设计一个正在发生的故事瞬间\n"
            "构图: 9比16，GPT自行选择全身/大腿以上/上半身/特写\n"
            "要求: 必须有唯一主视觉钩子，必须有明确道具语义锁定\n"
            "生成: 是"
        )
    if route.skill == "东方美学图鉴":
        return (
            "技能: 东方美学图鉴\n"
            "页面类型: 人物页 / 封面，按风格自动选择\n"
            f"风格: {route.style}\n"
            "年龄: 20-26\n"
            f"气质: {route.temperament}\n"
            f"场景: {route.scene}\n"
            f"服装: {route.outfit}\n"
            f"动作: {route.action}\n"
            f"构图: {route.composition}\n"
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
        "- 主体优先：脸和眼睛第一优先级，人物占画面60%以上。",
        "- 道具锁定：杯子、花束、灯笼、团扇、书籍等必须保持原物体语义。",
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
                structured_block(route),
                "```",
                "",
                "Prompt 摘要：",
                "",
                "```text",
                prompt_for(route),
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
