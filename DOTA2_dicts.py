WIN_NEGATIVE = [
    '{}侥幸赢得了比赛',
    '{}走狗屎运赢得了比赛',
    '{}躺赢了比赛',
    '{}打团都没来, 队友4V5赢得了比赛',
]

WIN_POSTIVE = [
    '{}带领团队走向了胜利',
    '{}暴打对面后赢得了胜利',
    '{} CARRY全场赢得了胜利',
    '{}把对面当猪宰了, 赢得了胜利',
    '{}又赢了, 这游戏就是这么枯燥, 且乏味',
    '{}直接进行一个比赛的赢',
]

LOSE_NEGATIVE = [
    '{}被人按在地上摩擦, 输掉了这场比赛',
    '{}悲惨地输掉了比赛',
    '{}头都被打歪了, 心态爆炸地输掉了比赛',
    '{}捕鱼被鱼吃了, 输掉了比赛',
    '{}打的是个几把',
    '{}直接进行一个比赛的输',
]

LOSE_POSTIVE = [
    '{}无力回天输掉了比赛',
    '{}尽力了, 但还是输了比赛',
    '{}背靠世界树, 虽败犹荣',
    '{}带不动队友, 输了比赛',
    '{}又输了, 很难受, 宁愿输的是我',
]


GAME_MODE = {
    0: "No Game Mode",
    1: "全英雄选择",
    2: "队长模式",
    3: "随机征召",
    4: "小黑屋",
    5: "全部随机",
    7: "万圣节活动",
    8: "反队长模式",
    9: "贪魔活动",
    10: "教程",
    11: "中路模式",
    12: "生疏模式",
    13: "新手模式",
    14: "Compendium Matchmaking",
    15: "自定义游戏",
    16: "队长征召",
    17: "平衡征召",
    18: "技能征召",
    19: "活动模式",
    20: "全英雄死亡随机",
    21: "中路SOLO",
    22: "全英雄选择",
    23: "加速模式"
}


LOBBY = {
    -1: "非法ID",
    0:  "普通匹配",
    1:  "练习",
    2:  "锦标赛",
    3:  "教程",
    4:  "合作对抗电脑",
    5:  "组排模式",
    6:  "单排模式",
    7:  "天梯匹配",
    8:  "中路SOLO",
    12: "天陨旦"
}


# 服务器ID列表
AREA_CODE = {
    111: "美国西部",
    112: "美国西部",
    114: "美国西部",
    121: "美国东部",
    122: "美国东部",
    123: "美国东部",
    124: "美国东部",
    131: "欧洲西部",
    132: "欧洲西部",
    133: "欧洲西部",
    134: "欧洲西部",
    135: "欧洲西部",
    136: "欧洲西部",
    142: "南韩",
    143: "南韩",
    151: "东南亚",
    152: "东南亚",
    153: "东南亚",
    161: "中国",
    163: "中国",
    171: "澳大利亚",
    181: "俄罗斯",
    182: "俄罗斯",
    183: "俄罗斯",
    184: "俄罗斯",
    185: "俄罗斯",
    186: "俄罗斯",
    191: "欧洲东部",
    192: "欧洲东部",
    200: "南美洲",
    202: "南美洲",
    203: "南美洲",
    204: "南美洲",
    211: "非洲南部",
    212: "非洲南部",
    213: "非洲南部",
    221: "中国",
    222: "中国",
    223: "中国",
    224: "中国",
    225: "中国",
    231: "中国",
    236: "中国",
    242: "智利",
    251: "秘鲁",
    261: "印度"
}

REGION = {
    "region_0": "自动",
    "region_1": "美国西部",
    "region_2": "美国东部",
    "region_3": "卢森堡",
    "region_5": "新加坡",
    "region_6": "迪拜",
    "region_7": "澳大利亚",
    "region_8": "斯德哥尔摩",
    "region_9": "奥地利",
    "region_10": "巴西",
    "region_11": "南非",
    "region_12": "电信（上海）",
    "region_13": "联通（一）",
    "region_14": "智利",
    "region_15": "秘鲁",
    "region_16": "印度",
    "region_17": "电信（广东）",
    "region_18": "电信（浙江）",
    "region_19": "日本",
    "region_20": "电信（华中）",
    "region_25": "联通（二）",
}

# 英雄昵称
# 每个英雄的第一个为游戏内默认名字
HEROES = {
    1:   'antimage',
    2:   'axe',
    3:   'bane',
    4:   'bloodseeker',
    5:   'crystal_maiden',
    6:   'drow_ranger',
    7:   'earthshaker',
    8:   'juggernaut',
    9:   'mirana',
    10:  'morphling',
    11:  'nevermore',
    12:  'phantom_lancer',
    13:  'puck',
    14:  'pudge',
    15:  'razor',
    16:  'sand_king',
    17:  'storm_spirit',
    18:  'sven',
    19:  'tiny',
    20:  'vengefulspirit',
    21:  'windrunner',
    22:  'zuus',
    23:  'kunkka',
    25:  'lina',
    26:  'lion',
    27:  'shadow_shaman',
    28:  'slardar',
    29:  'tidehunter',
    30:  'witch_doctor',
    31:  'lich',
    32:  'riki',
    33:  'enigma',
    34:  'tinker',
    35:  'sniper',
    36:  'necrolyte',
    37:  'warlock',
    38:  'beastmaster',
    39:  'queenofpain',
    40:  'venomancer',
    41:  'faceless_void',
    42:  'skeleton_king',
    43:  'death_prophet',
    44:  'phantom_assassin',
    45:  'pugna',
    46:  'templar_assassin',
    47:  'viper',
    48:  'luna',
    49:  'dragon_knight',
    50:  'dazzle',
    51:  'rattletrap',
    52:  'leshrac',
    53:  'furion',
    54:  'life_stealer',
    55:  'dark_seer',
    56:  'clinkz',
    57:  'omniknight',
    58:  'enchantress',
    59:  'huskar',
    60:  'night_stalker',
    61:  'broodmother',
    62:  'bounty_hunter',
    63:  'weaver',
    64:  'jakiro',
    65:  'batrider',
    66:  'chen',
    67:  'spectre',
    68:  'ancient_apparition',
    69:  'doom_bringer',
    70:  'ursa',
    71:  'spirit_breaker',
    72:  'gyrocopter',
    73:  'alchemist',
    74:  'invoker',
    75:  'silencer',
    76:  'obsidian_destroyer',
    77:  'lycan',
    78:  'brewmaster',
    79:  'shadow_demon',
    80:  'lone_druid',
    81:  'chaos_knight',
    82:  'meepo',
    83:  'treant',
    84:  'ogre_magi',
    85:  'undying',
    86:  'rubick',
    87:  'disruptor',
    88:  'nyx_assassin',
    89:  'naga_siren',
    90:  'keeper_of_the_light',
    91:  'wisp',
    92:  'visage',
    93:  'slark',
    94:  'medusa',
    95:  'troll_warlord',
    96:  'centaur',
    97:  'magnataur',
    98:  'shredder',
    99:  'bristleback',
    100: 'tusk',
    101: 'skywrath_mage',
    102: 'abaddon',
    103: 'elder_titan',
    104: 'legion_commander',
    105: 'techies',
    106: 'ember_spirit',
    107: 'earth_spirit',
    108: 'abyssal_underlord',
    109: 'terrorblade',
    110: 'phoenix',
    111: 'oracle',
    112: 'winter_wyvern',
    113: 'arc_warden',
    114: 'monkey_king',
    119: 'dark_willow',
    120: 'pangolier',
    121: 'grimstroke',
    123: 'hoodwink',
    126: 'void_spirit',
    128: 'snapfire',
    129: 'mars',
    135: 'dawnbreaker',
}

HEROES_CHINESE = {
    1:   ['敌法师', '敌法', 'AM'],
    2:   ['斧王'],
    3:   ['祸乱之源', '祸乱', '水桶腰'],
    4:   ['血魔'],
    5:   ['水晶室女', '冰女', 'CM'],
    6:   ['卓尔游侠', '小黑'],
    7:   ['撼地者', '小牛'],
    8:   ['主宰', '剑圣', 'jugg', '奶棒人'],
    9:   ['米拉娜', '白虎', 'pom'],
    10:  ['变体精灵', '水人'],
    11:  ['影魔', '影魔王', 'SF', '影儿魔儿'],
    12:  ['幻影长矛手', 'PL'],
    13:  ['帕克'],
    14:  ['帕吉', '屠夫', '扒鸡', '啪唧'],
    15:  ['剃刀', '电魂', '电棍'],
    16:  ['沙王', 'SK'],
    17:  ['风暴之灵', '蓝猫'],
    18:  ['斯温', '流浪剑客', '流浪'],
    19:  ['小小'],
    20:  ['复仇之魂', '复仇', 'VS'],
    21:  ['风行者', '风行', 'WR'],
    22:  ['宙斯'],
    23:  ['昆卡', '船长'],
    25:  ['莉娜', '火女'],
    26:  ['莱恩', '恶魔巫师', 'Lion'],
    27:  ['暗影萨满', '小Y', '小歪'],
    28:  ['斯拉达', '大鱼', '大鱼人'],
    29:  ['潮汐猎人', '潮汐', '西瓜皮'],
    30:  ['巫医'],
    31:  ['巫妖'],
    32:  ['力丸', '隐形刺客', '隐刺'],
    33:  ['谜团'],
    34:  ['修补匠', 'TK', 'Tinker'],
    35:  ['狙击手', '矮人火枪手', '火枪', '传说哥'],
    36:  ['瘟疫法师', '死灵法', 'NEC'],
    37:  ['术士'],
    38:  ['兽王'],
    39:  ['痛苦女王', '女王', 'QOP'],
    40:  ['剧毒术士', '剧毒'],
    41:  ['虚空假面', '虚空', 'JB脸'],
    42:  ['冥魂大帝', '骷髅王'],
    43:  ['死亡先知', 'DP'],
    44:  ['幻影刺客', '幻刺', 'PA'],
    45:  ['帕格纳', '骨法', '湮灭法师'],
    46:  ['圣堂刺客', '圣堂', 'TA'],
    47:  ['冥界亚龙', '毒龙', 'Viper'],
    48:  ['露娜', '月骑', 'Luna'],
    49:  ['龙骑士', '龙骑'],
    50:  ['戴泽', '暗影牧师', '暗牧'],
    51:  ['发条技师', '发条'],
    52:  ['拉席克', '老鹿'],
    53:  ['先知'],
    54:  ['噬魂鬼', '小狗'],
    55:  ['黑暗贤者', '黑贤'],
    56:  ['克林克兹', '小骷髅'],
    57:  ['全能骑士', '全能'],
    58:  ['魅惑魔女', '小鹿'],
    59:  ['哈斯卡', '神灵', '神灵武士'],
    60:  ['暗夜魔王', '夜魔'],
    61:  ['育母蜘蛛', '蜘蛛'],
    62:  ['赏金猎人', '赏金'],
    63:  ['编织者', '蚂蚁'],
    64:  ['杰奇洛', '双头龙'],
    65:  ['蝙蝠骑士', '蝙蝠'],
    66:  ['陈', '老陈'],
    67:  ['幽鬼', 'SPE', 'UG'],
    68:  ['远古冰魄', '冰魂'],
    69:  ['末日使者', '末日', 'Doom'],
    70:  ['熊战士', '拍拍', '拍拍熊'],
    71:  ['裂魂人', '白牛'],
    72:  ['矮人直升机', '飞机'],
    73:  ['炼金术士', '炼金'],
    74:  ['祈求者', '卡尔'],
    75:  ['沉默术士', '沉默'],
    76:  ['殁境神蚀者', '黑鸟'],
    77:  ['狼人'],
    78:  ['酒仙', '熊猫', '熊猫酒仙'],
    79:  ['暗影恶魔', '毒狗'],
    80:  ['德鲁伊', '熊德'],
    81:  ['混沌骑士', '混沌', 'CK'],
    82:  ['米波'],
    83:  ['树精卫士', '大树', '树精'],
    84:  ['食人魔魔法师', '蓝胖'],
    85:  ['不朽尸王', '尸王'],
    86:  ['拉比克'],
    87:  ['干扰者', '萨尔'],
    88:  ['司夜刺客', '小强'],
    89:  ['娜迦海妖', '小娜迦'],
    90:  ['光之守卫', '光法'],
    91:  ['艾欧', '小精灵'],
    92:  ['维萨吉', '死灵龙', '死灵飞龙'],
    93:  ['斯拉克', '小鱼', '小鱼人'],
    94:  ['美杜莎', '一姐', '美杜莎'],
    95:  ['巨魔战将', '巨魔', '巨馍蘸酱'],
    96:  ['半人马战行者', '人马', '半人马'],
    97:  ['马格纳斯', '猛犸'],
    98:  ['伐木机'],
    99:  ['钢背兽', '钢背'],
    100: ['巨牙海民', '海民'],
    101: ['天怒法师', '天怒'],
    102: ['亚巴顿'],
    103: ['上古巨神', '大牛'],
    104: ['军团指挥官', '军团'],
    105: ['工程师', '炸弹', '炸弹人'],
    106: ['灰烬之灵', '火猫'],
    107: ['大地之灵', '土猫'],
    108: ['孽主', '大屁股'],
    109: ['恐怖利刃', 'TB'],
    110: ['凤凰'],
    111: ['神谕者', '神谕'],
    112: ['寒冬飞龙', '冰龙'],
    113: ['天穹守望者', '电狗'],
    114: ['齐天大圣', '大圣'],
    119: ['邪影芳灵', '小仙女'],
    120: ['石鳞剑士', '滚滚'],
    121: ['天涯墨客', '墨客'],
    123: ['森海飞霞', '松鼠', '小松鼠', '小松许'],
    126: ['虚无之灵', '紫猫'],
    128: ['电炎绝手', '老奶奶'],
    129: ['玛尔斯'],
    135: ['破晓辰星'],
}

ITEMS = {
    1:    "blink",
    2:    "blades_of_attack",
    3:    "broadsword",
    4:    "chainmail",
    5:    "claymore",
    6:    "helm_of_iron_will",
    7:    "javelin",
    8:    "mithril_hammer",
    9:    "platemail",
    10:   "quarterstaff",
    11:   "quelling_blade",
    12:   "ring_of_protection",
    13:   "gauntlets",
    14:   "slippers",
    15:   "mantle",
    16:   "branches",
    17:   "belt_of_strength",
    18:   "boots_of_elves",
    19:   "robe",
    20:   "circlet",
    21:   "ogre_axe",
    22:   "blade_of_alacrity",
    23:   "staff_of_wizardry",
    24:   "ultimate_orb",
    25:   "gloves",
    26:   "lifesteal",
    27:   "ring_of_regen",
    28:   "sobi_mask",
    29:   "boots",
    30:   "gem",
    31:   "cloak",
    32:   "talisman_of_evasion",
    33:   "cheese",
    34:   "magic_stick",
    35:   "recipe_magic_wand",
    36:   "magic_wand",
    37:   "ghost",
    38:   "clarity",
    39:   "flask",
    40:   "dust",
    41:   "bottle",
    42:   "ward_observer",
    43:   "ward_sentry",
    44:   "tango",
    45:   "courier",
    46:   "tpscroll",
    47:   "recipe_travel_boots",
    48:   "travel_boots",
    49:   "recipe_phase_boots",
    50:   "phase_boots",
    51:   "demon_edge",
    52:   "eagle",
    53:   "reaver",
    54:   "relic",
    55:   "hyperstone",
    56:   "ring_of_health",
    57:   "void_stone",
    58:   "mystic_staff",
    59:   "energy_booster",
    60:   "point_booster",
    61:   "vitality_booster",
    62:   "recipe_power_treads",
    63:   "power_treads",
    64:   "recipe_hand_of_midas",
    65:   "hand_of_midas",
    66:   "recipe_oblivion_staff",
    67:   "oblivion_staff",
    68:   "recipe_pers",
    69:   "pers",
    70:   "recipe_poor_mans_shield",
    71:   "poor_mans_shield",
    72:   "recipe_bracer",
    73:   "bracer",
    74:   "recipe_wraith_band",
    75:   "wraith_band",
    76:   "recipe_null_talisman",
    77:   "null_talisman",
    78:   "recipe_mekansm",
    79:   "mekansm",
    80:   "recipe_vladmir",
    81:   "vladmir",
    85:   "recipe_buckler",
    86:   "buckler",
    87:   "recipe_ring_of_basilius",
    88:   "ring_of_basilius",
    89:   "recipe_pipe",
    90:   "pipe",
    91:   "recipe_urn_of_shadows",
    92:   "urn_of_shadows",
    93:   "recipe_headdress",
    94:   "headdress",
    95:   "recipe_sheepstick",
    96:   "sheepstick",
    97:   "recipe_orchid",
    98:   "orchid",
    99:   "recipe_cyclone",
    100:  "cyclone",
    101:  "recipe_force_staff",
    102:  "force_staff",
    103:  "recipe_dagon",
    104:  "dagon",
    105:  "recipe_necronomicon",
    106:  "necronomicon",
    107:  "recipe_ultimate_scepter",
    108:  "ultimate_scepter",
    109:  "recipe_refresher",
    110:  "refresher",
    111:  "recipe_assault",
    112:  "assault",
    113:  "recipe_heart",
    114:  "heart",
    115:  "recipe_black_king_bar",
    116:  "black_king_bar",
    117:  "aegis",
    118:  "recipe_shivas_guard",
    119:  "shivas_guard",
    120:  "recipe_bloodstone",
    121:  "bloodstone",
    122:  "recipe_sphere",
    123:  "sphere",
    124:  "recipe_vanguard",
    125:  "vanguard",
    126:  "recipe_blade_mail",
    127:  "blade_mail",
    128:  "recipe_soul_booster",
    129:  "soul_booster",
    130:  "recipe_hood_of_defiance",
    131:  "hood_of_defiance",
    132:  "recipe_rapier",
    133:  "rapier",
    134:  "recipe_monkey_king_bar",
    135:  "monkey_king_bar",
    136:  "recipe_radiance",
    137:  "radiance",
    138:  "recipe_butterfly",
    139:  "butterfly",
    140:  "recipe_greater_crit",
    141:  "greater_crit",
    142:  "recipe_basher",
    143:  "basher",
    144:  "recipe_bfury",
    145:  "bfury",
    146:  "recipe_manta",
    147:  "manta",
    148:  "recipe_lesser_crit",
    149:  "lesser_crit",
    150:  "recipe_armlet",
    151:  "armlet",
    152:  "invis_sword",
    153:  "recipe_sange_and_yasha",
    154:  "sange_and_yasha",
    155:  "recipe_satanic",
    156:  "satanic",
    157:  "recipe_mjollnir",
    158:  "mjollnir",
    159:  "recipe_skadi",
    160:  "skadi",
    161:  "recipe_sange",
    162:  "sange",
    163:  "recipe_helm_of_the_dominator",
    164:  "helm_of_the_dominator",
    165:  "recipe_maelstrom",
    166:  "maelstrom",
    167:  "recipe_desolator",
    168:  "desolator",
    169:  "recipe_yasha",
    170:  "yasha",
    171:  "recipe_mask_of_madness",
    172:  "mask_of_madness",
    173:  "recipe_diffusal_blade",
    174:  "diffusal_blade",
    175:  "recipe_ethereal_blade",
    176:  "ethereal_blade",
    177:  "recipe_soul_ring",
    178:  "soul_ring",
    179:  "recipe_arcane_boots",
    180:  "arcane_boots",
    181:  "orb_of_venom",
    182:  "stout_shield",
    183:  "recipe_invis_sword",
    184:  "recipe_ancient_janggo",
    185:  "ancient_janggo",
    186:  "recipe_medallion_of_courage",
    187:  "medallion_of_courage",
    188:  "smoke_of_deceit",
    189:  "recipe_veil_of_discord",
    190:  "veil_of_discord",
    191:  "recipe_necronomicon_2",
    192:  "recipe_necronomicon_3",
    193:  "necronomicon_2",
    194:  "necronomicon_3",
    196:  "diffusal_blade_2",
    197:  "recipe_dagon_2",
    198:  "recipe_dagon_3",
    199:  "recipe_dagon_4",
    200:  "recipe_dagon_5",
    201:  "dagon_2",
    202:  "dagon_3",
    203:  "dagon_4",
    204:  "dagon_5",
    205:  "recipe_rod_of_atos",
    206:  "rod_of_atos",
    207:  "recipe_abyssal_blade",
    208:  "abyssal_blade",
    209:  "recipe_heavens_halberd",
    210:  "heavens_halberd",
    211:  "recipe_ring_of_aquila",
    212:  "ring_of_aquila",
    213:  "recipe_tranquil_boots",
    214:  "tranquil_boots",
    215:  "shadow_amulet",
    216:  "enchanted_mango",
    217:  "recipe_ward_dispenser",
    218:  "ward_dispenser",
    219:  "recipe_travel_boots_2",
    220:  "travel_boots_2",
    221:  "recipe_lotus_orb",
    222:  "recipe_meteor_hammer",
    223:  "meteor_hammer",
    224:  "recipe_nullifier",
    225:  "nullifier",
    226:  "lotus_orb",
    227:  "recipe_solar_crest",
    228:  "recipe_octarine_core",
    229:  "solar_crest",
    230:  "recipe_guardian_greaves",
    231:  "guardian_greaves",
    232:  "aether_lens",
    233:  "recipe_aether_lens",
    234:  "recipe_dragon_lance",
    235:  "octarine_core",
    236:  "dragon_lance",
    237:  "faerie_fire",
    238:  "recipe_iron_talon",
    239:  "iron_talon",
    240:  "blight_stone",
    241:  "tango_single",
    242:  "crimson_guard",
    243:  "recipe_crimson_guard",
    244:  "wind_lace",
    245:  "recipe_bloodthorn",
    246:  "recipe_moon_shard",
    247:  "moon_shard",
    248:  "recipe_silver_edge",
    249:  "silver_edge",
    250:  "bloodthorn",
    251:  "recipe_echo_sabre",
    252:  "echo_sabre",
    253:  "recipe_glimmer_cape",
    254:  "glimmer_cape",
    255:  "recipe_aeon_disk",
    256:  "aeon_disk",
    257:  "tome_of_knowledge",
    258:  "recipe_kaya",
    259:  "kaya",
    260:  "refresher_shard",
    261:  "crown",
    262:  "recipe_hurricane_pike",
    263:  "hurricane_pike",
    265:  "infused_raindrop",
    266:  "recipe_spirit_vessel",
    267:  "spirit_vessel",
    268:  "recipe_holy_locket",
    269:  "holy_locket",
    270:  "recipe_ultimate_scepter_2",
    271:  "ultimate_scepter_2",
    272:  "recipe_kaya_and_sange",
    273:  "kaya_and_sange",
    274:  "recipe_yasha_and_kaya",
    275:  "recipe_trident",
    276:  "combo_breaker",
    277:  "yasha_and_kaya",
    279:  "ring_of_tarrasque",
    286:  "flying_courier",
    287:  "keen_optic",
    288:  "grove_bow",
    289:  "quickening_charm",
    290:  "philosophers_stone",
    291:  "force_boots",
    292:  "desolator_2",
    293:  "phoenix_ash",
    294:  "seer_stone",
    295:  "greater_mango",
    297:  "vampire_fangs",
    298:  "craggy_coat",
    299:  "greater_faerie_fire",
    300:  "timeless_relic",
    301:  "mirror_shield",
    302:  "elixer",
    303:  "recipe_ironwood_tree",
    304:  "ironwood_tree",
    305:  "royal_jelly",
    306:  "pupils_gift",
    307:  "tome_of_aghanim",
    308:  "repair_kit",
    309:  "mind_breaker",
    310:  "third_eye",
    311:  "spell_prism",
    312:  "horizon",
    313:  "fusion_rune",
    317:  "recipe_fallen_sky",
    325:  "princes_knife",
    326:  "spider_legs",
    327:  "helm_of_the_undying",
    328:  "mango_tree",
    329:  "recipe_vambrace",
    330:  "witless_shako",
    331:  "vambrace",
    334:  "imp_claw",
    335:  "flicker",
    336:  "spy_gadget",
    349:  "arcane_ring",
    354:  "ocean_heart",
    355:  "broom_handle",
    356:  "trusty_shovel",
    357:  "nether_shawl",
    358:  "dragon_scale",
    359:  "essence_ring",
    360:  "clumsy_net",
    361:  "enchanted_quiver",
    362:  "ninja_gear",
    363:  "illusionsts_cape",
    364:  "havoc_hammer",
    365:  "panic_button",
    366:  "apex",
    367:  "ballista",
    368:  "woodland_striders",
    369:  "trident",
    370:  "demonicon",
    371:  "fallen_sky",
    372:  "pirate_hat",
    373:  "dimensional_doorway",
    374:  "ex_machina",
    375:  "faded_broach",
    376:  "paladin_sword",
    377:  "minotaur_horn",
    378:  "orb_of_destruction",
    379:  "the_leveller",
    381:  "titan_sliver",
    473:  "voodoo_mask",
    485:  "blitz_knuckles",
    533:  "recipe_witch_blade",
    534:  "witch_blade",
    565:  "chipped_vest",
    566:  "wizard_glass",
    569:  "orb_of_corrosion",
    570:  "gloves_of_travel",
    571:  "trickster_cloak",
    573:  "elven_tunic",
    574:  "cloak_of_flames",
    575:  "venom_gland",
    576:  "gladiator_helm",
    577:  "possessed_mask",
    578:  "ancient_perseverance",
    582:  "oakheart",
    585:  "stormcrafter",
    588:  "overflowing_elixir",
    589:  "mysterious_hat",
    593:  "fluffy_hat",
    596:  "falcon_blade",
    597:  "recipe_mage_slayer",
    598:  "mage_slayer",
    599:  "recipe_falcon_blade",
    600:  "overwhelming_blink",
    603:  "swift_blink",
    604:  "arcane_blink",
    606:  "recipe_arcane_blink",
    607:  "recipe_swift_blink",
    608:  "recipe_overwhelming_blink",
    609:  "aghanims_shard",
    610:  "wind_waker",
    612:  "recipe_wind_waker",
    633:  "recipe_helm_of_the_overlord",
    635:  "helm_of_the_overlord",
    637:  "star_mace",
    638:  "penta_edged_sword",
    640:  "recipe_orb_of_corrosion",
    653:  "recipe_grandmasters_glaive",
    655:  "grandmasters_glaive",
    674:  "warhammer",
    675:  "psychic_headband",
    676:  "ceremonial_robe",
    677:  "book_of_shadows",
    678:  "giants_ring",
    679:  "vengeances_shadow",
    680:  "bullwhip",
    686:  "quicksilver_amulet",
    691:  "recipe_eternal_shroud",
    692:  "eternal_shroud",
    725:  "aghanims_shard_roshan",
    727:  "ultimate_scepter_roshan",
    731:  "satchel",
    1021: "river_painter",
    1022: "river_painter2",
    1023: "river_painter3",
    1024: "river_painter4",
    1025: "river_painter5",
    1026: "river_painter6",
    1027: "river_painter7",
    1028: "mutation_tombstone",
    1029: "super_blink",
    1030: "pocket_tower",
    1032: "pocket_roshan",
    1466: "gungir",
    1565: "recipe_gungir"
}

ITEM_SLOTS = ['item_0', 'item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'item_neutral']

SLOT = ['Radiant', 'Dire']
SLOT_CHINESE = ['天辉', '夜魇']

PLAYER_RANK = {
    0: '未知',
    1: '先锋',
    2: '卫士',
    3: '中军',
    4: '统帅',
    5: '传奇',
    6: '万古流芳',
    7: '超凡入圣',
    8: '冠绝一世',
}

SKILL_LEVEL = {1: 'Normal', 2: 'High', 3: 'Very High'}