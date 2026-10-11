package com.example.rubymod.item;

import com.example.rubymod.registry.ModTags;
import net.minecraft.world.item.ToolMaterial;

public final class ModToolMaterials {
    /**
     * Ruby tool tier (strictly above Netherite).
     *                      Netherite   Ruby
     *  durability          2031        2500
     *  speed               9.0         10.0
     *  attack dmg bonus    4.0         4.5
     *  enchantability      15          18
     */
    public static final ToolMaterial RUBY = new ToolMaterial(
            ModTags.INCORRECT_FOR_RUBY_TOOL,
            2500,
            10.0F,
            4.5F,
            18,
            ModTags.REPAIRS_RUBY_GEAR
    );

    private ModToolMaterials() {}
}
