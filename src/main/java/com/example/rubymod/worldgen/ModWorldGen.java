package com.example.rubymod.worldgen;

import com.example.rubymod.RubyMod;
import net.fabricmc.fabric.api.biome.v1.BiomeModifications;
import net.fabricmc.fabric.api.biome.v1.BiomeSelectors;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceKey;
import net.minecraft.world.level.levelgen.GenerationStep;
import net.minecraft.world.level.levelgen.placement.PlacedFeature;

/**
 * The ore itself is defined in data/ruby_mod/worldgen/{configured,placed}_feature/ruby_ore.json.
 * This class only injects the placed feature into every Overworld biome.
 */
public final class ModWorldGen {
    public static final ResourceKey<PlacedFeature> RUBY_ORE_PLACED =
            ResourceKey.create(Registries.PLACED_FEATURE, RubyMod.id("ruby_ore"));

    public static void init() {
        BiomeModifications.addFeature(
                BiomeSelectors.foundInOverworld(),
                GenerationStep.Decoration.UNDERGROUND_ORES,
                RUBY_ORE_PLACED);
    }

    private ModWorldGen() {}
}
