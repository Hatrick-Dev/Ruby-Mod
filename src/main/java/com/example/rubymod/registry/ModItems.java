package com.example.rubymod.registry;

import com.example.rubymod.RubyMod;
import com.example.rubymod.item.ModArmorMaterials;
import com.example.rubymod.item.ModToolMaterials;
import java.util.function.Function;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceKey;
import net.minecraft.world.item.AxeItem;
import net.minecraft.world.item.HoeItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ShovelItem;
import net.minecraft.world.item.equipment.ArmorType;

public final class ModItems {
    // Fire-resistant: items never burn in fire/lava and float on lava (vanilla netherite behaviour).
    public static final Item RUBY = register("ruby", Item::new, new Item.Properties().fireResistant());
    public static final Item RAW_RUBY = register("raw_ruby", Item::new, new Item.Properties().fireResistant());

    // Attack numbers are bonuses over fist: total = 1.0 base + material 4.5 + value.
    public static final Item RUBY_SWORD = register("ruby_sword", Item::new,
            new Item.Properties().sword(ModToolMaterials.RUBY, 3.5F, -2.4F).fireResistant());   // 9.0 dmg, 1.6 speed
    public static final Item RUBY_PICKAXE = register("ruby_pickaxe", Item::new,
            new Item.Properties().pickaxe(ModToolMaterials.RUBY, 1.0F, -2.8F).fireResistant()); // 6.5 dmg, 1.2 speed
    public static final Item RUBY_AXE = register("ruby_axe",
            p -> new AxeItem(ModToolMaterials.RUBY, 5.5F, -3.0F, p), new Item.Properties().fireResistant()); // 11.0 dmg, 1.0 speed
    public static final Item RUBY_SHOVEL = register("ruby_shovel",
            p -> new ShovelItem(ModToolMaterials.RUBY, 1.5F, -3.0F, p), new Item.Properties().fireResistant());
    public static final Item RUBY_HOE = register("ruby_hoe",
            p -> new HoeItem(ModToolMaterials.RUBY, -4.5F, 0.0F, p), new Item.Properties().fireResistant());

    public static final Item RUBY_HELMET = register("ruby_helmet", Item::new,
            new Item.Properties().humanoidArmor(ModArmorMaterials.RUBY, ArmorType.HELMET).fireResistant());
    public static final Item RUBY_CHESTPLATE = register("ruby_chestplate", Item::new,
            new Item.Properties().humanoidArmor(ModArmorMaterials.RUBY, ArmorType.CHESTPLATE).fireResistant());
    public static final Item RUBY_LEGGINGS = register("ruby_leggings", Item::new,
            new Item.Properties().humanoidArmor(ModArmorMaterials.RUBY, ArmorType.LEGGINGS).fireResistant());
    public static final Item RUBY_BOOTS = register("ruby_boots", Item::new,
            new Item.Properties().humanoidArmor(ModArmorMaterials.RUBY, ArmorType.BOOTS).fireResistant());

    private static <T extends Item> T register(String name, Function<Item.Properties, T> factory, Item.Properties props) {
        ResourceKey<Item> key = ResourceKey.create(Registries.ITEM, RubyMod.id(name));
        return Registry.register(BuiltInRegistries.ITEM, key, factory.apply(props.setId(key)));
    }

    public static void init() {}

    private ModItems() {}
}
