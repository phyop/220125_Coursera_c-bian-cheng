

"""
Abbreviation
总分 5
1.
第 1 个问题
題目敘述
寫一個程式將輸入做縮寫處理。比如說 "national"、"taiwan"、"university" 這三個字串的話，縮寫就是 "NTU"。注意，有四種字串必須直接省略，不納入縮寫中："of"、 "and"、"the" 以及 "at"。例如 "the"、"united"、"states"、"of"、"amarica" 將會被縮寫成 "USA"。

輸入格式
輸入會是一連串的小寫詞彙以及句號 (period '.')。要縮寫在一起的詞彙中，最後一個詞的結尾將會有一個句號。以前面舉的"NTU"為例，程式收到的輸入會是 "national"、"taiwan" 以及 "university."。注意有一個句號在字串 "university." 的結尾。你的程式將會一直讀入輸入直到 EOF。我們保證輸入的最後一個詞彙的結尾一定會有句號；"of"、"and"、"the" 以及 "at" 不會是各個縮寫的最後一個詞彙，意即不會有 "of." 這樣的字串出現。我們也保證每個縮寫至少都會有一個字元。

輸出格式
你的程式必須在一行 (single line)內輸出所有的縮寫。(縮寫間留一個空白)



輸入限制
一個字彙(包含句號)的長度不會超過 127 個字元。一個縮寫的長度將不會超過 127 個字元。

輸入範例
the united states of american. taiwan high speed rail. national aeronautics
and space administration. metropolitan rapid transit. north atlantic treaty
organization. european union. university of hong kong. national chiao tong
university. massachusetts institute of technology. united kingdom. national
taiwan university. university of california at san diego. immigration and
naturalization service.

輸出範例
USA THSR NASA MRT NATO EU UHK NCTU MIT UK NTU UCSD INS

#################################################################
題目

united nations security council. national science foundation. orbital drop
shock trooper. advanced research projects agency. user datagram protocol.
communications based train control. delivered duty paid. kill in action.
internet protocol suite. object oriented programming. automated teller
machine. central intelligence agency.

as soon as possible. union of soviet socialist republics. good game.
british broadcasting corporation. universal serial bus. university of
california at los angeles. national institutes of health. force operation
x. bachelor of science. human immunodeficiency virus. science fiction. seal
qualification training. special air service. domain name system. master of
arts.

food and drug administration. be right back. digital single lens reflex.
post meridiem. do it yourself. acquired immune deficiency syndrome. special
operations aviation regiment. missing in action. chat with you later.
strategic homeland intervention enforcement and logistics division. post
script. bursting with laughter. tactical assault groups. cable news
network.

laughing out loud. university of southern california. world wide web. also
known as. landing zone. gross domestic product. metropolitan transportation
authority. transport workers union. university of california berkeley.
defense advanced research projects agency. estimated time of arrival.
national basketball association. office of naval intelligence. federal
bureau of investigation.

the civil works administration. file transfer protocol. chief executive
officer. no problem. the social security administration. ante meridiem.
gross national product. close quarters combat. the agricultural adjustment
act. dynamic host configuration protocol. the civilian conservation corps.
united states geological survey. crime scene investigation.

#################################################################

答案

"""