package com.example.rubymod;

import com.example.rubymod.registry.ModBlocks;
import com.example.rubymod.registry.ModCreativeTabs;
import com.example.rubymod.registry.ModItems;
import com.example.rubymod.worldgen.ModWorldGen;
import net.fabricmc.api.ModInitializer;
import net.minecraft.resources.Identifier;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class RubyMod implements ModInitializer {
    public static final String MOD_ID = "ruby_mod";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

    public static Identifier id(String path) {
        return Identifier.fromNamespaceAndPath(MOD_ID, path);
    }

    @Override
    public void onInitialize() {
        // Order matters: blocks (and their BlockItems) -> items -> creative tab -> world generation.
        ModBlocks.init();
        ModItems.init();
        ModCreativeTabs.init();
        ModWorldGen.init();
        LOGGER.info("Ruby Mod loaded - Tier 6 gear online.");
    }
}
