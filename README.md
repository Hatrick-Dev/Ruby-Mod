# Ruby Mod (`ruby_mod`)

Tier 6 rubies for **Fabric / Minecraft 26.3**: tools, armor and a full building set that outclass Netherite.

## Requirements
- Minecraft 26.3, Fabric Loader >= 0.19.5, Fabric API 0.160.5+26.3
- **Java 25** (Minecraft 26.x requires it; Java 21 will not run or compile this version)

## Content
| Item | Stats |
|---|---|
| Tool material | 2500 durability, 10.0 speed, +4.5 damage, enchantability 18, repaired with Ruby |
| Sword / Axe | 9.0 dmg @ 1.6 speed / 11.0 dmg @ 1.0 speed |
| Armor (4/9/7/4 = 24) | toughness 4.0, knockback resistance 0.15 per piece, durability 462/672/630/546 |
| Perk | every ruby item is fire and lava proof (does not burn, floats on lava) |

Blocks: Ruby Block (beacon base, 50 hardness / 1200 blast resistance), Chiseled Ruby Block, Stairs, Slab, Wall, Ruby Ore, Deepslate Ruby Ore.
Everything lives in the **Ruby Mod** creative tab.

## Build
```bash
gradle wrapper --gradle-version latest   # once, to create ./gradlew
./gradlew build                          # build/libs/ruby_mod-<version>.jar (+ -sources.jar)
./gradlew releaseAssets                  # build/release/: jar, sources, zip, SHA256SUMS.txt, build-info.json
./gradlew runClient
```

## Release
Push a tag such as `v1.0.0` (or publish a GitHub release). The workflow in `.github/workflows/release.yml`
builds everything and attaches the five release assets.

## Regenerating resources
`python3 tools/generate_assets.py` rewrites all JSON and the placeholder textures (needs Pillow).
