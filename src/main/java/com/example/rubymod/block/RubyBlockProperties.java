package com.example.rubymod.block;

import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.MapColor;

/** Shared block property presets so ModBlocks stays readable. */
public final class RubyBlockProperties {
    /** Netherite-block-class hardness and blast resistance. */
    public static BlockBehaviour.Properties storage() {
        return BlockBehaviour.Properties.of()
                .mapColor(MapColor.COLOR_RED)
                .requiresCorrectToolForDrops()
                .strength(50.0F, 1200.0F)
                .sound(SoundType.METAL);
    }

    public static BlockBehaviour.Properties stoneOre() {
        return BlockBehaviour.Properties.of()
                .mapColor(MapColor.STONE)
                .requiresCorrectToolForDrops()
                .strength(3.0F, 3.0F);
    }

    public static BlockBehaviour.Properties deepslateOre() {
        return BlockBehaviour.Properties.of()
                .mapColor(MapColor.DEEPSLATE)
                .requiresCorrectToolForDrops()
                .strength(4.5F, 3.0F)
                .sound(SoundType.DEEPSLATE);
    }

    private RubyBlockProperties() {}
}
