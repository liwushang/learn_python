# -*-coding:utf-8-*-
import re

content = """
每个人都知道，我们的人生只有这一次，但是我们这样活着，然后死了，离开了这个世界，
却没有任何一样事物可以证明你在这个世界上曾经存在过。年华和岁月我们都含在嘴边说要珍惜，
韶光易逝，莫等闲，白了少年头，却又怎知在我们在心中叹息时间过得太快的时候，
一切都已经离我们而去，再也如那字迹所说，一切都不会再回来了。

当我们都在为人生所奋斗的时候，才发现，一切都太快了，我们都抓不住这一切。所有的事物就如那流水
般，缓缓的流淌着，然后被这世界吞噬了。时间都去哪儿了？我也在扪心自问。这时间太快了，我们的童
年只是在转眼间便淹没在了那时间的大海之中。一辈子，说长便长，说短便短，谁又能来衡量这我们都无
法抓住岁月呢？

躺在岁月的怀中哭泣，没有人可以知道我们活得有多累，我们在不断的打拼，为的是什么？只是为了可以
让自己今后的生活可以变得更好，比别人活得灿烂，比别人活得辉煌罢了。人就只有这一生，我们都不能
荒废这时间和岁月，因为我们都资格和权利。时间太快，当我们的.真的老了的时候，才发现自己这一生
活得太过平凡，没有打拼过，也没有去真真正正的潇洒过那么一次。

趁我们还年轻，应该好好的去享受在活着的时间之中的每一刻，因为我们都太卑微，没有资格让时间为
我们而停留。到了老年的时候，才会羡慕那些年轻的孩子，因为我们也曾年轻过，只是没有让自己在年轻
的时候活得足够让自己觉得，这辈子足矣。

然后我们就这样默默的等着这时间从我们的身边溜走了，我们抓不住啊！不禁感叹到，这时间，我能奈
你如何？趁我们现在还年轻，学会做点儿让自己今后老了时候感到欣慰的事情。不是去耍小孩子脾气，
因为我们已经开不起这样的玩笑了。玩笑就是在你觉得时间还长，一辈子那么长，长得让自己都觉得活得没
有任何意义，却不知道，这样真的是一个笑话。这一辈子，我们都扪心自问，这辈子活得有意义吗？

"""

import      jieba
import re
content = re.sub(r"\s。，？","",content)
word_list = jieba.cut(content)
print(list(word_list))


