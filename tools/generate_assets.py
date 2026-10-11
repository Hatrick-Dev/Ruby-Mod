#!/usr/bin/env python3
"""Generates every JSON resource (blockstates, models, item definitions, recipes,
loot tables, tags, worldgen, lang) and placeholder PNG textures for ruby_mod.

Run from the project root:  python3 tools/generate_assets.py
Requires: Pillow (pip install pillow)
Re-running overwrites generated files, so hand-edited JSON should be moved elsewhere.
"""
import json
import os
import random

from PIL import Image

MOD = "ruby_mod"
RES = "src/main/resources"
ASSETS = f"{RES}/assets/{MOD}"
DATA = f"{RES}/data/{MOD}"
MC_DATA = f"{RES}/data/minecraft"


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)
        f.write("\n")


# --------------------------------------------------------------------------- #
# Content definition
# --------------------------------------------------------------------------- #
CUBES = ["ruby_block", "chiseled_ruby_block", "ruby_ore", "deepslate_ruby_ore"]
FLAT_ITEMS = ["ruby", "raw_ruby"]
TOOLS = ["ruby_sword", "ruby_pickaxe", "ruby_axe", "ruby_shovel", "ruby_hoe"]
ARMOR = {
    "ruby_helmet": "head_armor",
    "ruby_chestplate": "chest_armor",
    "ruby_leggings": "leg_armor",
    "ruby_boots": "foot_armor",
}

LANG = {
    f"itemGroup.{MOD}.ruby_tab": "Ruby Mod",
    f"item.{MOD}.ruby": "Ruby",
    f"item.{MOD}.raw_ruby": "Raw Ruby",
    f"item.{MOD}.ruby_sword": "Ruby Sword",
    f"item.{MOD}.ruby_pickaxe": "Ruby Pickaxe",
    f"item.{MOD}.ruby_axe": "Ruby Axe",
    f"item.{MOD}.ruby_shovel": "Ruby Shovel",
    f"item.{MOD}.ruby_hoe": "Ruby Hoe",
    f"item.{MOD}.ruby_helmet": "Ruby Helmet",
    f"item.{MOD}.ruby_chestplate": "Ruby Chestplate",
    f"item.{MOD}.ruby_leggings": "Ruby Leggings",
    f"item.{MOD}.ruby_boots": "Ruby Boots",
    f"block.{MOD}.ruby_block": "Block of Ruby",
    f"block.{MOD}.chiseled_ruby_block": "Chiseled Ruby Block",
    f"block.{MOD}.ruby_ore": "Ruby Ore",
    f"block.{MOD}.deepslate_ruby_ore": "Deepslate Ruby Ore",
    f"block.{MOD}.ruby_stairs": "Ruby Stairs",
    f"block.{MOD}.ruby_slab": "Ruby Slab",
    f"block.{MOD}.ruby_wall": "Ruby Wall",
}


def i(name):
    return f"{MOD}:{name}"


# --------------------------------------------------------------------------- #
# Lang
# --------------------------------------------------------------------------- #
write_json(f"{ASSETS}/lang/en_us.json", LANG)

# --------------------------------------------------------------------------- #
# Item definitions + item models
# --------------------------------------------------------------------------- #
def item_definition(name, model):
    write_json(f"{ASSETS}/items/{name}.json", {"model": {"type": "minecraft:model", "model": model}})


for n in FLAT_ITEMS + list(ARMOR):
    write_json(f"{ASSETS}/models/item/{n}.json",
               {"parent": "minecraft:item/generated", "textures": {"layer0": i(f"item/{n}")}})
    item_definition(n, i(f"item/{n}"))

for n in TOOLS:
    write_json(f"{ASSETS}/models/item/{n}.json",
               {"parent": "minecraft:item/handheld", "textures": {"layer0": i(f"item/{n}")}})
    item_definition(n, i(f"item/{n}"))

# --------------------------------------------------------------------------- #
# Blocks: blockstates + models
# --------------------------------------------------------------------------- #
for n in CUBES:
    write_json(f"{ASSETS}/blockstates/{n}.json", {"variants": {"": {"model": i(f"block/{n}")}}})
    write_json(f"{ASSETS}/models/block/{n}.json",
               {"parent": "minecraft:block/cube_all", "textures": {"all": i(f"block/{n}")}})
    item_definition(n, i(f"block/{n}"))

# Slab
tex = {"bottom": i("block/ruby_block"), "top": i("block/ruby_block"), "side": i("block/ruby_block")}
write_json(f"{ASSETS}/models/block/ruby_slab.json", {"parent": "minecraft:block/slab", "textures": tex})
write_json(f"{ASSETS}/models/block/ruby_slab_top.json", {"parent": "minecraft:block/slab_top", "textures": tex})
write_json(f"{ASSETS}/blockstates/ruby_slab.json", {"variants": {
    "type=bottom": {"model": i("block/ruby_slab")},
    "type=double": {"model": i("block/ruby_block")},
    "type=top": {"model": i("block/ruby_slab_top")},
}})
item_definition("ruby_slab", i("block/ruby_slab"))

# Stairs
for suffix, parent in (("", "stairs"), ("_inner", "inner_stairs"), ("_outer", "outer_stairs")):
    write_json(f"{ASSETS}/models/block/ruby_stairs{suffix}.json",
               {"parent": f"minecraft:block/{parent}", "textures": tex})
STAIR_Y = {  # (half, facing) -> {shape: y}
    ("bottom", "east"): dict(straight=0, outer_right=0, outer_left=270, inner_right=0, inner_left=270),
    ("bottom", "west"): dict(straight=180, outer_right=180, outer_left=90, inner_right=180, inner_left=90),
    ("bottom", "south"): dict(straight=90, outer_right=90, outer_left=0, inner_right=90, inner_left=0),
    ("bottom", "north"): dict(straight=270, outer_right=270, outer_left=180, inner_right=270, inner_left=180),
    ("top", "east"): dict(straight=0, outer_right=90, outer_left=0, inner_right=90, inner_left=0),
    ("top", "west"): dict(straight=180, outer_right=270, outer_left=180, inner_right=270, inner_left=180),
    ("top", "south"): dict(straight=90, outer_right=180, outer_left=90, inner_right=180, inner_left=90),
    ("top", "north"): dict(straight=270, outer_right=0, outer_left=270, inner_right=0, inner_left=270),
}
variants = {}
for (half, facing), shapes in STAIR_Y.items():
    for shape, y in shapes.items():
        model = "ruby_stairs" if shape == "straight" else \
            "ruby_stairs_outer" if shape.startswith("outer") else "ruby_stairs_inner"
        v = {"model": i(f"block/{model}")}
        if half == "top":
            v["x"] = 180
        if y:
            v["y"] = y
        if half == "top" or y:
            v["uvlock"] = True
        variants[f"facing={facing},half={half},shape={shape}"] = v
write_json(f"{ASSETS}/blockstates/ruby_stairs.json", {"variants": variants})
item_definition("ruby_stairs", i("block/ruby_stairs"))

# Wall
wtex = {"wall": i("block/ruby_block")}
write_json(f"{ASSETS}/models/block/ruby_wall_post.json", {"parent": "minecraft:block/template_wall_post", "textures": wtex})
write_json(f"{ASSETS}/models/block/ruby_wall_side.json", {"parent": "minecraft:block/template_wall_side", "textures": wtex})
write_json(f"{ASSETS}/models/block/ruby_wall_side_tall.json", {"parent": "minecraft:block/template_wall_side_tall", "textures": wtex})
write_json(f"{ASSETS}/models/block/ruby_wall_inventory.json", {"parent": "minecraft:block/wall_inventory", "textures": wtex})
multipart = [{"when": {"up": "true"}, "apply": {"model": i("block/ruby_wall_post")}}]
for kind, model in (("low", "ruby_wall_side"), ("tall", "ruby_wall_side_tall")):
    for side, y in (("north", 0), ("east", 90), ("south", 180), ("west", 270)):
        apply = {"model": i(f"block/{model}"), "uvlock": True}
        if y:
            apply["y"] = y
        multipart.append({"when": {side: kind}, "apply": apply})
write_json(f"{ASSETS}/blockstates/ruby_wall.json", {"multipart": multipart})
item_definition("ruby_wall", i("block/ruby_wall_inventory"))

# Armor equipment asset (worn model)
write_json(f"{ASSETS}/equipment/ruby.json", {"layers": {
    "humanoid": [{"texture": i("ruby")}],
    "humanoid_leggings": [{"texture": i("ruby")}],
}})

# --------------------------------------------------------------------------- #
# Loot tables
# --------------------------------------------------------------------------- #
def simple_loot(name, entry_extra=None):
    entry = {"type": "minecraft:item", "name": i(name)}
    if entry_extra:
        entry.update(entry_extra)
    write_json(f"{DATA}/loot_table/blocks/{name}.json", {
        "type": "minecraft:block",
        "pools": [{
            "bonus_rolls": 0.0,
            "conditions": [{"condition": "minecraft:survives_explosion"}],
            "entries": [entry],
            "rolls": 1.0,
        }],
        "random_sequence": i(f"blocks/{name}"),
    })


for n in ("ruby_block", "chiseled_ruby_block", "ruby_stairs", "ruby_wall"):
    simple_loot(n)

simple_loot("ruby_slab", {"functions": [
    {"add": False, "conditions": [{"block": i("ruby_slab"), "condition": "minecraft:block_state_property",
                                    "properties": {"type": "double"}}],
     "count": 2.0, "function": "minecraft:set_count"},
    {"function": "minecraft:explosion_decay"},
]})


def ore_loot(name):
    write_json(f"{DATA}/loot_table/blocks/{name}.json", {
        "type": "minecraft:block",
        "pools": [{
            "bonus_rolls": 0.0,
            "entries": [{
                "type": "minecraft:alternatives",
                "children": [
                    {"type": "minecraft:item", "name": i(name), "conditions": [{
                        "condition": "minecraft:match_tool",
                        "predicate": {"predicates": {"minecraft:enchantments": [
                            {"enchantments": "minecraft:silk_touch", "levels": {"min": 1}}]}}}]},
                    {"type": "minecraft:item", "name": i("raw_ruby"), "functions": [
                        {"enchantment": "minecraft:fortune", "formula": "minecraft:ore_drops",
                         "function": "minecraft:apply_bonus"},
                        {"function": "minecraft:explosion_decay"}]},
                ],
            }],
            "rolls": 1.0,
        }],
        "random_sequence": i(f"blocks/{name}"),
    })


ore_loot("ruby_ore")
ore_loot("deepslate_ruby_ore")

# --------------------------------------------------------------------------- #
# Recipes
# --------------------------------------------------------------------------- #
def recipe(name, obj):
    write_json(f"{DATA}/recipe/{name}.json", obj)


R = i("ruby")
RB = i("ruby_block")


def shaped(name, pattern, key, result, count=1, category="equipment"):
    recipe(name, {"type": "minecraft:crafting_shaped", "category": category, "pattern": pattern,
                  "key": key, "result": {"id": i(result), "count": count}})


recipe("ruby_block_from_rubies", {"type": "minecraft:crafting_shaped", "category": "building",
                                  "pattern": ["RRR", "RRR", "RRR"], "key": {"R": R},
                                  "result": {"id": RB}})
recipe("ruby_from_ruby_block", {"type": "minecraft:crafting_shapeless", "category": "misc",
                                "ingredients": [RB], "result": {"id": R, "count": 9}})

shaped("ruby_stairs", ["R  ", "RR ", "RRR"], {"R": RB}, "ruby_stairs", 4, "building")
shaped("ruby_slab", ["RRR"], {"R": RB}, "ruby_slab", 6, "building")
shaped("ruby_wall", ["RRR", "RRR"], {"R": RB}, "ruby_wall", 6, "building")
shaped("chiseled_ruby_block", ["S", "S"], {"S": i("ruby_slab")}, "chiseled_ruby_block", 1, "building")

for result, count in (("ruby_stairs", 1), ("ruby_slab", 2), ("ruby_wall", 1), ("chiseled_ruby_block", 1)):
    recipe(f"{result}_from_ruby_block_stonecutting",
           {"type": "minecraft:stonecutting", "ingredient": RB, "result": {"id": i(result), "count": count}})

for kind, t, cook in (("smelting", "minecraft:smelting", 200), ("blasting", "minecraft:blasting", 100)):
    for src in ("raw_ruby", "ruby_ore", "deepslate_ruby_ore"):
        recipe(f"ruby_from_{kind}_{src}", {"type": t, "category": "misc", "ingredient": i(src),
                                           "result": {"id": R}, "experience": 1.5, "cookingtime": cook})

STICK = "minecraft:stick"
shaped("ruby_sword", ["R", "R", "S"], {"R": R, "S": STICK}, "ruby_sword")
shaped("ruby_pickaxe", ["RRR", " S ", " S "], {"R": R, "S": STICK}, "ruby_pickaxe")
shaped("ruby_axe", ["RR", "RS", " S"], {"R": R, "S": STICK}, "ruby_axe")
shaped("ruby_shovel", ["R", "S", "S"], {"R": R, "S": STICK}, "ruby_shovel")
shaped("ruby_hoe", ["RR", " S", " S"], {"R": R, "S": STICK}, "ruby_hoe")
shaped("ruby_helmet", ["RRR", "R R"], {"R": R}, "ruby_helmet")
shaped("ruby_chestplate", ["R R", "RRR", "RRR"], {"R": R}, "ruby_chestplate")
shaped("ruby_leggings", ["RRR", "R R", "R R"], {"R": R}, "ruby_leggings")
shaped("ruby_boots", ["R R", "R R"], {"R": R}, "ruby_boots")

# --------------------------------------------------------------------------- #
# Tags
# --------------------------------------------------------------------------- #
def tag(path, values):
    write_json(path, {"replace": False, "values": values})


ALL_BLOCKS = [i(n) for n in ("ruby_block", "chiseled_ruby_block", "ruby_ore", "deepslate_ruby_ore",
                            "ruby_stairs", "ruby_slab", "ruby_wall")]
tag(f"{MC_DATA}/tags/block/mineable/pickaxe.json", ALL_BLOCKS)
tag(f"{MC_DATA}/tags/block/needs_diamond_tool.json", ALL_BLOCKS)  # Netherite-tier requirement
tag(f"{MC_DATA}/tags/block/beacon_base_blocks.json", [RB])
tag(f"{MC_DATA}/tags/block/stairs.json", [i("ruby_stairs")])
tag(f"{MC_DATA}/tags/block/slabs.json", [i("ruby_slab")])
tag(f"{MC_DATA}/tags/block/walls.json", [i("ruby_wall")])
tag(f"{MC_DATA}/tags/item/stairs.json", [i("ruby_stairs")])
tag(f"{MC_DATA}/tags/item/slabs.json", [i("ruby_slab")])
tag(f"{MC_DATA}/tags/item/walls.json", [i("ruby_wall")])
tag(f"{MC_DATA}/tags/item/swords.json", [i("ruby_sword")])
tag(f"{MC_DATA}/tags/item/pickaxes.json", [i("ruby_pickaxe")])
tag(f"{MC_DATA}/tags/item/axes.json", [i("ruby_axe")])
tag(f"{MC_DATA}/tags/item/shovels.json", [i("ruby_shovel")])
tag(f"{MC_DATA}/tags/item/hoes.json", [i("ruby_hoe")])
for armor_name, armor_tag in ARMOR.items():
    tag(f"{MC_DATA}/tags/item/{armor_tag}.json", [i(armor_name)])
tag(f"{MC_DATA}/tags/item/trimmable_armor.json", [i(a) for a in ARMOR])
# Mod tags
tag(f"{DATA}/tags/item/repairs_ruby_gear.json", [R])
tag(f"{DATA}/tags/block/incorrect_for_ruby_tool.json", [])  # empty: ruby mines everything

# --------------------------------------------------------------------------- #
# World generation
# --------------------------------------------------------------------------- #
write_json(f"{DATA}/worldgen/configured_feature/ruby_ore.json", {
    "type": "minecraft:ore",
    "config": {
        "discard_chance_on_air_exposure": 0.5,
        "size": 5,
        "targets": [
            {"state": {"Name": i("ruby_ore")},
             "target": {"predicate_type": "minecraft:tag_match", "tag": "minecraft:stone_ore_replaceables"}},
            {"state": {"Name": i("deepslate_ruby_ore")},
             "target": {"predicate_type": "minecraft:tag_match", "tag": "minecraft:deepslate_ore_replaceables"}},
        ],
    },
})
write_json(f"{DATA}/worldgen/placed_feature/ruby_ore.json", {
    "feature": i("ruby_ore"),
    "placement": [
        {"type": "minecraft:count", "count": 3},
        {"type": "minecraft:in_square"},
        {"type": "minecraft:height_range", "height": {
            "type": "minecraft:trapezoid",
            "min_inclusive": {"absolute": -64},
            "max_inclusive": {"absolute": 16}}},
        {"type": "minecraft:biome"},
    ],
})

# --------------------------------------------------------------------------- #
# Textures (procedural placeholders - replace with real art any time)
# --------------------------------------------------------------------------- #
rng = random.Random(1337)
TEX = f"{ASSETS}/textures"
os.makedirs(f"{TEX}/block", exist_ok=True)
os.makedirs(f"{TEX}/item", exist_ok=True)
os.makedirs(f"{TEX}/entity/equipment/humanoid", exist_ok=True)
os.makedirs(f"{TEX}/entity/equipment/humanoid_leggings", exist_ok=True)

RUBY_SHADES = [(122, 8, 30), (155, 14, 40), (190, 24, 52), (222, 48, 72), (245, 100, 120)]
STONE = [(118, 118, 118), (126, 126, 126), (134, 134, 134), (110, 110, 110), (142, 142, 142)]
DEEP = [(60, 60, 66), (68, 68, 74), (76, 76, 82), (54, 54, 60), (82, 82, 88)]


def ruby_facets(size_w, size_h):
    img = Image.new("RGBA", (size_w, size_h))
    px = img.load()
    for y in range(size_h):
        for x in range(size_w):
            d = ((x * 3 + y * 5) // 4) % 5
            if (x // 4 + y // 4) % 2 == 0:
                d = min(4, d + 1)
            px[x, y] = RUBY_SHADES[d] + (255,)
    for y in range(size_h):  # darker outline per 16px tile
        for x in range(size_w):
            if x % 16 in (0, 15) or y % 16 in (0, 15):
                px[x, y] = RUBY_SHADES[0] + (255,)
    return img


def noise_stone(palette):
    img = Image.new("RGBA", (16, 16))
    px = img.load()
    for y in range(16):
        for x in range(16):
            px[x, y] = rng.choice(palette) + (255,)
    return img


def ore(palette):
    img = noise_stone(palette)
    px = img.load()
    for cx, cy in ((4, 4), (11, 5), (6, 11), (12, 12)):
        for dx, dy in ((0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (0, -1)):
            x, y = cx + dx, cy + dy
            if 0 <= x < 16 and 0 <= y < 16:
                px[x, y] = RUBY_SHADES[rng.choice((2, 3, 3, 4))] + (255,)
        px[cx, cy] = RUBY_SHADES[4] + (255,)
    return img


ruby_facets(16, 16).save(f"{TEX}/block/ruby_block.png")
chis = ruby_facets(16, 16)
cp = chis.load()
for k in range(3, 13):  # chiseled frame + cross
    for pos in ((k, 3), (k, 12), (3, k), (12, k)):
        cp[pos] = RUBY_SHADES[0] + (255,)
for k in range(5, 11):
    cp[k, 8] = RUBY_SHADES[4] + (255,)
    cp[8, k] = RUBY_SHADES[4] + (255,)
chis.save(f"{TEX}/block/chiseled_ruby_block.png")
ore(STONE).save(f"{TEX}/block/ruby_ore.png")
ore(DEEP).save(f"{TEX}/block/deepslate_ruby_ore.png")

# Item sprites ------------------------------------------------------------- #
OUTLINE = (58, 4, 14, 255)
HANDLE = [(88, 58, 28, 255), (120, 82, 40, 255)]
R_MAIN = [(s + (255,)) for s in RUBY_SHADES]


def sprite_from_map(rows, mapping):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    px = img.load()
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch in mapping:
                px[x, y] = mapping[ch]
    return add_outline(img)


def add_outline(img):
    out = img.copy()
    src, dst = img.load(), out.load()
    for y in range(16):
        for x in range(16):
            if src[x, y][3] == 0:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 16 and 0 <= ny < 16 and src[nx, ny][3] > 0:
                        dst[x, y] = OUTLINE
                        break
    return out


GEM_MAP = {"a": R_MAIN[0], "b": R_MAIN[1], "c": R_MAIN[2], "d": R_MAIN[3], "e": R_MAIN[4]}
sprite_from_map([
    "................",
    "................",
    "................",
    "....eeddddcc....",
    "...edddddccbb...",
    "..edddddcccbbb..",
    "..ddddccccbbba..",
    "...dcccccbbba...",
    "....ccccbbba....",
    ".....cccbba.....",
    "......ccba......",
    ".......ba.......",
    "................",
    "................",
    "................",
    "................",
], GEM_MAP).save(f"{TEX}/item/ruby.png")
sprite_from_map([
    "................",
    "................",
    "................",
    ".....ddcc.......",
    "....dddccbb.....",
    "...ddccccbbb....",
    "...dcccbbbbaa...",
    "....cccbbbba....",
    "...ddcccbbba....",
    "..dddcccbbaa....",
    "..ddccbbbaa.....",
    "...cccbbaa......",
    "....bbaa........",
    "................",
    "................",
    "................",
], GEM_MAP).save(f"{TEX}/item/raw_ruby.png")

H = {"h": HANDLE[0], "i": HANDLE[1]}
H.update(GEM_MAP)
sprite_from_map([
    "..............dc",
    ".............ddc",
    "............ddcb",
    "...........ddcb.",
    "..........ddcb..",
    ".........ddcb...",
    "..d.....ddcb....",
    "...d...ddcb.....",
    "....d.ddcb......",
    ".....ddcb.......",
    "....hhdb........",
    "...hi.hh........",
    "..hi............",
    ".hh.............",
    "................",
    "................",
], H).save(f"{TEX}/item/ruby_sword.png")
sprite_from_map([
    "................",
    "....dddddddd....",
    "..ddddccccbbbb..",
    ".dddc......bbbb.",
    ".ddc....hi...bb.",
    ".dc....hi.....b.",
    "......hi........",
    ".....hi.........",
    "....hi..........",
    "...hi...........",
    "..hi............",
    ".hi.............",
    ".h..............",
    "................",
    "................",
    "................",
], H).save(f"{TEX}/item/ruby_pickaxe.png")
sprite_from_map([
    "................",
    "......dddd......",
    ".....ddddcc.....",
    ".....dddcccb....",
    ".....ddcccbb....",
    ".....hdcbb......",
    "....hi.b........",
    "...hi...........",
    "..hi............",
    ".hi.............",
    ".h..............",
    "................",
    "................",
    "................",
    "................",
    "................",
], H).save(f"{TEX}/item/ruby_axe.png")
sprite_from_map([
    "..........dd....",
    ".........dddc...",
    ".........ddccb..",
    ".........dccbb..",
    "..........cbb...",
    ".........hi.....",
    "........hi......",
    ".......hi.......",
    "......hi........",
    ".....hi.........",
    "....hi..........",
    "...hi...........",
    "..hi............",
    ".hh.............",
    "................",
    "................",
], H).save(f"{TEX}/item/ruby_shovel.png")
sprite_from_map([
    "................",
    "....dddd........",
    "...ddcccc.......",
    "...dc..ccb......",
    "......hbbb......",
    ".....hi.........",
    "....hi..........",
    "...hi...........",
    "..hi............",
    ".hi.............",
    ".h..............",
    "................",
    "................",
    "................",
    "................",
    "................",
], H).save(f"{TEX}/item/ruby_hoe.png")

sprite_from_map([
    "................", "................", "....eddddddc....", "...edddddddcc...",
    "...ddddddddcc...", "...ddcccccccb...", "...ddc....cbb...", "...dcc....cbb...",
    "...dc......cb...", "................", "................", "................",
    "................", "................", "................", "................",
], GEM_MAP).save(f"{TEX}/item/ruby_helmet.png")
sprite_from_map([
    "................", "..dd........cc..", ".dddd.eddc.cccb.", ".ddddeddddcccbb.",
    ".dddddddddccbbb.", "..dddddddcccbb..", "...ddddddcccb...", "...dddddcccbb...",
    "...ddddccccbb...", "...dddcccccbb...", "...ddcccccbba...", "...dccccccbb....",
    "....cccccbba....", "................", "................", "................",
], GEM_MAP).save(f"{TEX}/item/ruby_chestplate.png")
sprite_from_map([
    "................", "...eddddddddc...", "...eddddddddcc..", "...dddcccccccc..",
    "...ddcc...cccb..", "...ddcc...cccb..", "...ddcc...cccb..", "...dcc....ccbb..",
    "...dcc....ccbb..", "...dcc....ccbb..", "...dc.....cbb...", "...bb.....bba...",
    "................", "................", "................", "................",
], GEM_MAP).save(f"{TEX}/item/ruby_leggings.png")
sprite_from_map([
    "................", "................", "................", "................",
    "................", "................", "...ddc....ccb...", "...ddc....ccb...",
    "..dddcc..ccbbb..", "..ddcccc.cccbb..", ".dddcccc.ccbbbb.", ".dccccbb.ccbbba.",
    ".bbbbbbb.bbbbbb.", "................", "................", "................",
], GEM_MAP).save(f"{TEX}/item/ruby_boots.png")

# Armor worn layers (64x32) - UV regions share one tiled ruby pattern
ruby_facets(64, 32).save(f"{TEX}/entity/equipment/humanoid/ruby.png")
legs = ruby_facets(64, 32)
lp = legs.load()
for x in range(64):  # darker belt line on the legging layer
    for y in (16, 17):
        lp[x, y] = RUBY_SHADES[0] + (255,)
legs.save(f"{TEX}/entity/equipment/humanoid_leggings/ruby.png")

# Mod icon
icon = Image.open(f"{TEX}/item/ruby.png").resize((128, 128), Image.NEAREST)
icon.save(f"{ASSETS}/icon.png")

print("ruby_mod: assets generated")
