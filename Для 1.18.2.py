from PIL import Image
import pyperclip
import math

R = {'1acacia_wood':'76', '1black_terracotta':'37', '1black_wool':'25', '1blue_ice':'160', '1blue_terracotta':'76', '1blue_wool':'51', '1brown_terracotta':'76', '1clay':'164', '1crimson_hyphae':'92', '1crimson_nylium':'189', '1crimson_planks':'148', '1cyan_terracotta':'87', '1cyan_wool':'76', '1dark_oak_wood':'102', '1diamond_block':'92', '1diorite':'255', '1emerald_block':'0', '1gold_block':'250', '1gray_terracotta':'57', '1green_terracotta':'76', '1green_wool':'102', '1hopper':'112', '1iron_block':'167', '1jungle_wood':'151', '1lapis_block':'74', '1light_blue_terracotta':'112', '1light_blue_wool':'102', '1light_gray_terracotta':'135', '1light_gray_wool':'153', '1lime_terracotta':'103', '1lime_wool':'127', '1magenta_terracotta':'149', '1magenta_wool':'178', '1mushroom_stem':'199', '1netherrack':'112', '1oak_leaves':'0', '1oak_wood':'143', '1orange_terracotta':'159', '1pink_terracotta':'160', '1pink_wool':'242', '1podzol':'129', '1purple_terracotta':'122', '1purple_wool':'127', '1red_sandstone':'216', '1red_terracotta':'142', '1red_wool':'153', '1redstone_block':'255', '1sandstone':'247', '1slime_block':'127', '1snow_block':'255', '1sponge':'229', '1warped_hyphae':'86', '1warped_nylium':'22', '1warped_planks':'58', '1warped_wart_block':'20', '1water':'64', '1white_terracotta':'209', '1yellow_terracotta':'186', '2acacia_wood':'65', '2black_terracotta':'31', '2black_wool':'21', '2blue_ice':'136', '2blue_terracotta':'65', '2blue_wool':'43', '2brown_terracotta':'65', '2clay':'139', '2crimson_hyphae':'78', '2crimson_nylium':'161', '2crimson_planks':'126', '2cyan_terracotta':'74', '2cyan_wool':'65', '2dark_oak_wood':'87', '2diamond_block':'78', '2diorite':'217', '2emerald_block':'0', '2gold_block':'213', '2gray_terracotta':'48', '2green_terracotta':'65', '2green_wool':'87', '2hopper':'95', '2iron_block':'142', '2jungle_wood':'128', '2lapis_block':'63', '2light_blue_terracotta':'95', '2light_blue_wool':'87', '2light_gray_terracotta':'115', '2light_gray_wool':'130', '2lime_terracotta':'88', '2lime_wool':'108', '2magenta_terracotta':'127', '2magenta_wool':'151', '2mushroom_stem':'169', '2netherrack':'95', '2oak_leaves':'0', '2oak_wood':'122', '2orange_terracotta':'135', '2pink_terracotta':'136', '2pink_wool':'206', '2podzol':'110', '2purple_terracotta':'104', '2purple_wool':'108', '2red_sandstone':'184', '2red_terracotta':'121', '2red_wool':'130', '2redstone_block':'217', '2sandstone':'210', '2slime_block':'108', '2snow_block':'217', '2sponge':'195', '2warped_hyphae':'73', '2warped_nylium':'19', '2warped_planks':'49', '2warped_wart_block':'17', '2water':'54', '2white_terracotta':'178', '2yellow_terracotta':'158', '3acacia_wood':'53', '3black_terracotta':'26', '3black_wool':'18', '3blue_ice':'112', '3blue_terracotta':'53', '3blue_wool':'36', '3brown_terracotta':'53', '3clay':'115', '3crimson_hyphae':'64', '3crimson_nylium':'132', '3crimson_planks':'104', '3cyan_terracotta':'61', '3cyan_wool':'53', '3dark_oak_wood':'71', '3diamond_block':'64', '3diorite':'179', '3emerald_block':'0', '3gold_block':'175', '3gray_terracotta':'40', '3green_terracotta':'53', '3green_wool':'71', '3hopper':'78', '3iron_block':'117', '3jungle_wood':'106', '3lapis_block':'52', '3light_blue_terracotta':'78', '3light_blue_wool':'71', '3light_gray_terracotta':'95', '3light_gray_wool':'107', '3lime_terracotta':'72', '3lime_wool':'89', '3magenta_terracotta':'104', '3magenta_wool':'125', '3mushroom_stem':'139', '3netherrack':'78', '3oak_leaves':'0', '3oak_wood':'100', '3orange_terracotta':'111', '3pink_terracotta':'112', '3pink_wool':'169', '3podzol':'90', '3purple_terracotta':'85', '3purple_wool':'89', '3red_sandstone':'151', '3red_terracotta':'99', '3red_wool':'107', '3redstone_block':'179', '3sandstone':'173', '3slime_block':'89', '3snow_block':'179', '3sponge':'160', '3warped_hyphae':'60', '3warped_nylium':'15', '3warped_planks':'41', '3warped_wart_block':'14', '3water':'45', '3white_terracotta':'146', '3yellow_terracotta':'130'}
G = {'1acacia_wood':'76', '1black_terracotta':'22', '1black_wool':'25', '1blue_ice':'160', '1blue_terracotta':'62', '1blue_wool':'76', '1brown_terracotta':'50', '1clay':'168', '1crimson_hyphae':'25', '1crimson_nylium':'48', '1crimson_planks':'63', '1cyan_terracotta':'92', '1cyan_wool':'127', '1dark_oak_wood':'76', '1diamond_block':'219', '1diorite':'252', '1emerald_block':'217', '1gold_block':'238', '1gray_terracotta':'41', '1green_terracotta':'82', '1green_wool':'127', '1hopper':'112', '1iron_block':'167', '1jungle_wood':'109', '1lapis_block':'128', '1light_blue_terracotta':'108', '1light_blue_wool':'153', '1light_gray_terracotta':'107', '1light_gray_wool':'153', '1lime_terracotta':'117', '1lime_wool':'204', '1magenta_terracotta':'87', '1magenta_wool':'76', '1mushroom_stem':'199', '1netherrack':'2', '1oak_leaves':'124', '1oak_wood':'119', '1orange_terracotta':'82', '1pink_terracotta':'77', '1pink_wool':'127', '1podzol':'86', '1purple_terracotta':'73', '1purple_wool':'63', '1red_sandstone':'127', '1red_terracotta':'60', '1red_wool':'51', '1redstone_block':'0', '1sandstone':'233', '1slime_block':'178', '1snow_block':'255', '1sponge':'229', '1warped_hyphae':'44', '1warped_nylium':'126', '1warped_planks':'142', '1warped_wart_block':'180', '1water':'64', '1white_terracotta':'177', '1yellow_terracotta':'133', '2acacia_wood':'65', '2black_terracotta':'19', '2black_wool':'21', '2blue_ice':'136', '2blue_terracotta':'53', '2blue_wool':'65', '2brown_terracotta':'43', '2clay':'143', '2crimson_hyphae':'21', '2crimson_nylium':'41', '2crimson_planks':'54', '2cyan_terracotta':'78', '2cyan_wool':'108', '2dark_oak_wood':'65', '2diamond_block':'186', '2diorite':'214', '2emerald_block':'184', '2gold_block':'202', '2gray_terracotta':'35', '2green_terracotta':'70', '2green_wool':'108', '2hopper':'95', '2iron_block':'142', '2jungle_wood':'93', '2lapis_block':'109', '2light_blue_terracotta':'92', '2light_blue_wool':'130', '2light_gray_terracotta':'91', '2light_gray_wool':'130', '2lime_terracotta':'99', '2lime_wool':'173', '2magenta_terracotta':'74', '2magenta_wool':'65', '2mushroom_stem':'169', '2netherrack':'2', '2oak_leaves':'105', '2oak_wood':'101', '2orange_terracotta':'70', '2pink_terracotta':'65', '2pink_wool':'108', '2podzol':'73', '2purple_terracotta':'62', '2purple_wool':'54', '2red_sandstone':'108', '2red_terracotta':'51', '2red_wool':'43', '2redstone_block':'0', '2sandstone':'198', '2slime_block':'151', '2snow_block':'217', '2sponge':'195', '2warped_hyphae':'37', '2warped_nylium':'107', '2warped_planks':'121', '2warped_wart_block':'153', '2water':'54', '2white_terracotta':'150', '2yellow_terracotta':'113', '3acacia_wood':'53', '3black_terracotta':'15', '3black_wool':'18', '3blue_ice':'112', '3blue_terracotta':'43', '3blue_wool':'53', '3brown_terracotta':'35', '3clay':'118', '3crimson_hyphae':'18', '3crimson_nylium':'34', '3crimson_planks':'44', '3cyan_terracotta':'64', '3cyan_wool':'89', '3dark_oak_wood':'53', '3diamond_block':'153', '3diorite':'176', '3emerald_block':'152', '3gold_block':'167', '3gray_terracotta':'29', '3green_terracotta':'57', '3green_wool':'89', '3hopper':'78', '3iron_block':'117', '3jungle_wood':'76', '3lapis_block':'90', '3light_blue_terracotta':'76', '3light_blue_wool':'107', '3light_gray_terracotta':'75', '3light_gray_wool':'107', '3lime_terracotta':'82', '3lime_wool':'143', '3magenta_terracotta':'61', '3magenta_wool':'53', '3mushroom_stem':'139', '3netherrack':'1', '3oak_leaves':'87', '3oak_wood':'83', '3orange_terracotta':'57', '3pink_terracotta':'54', '3pink_wool':'89', '3podzol':'60', '3purple_terracotta':'51', '3purple_wool':'44', '3red_sandstone':'89', '3red_terracotta':'42', '3red_wool':'36', '3redstone_block':'0', '3sandstone':'163', '3slime_block':'125', '3snow_block':'179', '3sponge':'160', '3warped_hyphae':'31', '3warped_nylium':'88', '3warped_planks':'99', '3warped_wart_block':'126', '3water':'45', '3white_terracotta':'124', '3yellow_terracotta':'93'}
B = {'1acacia_wood':'76', '1black_terracotta':'16', '1black_wool':'25', '1blue_ice':'255', '1blue_terracotta':'92', '1blue_wool':'178', '1brown_terracotta':'35', '1clay':'184', '1crimson_hyphae':'29', '1crimson_nylium':'49', '1crimson_planks':'97', '1cyan_terracotta':'92', '1cyan_wool':'153', '1dark_oak_wood':'51', '1diamond_block':'213', '1diorite':'245', '1emerald_block':'58', '1gold_block':'77', '1gray_terracotta':'35', '1green_terracotta':'42', '1green_wool':'51', '1hopper':'112', '1iron_block':'167', '1jungle_wood':'77', '1lapis_block':'255', '1light_blue_terracotta':'138', '1light_blue_wool':'216', '1light_gray_terracotta':'98', '1light_gray_wool':'153', '1lime_terracotta':'53', '1lime_wool':'25', '1magenta_terracotta':'108', '1magenta_wool':'216', '1mushroom_stem':'199', '1netherrack':'0', '1oak_leaves':'0', '1oak_wood':'72', '1orange_terracotta':'36', '1pink_terracotta':'78', '1pink_wool':'165', '1podzol':'49', '1purple_terracotta':'88', '1purple_wool':'178', '1red_sandstone':'51', '1red_terracotta':'46', '1red_wool':'51', '1redstone_block':'0', '1sandstone':'163', '1slime_block':'56', '1snow_block':'255', '1sponge':'51', '1warped_hyphae':'62', '1warped_nylium':'134', '1warped_planks':'140', '1warped_wart_block':'133', '1water':'255', '1white_terracotta':'161', '1yellow_terracotta':'36', '2acacia_wood':'65', '2black_terracotta':'14', '2black_wool':'21', '2blue_ice':'217', '2blue_terracotta':'78', '2blue_wool':'151', '2brown_terracotta':'30', '2clay':'156', '2crimson_hyphae':'25', '2crimson_nylium':'42', '2crimson_planks':'82', '2cyan_terracotta':'78', '2cyan_wool':'130', '2dark_oak_wood':'43', '2diamond_block':'181', '2diorite':'208', '2emerald_block':'49', '2gold_block':'65', '2gray_terracotta':'30', '2green_terracotta':'36', '2green_wool':'43', '2hopper':'95', '2iron_block':'142', '2jungle_wood':'65', '2lapis_block':'217', '2light_blue_terracotta':'117', '2light_blue_wool':'184', '2light_gray_terracotta':'83', '2light_gray_wool':'130', '2lime_terracotta':'45', '2lime_wool':'21', '2magenta_terracotta':'92', '2magenta_wool':'184', '2mushroom_stem':'169', '2netherrack':'0', '2oak_leaves':'0', '2oak_wood':'61', '2orange_terracotta':'31', '2pink_terracotta':'66', '2pink_wool':'140', '2podzol':'42', '2purple_terracotta':'75', '2purple_wool':'151', '2red_sandstone':'43', '2red_terracotta':'39', '2red_wool':'43', '2redstone_block':'0', '2sandstone':'139', '2slime_block':'48', '2snow_block':'217', '2sponge':'43', '2warped_hyphae':'53', '2warped_nylium':'114', '2warped_planks':'119', '2warped_wart_block':'113', '2water':'217', '2white_terracotta':'137', '2yellow_terracotta':'31', '3acacia_wood':'53', '3black_terracotta':'11', '3black_wool':'18', '3blue_ice':'179', '3blue_terracotta':'64', '3blue_wool':'125', '3brown_terracotta':'25', '3clay':'129', '3crimson_hyphae':'20', '3crimson_nylium':'34', '3crimson_planks':'68', '3cyan_terracotta':'64', '3cyan_wool':'107', '3dark_oak_wood':'36', '3diamond_block':'149', '3diorite':'172', '3emerald_block':'41', '3gold_block':'54', '3gray_terracotta':'25', '3green_terracotta':'29', '3green_wool':'36', '3hopper':'78', '3iron_block':'117', '3jungle_wood':'54', '3lapis_block':'179', '3light_blue_terracotta':'97', '3light_blue_wool':'151', '3light_gray_terracotta':'69', '3light_gray_wool':'107', '3lime_terracotta':'37', '3lime_wool':'18', '3magenta_terracotta':'76', '3magenta_wool':'151', '3mushroom_stem':'139', '3netherrack':'0', '3oak_leaves':'0', '3oak_wood':'50', '3orange_terracotta':'25', '3pink_terracotta':'55', '3pink_wool':'116', '3podzol':'34', '3purple_terracotta':'62', '3purple_wool':'125', '3red_sandstone':'36', '3red_terracotta':'32', '3red_wool':'36', '3redstone_block':'0', '3sandstone':'114', '3slime_block':'39', '3snow_block':'179', '3sponge':'36', '3warped_hyphae':'43', '3warped_nylium':'94', '3warped_planks':'98', '3warped_wart_block':'93', '3water':'179', '3white_terracotta':'113', '3yellow_terracotta':'25'}

modul = 100000
block  = "minecraft:brown_terracotta"
key = 0

ymin = 50
ymax = 0
x0 = -64
x = x0
y0 = 60
y = y0
z0 = -64
z = z0
printblock = 0

img = Image.open("5art.jpg")

p1 = str('summon falling_block ~ ~1 ~ {Time:1,BlockState:{Name:redstone_block},Passengers:[{id:falling_block,Passengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},Passengers:[{id:command_block_minecart,Command:\'gamerule commandBlockOutput false\'},')

p2 = " "

p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x) +" "+ str(y) +" "+ str(z-1)+ " "+ str(x+128) +" "+ str(y) +" "+ str(z -1) +" "+ block + '\'},')
#строчка выше - для того, чтобы задать 1 цвет вне рисунка (для яркости блока), делается в 1 итерации

for i in range (15, 16): #16 столбцов
    
    y = y0
    z = z0
    x = x0 + i*8
    
    for j in range (0, 16): #16 строк 1 столбца, потом 2, потом...
    
        color = img.getpixel((i, j)) #определить ргб точки
        r1, g1, b1 = color #сделать из кортежа 3 переменные
        
        for key in R: #число цветов 177
            r2 = int(R[key])
            g2 = int(G[key])
            b2 = int(B[key])
            modul1 = ((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)
            if modul1 < modul:
                modul = modul1
                block = key
            #print (block)
        printblock = "minecraft:" + block[1:]
        a = 0
        if int(block[0]) == 1:
            for a in range (0,8):
                y += 1
                p3 = str('{id:command_block_minecart,Command:\'' +'fill '+ str(x) +" "+ str(y) +" "+ str(z)+ " "+ str(x + 7) +" "+ str(y) +" "+ str(z) +" "+ printblock + '\'},')
                p2 += p3
                z += 1
                
                a += 1
                
        elif int(block[0]) == 3:
            for a in range (0,8):
                y += -1
                p3 = str('{id:command_block_minecart,Command:\'' +'fill '+ str(x) +" "+ str(y) +" "+ str(z)+ " "+ str(x + 7) +" "+ str(y) +" "+ str(z) +" "+ printblock + '\'},')
                p2 += p3
                z += 1
                
                a += 1
                 
        else:        
            p3 = str('{id:command_block_minecart,Command:\'' +'fill '+ str(x) +" "+ str(y) +" "+ str(z)+ " "+ str(x + 7) +" "+ str(y) +" "+ str(z + 7) +" "+ printblock + '\'},')
            p2 += p3
            j += 1
            z += 8
        modul = 100000
        if ymin > y:
            ymin = y
        if ymax < y:
            ymax = y
    if len (p2) > 32500:
        print(i)
        break
    i += 1
    


p4 = str('{id:command_block_minecart,Command:\'setblock ~ ~1 ~ command_block{auto:1,Command:"fill ~ ~ ~ ~ ~-3 ~ air"}\'},{id:command_block_minecart,Command:\'kill @e[type=command_block_minecart,distance=..1]\'}]}]}]}')
end =  p1 + p2 + p4
print (end)


print (ymin, ymax)

pyperclip.copy(p1 + p2 + p4)
print ('Код скопирован в буфер обмена')