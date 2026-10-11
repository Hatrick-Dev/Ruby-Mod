package com.example.rubymod.registry;

import com.example.rubymod.RubyMod;
import com.example.rubymod.block.RubyBlockProperties;
import java.util.function.Function;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceKey;
import net.minecraft.util.valueproviders.UniformInt;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.DropExperienceBlock;
import net.minecraft.world.level.block.SlabBlock;
import net.minecraft.world.level.block.StairBlock;
import net.minecraft.world.level.block.WallBlock;
import net.minecraft.world.level.block.state.BlockBehaviour;

public final class ModBlocks {
    public static final Block RUBY_BLOCK = register("ruby_block", Block::new, RubyBlockProperties.storage());

    public static final Block RUBY_ORE = register("ruby_ore",
            p -> new DropExperienceBlock(UniformInt.of(3, 7), p), RubyBlockProperties.stoneOre());
    public static final Block DEEPSLATE_RUBY_ORE = register("deepslate_ruby_ore",
            p -> new DropExperienceBlock(UniformInt.of(3, 7), p), RubyBlockProperties.deepslateOre());

    public static final Block CHISELED_RUBY_BLOCK = register("chiseled_ruby_block", Block::new,
            BlockBehaviour.Properties.ofFullCopy(RUBY_BLOCK));
    public static final Block RUBY_STAIRS = register("ruby_stairs",
            p -> new StairBlock(RUBY_BLOCK.defaultBlockState(), p), BlockBehaviour.Properties.ofFullCopy(RUBY_BLOCK));
    public static final Block RUBY_SLAB = register("ruby_slab", SlabBlock::new,
            BlockBehaviour.Properties.ofFullCopy(RUBY_BLOCK));
    public static final Block RUBY_WALL = register("ruby_wall", WallBlock::new,
            BlockBehaviour.Properties.ofFullCopy(RUBY_BLOCK));

    /** Registers the block AND a matching fire-resistant BlockItem. */
    private static <T extends Block> T register(String name, Function<BlockBehaviour.Properties, T> factory,
                                                BlockBehaviour.Properties props) {
        ResourceKey<Block> blockKey = ResourceKey.create(Registries.BLOCK, RubyMod.id(name));
        T block = factory.apply(props.setId(blockKey));
        Registry.register(BuiltInRegistries.BLOCK, blockKey, block);

        ResourceKey<Item> itemKey = ResourceKey.create(Registries.ITEM, RubyMod.id(name));
        Registry.register(BuiltInRegistries.ITEM, itemKey,
                new BlockItem(block, new Item.Properties().setId(itemKey).useBlockDescriptionPrefix().fireResistant()));
        return block;
    }

    /** Touching this class from the mod initializer triggers the static registrations above. */
    public static void init() {}

    private ModBlocks() {}
}
