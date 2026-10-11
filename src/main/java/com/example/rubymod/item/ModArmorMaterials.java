package com.example.rubymod.item;

import com.example.rubymod.RubyMod;
import com.example.rubymod.registry.ModTags;
import java.util.Map;
import net.minecraft.resources.ResourceKey;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.world.item.equipment.ArmorMaterial;
import net.minecraft.world.item.equipment.ArmorType;
import net.minecraft.world.item.equipment.EquipmentAsset;
import net.minecraft.world.item.equipment.EquipmentAssets;

public final class ModArmorMaterials {
    /** Points at assets/ruby_mod/equipment/ruby.json (the worn-armor model). */
    public static final ResourceKey<EquipmentAsset> RUBY_ASSET =
            ResourceKey.create(EquipmentAssets.ROOT_ID, RubyMod.id("ruby"));

    /**
     * Durability multiplier 42 -> helmet 462, chestplate 672, leggings 630, boots 546
     * (vanilla per-slot factors 11/16/15/13). Defense 4+9+7+4 = 24 (Netherite 20).
     */
    public static final ArmorMaterial RUBY = new ArmorMaterial(
            42,
            Map.of(
                    ArmorType.HELMET, 4,
                    ArmorType.CHESTPLATE, 9,
                    ArmorType.LEGGINGS, 7,
                    ArmorType.BOOTS, 4
            ),
            18,
            SoundEvents.ARMOR_EQUIP_NETHERITE,
            4.0F,
            0.15F,
            ModTags.REPAIRS_RUBY_GEAR,
            RUBY_ASSET
    );

    private ModArmorMaterials() {}
}
