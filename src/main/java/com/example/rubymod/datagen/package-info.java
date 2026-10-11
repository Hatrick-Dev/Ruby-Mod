/**
 * Data generation for ruby_mod.
 *
 * <p>The mod's JSON (blockstates, models, item definitions, recipes, loot tables, tags,
 * worldgen, lang) and placeholder textures are produced by {@code tools/generate_assets.py}
 * and committed under {@code src/main/resources}. That keeps the build independent of
 * Fabric's datagen API, which changes between Minecraft releases.
 *
 * <p>If you prefer in-Java datagen, add your providers to this package and register them via
 * a {@code DataGeneratorEntrypoint} (see https://docs.fabricmc.net/develop/data-generation/setup).
 */
package com.example.rubymod.datagen;
