# Style Taxonomy

Use this file before adding or selecting a style template. The goal is to keep
the skill universe clear: one visual direction should have one canonical home.

## Canonical Style Families

These are the only primary generation families currently supported.

| Family | Canonical file | Use for | Do not split into |
|---|---|---|---|
| 东方幻想古风 | `styles/东方幻想古风.md` | mythic, xianxia-adjacent, wonder-scale, supernatural, palace ritual, Dunhuang fantasy, moon palace, bronze oracle, dragon court | separate goddess, xianxia, Dunhuang fantasy, palace fantasy, mythic heroine templates |
| 古典东方美人 | `styles/古典东方美人.md` | non-fantasy classical beauty, Song/Tang/Jiangnan/Kunqu/celadon/literati scenes, realistic or lightly stylized classical portraiture | separate Song beauty, Tang beauty, Jiangnan beauty, Kunqu beauty templates |
| 现代东方美人 | `styles/现代东方美人.md` | modern realistic Eastern beauty, new-Chinese fashion, qipao cinema, jewelry/editorial, modern tea room, quiet luxury, urban scenes | separate qipao, jewelry, modern tea, new-Chinese fashion templates |
| Cosplay展会摄影 | `styles/Cosplay展会摄影.md` | official convention cosplay photography, coser, ChinaJoy, Bilibili World, Tokyo Game Show, AAA original game-character cosplay, Vogue editorial convention portrait | separate ChinaJoy, BW, TGS, coser, racing queen, game booth templates |
| 古风闺蜜 / AncientFemaleCompanionship | `styles/古风闺蜜.md` | two-person ancient Chinese female companionship, sisters, close friends, confidantes, travel companions, night talk, hair braiding, umbrella sharing, reunion, farewell | separate ancient girlfriends, sisterhood, Jiangnan companions, lantern reunion templates |
| 甜系纯欲生活写真 | `styles/甜系纯欲生活写真.md` | modern girlfriend/lifestyle portrait, real young women, story moment, natural attraction, casual street/home/cafe/bookstore scenes | separate SweetHomeGirl, girlfriend POV, pure-desire lifestyle templates |
| 东方美学图鉴 | `styles/东方美学图鉴.md` | Xiaohongshu / museum-catalog visual content system: covers, overview pages, character pages, cultural atlas, four beauties, four talented women, flower gods, solar terms | separate cover, character page, cultural atlas, Xiaohongshu card templates |

## Supporting Files

These files are not primary style templates. They should not be used as route
families in automation or user-facing style lists.

| File | Role |
|---|---|
| `styles/东方美人审美系统.md` | upper-level temperament and aesthetic selector used before choosing a route family |
| `styles/甜系纯欲生活写真-场景素材库.md` | optional SweetHomeGirl micro-scene expansion library |
| `references/oriental-visual-discipline.md` | hidden clean system and de-noise rules, especially for ornate fantasy routes |
| `references/gufeng-visual-library.md` | shared gu feng visual vocabulary, not a route family |
| `references/wow-factor-system.md` | first-glance visual hook system, not a style template |
| `references/character-subject-system.md` | face, posture, gesture, and subject integrity system |
| `references/quality-control.md` | global prompt QA and failure prevention |
| `references/global-negative-system.md` | shared anatomy, hands, feet, face integrity, prop semantics, multi-subject boundary, and quality negative base |

## Current Route Inventory

### 东方幻想古风

- 天象神朝
- 昆仑雪剑
- 敦煌壁画神女
- 沧海龙庭
- 莲梦镇邪
- 凤阙宫火
- 绮罗金帐
- 月宫炼华
- 青铜神谕城
- 雾浴私语

### 古典东方美人

- 洛神水镜
- 宋韵茶影
- 唐宫夜宴
- 唐宫花泉仪式
- 江南烟雨
- 青瓷月影
- 昆曲花影
- 竹林清谈
- 胭脂雪
- 玉楼春睡

### 现代东方美人

- 新中式杂志
- 东方静奢
- 旗袍电影感
- 东方珠宝大片
- 现代茶室光影
- 都市晚宴东方
- 江南现代诗意
- 美术馆开幕夜
- 雨夜出租车窗
- 东方香氛空间
- 城市天桥晨光

### Cosplay展会摄影

- 官方展台女武神
- 赛博巫女发布区
- 星际驾驶员摄影区
- 皇家护卫合影墙
- 赛车皇后主舞台
- AI操作员试玩区
- 狐妖偶像展台
- 女侦探互动展区

### 古风闺蜜 / AncientFemaleCompanionship

- 闺阁夜话
- 灯下梳发
- 同榻共读
- 夏夜纳凉
- 守夜温灯
- 江南湖亭共伞
- 山寺晨行
- 灯会重逢
- 书肆听雨

### 甜系纯欲生活写真

- 人民广场迎面走来
- 雨后街角花店
- 夜晚自助洗衣房
- 便利店半夜买饮料
- 书店翻书抬头
- 夏夜自动贩卖机
- 清晨早餐店
- 地铁口等你
- 水果摊夏风
- 咖啡馆靠窗写字

### 东方美学图鉴

- 四大才女人物页
- 四大美人封面
- 十二花神人物页
- 二十四节气人物页
- 敦煌飞天图鉴
- 朝代服饰时间轴
- 东方器物人物页
- 十二花神总览

## Boundary Rules

1. If a request is about supernatural spectacle, mythic power, impossible scale,
   ritual space, or fantasy worldbuilding, use `东方幻想古风`.
2. If a request is classical but not supernatural, use `古典东方美人`.
3. If a request is modern, realistic, editorial, new-Chinese fashion, urban, or
   jewelry-led, use `现代东方美人`.
4. If the request is about coser, cosplay convention, ChinaJoy, Bilibili World,
   Tokyo Game Show, official booth photography, AAA game character costume, or
   a polished convention portrait, use `Cosplay展会摄影`.
5. If the subject is two ancient women and the relationship is the point, use
   `古风闺蜜 / AncientFemaleCompanionship`, even when the scene is Jiangnan,
   mountain, festival, or bookstore.
6. If the subject is one modern lifestyle woman with girlfriend/story feeling,
   use `甜系纯欲生活写真`.
7. If the output is a designed content page, cover, character page, overview,
   cultural card, or museum-catalog layout, use `东方美学图鉴`.
8. `东方美人审美系统` can modify any compatible family, but it is not a standalone
   output template.
9. Do not create a new style file when the request can be represented as a new
   route inside an existing canonical family.

## Merge Candidates And Decisions

- `甜系纯欲生活写真-场景素材库.md` stays as a subordinate scene library, not a
  separate style.
- `东方美人审美系统.md` stays as a shared aesthetic layer, not a separate style.
- `古风闺蜜` and `AncientFemaleCompanionship` are one family. The English name is
  an alias and should not become a second file.
- `敦煌飞天` can appear in both `东方幻想古风` and `东方美学图鉴`; the split is by
  output type. Fantasy key visual goes to `东方幻想古风`; catalog/page design goes
  to `东方美学图鉴`.
- `江南` can appear in classical, modern, and companionship families; the split
  is by subject and era, not by location.
