def metal_dict(metal_ls, value_ls):
    metal_value_dict = {}
    metal_value_dict = dict(zip(metal_ls, value_ls))
    return metal_value_dict

def total_price(metal_type, width, height, length, metal_value_dict):
    # 如果按照原題的main，那type:value的對應勢必要寫死在int value()中，這樣不好
    if metal_type not in metal_value_dict.keys():
        return -1
    if width <= 0 or height <= 0 or length <= 0:
        return -2
    temp = gcd(width, height)
    bulk_gcd = gcd(temp, length)
    cubic_vol = bulk_gcd**3
    cubic_numbers = width/bulk_gcd * height/bulk_gcd * length/bulk_gcd
    value = metal_value_dict[metal_type]
    price = cubic_vol**2 * cubic_numbers * value
    return int(price)

def gcd(a, b):
    if (a%b) == 0:
        return b
    else:
        return gcd(b, a%b)

if __name__ == "__main__":
    # 金、銀、銅、鉛、鐵、鈦
    metal_ls = [79 ,47 ,29 ,82 ,26 ,22]
    value_ls = [30, 10, 4, 5, 3, 9]
    metal_value_dict = metal_dict(metal_ls, value_ls) # 建立各金屬單價的字典

    file_from = './in.txt'
    with open(file_from, 'r') as f:
        for line in f:
            try:
                metal_type, width, height, length = map(int, line.strip().split())
                price = total_price(metal_type, width, height, length, metal_value_dict)
                print(price)
            except:
                None # 遇到空行時，什麼也不做，就繼續讀下一個line

"""
1*1*1大小的金塊，切成長1的正方體塊價值：(1*1*1)**2 * 1方塊 * 30元 = 30
2*2*2大小的金塊，切成長1的正方體塊價值：(1*1*1)**2 * 8方塊 * 30元 = 240
2*2*2大小的金塊，切成長2的正方體塊價值：(2*2*2)**2 * 1方塊 * 30元 = 1920（切長1的價格才240）
4*8*2大小的金塊，切成長1的正方體塊價值：(1*1*1)**2 * 64方塊 * 30元 = 1920
4*8*2大小的金塊，切成長2的正方體塊價值：(2*2*2)**2 * (4/2 × 8/2 × 2/2)方塊 * 30元 = 15360（切長1的價格才1920）
"""

"""
題目敘述
寫一個涵式來計算一個金屬塊的價值。函式原型如下：

int value(int type, int width, int height, int length);
一個金屬塊的價值由金屬類型及長、寬、高來決定。共有六種金屬：金、銀、銅、鉛、鐵以及鈦；六種金屬的價值依序為：30、10、4、5、3、9。
一個金屬塊必須被切成同樣大小的正方體才能販售，並且不能有任何剩餘的金屬。例如，
一個 4 x 8 x 2 大小的金屬塊只能被切成 2 x 2 x 2 或是 1 x 1 x 1 大小的正方體。
而金屬正方體的價值計算方式為其體積的平方乘以該金屬單位價值。因此，
2 x 2 x 2 大小的正方體金塊價值為 8 x 8 x 30 = 1920；
而4 x 8 x 2 的金塊，最高價值就是 1920 x 8 = 15360。

輸入格式
type 這個參數將會表明該金屬塊為哪種金屬。若是 79，代表是金。而 47、29、82、26、22 分別代表銀、銅、鉛、鐵以及鈦。width、height、length 代表該金屬塊的長、寬、高。

輸出格式
涵式必須確認 type 參數。若 type 並非上述六種金屬，必須回傳 -1。接著，函式必須確認三個維度的長度。width、 height、 length 皆能以 int 變數儲存。然而任何一個維度的值為零或負時，必須回傳 -2。若參數都沒有問題，請計算並回傳輸入的金屬塊價值。我們保證金屬價值能用 int 變數儲存。

輸入範例
79 4 8 2
輸出範例
15360

注意事項
請根據下列的 main () 函式為基礎，加上 value () 函式。

/* add your value() based on this code */
#include <stdio.h>

int main ()
{
    int type, width, height, length;
    scanf ( "%d%d%d%d", &type, &width, &height, &length );
    printf ( "%d", value ( type, width, height, length ) );
    return 0;
}
"""