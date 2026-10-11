package com.example.rubymod.registry;

import com.example.rubymod.RubyMod;
import net.minecraft.core.registries.Registries;
import net.minecraft.tags.TagKey;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;

public final class ModTags {
    /** Blocks that Ruby tools can NOT mine. Data file is empty, so ruby mines everything netherite can. */
    public static final TagKey<Block> INCORRECT_FOR_RUBY_TOOL =
            TagKey.create(Registries.BLOCK, RubyMod.id("incorrect_for_ruby_tool"));

    /** Items accepted as repair material for ruby tools and armor (anvil). */
    public static final TagKey<Item> REPAIRS_RUBY_GEAR =
            TagKey.create(Registries.ITEM, RubyMod.id("repairs_ruby_gear"));

    private ModTags() {}
}
