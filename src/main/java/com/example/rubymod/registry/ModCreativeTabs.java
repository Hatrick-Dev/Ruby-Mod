package com.example.rubymod.registry;

import com.example.rubymod.RubyMod;
import net.fabricmc.fabric.api.creativetab.v1.FabricCreativeModeTab;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceKey;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.ItemStack;

public final class ModCreativeTabs {
    public static final ResourceKey<CreativeModeTab> RUBY_TAB_KEY =
            ResourceKey.create(Registries.CREATIVE_MODE_TAB, RubyMod.id("ruby_tab"));

    public static final CreativeModeTab RUBY_TAB = FabricCreativeModeTab.builder()
            .title(Component.translatable("itemGroup.ruby_mod.ruby_tab"))
            .icon(() -> new ItemStack(ModBlocks.RUBY_BLOCK))
            .displayItems((params, output) -> {
                // Materials
                output.accept(ModItems.RAW_RUBY);
                output.accept(ModItems.RUBY);
                // Blocks & building set
                output.accept(ModBlocks.RUBY_ORE);
                output.accept(ModBlocks.DEEPSLATE_RUBY_ORE);
                output.accept(ModBlocks.RUBY_BLOCK);
                output.accept(ModBlocks.CHISELED_RUBY_BLOCK);
                output.accept(ModBlocks.RUBY_STAIRS);
                output.accept(ModBlocks.RUBY_SLAB);
                output.accept(ModBlocks.RUBY_WALL);
                // Tools
                output.accept(ModItems.RUBY_SWORD);
                output.accept(ModItems.RUBY_PICKAXE);
                output.accept(ModItems.RUBY_AXE);
                output.accept(ModItems.RUBY_SHOVEL);
                output.accept(ModItems.RUBY_HOE);
                // Armor
                output.accept(ModItems.RUBY_HELMET);
                output.accept(ModItems.RUBY_CHESTPLATE);
                output.accept(ModItems.RUBY_LEGGINGS);
                output.accept(ModItems.RUBY_BOOTS);
            })
            .build();

    public static void init() {
        Registry.register(BuiltInRegistries.CREATIVE_MODE_TAB, RUBY_TAB_KEY, RUBY_TAB);
    }

    private ModCreativeTabs() {}
}
